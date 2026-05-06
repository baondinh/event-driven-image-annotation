# tests/test_config.py

from edia.config import AppConfig

class TestAppConfig: 
    def test_default_config(self): 
        config = AppConfig()
        assert config.logging.level == "DEBUG"