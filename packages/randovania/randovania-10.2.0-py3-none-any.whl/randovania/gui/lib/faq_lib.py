from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6 import QtCore, QtWidgets

if TYPE_CHECKING:
    from randovania.game.game_enum import RandovaniaGame


def format_game_faq(game: RandovaniaGame, widget: QtWidgets.QLabel) -> None:
    widget.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
    widget.setText("\n\n&nbsp;\n".join(f"### {question}\n{answer}" for question, answer in game.data.faq))
