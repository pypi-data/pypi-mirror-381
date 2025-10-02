# Copyright Axis Communications AB.
#
# For a full list of individual contributors, please see the commit history.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""ETR log area handler."""
import logging
import traceback
import hashlib
import time
from copy import deepcopy
from pathlib import Path
from shutil import make_archive, rmtree
from json.decoder import JSONDecodeError

from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError, NewConnectionError
from etos_test_runner.lib.events import EventPublisher


class LogArea:
    """Library for uploading logs to log area."""

    logger = logging.getLogger(__name__)

    def __init__(self, etos):
        """Initialize with an ETOS instance.

        :param etos: Instance of ETOS library.
        :type etos: :obj:`etos_lib.etos.Etos`
        """
        self.etos = etos
        self.event_publisher = EventPublisher(etos)
        self.identifier = self.etos.config.get("suite_id")
        self.suite_name = self.etos.config.get("test_config").get("name").replace(" ", "-")
        self.log_area = self.etos.config.get("test_config").get("log_area")
        self.logs = []
        self.artifacts = []

    @property
    def persistent_logs(self):
        """All persistent log formatted for EiffelTestSuiteFinishedEvent.

        :return: All persistent logs.
        :rtype: list
        """
        return [{"name": log["name"], "uri": log["uri"]} for log in self.logs]

    def _fix_name(self, path, test_name=None):
        """Fix the name of a file.

        "Fixing" means:

            - Prepend test name if file was gathered by a test case.
            - Prepend "log_info" if supplied by environment provider.
            - Reduce the size of the filename if it's too large.
            - Prepend a counter if filename already exists.

        :param path: Path to a file to fix.
        :type path: :obj:`pathlib.Path`
        :param test_name: Test name if this file was gathered during a test case.
        :type test_name: str
        :return: A new and improved path and filename.
        :rtype: :obj:`pathlib.Path`
        """
        directory, filename = path.parent, path.name
        if test_name is not None:
            self.logger.info("File collected as part of test case. Prepending %r", test_name)
            filename = f"{test_name}_{filename}"
            self.logger.info("Result: %r", filename)
        if self.log_area.get("logs"):
            prepend = self.log_area.get("logs").get("prepend", "")
            join_character = self.log_area.get("logs").get("join_character", "_")
            self.logger.info(
                "Log instructions added by environment provider. Prepending %r", prepend
            )
            filename = f"{prepend}{join_character}{filename}"
            self.logger.info("Result: %r", filename)
        if len(filename) + 5 > 255:  # +5 as to be able to prepend counter.
            max_length = 250
            self.logger.info(
                "Filename is too long at %r. Reduce size to %r.", len(filename) + 5, max_length
            )
            # Split filename into base and extension
            if "." in filename:
                base, suffix = filename.rsplit(".", 1)
            else:
                base, suffix = filename, ""

            # Remove trailing dots to avoid double dots (e.g., "file..txt")
            base_clean = base.rstrip(".")

            # Calculate max length for base part
            # max_length total - extension length - 1 for dot (if extension exists)
            if suffix:
                max_base_length = max_length - len(suffix) - 1
                truncated_base = base_clean[:max_base_length].rstrip(".")
                filename = f"{truncated_base}.{suffix}"
            else:
                truncated_base = base_clean[:max_length].rstrip(".")
                filename = truncated_base
            self.logger.info("Result: %r", filename)
        log_names = [item["name"] for item in self.logs + self.artifacts]
        index = 0
        while filename in log_names:
            index += 1
            filename = f"{index}_{filename}"
            self.logger.info("Log name already exists. Rename to %r.", filename)
        return path.rename(directory.joinpath(filename))

    def collect(self, path):
        """Collect logs and artifacts from path.

        :param path: Path to collect logs and artifacts from.
        :type path: :obj:`pathlib.Path`
        :return: Filenames and paths.
        :rtype: list
        """
        test_name = self.etos.config.get("test_name")
        items = []
        self.logger.info("Collecting logs/artifacts for %r", test_name or "global")
        for item in path.iterdir():
            if item.is_dir():
                # Clean the archive name to avoid double dots when make_archive appends .tar.gz
                archive_name = str(item.relative_to(Path.cwd())).rstrip(".")
                compressed_item = make_archive(
                    archive_name,
                    format="gztar",
                    root_dir=path,
                    base_dir=item.name,
                    logger=self.logger,
                )
                rmtree(item)
                item = Path(compressed_item)
            item = self._fix_name(item, test_name)
            items.append({"name": item.name, "file": item})
        return items

    def upload_logs(self, logs):
        """Upload logs to log area.

        :param logs: Logs to upload.
        :type logs: list
        """
        for log in logs:
            log["uri"], log["checksums"] = self.__upload(
                self.etos.config.get("context"),
                log["file"],
                log["name"],
                self.etos.config.get("main_suite_id"),
                self.etos.config.get("sub_suite_id"),
            )
            event = {
                "event": "report",
                "data": {
                    "url": log["uri"],
                    "name": log["name"],
                    "checksums": log["checksums"],
                },
            }
            self.logger.info("Sending event:      %r", event)
            self.event_publisher.publish(event)
            self.logs.append(log)
            log["file"].unlink()

    def _artifact_created(self, artifacts):
        """Send artifact created event.

        :param artifacts: Artifacts that exists within this event.
        :type artifacts: list
        """
        test_name = self.etos.config.get("test_name")
        if test_name:
            identity = f"pkg:etos-test-output/{self.suite_name}/{test_name}"
        else:
            identity = f"pkg:etos-test-output/{self.suite_name}"
        file_information = []
        for artifact in artifacts:
            file_information.append({"name": artifact["file"].name})
        return self.etos.events.send_artifact_created_event(
            identity,
            fileInformation=file_information,
            links={
                "CONTEXT": self.etos.config.get("context"),
                "CAUSE": self.etos.config.get("sub_suite_id"),
            },
        )

    def _artifact_published(self, artifact_created, published_url):
        """Send artifact published event.

        :param artifact_created: The created artifact to publish.
        :type artifact_created: :obj:`eiffellib.events.EiffelArtifactCreatedEvent`
        :param published_url: URL to the published directory.
        :type published_url: str
        """
        log_area_type = self.log_area.get("type", "OTHER")
        locations = [{"uri": published_url, "type": log_area_type}]
        self.etos.events.send_artifact_published_event(
            locations,
            artifact_created,
            links={"CONTEXT": self.etos.config.get("context")},
        )

    def upload_artifacts(self, artifacts):
        """Upload artifacts to log area.

        :param artifacts: Artifacs to upload.
        :type artifacts: list
        :return: Artifact name and URI
        :rtype: tuple
        """
        if not artifacts:
            return
        log_area_folder = (
            f"{self.etos.config.get('main_suite_id')}/{self.etos.config.get('sub_suite_id')}"
        )
        self.logger.info("Uploading artifacts %r to log area", artifacts)
        artifact_created = self._artifact_created(artifacts)

        for artifact in artifacts:
            artifact["uri"], artifact["checksums"] = self.__upload(
                self.etos.config.get("context"),
                artifact["file"],
                artifact["name"],
                self.etos.config.get("main_suite_id"),
                self.etos.config.get("sub_suite_id"),
            )
            event = {
                "event": "artifact",
                "data": {
                    "url": artifact["uri"],
                    "name": artifact["name"],
                    "directory": self.suite_name,
                    "checksums": artifact["checksums"],
                },
            }
            self.logger.info("Sending event:      %r", event)
            self.event_publisher.publish(event)
            self.artifacts.append(artifact)
            artifact["file"].unlink()

        upload = deepcopy(self.log_area.get("upload"))
        data = {
            "context": self.etos.config.get("context"),
            "folder": log_area_folder,
            "sub_suite_id": self.etos.config.get("sub_suite_id"),
            "main_suite_id": self.etos.config.get("main_suite_id"),
            "name": "",
        }
        published_url = upload["url"].format(**data)
        self._artifact_published(artifact_created, published_url)

    def __upload(
        self, context, log, name, main_suite_id, sub_suite_id
    ):  # pylint:disable=too-many-positional-arguments,too-many-arguments
        """Upload log to a storage location.

        :param context: Context for the http request.
        :type context: str
        :param log: Path to the log to upload.
        :type log: str
        :param name: Name of file to upload.
        :type name: str
        :param main_suite_id: Main suite ID for folder creation.
        :type main_suite_id: str
        :param sub_suite_id: Sub suite ID for folder creation.
        :type sub_suite_id: str
        :return: URI where log was uploaded to.
        :rtype: str
        """
        upload = deepcopy(self.log_area.get("upload"))
        folder = f"{main_suite_id}/{sub_suite_id}"
        data = {
            "context": context,
            "name": name,
            "sub_suite_id": sub_suite_id,
            "main_suite_id": main_suite_id,
            "folder": folder,
        }

        # ETOS Library, for some reason, uses the key 'verb' instead of 'method'
        # for HTTP method.
        upload["verb"] = upload.pop("method")
        upload["url"] = upload["url"].format(**data)
        upload["timeout"] = upload.get("timeout", 30)
        if upload.get("auth"):
            upload["auth"] = self.__auth(**upload["auth"])

        checksums = {}
        with open(log, "rb") as log_file:
            content = log_file.read()
            checksums["SHA-256"] = hashlib.sha256(content).hexdigest()
            for _ in range(3):
                request_generator = self.__retry_upload(file_contents=content, **upload)
                try:
                    for response in request_generator:
                        self.logger.debug("%r", response)
                        if not upload.get("as_json", True):
                            self.logger.debug("%r", response.text)
                        self.logger.info("Uploaded log %r.", log)
                        self.logger.info("Upload URI          %r", upload["url"])
                        self.logger.info("Data:               %r", data)
                        self.logger.info("Checksum(sha256):   %r", checksums["SHA-256"])
                        break
                    break
                except:  # noqa pylint:disable=bare-except
                    self.logger.error("%r", traceback.format_exc())
                    self.logger.error("Failed to upload log!")
                    self.logger.error("Attempted upload of %r", log)
        return upload["url"], checksums

    def __retry_upload(
        self, verb, url, file_contents, timeout=None, as_json=True, **requests_kwargs
    ):  # pylint:disable=too-many-positional-arguments,too-many-arguments
        """Attempt to connect to url for x time.

        :param verb: Which HTTP verb to use. GET, PUT, POST
                     (DELETE omitted)
        :type verb: str
        :param url: URL to retry upload request
        :type url: str
        :param file_contents: File contents to upload
        :type file_contents: bytes
        :param timeout: How long, in seconds, to retry request.
        :type timeout: int or None
        :param as_json: Whether or not to return json instead of response.
        :type as_json: bool
        :param request_kwargs: Keyword arguments for the requests command.
        :type request_kwargs: dict
        :return: HTTP response or json.
        :rtype: Response or dict
        """
        if timeout is None:
            timeout = self.etos.debug.default_http_timeout
        end_time = time.time() + timeout
        self.logger.debug("Retrying URL %s for %d seconds with a %s request.", url, timeout, verb)
        iteration = 0
        while time.time() < end_time:
            iteration += 1
            self.logger.debug("Iteration: %d", iteration)
            try:
                request = getattr(self.etos.http, verb.lower())
                response = request(url, data=file_contents, **requests_kwargs)
                if as_json:
                    yield response.json()
                else:
                    yield response
                break
            except (
                ConnectionError,
                HTTPError,
                NewConnectionError,
                MaxRetryError,
                TimeoutError,
                JSONDecodeError,
            ):
                self.logger.warning("%r", traceback.format_exc())
                time.sleep(2)
        else:
            raise ConnectionError(f"Unable to {verb} {url} with params {requests_kwargs}")

    @staticmethod
    def __auth(username, password, type="basic"):  # pylint:disable=redefined-builtin
        """Create an authentication for HTTP request.

        :param username: Username to authenticate.
        :type username: str
        :param password: Password to authenticate with.
        :type password: str
        :param type: Type of authentication. 'basic' or 'digest'.
        :type type: str
        :return: Authentication method.
        :rtype: :obj:`requests.auth`
        """
        if type.lower() == "basic":
            return HTTPBasicAuth(username, password)
        return HTTPDigestAuth(username, password)
