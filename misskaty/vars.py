# * @author        Yasir Aris M <yasiramunandar@gmail.com>
# * @date          2023-06-21 22:12:27
# * @projectName   MissKatyPyro
# * Copyright ©YasirPedia All rights reserved
import sys
from logging import getLogger
from os import environ

import dotenv

LOGGER = getLogger("MissKaty")

dotenv.load_dotenv("config.env", override=True)

# Required ENV
API_ID = environ.get("API_ID", "29722120")
if not API_ID:
    LOGGER.error("API_ID variable is missing! Exiting now")
    sys.exit(1)
else:
    API_ID = int(API_ID)
API_HASH = environ.get("API_HASH", "91f3bf8651edfa748856cfcad07f55bb")
if not API_HASH:
    LOGGER.error("API_HASH variable is missing! Exiting now")
    sys.exit(1)
BOT_TOKEN = environ.get("BOT_TOKEN", "6663040181:AAEdRPMg1h8CaImyX5Wf8ERWNdUg8y97S-k")
if not BOT_TOKEN:
    LOGGER.error("BOT_TOKEN variable is missing! Exiting now")
    sys.exit(1)
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://helloyeager8:dSaini9485@cluster0.bhqp2fq.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
if not DATABASE_URI:
    LOGGER.error("DATABASE_URI variable is missing! Exiting now")
    sys.exit(1)
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1001829052958")
if not LOG_CHANNEL:
    LOGGER.error("LOG_CHANNEL variable is missing! Exiting now")
    sys.exit(1)
else:
    LOG_CHANNEL = int(LOG_CHANNEL)

# Optional ENV
USER_SESSION = environ.get("USER_SESSION")
DATABASE_NAME = environ.get("DATABASE_NAME", "MissKatyDB")
TZ = environ.get("TZ", "Asia/Kolkata")
        for x in environ.get(
            "SUDO",
            "1983471689",
        ).split()
    }
)
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "YasirPediaChannel")
AUTO_RESTART = environ.get("AUTO_RESTART", False)
OPENAI_API = environ.get("OPENAI_API")

## Config For AUtoForwarder
# Forward From Chat ID
FORWARD_FROM_CHAT_ID = list(
    {
        int(x)
        for x in environ.get(
            "FORWARD_FROM_CHAT_ID",
            "-1001128045651 -1001455886928 -1001686184174",
        ).split()
    }
)
# Forward To Chat ID
FORWARD_TO_CHAT_ID = list(
    {int(x) for x in environ.get("FORWARD_TO_CHAT_ID", "-1001210537567").split()}
)
FORWARD_FILTERS = list(set(environ.get("FORWARD_FILTERS", "video document").split()))
BLOCK_FILES_WITHOUT_EXTENSIONS = bool(
    environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", True)
)
BLOCKED_EXTENSIONS = list(
    set(
        environ.get(
            "BLOCKED_EXTENSIONS",
            "html htm json txt php gif png ink torrent url nfo xml xhtml jpg",
        ).split()
    )
)
MINIMUM_FILE_SIZE = environ.get("MINIMUM_FILE_SIZE")
CURRENCY_API = environ.get("CURRENCY_API")
