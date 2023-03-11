from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    PROTOCOL: str = "amqp"
    USERNAME: str = "rabbitmq"
    PASSWORD: str = "rabbitmq"
    HOST: str = "localhost"
    PORT: str = "5672"
    broker_url: str = f"{PROTOCOL}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}"
    imports: list[str] = ["tasks", ]

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "JOB_"
