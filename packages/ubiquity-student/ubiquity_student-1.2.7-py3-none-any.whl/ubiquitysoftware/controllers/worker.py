"""Module managing the worker"""
#      ubiquity
#      Copyright (C) 2022  INSA Rouen Normandie - CIP
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

import signal
import time
import os
from datetime import datetime, timezone
from enum import unique, IntEnum
from json import loads
from os import stat
from os.path import isfile, join
from threading import Thread
from typing import List, Optional

import requests

from ubiquitysoftware.views.utils import gettext, MessageLevel, ErrorMessage, LabelEnum

_ = gettext.gettext

TIMEOUT = 5

@unique
class StatusCode(IntEnum):
    """Enum class for status codes"""
    OK = 200
    CREATED = 201
    SUSPENDED = 423
    UNPROCESSABLE_ENTITY = 422


def get_current_time() -> str:
    """Function returning the current time

    :return: The current time
    """
    return time.strftime("%H:%M:%S", time.localtime())


def time_updated_file(file_path):
    """Function returning the time of the updated file

    :param file_path: The file path
    :return: The time of the updated file
    """
    return stat(file_path)[8]


def file_is_updated(file_path, old_time):
    """Function verifying the file is updated

    :param file_path: The file path
    :param old_time: The old time of the updated file
    :return: True if the times is different, False if not
    """
    return old_time != time_updated_file(file_path)


class Worker:
    """Class managing the worker"""
    def __init__(self, model, has_gui, view, fn_display=None):
        self._model = model
        self._view = view
        self._has_gui = has_gui
        self.running = False
        if self._has_gui:
            self._thread = Thread(target=self._worker)
        else:
            self.fn_display = fn_display
        self._files_watching = {}
        self._followed_files = self._get_files_to_follow()
        self._init_files()
        if not self._has_gui:
            self._get_progress()

    def _init_files(self):
        """Method initializing the files to follow"""
        student_files = self._get_student_files()
        other_files = self._check_file_exist(student_files)
        self._check_file_previous_date(student_files, other_files)

    def _check_file_exist(self, student_files: List[str]) -> List[str]:
        """
        Checking if files not created locally exist in the database

        Args:
            student_files (List[str]): Student files list

        Returns:
            List[str]: Other files list
        """
        other_files = []
        for file_path in student_files:
            if not os.path.exists(file_path):
                other_files.append(file_path)
        if len(other_files) > 0:
            message = LabelEnum.OVER_FILES.value if len(other_files) > 1 else LabelEnum.ANOTHER_FILE.value
            question = LabelEnum.ADD_THEM.value if len(other_files) > 1 else LabelEnum.ADD_IT.value
            response = self._ask_for_download(other_files, message, question)
            if not response:
                for other_file in other_files:
                    self._delete(other_file)
        return other_files

    def _check_file_previous_date(self, student_files: List[str], other_files: List[str]) -> List[str]:
        """
        Checking previous modification dates

        Args:
            student_files (List[str]): Student files list
            other_files (List[str]): Other files list

        Returns:
            List[str]: Update files list
        """
        update_files = []
        for file_path in student_files:
            if file_path in other_files:
                continue
            if isfile(file_path):
                client_update_date = datetime.fromtimestamp(os.path.getmtime(file_path),
                                                            tz=timezone.utc).isoformat()
                server_update_date = self._get_last_update_date(file_path)
                if server_update_date is not None and client_update_date > server_update_date:
                    update_files.append(file_path)
        if len(update_files) > 0:
            self._ask_for_download(update_files, LabelEnum.OLDER_VERSION.value, LabelEnum.REPLACE_FILE.value)
        return update_files

    def run(self):
        """Method running the worker"""
        self.running = True
        if self._has_gui:
            self._thread.start()
        else:
            self._worker()

    def stop(self):
        """Method stopping the worker"""
        if self.running:
            self.running = False
            if self._has_gui:
                self._thread.join()

    def _worker(self):
        """Method for the worker"""
        while self.running:
            files_path_watching = self._files_watching.copy().keys()
            self._post_or_delete_files_watching(files_path_watching)
            files_path_not_watching = [file_path for file_path in self._followed_files
                                       if file_path not in files_path_watching]
            self._post_new_files(files_path_not_watching)
            time.sleep(0.5)

    def _post_or_delete_files_watching(self, files_path):
        """Method for the files watching

        :param files_path: The files path
        """
        for file_path in files_path:
            if not isfile(file_path):
                self._delete(file_path)
            elif file_is_updated(file_path, self._files_watching[file_path]):
                self._post(file_path)

    def _post_new_files(self, files_path):
        """Method for the new files to watch

        :param files_path: The files path
        """
        for file_path in files_path:
            if isfile(file_path):
                self._post(file_path)

    def _handle_suspended(self) -> None:
        """Handles the suspended."""
        self.running = False
        signal.raise_signal(signal.SIGTERM)

    def _post(self, file_path) -> None:
        try:
            with open(file_path, "r", encoding='utf8') as file:
                data = {'code': file.read(),
                        'last_update_date': datetime.fromtimestamp(os.path.getmtime(file_path),
                                                                    tz=timezone.utc).isoformat()}
            file_name = file_path[len(self._model.directory.get()):]
            response = requests.post(self._model.url_api_action_file(file_name), data=data, timeout=TIMEOUT)
            if response.status_code in [StatusCode.OK, StatusCode.CREATED]:
                self._files_watching[file_path] = time_updated_file(file_path)
                if not self._has_gui and self.running:
                    self._get_progress()
                self._view.display_message(message=LabelEnum.UPDATING.value, level=MessageLevel.INFORMATION)
            elif response.status_code == StatusCode.SUSPENDED:
                self._handle_suspended()
            elif response.status_code == StatusCode.UNPROCESSABLE_ENTITY:
                self._view.display_message(message=response.json().get('error', 
                                        ErrorMessage.UNPROCESSABLE_ENTITY.value),
                                        level=MessageLevel.ERROR)
                self._files_watching[file_path] = time_updated_file(file_path)
            else: # StatusCode.BAD_REQUEST
                self._view.display_message(message=ErrorMessage.BAD_REQUEST.value, level=MessageLevel.ERROR)
        except UnicodeDecodeError:
            pass

    def _delete(self, file_path) -> None:
        file_name = file_path[len(self._model.directory.get()):]
        response = requests.delete(self._model.url_api_action_file(file_name), timeout=TIMEOUT)
        if response.status_code == StatusCode.OK:
            try:
                self._files_watching.pop(file_path)
            except KeyError:
                pass
            if not self._has_gui and self.running:
                self._get_progress()
        elif response.status_code == StatusCode.SUSPENDED:
            self._handle_suspended()

    def _get_files_to_follow(self) -> List[str]:
        """Method getting the server teacher file paths

        :return: The list of file paths
        """
        response = requests.get(self._model.url_api_file_paths(), timeout=TIMEOUT)
        content = loads(response.content)
        return [join(self._model.directory.get(), file['file_path']) for file in content]

    def _get_student_files(self) -> List[str]:
        """Method getting the server student file paths

        :return: The list of file paths
        """
        response = requests.get(self._model.url_api_student_file_paths(), timeout=TIMEOUT)
        content = loads(response.content)
        return [join(self._model.directory.get(), file['file_path']) for file in content]

    def _get_progress(self) -> None:
        """Method getting the student progress"""
        response = requests.get(self._model.url_api_get_progress(), timeout=TIMEOUT)
        self.fn_display(loads(response.content))

    def _get_last_update_date(self, file_path: str) -> Optional[datetime]:
        """
        Returns the last update date of the file stored in the database on the server.

        Args:
            file_path (str): The path or name of the file.

        Returns:
            Optional[datetime]: The last update date of the file, or None if it cannot be found.
        """
        try:
            # DRF on the server side allows data to be passed in the body of the GET request.
            # "json=" defines the type so that serialization by the requests library is possible.
            response = requests.get(self._model.url_update_date(), json={'file_path': file_path}, timeout=TIMEOUT)
            if response.status_code == StatusCode.OK:
                data = response.json()
                return data.get('update_date')
            if response.status_code == StatusCode.SUSPENDED:
                self._handle_suspended()
            else: # StatusCode.BAD_REQUEST
                self._view.display_message(message=ErrorMessage.DIRECTORY_DOES_NOT_EXIST.value,
                                           level=MessageLevel.ERROR)

        except requests.exceptions.RequestException as execp:
            self._view.display_message(message=_("HTTP request error: {e}").format(e=execp),
                                       level=MessageLevel.ERROR)
        except UnicodeDecodeError:
            self._view.display_message(message=_("Decoding error for file handling."),
                                       level=MessageLevel.ERROR)
        except Exception as execp:
            self._view.display_message(message=_("Error : {e}").format(e=execp),
                                       level=MessageLevel.ERROR)
        return None

    def _ask_for_download(self, download_files: List[str], message: str, question: str) -> bool:
        """
        Asks the view to prompt the user whether the file should be downloaded.

        Args:
            download_files (List[str]): List of files to be downloaded.
            message (str): Message indicating the update.
            question (str): Question for confirmation.

        Returns:
            bool: User's confirmation response for downloading.
        """
        files_path = "\n".join(f"- {file}" for file in download_files)
        choice: bool = self._view.ask_for_download(f"{message}\n {files_path}\n\n{question}\n")
        if choice:
            for download_file in download_files:
                # DRF on the server side allows data to be passed in the body of the GET request.
                # "json=" defines the type so that serialization by the requests library is possible.
                response = requests.get(self._model.url_download_files(),
                                        json={'file_path': download_file},
                                        stream=True, timeout=TIMEOUT)
                if response.status_code == StatusCode.OK:
                    try:
                        with open(download_file, 'wb') as file:
                            for chunk in response.iter_content(chunk_size=1024):
                                if chunk:
                                    file.write(chunk)
                        self._view.display_message(
                            message=_("The file {download_file} has been downloaded successfully.").format(
                                download_file=download_file), level=MessageLevel.SUCCESS)
                    except Exception as execp:
                        self._view.display_message(message=_("Error reading file! : {e}").format(e=execp),
                                                   level=MessageLevel.ERROR)
                elif response.status_code == StatusCode.SUSPENDED:
                    self._handle_suspended()
                else: # StatusCode.BAD_REQUEST
                    self._view.display_message(message=_("Error downloading the file {download_file}. \
                    Status code: {response_status_code}").format(download_file=download_file,
                                                                response_status_code=response.status_code),
                                            level=MessageLevel.ERROR)
        return choice
