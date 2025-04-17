"""Test setup"""
from build import build

def pytest_configure():
    """Calls the build function"""
    build()
