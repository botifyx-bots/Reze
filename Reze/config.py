import orjson
import os


def get_user_list(config, key):
    with open("{}/Reze/{}".format(os.getcwd(), config), "rb") as json_file:
        return orjson.loads(json_file.read())[key]

class Config(object):
    API_HASH = "a00" # API_HASH from my.telegram.org
    API_ID = 0 # API_ID from my.telegram.org

    BOT_ID = 0 # BOT_ID
    BOT_USERNAME = "BotifyX_Pro_Botz" # BOT_USERNAME

    MONGO_DB_URL = "mongodb+srv://xxxxxxxx:xxxxxxxx@cluster0.t3frstc.mongodb.net/?appName=Cluster0" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "BotifyX_Pro_Botz" # Support Chat Username
    UPDATE_CHANNEL = "BotifyX_Pro_Botz" # Update Channel Username
    START_PIC = "https://i.ibb.co/3Lf2Vts/image.png" # Start Image
    DEV_USERS = [123456789] # Dev Users
    TOKEN = "8040443613:Axxxxxxxxxxxxx" # Bot Token from @BotFather
    CLONE_LIMIT = 50 # Number of clones your bot can make

    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

    EVENT_LOGS = -100 # Event Logs Chat ID
    OWNER_ID = 123456789 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "Reze" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    GROQ_API_KEY = "gsk_mm" # GROQ API Key from groq.com


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
