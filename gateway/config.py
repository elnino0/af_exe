import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from a .env file (if it exists)
load_dotenv()

# Print all environment variables (similar to console.log("env: ", process.env) in JS)
print("env:", os.environ)

class ENV:
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    XYZ_API_URL: Optional[int]
    XYZ_API_KEY: Optional[str]


class Config:
    def __init__(self, **kwargs):
        self.xyz_api_url = kwargs["XYZ_API_URL"]
        self.xyz_api_key = kwargs["XYZ_API_KEY"]
        


def get_config() -> ENV:
    return ENV(
        XYZ_API_KEY=os.environ.get("XYZ_API_KEY"),
        XYZ_API_URL=os.environ.get("XYZ_API_URL"),
    )

def get_sanitized_config(config: ENV) -> Config:
    sanitized_config = {}
    for key, value in config.__dict__.items():
        if value is None:
            raise ValueError(f"Missing key {key} in .env file")
        sanitized_config[key] = value
    return Config(**sanitized_config)

config_env = get_config()
AppConfig = get_sanitized_config(config_env)
