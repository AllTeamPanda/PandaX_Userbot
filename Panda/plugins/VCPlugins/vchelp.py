from . import pandaub

plugin_category = "plugins"


@pandaub.ilhammansiz_cmd(
    pattern="covid(?: |$)(.*)",
    command=("covid", plugin_category),
    info={
        "header": "To get latest information about covid-19.",
        "description": "Get information about covid-19 data in the given country/state.",
        "usage": "{tr}covid <state_name/country_name>",
        "examples": ["{tr}covid", "{tr}covid", "{tr}covid world"],
    },
)
