"""This module does the configuration of the application"""

import os
import sys
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    if "pytest" in sys.modules:
        load_dotenv(dotenv_path=os.path.join(dirname, "..", ".test.env"), override=True)
    else:
        load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DREAMS_FILENAME = os.getenv("DREAMS_FILENAME") or "dreams.csv"
DREAMS_FILE_PATH = os.path.join(dirname, "..", "data", DREAMS_FILENAME)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

DATA_FOLDER = os.path.join(dirname, "..", "data")
