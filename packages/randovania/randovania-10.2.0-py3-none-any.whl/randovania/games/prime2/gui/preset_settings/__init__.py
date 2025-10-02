from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from randovania.gui.lib.window_manager import WindowManager
    from randovania.gui.preset_settings.preset_tab import PresetTab
    from randovania.interface_common.preset_editor import PresetEditor


def prime2_preset_tabs(editor: PresetEditor, window_manager: WindowManager) -> list[type[PresetTab]]:
    from randovania.games.prime2.gui.preset_settings.echoes_beam_configuration_tab import PresetEchoesBeamConfiguration
    from randovania.games.prime2.gui.preset_settings.echoes_dock_rando_tab import PresetEchoesDockRando
    from randovania.games.prime2.gui.preset_settings.echoes_goal_tab import PresetEchoesGoal
    from randovania.games.prime2.gui.preset_settings.echoes_item_pool_tab import EchoesPresetItemPool
    from randovania.games.prime2.gui.preset_settings.echoes_patches_tab import PresetEchoesPatches
    from randovania.games.prime2.gui.preset_settings.echoes_starting_area import PresetEchoesStartingArea
    from randovania.games.prime2.gui.preset_settings.echoes_teleporters_tab import PresetTeleportersPrime2
    from randovania.games.prime2.gui.preset_settings.echoes_translators_tab import PresetEchoesTranslators
    from randovania.gui.preset_settings.generation_tab import PresetGeneration
    from randovania.gui.preset_settings.hints_tab import PresetHints
    from randovania.gui.preset_settings.location_pool_tab import PresetLocationPool
    from randovania.gui.preset_settings.patcher_energy_tab import PresetPatcherEnergy
    from randovania.gui.preset_settings.trick_level_tab import PresetTrickLevel

    return [
        PresetTrickLevel,
        PresetGeneration,
        PresetHints,
        PresetEchoesGoal,
        PresetLocationPool,
        EchoesPresetItemPool,
        PresetPatcherEnergy,
        PresetTeleportersPrime2,
        PresetEchoesStartingArea,
        PresetEchoesDockRando,
        PresetEchoesTranslators,
        PresetEchoesBeamConfiguration,
        PresetEchoesPatches,
    ]
