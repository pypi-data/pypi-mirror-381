from bluer_objects import README

from bluer_sbc.designs.consts import assets2

image_template = assets2 + "bluer-shelter/{}?raw=true"

marquee = README.Items(
    [
        {
            "name": "bluer-shelter",
            "marquee": image_template.format("01.png"),
            "url": "./bluer_sbc/docs/bluer-shelter.md",
        }
    ]
)

items = README.Items(
    [
        {
            "marquee": image_template.format(f"{index+1:02}.png"),
            "name": "",
        }
        for index in range(4)
    ],
)
