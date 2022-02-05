#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import Client, __version__

from . import API_HASH, APP_ID, LOGGER, \
    BOT_SESSION, BOT_TOKEN 

from .user import User



class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            BOT_SESSION,
            api_hash=5820bc246505e0ff60af5391d649f9a6,
            api_id=8406611,
            plugins={
                "root": "bot/plugins"
            },
            workers=4,
            bot_token=5096855002:AAHmLn_vnq7OLXxAs6qR8hOalJMqqL6hmpg
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
