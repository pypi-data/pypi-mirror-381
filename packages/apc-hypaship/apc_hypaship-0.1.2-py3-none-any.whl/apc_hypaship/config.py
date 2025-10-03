import os
from datetime import date, time
from functools import lru_cache
from pathlib import Path
import base64
from typing import Annotated

from loguru import logger
from pydantic import BaseModel, ConfigDict, SecretStr, AliasGenerator, StringConstraints
from pydantic.alias_generators import to_pascal
from pydantic_settings import BaseSettings, SettingsConfigDict


def encode_b64_str(s: str) -> str:
    return base64.b64encode(s.encode('utf8')).decode('utf8')


def get_remote_user(login, password) -> str:
    usr_str = f'{login}:{password}'
    return f'Basic {encode_b64_str(usr_str)}'


def apc_date(d: date) -> str:
    return d.strftime('%d/%m/%Y')


def load_env() -> Path:
    apc_env = Path(os.getenv('APC_ENV'))
    if not apc_env.exists():
        raise ValueError('APC_ENV not set correctly')
    logger.debug(f'Loading APC environment from {apc_env}')
    return apc_env


class APCSettings(BaseSettings):
    apc_email: SecretStr
    apc_password: SecretStr
    base_url: str
    model_config = SettingsConfigDict(env_file=load_env())

    @property
    def headers(self) -> dict:
        usr = self.apc_email.get_secret_value()
        pwd = self.apc_password.get_secret_value()
        return {
            'Content-Type': 'application/json',
            'remote-user': get_remote_user(usr, pwd),
        }

    @property
    def services_endpoint(self) -> str:
        return self.base_url + 'ServiceAvailability.json'

    @property
    def orders_endpoint(self) -> str:
        return self.base_url + 'Orders.json'

    def one_order_endpoint(self, order_num: str) -> str:
        return self.base_url + f'Orders/{order_num}.json'

    def track_endpoint(self, order_num: str) -> str:
        return self.base_url + f'Tracks/{order_num}.json'


@lru_cache
def apc_settings() -> APCSettings:
    return APCSettings()


class APCBaseModel(BaseModel):
    model_config = ConfigDict(
        json_encoders={
            time: lambda v: v.strftime('%H:%M'),
            date: lambda v: v.strftime('%d/%m/%Y'),
        },
        alias_generator=AliasGenerator(
            alias=to_pascal,
        ),
        populate_by_name=True,
        use_enum_values=True,
    )


def str_length_const(length: int):
    return Annotated[
        str,
        StringConstraints(strip_whitespace=True, max_length=length),
    ]
