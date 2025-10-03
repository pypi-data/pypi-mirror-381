import os
from typing import List

from bluer_options.help.functions import get_help
from bluer_objects import file, README

from bluer_sbc import NAME, VERSION, ICON, REPO_NAME
from bluer_sbc.designs.cheshmak import items as cheshmak_items
from bluer_sbc.designs.cheshmak import marquee as cheshmak_marquee
from bluer_sbc.designs.blue_bracket import items as blue_bracket_items
from bluer_sbc.designs.bluer_swallow import items as bluer_swallow_items
from bluer_sbc.designs.bluer_swallow import marquee as bluer_swallow_marquee
from bluer_sbc.designs.bluer_swallow_head import items as bluer_swallow_head_items
from bluer_sbc.designs.bluer_swallow_head import marquee as bluer_swallow_head_marquee
from bluer_sbc.designs.bryce import items as bryce_items
from bluer_sbc.designs.bryce import marquee as bryce_marquee
from bluer_sbc.designs.nafha import items as nafha_items
from bluer_sbc.designs.nafha import marquee as nafha_marquee
from bluer_sbc.designs.ultrasonic_sensor_tester import (
    marquee as ultrasonic_sensor_tester_marquee,
)
from bluer_sbc.designs.ultrasonic_sensor_tester import (
    items as ultrasonic_sensor_tester_items,
)
from bluer_sbc.help.functions import help_functions


def build():
    return all(
        README.build(
            items=readme.get("items", []),
            cols=readme.get("cols", 3),
            path=os.path.join(file.path(__file__), readme["path"]),
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
            help_function=lambda tokens: get_help(
                tokens,
                help_functions,
                mono=True,
            ),
        )
        for readme in [
            {
                "items": bluer_swallow_marquee
                + bluer_swallow_head_marquee
                + ultrasonic_sensor_tester_marquee
                + bryce_marquee
                + cheshmak_marquee
                + nafha_marquee
                + blue_bracket_items,
                "path": "..",
            },
            {
                "items": bluer_swallow_items,
                "path": "./docs/bluer-swallow.md",
            },
            {
                "items": bluer_swallow_head_items,
                "path": "./docs/bluer-swallow-head.md",
            },
            {
                "items": bryce_items,
                "path": "./docs/bryce.md",
            },
            {
                "items": ultrasonic_sensor_tester_items,
                "path": "./docs/ultrasonic-sensor-tester.md",
            },
            {
                "items": cheshmak_items,
                "path": "./docs/cheshmak.md",
            },
            {
                "cols": 4,
                "items": nafha_items,
                "path": "./docs/nafha.md",
            },
        ]
        + [
            {"path": f"./docs/aliases/{item}.md"}
            for item in [
                "camera",
                "hardware",
                "rpi",
            ]
        ]
    )
