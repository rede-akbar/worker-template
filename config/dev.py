from .base import BaseConfig


class DevConfig(BaseConfig):
    task_default_exchange: str = "dev"
    task_default_queue: str = "dev-puller"


locals().update(DevConfig().dict(exclude_none=True))
