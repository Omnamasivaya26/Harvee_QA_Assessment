"""Centralized configuration for the Sauce Demo assessment suite."""
import os

BASE_URL = os.getenv("SAUCE_BASE_URL", "https://www.saucedemo.com/")
STANDARD_USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
LOCKED_USERNAME = os.getenv("SAUCE_LOCKED_USERNAME", "locked_out_user")
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
FIRST_NAME = os.getenv("CHECKOUT_FIRST_NAME", "Manoj")
LAST_NAME = os.getenv("CHECKOUT_LAST_NAME", "Kumar")
POSTAL_CODE = os.getenv("CHECKOUT_POSTAL_CODE", "642001")
