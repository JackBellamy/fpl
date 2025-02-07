import configparser
import os

# from pathlib import Path
# os.path.join(os.getcwd(), "fpl\\", "credentials.cfg") 

config_path = os.path.abspath("docs\\_static\\credentials.cfg")
config = configparser.ConfigParser()
config.read(config_path)

if not config.sections():
    raise FileNotFoundError(f"Configuration file not found or empty: {config_path}")

#print(config)

TEMP_ENV_VARS = {
    "FPL_EMAIL": config["CREDENTIALS"]["FPL_EMAIL"] or os.getenv("FPL_EMAIL"),
    "FPL_PASSWORD": config["CREDENTIALS"]["FPL_PASSWORD"] or os.getenv("FPL_PASSWORD")
}

# TEMP_ENV_VARS = {
#     "FPL_EMAIL": config["CREDENTIALS"].get("FPL_EMAIL", os.getenv("FPL_EMAIL")),
#     "FPL_PASSWORD": config["CREDENTIALS"].get("FPL_PASSWORD", os.getenv("FPL_PASSWORD"))
# }

ENV_VARS_TO_SUSPEND = [
]
