from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 23391941)  # api id
API_HASH = environ.get("API_HASH", "392f541aae8545711de9d77e8d324b82")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "6683891175:AAG7Ub8tNlukccbvpe_MK1DBuVOIsKYdq14")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-12722.c74.us-east-1-4.ec2.redns.redis-cloud.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 12722)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "wBnSTIOiMCw2N8lsDcfMq0ScDkxAHKV4"
)  # redis password


ADMINS = [766716953]
OWNER_ID = 766716953  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002019190679  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1001999304148
DUMP_CHANNEL = -1001999304148 


# Config
COOKIE = environ.get("COOKIE", "csrfToken=DKdK4CcoibdkIgNLm6DbzI9Y; lang=en; TSID=eeRnKP1it7v9AB9b6xqJEiIwyL8mYcxY; __bid_n=18edb1deff14b4744f4207; _ga=GA1.1.2112040923.1713073157; __stripe_mid=28add43a-9e57-44bb-b28b-8cbaae076d3b38a5b4; ndus=YT24CKxteHuitbd0xAQ0IpcQzh1KrvMb8FU_C7oc; browserid=6pHvmG9AgZFsosafSp0kwJi8SQhuJ604SSwki68GfqzdvDgJ5wc_5f-08gg=;  _ga_06ZNKL8C2E=GS1.1.1715856342.11.0.1715856359.43.0.0 ndut_fmt=B476F689AE9FF0EDD82DB98A5DCE82EFD38D2254B2266C2630DDC1607418C288;")
