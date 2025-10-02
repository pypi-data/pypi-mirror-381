import redis
from typing import Dict, Optional

from yitool.const import __ENV__
from yitool.enums import DB_TYPE
from yitool.utils.env_utils import EnvUtils

class YiRedis(redis.Redis):
    def __init__(self, host = "localhost", port = 6379, db = 0, password = None, socket_timeout = None, socket_connect_timeout = None, socket_keepalive = None, socket_keepalive_options = None, connection_pool = None, unix_socket_path = None, encoding = "utf-8", encoding_errors = "strict", decode_responses = False, retry_on_timeout = False, retry = ..., retry_on_error = None, ssl = False, ssl_keyfile = None, ssl_certfile = None, ssl_cert_reqs = "required", ssl_ca_certs = None, ssl_ca_path = None, ssl_ca_data = None, ssl_check_hostname = True, ssl_password = None, ssl_validate_ocsp = False, ssl_validate_ocsp_stapled = False, ssl_ocsp_context = None, ssl_ocsp_expected_cert = None, ssl_min_version = None, ssl_ciphers = None, max_connections = None, single_connection_client = False, health_check_interval = 0, client_name = None, lib_name = "redis-py", lib_version = ..., username = None, redis_connect_func = None, credential_provider = None, protocol = 2, cache = None, cache_config = None, event_dispatcher = None):
        super().__init__(host, port, db, password, socket_timeout, socket_connect_timeout, socket_keepalive, socket_keepalive_options, connection_pool, unix_socket_path, encoding, encoding_errors, decode_responses, retry_on_timeout, retry, retry_on_error, ssl, ssl_keyfile, ssl_certfile, ssl_cert_reqs, ssl_ca_certs, ssl_ca_path, ssl_ca_data, ssl_check_hostname, ssl_password, ssl_validate_ocsp, ssl_validate_ocsp_stapled, ssl_ocsp_context, ssl_ocsp_expected_cert, ssl_min_version, ssl_ciphers, max_connections, single_connection_client, health_check_interval, client_name, lib_name, lib_version, username, redis_connect_func, credential_provider, protocol, cache, cache_config, event_dispatcher)
    
    def clear(self, pattern) -> int:
        keys = self.keys(pattern)
        if not keys:
            return 0
        cnt = 0
        for key in keys:
            self.delete(key)
            cnt += 1
        return cnt
        
    def hclear(self, name: str) -> int:
        """清空hash表"""
        cnt = 0
        for key in self.hkeys(name):
            self.hdel(name, key)
            cnt += 1
        return cnt
        
    @staticmethod
    def load_env_values(values: Dict[str, str]) -> Dict[str, str]:
        db_type = DB_TYPE.REDIS.value.upper()
        return {
            'host': values.get(f'{db_type}_HOST'),
            'port': values.get(f'{db_type}_PORT'),
            'db': values.get(f'{db_type}_DB'),
            'password': values.get(f'{db_type}_PASSWORD'),
        }
        
    @classmethod
    def from_env(cls, env_path: Optional[str] = __ENV__) -> 'YiRedis':
        values = EnvUtils.dotenv_values(env_path)
        redis_values = cls.load_env_values(values)
        return cls(
            host=redis_values['host'],
            port=int(redis_values['port']),
            db=int(redis_values['db']),
            password=redis_values['password']
        )
