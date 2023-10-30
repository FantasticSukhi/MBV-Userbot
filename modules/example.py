#  Moon-Userbot - telegram userbot
#  Copyright (C) 2020-present Moon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix

#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


# if your module has packages from PyPi

# from utils.scripts import import_library
# example_1 = import_library("example_1")
# example_2 = import_library("example_2")

# import_library() will automatically install required library
# if it isn't installed


@Client.on_message(filters.command("example_edit", prefix) & filters.me)
async def example_edit(client: Client, message: Message):
    try:
        await message.edit("<code>This is an example module</code>")
    except Exception as e:
        await message.edit(f"<code>{e.__class__.__name__}: {str(e)}</code>")


@Client.on_message(filters.command("example_send", prefix) & filters.me)
async def example_send(client: Client, message: Message):
    try:
        await client.send_message(message.chat.id, "<b>This is an example module</b>")
    except Exception as e:
        await message.edit(f"<code>{e.__class__.__name__}: {str(e)}</code>")


# This adds instructions for your module
modules_help.update(
    {
        "example": {
            "example_send": "This command sends an example message",
            "example_edit": "This command edits a message with an example text",
        }
    }
)

# modules_help["example"] = { "example_send [text]": "example send" }
#                  |            |              |        |
#                  |            |              |        └─ command description
#           module_name         command_name   └─ optional command arguments
#        (only snake_case)   (only snake_case too)
