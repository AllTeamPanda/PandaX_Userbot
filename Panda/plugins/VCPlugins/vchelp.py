from . import vcClient

plugin_category = "plugins"


@vcClient.ilhammansiz_cmd(
    pattern="play(?: |$)(.*)",
    command=("play", plugin_category),
    info={
        "header": "Play the song in voice chat.",
        "description": "Play the song in voice chat, or add the song to queue..",
        "usage": "{tr}play <song name/link>",
        "examples": ["{tr}play"],
    },
)
