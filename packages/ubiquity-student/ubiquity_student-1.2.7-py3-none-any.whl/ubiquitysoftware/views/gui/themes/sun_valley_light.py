"""Module for the sun valley light theme"""
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

from . import sv_ttk
from .base import BaseTheme
from ...utils import gettext

_ = gettext.gettext


class SunValleyLightTheme(BaseTheme):
    """Class for the sun valley light theme"""
    @classmethod
    def theme_id(cls):
        return "sun-valley-light"

    @classmethod
    def theme_name(cls):
        return _("Sun Valley light")

    @classmethod
    def use_theme(cls, config):
        super().use_theme(config)
        sv_ttk.use_light_theme()
