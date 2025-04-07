"""This module tests the configuration using the build-function"""

from build import build

def pytest_configure():
    """Calls the build function"""
    build()
