"""Constants for the Yandex Object Storage integration."""

from collections.abc import Callable
from typing import Final

from homeassistant.util.hass_dict import HassKey

DOMAIN: Final = "aws_s3_fork"

CONF_ACCESS_KEY_ID = "access_key_id"
CONF_SECRET_ACCESS_KEY = "secret_access_key"
CONF_ENDPOINT_URL = "endpoint_url"
CONF_BUCKET = "bucket"

YANDEX_DOMAIN = "storage.yandexcloud.net"
DEFAULT_ENDPOINT_URL = f"https://{YANDEX_DOMAIN}/"

DATA_BACKUP_AGENT_LISTENERS: HassKey[list[Callable[[], None]]] = HassKey(
    f"{DOMAIN}.backup_agent_listeners"
)

DESCRIPTION_YANDEX_DOCS_URL = "https://cloud.yandex.com/en/docs/storage/s3/api-ref"
DESCRIPTION_BOTO3_DOCS_URL = "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html"
