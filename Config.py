import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5590537210:AAGpKf0XTY4beZ7AZ6YEOnSp8844ruR97II")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzcBuwRYM_lEHu61x0rybS5EGZxW9ufxQo7_qk7x2pec6A4oiatQ5LMow9R5MMIWaHTushspyGe7J4BHhHIPnR-i8kY3Cd-FdMX_UcZufG4HnDsbr6p1LoarCVCmLUndGcpB2y9Ugo0Hbi64Z-9PoxSyTp4LOGe406WRXIykSVOn0kHim5kibaXqDG06IhnoBoh_jgW1xRptwBclyUO5zwt3nVUrH4CAG5GuHXocf_xkA-mBj2bh289fdayyUPhTfMriitlvEmeO8L2HT1HEyFLwgvTEU2phSKnVUdzr-FFOgGo-gjh0F91m6We_IWq634j2dxI-IvqnA-Fo-JM_k1jNaxg=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Shinchan_Music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Mrnhgrx") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Shizuka_update") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
