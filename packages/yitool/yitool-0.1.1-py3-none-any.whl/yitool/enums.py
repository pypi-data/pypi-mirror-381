from enum import Enum
from typing import Union

class YiEnum(Enum):
    @classmethod
    def has(cls, val: Union[str, int]) -> bool:
        return val in cls.__members__.values()


class DB_TYPE(YiEnum):
    """数据库类型枚举"""
    REDIS = 'redis'
    MYSQL = 'mysql'
    MSSQL = 'mssql'