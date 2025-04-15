"""This module tests the configuration using the build-function"""

import os
from build import build

os.environ["TESTING"] = "1"

def pytest_configure():
    """Calls the build function"""
    build()
