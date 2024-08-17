import os

from utils.requests_helper import BaseSession


def gateway_url() -> BaseSession:
    base_domain = os.getenv('GATEWAY_URL')
    return BaseSession(base_url=base_domain)

