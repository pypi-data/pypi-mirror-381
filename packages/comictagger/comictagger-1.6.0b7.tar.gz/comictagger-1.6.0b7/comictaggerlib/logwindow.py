"""A PyQT4 dialog to a text file or log"""

#
# Copyright 2012-2014 ComicTagger Authors
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
from __future__ import annotations

import logging

from PyQt6 import QtCore, QtWidgets, uic

from comictaggerlib.ui import qtutils, ui_path

logger = logging.getLogger(__name__)


class LogWindow(QtWidgets.QDialog):
    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super().__init__(parent)

        with (ui_path / "logwindow.ui").open(encoding="utf-8") as uifile:
            uic.loadUi(uifile, self)

        self.setWindowFlags(
            QtCore.Qt.WindowType(
                self.windowFlags()
                | QtCore.Qt.WindowType.WindowSystemMenuHint
                | QtCore.Qt.WindowType.WindowMaximizeButtonHint
            )
        )

    def set_text(self, text: str | bytes | None) -> None:
        try:
            if text is not None:
                if isinstance(text, bytes):
                    text = text.decode("utf-8")
                self.textEdit.setPlainText(text)
        except AttributeError:
            pass
        except Exception as e:
            logger.exception("Displaying raw tags failed")
            qtutils.qt_error("Displaying raw tags failed:", e)
