"""Module for the abstract theme"""
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
import abc


class BaseTheme(abc.ABC): # pylint: disable=no-member
    """Class for the abstract theme"""
    @classmethod
    @abc.abstractmethod # pylint: disable=no-member
    def theme_id(cls):
        """Returning the theme id"""

    @classmethod
    @abc.abstractmethod # pylint: disable=no-member
    def theme_name(cls):
        """Returning the theme name"""

    @classmethod
    @abc.abstractmethod # pylint: disable=no-member
    def use_theme(cls, config):
        """The use theme"""
        config.set_theme(cls.theme_id())
