from .base import BaseConfig


class ProdConfig(BaseConfig):
    pass


locals().update(ProdConfig().dict(exclude_none=True))
