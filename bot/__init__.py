#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
from logging.handlers import RotatingFileHandler

APP_ID = int(os.environ.get("8406611"))

API_HASH = os.environ.get("5820bc246505e0ff60af5391d649f9a6")

BOT_TOKEN = os.environ.get("5096855002:AAHmLn_vnq7OLXxAs6qR8hOalJMqqL6hmpg")

BOT_SESSION = os.environ.get("BOT_SESSION", "bot")

DB_URI = os.environ.get("mongodb+srv://youtick:youtick@cluster0.qaaju.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("USER_SESSION")

LOG_FILE_NAME = "autofilterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
