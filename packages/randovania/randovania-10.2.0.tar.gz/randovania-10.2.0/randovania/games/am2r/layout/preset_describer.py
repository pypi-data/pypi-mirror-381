from __future__ import annotations

from typing import TYPE_CHECKING

from randovania.games.am2r.layout.am2r_configuration import AM2RArtifactConfig, AM2RConfiguration
from randovania.layout.preset_describer import (
    GamePresetDescriber,
    fill_template_strings_from_tree,
    message_for_required_mains,
)

if TYPE_CHECKING:
    from randovania.game.gui import ProgressiveItemTuples
    from randovania.layout.base.base_configuration import BaseConfiguration


def describe_artifacts(artifacts: AM2RArtifactConfig) -> list[dict[str, bool]]:
    has_artifacts = artifacts.required_artifacts > 0
    if has_artifacts and artifacts.prefer_anywhere:
        return [
            {
                f"{artifacts.required_artifacts} Metroid DNA out of {artifacts.placed_artifacts}": True,
            },
            {
                "Place anywhere": artifacts.prefer_anywhere,
            },
        ]
    elif has_artifacts:
        return [
            {
                f"{artifacts.required_artifacts} Metroid DNA out of {artifacts.placed_artifacts}": True,
            },
            {
                "Prefers Metroids": artifacts.prefer_metroids,
                "Prefers major bosses": artifacts.prefer_bosses,
            },
        ]
    else:
        return [
            {
                "Kill the Queen": True,
            }
        ]


class AM2RPresetDescriber(GamePresetDescriber):
    def format_params(self, configuration: BaseConfiguration) -> dict[str, list[str]]:
        assert isinstance(configuration, AM2RConfiguration)

        def describe_probability(probability: int, attribute: str) -> str | None:
            if probability == 0:
                return None

            return f"{probability / 10:.1f}% chance of a room being {attribute}"

        darkness_probability = describe_probability(configuration.darkness_chance, "dark")
        submerged_water_probability = describe_probability(configuration.submerged_water_chance, "submerged in water")
        submerged_lava_probability = describe_probability(configuration.submerged_lava_chance, "submerged in lava")

        template_strings = super().format_params(configuration)

        extra_message_tree = {
            "Game Changes": [
                message_for_required_mains(
                    configuration.ammo_pickup_configuration,
                    {
                        "Missiles need Launcher": "Missile Tank",
                        "Super Missiles need Launcher": "Super Missile Tank",
                        "Power Bombs need Launcher": "Power Bomb Tank",
                    },
                    mains_are_default_required=False,
                ),
                {f"Energy per Tank: {configuration.energy_per_tank}": configuration.energy_per_tank != 100},
                {f"First Suit Damage Reduction {configuration.first_suit_dr}%": configuration.first_suit_dr != 50},
                {f"Second Suit Damage Reduction {configuration.second_suit_dr}%": configuration.second_suit_dr != 75},
                {
                    f"Transport Pipes: {configuration.teleporters.description('transporters')}": (
                        not configuration.teleporters.is_vanilla
                    )
                },
                {
                    "Enable Septoggs": configuration.septogg_helpers,
                    "Add new Nest Pipes": configuration.nest_pipes,
                    "Respawn bomb blocks": configuration.respawn_bomb_blocks,
                    "Softlock block checks": configuration.softlock_prevention_blocks,
                    "Screw blocks near Pipes": configuration.screw_blocks,
                    "Grave Grotto Bomb Blocks": configuration.grave_grotto_blocks,
                    "Industrial Complex Bomb Blocks": configuration.a3_entrance_blocks,
                },
                {
                    "Skip gameplay cutscenes": configuration.skip_cutscenes,
                    "Skip item cutscenes": configuration.skip_item_cutscenes,
                    "Enable Fusion Mode": configuration.fusion_mode,
                    "Open Missile Doors with Supers": configuration.supers_on_missile_doors,
                },
                {
                    "Horizontally flipped gameplay": configuration.horizontally_flip_gameplay,
                    "Vertically flipped gameplay": configuration.vertically_flip_gameplay,
                    darkness_probability: darkness_probability is not None,
                    submerged_water_probability: submerged_water_probability is not None,
                    submerged_lava_probability: submerged_lava_probability is not None,
                },
            ],
            "Goal": describe_artifacts(configuration.artifacts),
        }

        fill_template_strings_from_tree(template_strings, extra_message_tree)

        return template_strings

    def progressive_items(self) -> ProgressiveItemTuples:
        from randovania.games.am2r.layout import progressive_items

        return progressive_items.tuples()
