# src\file_conversor\config\config.py

import json
import locale

from pathlib import Path
from typing import Any

from file_conversor.config.environment import Environment


class Configuration:

    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self) -> None:
        super().__init__()

        self.__config_path = Environment.get_resources_folder() / ".config.json"
        # Define configuration dictionary
        language = "en_US"
        if locale.getlocale() and locale.getlocale()[0]:
            language = locale.getlocale()[0]
        self.__data = {
            "language": language,      # Default: system language or "en_US"
            "install-deps": True,      # Default: ask user to confirm dependency installation
            "audio-bitrate": 0,        # Default audio bitrate in kbps
            "video-bitrate": 0,        # Default video bitrate in kbps
            "video-format": "mp4",     # Default video format
            "video-encoding-speed": "medium",  # Default video encoding speed
            "video-quality": "medium",  # Default video quality
            "image-quality": 90,        # Default image quality 90%
            "image-dpi": 200,           # Default image => PDF dpi
            "image-fit": 'into',        # Default image => PDF fit mode
            "image-page-size": None,    # Default image => PDF page size
            "image-resampling": "bicubic",  # Default image resampling algorithm
            "pdf-compression": "medium",  # Default PDF compression level
        }

        self.load()

    def __repr__(self) -> str:
        return repr(self.__data)

    def __str__(self) -> str:
        return str(self.__data)

    def __getitem__(self, key) -> Any:
        return self.__data[key]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __delitem__(self, key):
        del self.__data[key]

    def __contains__(self, key):
        return key in self.__data

    def __len__(self):
        return len(self.__data)

    def get_path(self) -> Path:
        return self.__config_path

    def to_dict(self):
        return self.__data.copy()

    def clear(self):
        self.__data.clear()
        self.load()

    def update(self, new: dict):
        self.__data.update(new)

    def load(self):
        """Load app configuration file"""
        if self.__config_path.exists():
            self.__data.update(json.loads(self.__config_path.read_text()))

    def save(self):
        """Save app configuration file"""
        self.__config_path.write_text(json.dumps(self.__data, indent=2))
