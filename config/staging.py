from .base import BaseConfig


class StagingConfig(BaseConfig):
    pass


locals().update(StagingConfig().dict(exclude_none=True))
