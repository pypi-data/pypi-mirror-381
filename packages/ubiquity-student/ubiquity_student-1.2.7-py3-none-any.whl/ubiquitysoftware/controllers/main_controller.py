"""Module managing the application controller"""
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
import os.path
import shutil
from datetime import datetime
from enum import unique, Enum, auto
from io import BytesIO
from json import loads
from json.decoder import JSONDecodeError
from typing import Optional
from zipfile import ZipFile

import requests

from ubiquitysoftware.controllers.config_file import Config
from ubiquitysoftware.controllers.worker import Worker, StatusCode
from ubiquitysoftware.version import VERSION
from ubiquitysoftware.model import Model
from ubiquitysoftware.views.utils import print_message, LabelEnum, ErrorMessage, print_value, ConsoleColor



@unique
class Returns(Enum):
    """Enum class for returns on submit method"""
    CHOICE = auto()
    OK = auto()
    ERROR = auto()


class MainController:
    """Class managing the main controller"""
    def __init__(self, config: Config, model: Model, has_gui) -> None:
        super().__init__()
        self.model = model
        self.view = None
        self.worker = None
        self.config = config
        self.has_gui = has_gui
        self.is_new_project = False

    def set_view(self, view):
        """ Méthode pour injecter la vue après la création du contrôleur. """
        self.view = view


    def init_values(self) -> None:
        """Method initializing the state values"""
        if Config.DEFAULT in self.config.configs[Config.HISTORY] and True not in [self.model.has_server(),
                                                                                  self.model.has_student_key(),
                                                                                  self.model.has_group_key(),
                                                                                  self.model.has_directory()]:
            self.model.server.set(self.config.configs[Config.HISTORY][Config.DEFAULT][Config.SERVER])
            self.model.student_key.set(self.config.configs[Config.HISTORY][Config.DEFAULT][Config.STUDENT_KEY])

    def _check_values(self) -> Optional[ErrorMessage]:
        """Method verifying if the state values are valid

        :return: True if the values are valid, False if not
        """
        error = self._check_values_not_empty()
        if error is None:
            error = self._check_connection()
        if error is None:
            error = self._check_directory()
        if isinstance(error, ErrorMessage):
            self.model.error.set(error.value)
            return error
        return None

    def _check_values_not_empty(self) -> Optional[ErrorMessage]:
        """Method verifying if the state values are not empty

        :return: None if the values are valid, Error if not
        """
        if "" in [self.model.server.get(), self.model.student_key.get(),
                  self.model.group_key.get(), self.model.directory.get()]:
            return ErrorMessage.EMPTY_FIELD
        return None

    def _check_version(self) -> Optional[ErrorMessage]:
        """Method verifying if the client version is OK

        :return: None if the client version is OK, Error if not
        """
        response = requests.get(self.model.url_api_check_version(), timeout=5)
        try:
            content = loads(response.content)
            self.model.client_version_min = content['version_min']
            if content['version_min'] <= VERSION:
                return None
        except JSONDecodeError:
            return None
        return ErrorMessage.VERSION

    def _check_connection(self) -> Optional[ErrorMessage]:
        """Method verifying if the connection is OK

        :return: None if the status code is OK, Error if not
        """
        try:
            response = self._check_version()
            if response:
                return response
            response = requests.get(self.model.url_api_connection_check(), timeout=5)
            if response.status_code == StatusCode.SUSPENDED:
                return ErrorMessage.PRACTICAL_WORK_SUSPENDED
            if response.status_code != StatusCode.OK:
                if self.config.check_is_config(self.model):
                    return ErrorMessage.CONFIG_DELETED
                return ErrorMessage.INVALID_KEYS
            content = loads(response.content)
            self.model.name.set(content['name'])
            self.model.date_update.set(content['date_update'])
            self.is_new_project = content['is_new']
        except requests.exceptions.RequestException:
            return ErrorMessage.CONNECTION_FAILED
        return None

    def _check_directory(self) -> Optional[ErrorMessage]:
        """Method verifying if the directory exits

        :return: None if exists, Error if not
        """
        if not os.path.exists(self.model.directory.get()):
            return ErrorMessage.DIRECTORY_DOES_NOT_EXIST
        return None

    def extract_zip(self, has_color: bool = False) -> None:
        """Extract a zip file to the working directory

        :param has_color: True if text has color, False if not
        """
        response = requests.get(self.model.url_api_get_student_environment(), timeout=5)
        with ZipFile(BytesIO(response.content)) as zip_file:
            print_message(LabelEnum.STUDENT_ENVIRONMENT_RECOVERED)
            for filename in zip_file.namelist():
                if os.path.exists(os.path.join(self.model.directory.get(), filename)):
                    print_message(LabelEnum.WARNING_FILE_EXISTS,
                                color=ConsoleColor.WARNING if has_color else None,
                                end=" ")
                    print_value(filename)
                else:
                    zip_file.extract(filename, self.model.directory.get())
                    attr = zip_file.getinfo(filename).external_attr >> 16
                    if attr != 0:
                        os.chmod(os.path.join(self.model.directory.get(), filename), attr)
        print_message(LabelEnum.EXTRACT_ZIP_COMPLETED, 1)

    def extract_restored_zip(self) -> None:
        """Extract a restored zip file to the working directory"""
        response = requests.get(self.model.url_api_restore_student_environment(), timeout=5)
        print_message(LabelEnum.RESTORING)
        with ZipFile(BytesIO(response.content)) as zip_file:
            print_message(LabelEnum.STUDENT_ENVIRONMENT_RECOVERED)
            for filename in zip_file.namelist():
                if not os.path.exists(os.path.join(self.model.directory.get(), filename)):
                    zip_file.extract(filename, self.model.directory.get())
                    print_message(LabelEnum.EXTRACT_RESTORED_FILE, end=" ")
                    print_value(filename)
        print_message(LabelEnum.EXTRACT_ZIP_COMPLETED, 1)

    def extract_updated_zip(self) -> None:
        """Extract a update zip file to the working directory"""
        response = requests.get(self.model.url_api_update_student_environment(), timeout=5)
        print_message(LabelEnum.UPDATING)
        with ZipFile(BytesIO(response.content)) as zip_file:
            print_message(LabelEnum.STUDENT_ENVIRONMENT_RECOVERED)
            for filename in zip_file.namelist():
                zip_file.extract(filename, self.model.directory.get())
                print_message(LabelEnum.EXTRACT_UPDATED_FILE, end=" ")
                print_value(filename)
        print_message(LabelEnum.EXTRACT_ZIP_COMPLETED, 1)

    def copy_to_back(self):
        """Method copying files to the ".ubiquity_backs" directory"""
        local_file_names = os.listdir(self.model.directory.get())
        back_base = os.path.join(self.model.directory.get(), ".ubiquity_backs")
        back_dir = os.path.join(back_base, f'back_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}')
        os.makedirs(back_dir, mode=0o755, exist_ok=True)

        response = requests.get(self.model.url_api_get_student_environment(), timeout=5)
        with ZipFile(BytesIO(response.content)) as zip_file:
            for server_practical_work_file_name in zip_file.namelist():
                if server_practical_work_file_name in local_file_names:
                    old_file_path = os.path.join(self.model.directory.get(), server_practical_work_file_name)
                    shutil.move(old_file_path, back_dir)
                    zip_file.extract(server_practical_work_file_name, self.model.directory.get())

    def _check_is_new(self) -> bool:
        """Method checking if is a new project

        :return: True if is a new project, False if not
        """
        return not self.config.check_is_config(self.model)

    def _add_config(self) -> None:
        """Method adding a config"""
        self.config.add_config(self.model)
        self.config.init_update_config(self.model)

    def add_update_config(self):
        """Method adding an update for the current practical work"""
        self.config.add_update_config(self.model)

    def update_with_config(self, config: dict) -> None:
        """Method updating the model with the config values

        :param config: The config
        """
        self.model.server.set(config[Config.SERVER])
        self.model.student_key.set(config[Config.STUDENT_KEY])
        self.model.group_key.set(config[Config.GROUP_KEY])
        self.model.directory.set(config[Config.DIRECTORY])
        self.model.error.set('')

    def run(self, fn_display=None) -> None:
        """Method running the worker and add values in the config file"""
        self._add_config()
        if self.has_gui:
            self.worker = Worker(self.model, self.has_gui, self.view)
        else:
            self.worker = Worker(self.model, self.has_gui, self.view, fn_display)
        self.worker.run()

    def stop(self) -> None:
        """Method stopping the worker"""
        self.worker.stop()

    def submit(self, has_color: bool = False) -> Returns:
        """Method verifying the values and run the worker

        :param has_color: True if text has color, False if not
        :return: The status of the return on the form validation
        """
        error = self._check_values()
        if not isinstance(error, ErrorMessage):
            if self.is_new_project:
                self.extract_zip(has_color)
            elif not self.config.check_directory(self.model):
                return Returns.CHOICE
            return Returns.OK
        if error is not ErrorMessage.VERSION and error is not ErrorMessage.CONNECTION_FAILED \
                and error is not ErrorMessage.PRACTICAL_WORK_SUSPENDED and self.config.check_is_config(self.model):
            self.config.remove_config(self.model)
        return Returns.ERROR
