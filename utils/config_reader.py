import configparser
import os


class ConfigReader:
    """Read configuration from properties file"""

    def __init__(self, config_path="config/config.properties"):
        self.config = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), config_path)

        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

        self.config.read(config_file)

    def get_value(self, key, default=None, section="CONFIG"):
        """Get configuration value by key and section"""
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default
