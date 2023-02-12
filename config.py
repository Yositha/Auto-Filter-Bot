
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5808072594:AAHZ_KkXSNPC50EopooQagqlZCcQfzlRvnw")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "23249233"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "a3b61c2cdbb13ed5893be97ea0c3ea85")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQFiwVEAKdnjY-s48CwVrIB3NkaDo1hIIeUwyQ9-Jl8-700KMbk3LiAeplB6SvoerZN37mPQZ4GFybSNwNSRQTo_C0qDvcaT3r7adsvjF6z3uVGqLOrMhJn_4C-Onn_RSpni_Hypv8YqpuQ9lZvOkwf2CY0K9K4mI2MRuI-WV_nLpCjXdz5brB-2fVh2xUEhIVW2c_kh0Su3ecgqgJ7zSV2VBwPp-HabM1s_viVoP9YgZoRSoFX_HdKzRMlY_ExsPbbR8hNaY7e8PqkOe1wFqbeBHSNW51Ls5FdP17NjNBRvrQVGM5A3tWJcg4e5x_hb8MleVUpAcfoL18eS4DF5fZlIUWgylQAAAAFsb-QSAA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001518519632")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

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
