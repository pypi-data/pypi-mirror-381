import configparser
import itertools
import json
from pathlib import Path

locale = configparser.ConfigParser()


def get_localized_name(n: str) -> str:
    for k in ["item-name", "entity-name", "fluid-name", "equipment-name", "recipe-name", "technology-name"]:
        if n in locale[k]:
            return locale[k][n]
        if f"{n}-1" in locale[k]:
            return locale[k][f"{n}-1"]

    if n.startswith("fill-"):
        return f"Fill {locale['fluid-name'][n[5:-7]]} barrel"

    if n.endswith("-barrel"):
        return f"{locale['fluid-name'][n[:-7]]} barrel"

    hardcoded_names = {
        "solid-fuel-from-heavy-oil": "Solid Fuel (Heavy Oil)",
        "solid-fuel-from-light-oil": "Solid Fuel (Light Oil)",
        "solid-fuel-from-petroleum-gas": "Solid Fuel (Petroleum Gas)",
    }

    try:
        return hardcoded_names[n]
    except KeyError:
        i = n.rfind("-")
        if i != -1:
            front, number = n[:i], n[i + 1 :]
            if number.isdigit():
                return f"{get_localized_name(front)} {number}"
        raise


def read_locales(factorio_path: Path) -> None:
    with factorio_path.joinpath("data/base/locale/en/base.cfg").open() as fp:
        locale.read_file(itertools.chain(["[global]"], fp), source="base.cfg")
    locale.read([factorio_path.joinpath("mods/randovania/locale/en/strings.cfg")])


def template_req(name: str) -> dict:
    return {
        "type": "template",
        "data": name,
    }


def tech_req(tech_name: str) -> dict:
    return {
        "type": "resource",
        "data": {
            "type": "items",
            "name": tech_name,
            "amount": 1,
            "negate": False,
        },
    }


def and_req(entries: list, comment: str | None = None) -> dict:
    if len(entries) == 1:
        return entries[0]
    return {"type": "and", "data": {"comment": comment, "items": entries}}


def or_req(entries: list, comment: str | None = None) -> dict:
    if len(entries) == 1:
        return entries[0]
    return {"type": "or", "data": {"comment": comment, "items": entries}}


def load_existing_pickup_ids(region_path: Path) -> dict[str, int]:
    try:
        with region_path.open() as f:
            all_areas = json.load(f)["areas"]
    except FileNotFoundError:
        return {}

    result = {}

    for area in all_areas.values():
        for node_data in area["nodes"].values():
            if node_data["node_type"] == "pickup":
                result[node_data["extra"]["original_tech"]] = node_data["pickup_index"]

    return result
