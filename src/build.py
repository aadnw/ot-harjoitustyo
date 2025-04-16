"""This module initializes the database"""
import os

from initalize_database import initialize_database
from config import DATA_FOLDER


def build():
    """Create the database"""
    if not os.path.isdir(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)
    initialize_database()


if __name__ == "__main__":
    build()
