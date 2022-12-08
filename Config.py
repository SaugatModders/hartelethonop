import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22078178"))
    API_HASH = os.environ.get("API_HASH", "d8b5fdd23f55a4ae9f709807b88406be")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5585173601:AAGf7mCLGkJd-doPlqUu1CouEd97ZKI4wow")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu2MF_sdqxDsp5PE2Sta-xnPVcaZ_e-vKgKDxIzQl4EnCpu_yiNkNiwm4k7guNHL1VP10MPmrjPCsfohVlktPyzv2tHweZOabsjFwge80kNebZeiPe3v_KndDxkHLLP6YgjTPnPcJGCtjc8FN0nJc3dOw2HMpnmv9e6xuq7IyHTGUtLxM2BwYiCTioxMFBYqyJptoFTqJHRY_-1TC8z4_4MCKwhJIKhEDnKA78hcIcLOXjJnPOYukcZvhtUlvcpfDv1_JQ7RnzQRWFyIeDtmTT1p1dc6Vqos_AjB-MRs7P9M8lAblI_VvY3Vi_JoSnx9KKcLN3jAyJtqT3NAbKs0sCZY=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Shizuka_Music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Mrnhgrx") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Shizuka_update") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/6e0dab99a08982feb5215.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5285125597")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
