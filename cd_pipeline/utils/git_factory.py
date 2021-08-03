import hmac
import json
import hashlib

import git

from ...configs import get_config_variable




class GitImplementation:


    def __init__(self):

        self._github_repo_url = get_config_variable('GITHUB_REPO')
        self._local_repo_path = get_config_variable('LOCAL_REPO')
        self._shared_secret_key = get_config_variable('GITHUB_SECRET_KEY')

    def __generate_hash(
        self,
        request_data: bytes,
    ) -> str:

    key = self._shared_secret_key
    key_bytes = key.encode()
    sha256_hash = hmac.new(key=key_bytes, msg=request_data, digestmod=hashlib.sha256)

    return sha256_hash.hexdigest()

    def github_data_is_valid(
        self,
        request_data: bytes,
        request_header: dict[str, str]
    ) -> bool:

        sha256_digest = self.__generate_hash(request_data)
        return hmac.compare_digest(sha256_digest, request_header)
