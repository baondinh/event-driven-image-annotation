# edia/config.py

import logging 
from datetime import datetime
from dataclasses import dataclass, field
from typing import Literal, Dict
from pathlib import Path 

import yaml

logger = logging.getLogger(__name__)

#---------------------
# Database
#---------------------
# @dataclass  
# class DatabaseConfig: 
#     """
#     Controls where SQLite .db lives
#     Used by: 
#         edia/db/connection.py -> DatabaseConnection
#     """
#     path: str = "edia.db"
#     echo: bool = False 
#     timeout: float = 30.0

#---------------------
# Logging 
#---------------------
@dataclass
class LoggingConfig:
    """
    Controls logging and output file 
    Used by: 
        edia/logging_config.py -> setup_logging()
    """
    level: str = "DEBUG"
    log_dir: str = "logs"
    log_file: str = "edia"
    max_bytes: int = 5_242_880  # 5 MB
    backup_count: int = 3
    format: str = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    date_format: str = "%Y-%m-%d %H:%M:%S"


#---------------------
# AppConfig 
#---------------------
@dataclass
class AppConfig: 
    """
    Root configuration object that CLI and tests instantiate directly
    Other config dataclasses are accessed as attributes through this object
    """
    logging:        LoggingConfig       = field(default_factory=LoggingConfig)

def load_config(config_path: str | Path = "config.yaml") -> AppConfig:
    """
    Load config from YAML file and return AppConfig object
    """
    with open(config_path, "r") as f:
        config_dict = yaml.safe_load(f)

    # Convert nested dict to AppConfig dataclass
    app_config = AppConfig(
        logging=LoggingConfig(**config_dict.get("logging", {})),
    )

    logger.debug(f"Loaded config: {app_config}")
    return app_config