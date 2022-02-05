#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import Client, __version__

from . import API_HASH, APP_ID, LOGGER, \
    USER_SESSION


class User(Client):
    def __init__(self):
        super().__init__(
            USER_SESSION,
            api_hash=5820bc246505e0ff60af5391d649f9a6,
            api_id=8406611,
            workers=4
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
