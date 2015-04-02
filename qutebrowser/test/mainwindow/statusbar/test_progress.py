# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2014-2015 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
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


"""Test Percentage widget."""

from collections import namedtuple

import pytest

from qutebrowser.browser import webview
from qutebrowser.mainwindow.statusbar.progress import Progress


@pytest.fixture
def progress_widget(qtbot, default_config):
    """
    Creates a Progress widget and checks it initial state.
    """
    widget = Progress()
    qtbot.add_widget(widget)
    assert not widget.isVisible()
    assert not widget.isTextVisible()
    return widget


def test_load_started(progress_widget):
    """
    Args:
        progress_widget: Progress widget that will be tested.
    """
    progress_widget.on_load_started()
    assert progress_widget.value() == 0
    assert progress_widget.isVisible()


# mock tab object
Tab = namedtuple('Tab', 'progress load_status')


@pytest.mark.parametrize('tab, expected_visible', [
    (Tab(15, webview.LoadStatus.loading), True),
    (Tab(100, webview.LoadStatus.success), False),
    (Tab(100, webview.LoadStatus.error), False),
    (Tab(100, webview.LoadStatus.warn), False),
    (Tab(100, webview.LoadStatus.none), False),
])
def test_tab_changed(progress_widget, tab, expected_visible):
    """
    Test that progress widget value and visibility state match expectations,
    using a dummy Tab object.

    Args:
        progress_widget: Progress widget that will be tested.
    """
    progress_widget.on_tab_changed(tab)
    assert (progress_widget.value(), progress_widget.isVisible()) == \
           (tab.progress, expected_visible)