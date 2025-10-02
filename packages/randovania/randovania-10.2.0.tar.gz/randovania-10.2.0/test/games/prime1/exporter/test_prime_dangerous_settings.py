from __future__ import annotations

from randovania.layout.layout_description import LayoutDescription


def test_dangerous_settings(test_files_dir):
    rdvgame = test_files_dir.joinpath("log_files", "prime1_crazy_seed.rdvgame")
    layout_description = LayoutDescription.from_file(rdvgame)
    preset = layout_description.get_preset(0)

    assert preset.dangerous_settings() == [
        "Permanently Locked is unsafe as a target in Door Lock Types",
        "One-way anywhere teleporters",
        "Shuffled Item Position",
        "Room Randomizer",
        "Extra Superheated Rooms",
        "Submerged Rooms",
        "Dangerous Gravity Suit Logic",
        "Dangerous Random Enemy Attributes",
    ]
