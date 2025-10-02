from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import MagicMock

import pytest

from randovania.bitpacking import construct_pack
from randovania.network_common.remote_inventory import RemoteInventory
from randovania.server import database
from randovania.server.multiplayer import web_api

if TYPE_CHECKING:
    import peewee

    from randovania.server.server_app import ServerApp


def test_admin_sessions(server_app: ServerApp, solo_two_world_session: database.MultiplayerSession) -> None:
    # Setup
    web_api.setup_app(server_app)

    # Run
    with server_app.app.test_request_context("/sessions"):
        result = web_api.admin_sessions(MagicMock())

    entry = "<td>The Name</td><td>2020-05-02 10:20:00+00:00</td><td>1</td><td>2</td><td>False</td></tr>"
    assert entry in result


def test_admin_session_missing(server_app: ServerApp, clean_database: peewee.SqliteDatabase) -> None:
    # Setup
    web_api.setup_app(server_app)

    # Run
    with server_app.app.test_request_context("/session/1"):
        result = web_api.admin_session(MagicMock(), 1)

    assert result == ("Session not found", 404)


def test_admin_session_exists(server_app: ServerApp, solo_two_world_session: database.MultiplayerSession) -> None:
    # Setup
    web_api.setup_app(server_app)

    assoc = database.WorldUserAssociation.get_by_instances(world=1, user=1234)
    assoc.inventory = construct_pack.encode(
        {"Charge": 1},
        RemoteInventory,
    )
    assoc.save()

    # Run
    with server_app.app.test_request_context("/session/1"):
        result = web_api.admin_session(MagicMock(), 1)

    entry1 = "<td>The Name</td><td>World 1</td><td>prime1</td><td>Disconnected</td><td>Charge Beam x1</td>"
    entry2 = "<td>The Name</td><td>World 2</td><td>prime2</td><td>Disconnected</td><td>Missing</td><td>False</td>"
    assert entry1 in result
    assert entry2 in result


def test_delete_session_get(server_app: ServerApp, solo_two_world_session: database.MultiplayerSession) -> None:
    # Setup
    web_api.setup_app(server_app)

    # Run
    with server_app.app.test_request_context("/session/1/delete", method="GET"):
        result = web_api.delete_session(MagicMock(), 1)

    assert result == '<form method="POST"><input type="submit" value="Confirm delete"></form>'
    assert database.MultiplayerSession.get_by_id(1) == solo_two_world_session


def test_delete_session_post(server_app: ServerApp, solo_two_world_session: database.MultiplayerSession) -> None:
    # Setup
    web_api.setup_app(server_app)

    # Run
    with server_app.app.test_request_context("/session/1/delete", method="POST"):
        result = web_api.delete_session(MagicMock(), 1)

    assert result == "Session deleted. <a href='/sessions'>Return to list</a>"

    with pytest.raises(database.MultiplayerSession.DoesNotExist):
        database.MultiplayerSession.get_by_id(1)
