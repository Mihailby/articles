# config.py
import os

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

DATA_DIR = os.getenv("DATA_DIR", "data/")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output/")

SVG_URL = "https://raw.githubusercontent.com/Mihailby/articles/main/pls.svg"
THEME = "auto"   # "dark", "light", "auto"