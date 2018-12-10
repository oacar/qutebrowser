# Copyright 2018 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""Hooks for extensions."""

import importlib
import types
import typing


from qutebrowser.extensions import loader


class init:  # noqa: N801,N806 pylint: disable=invalid-name

    """Decorator to mark a function to run when initializing."""

    def __call__(self, func: typing.Callable) -> typing.Callable:
        module = importlib.import_module(func.__module__)
        info = loader.add_module_info(module)
        info.init_hook = func