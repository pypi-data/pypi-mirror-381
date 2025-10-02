# -*- coding: utf-8 -*-
import json
from datetime import datetime, date
from tornado.escape import json_decode
from typing import Dict, Any

from yitool.utils.path_utils import PathUtils

# 自定义 JSON 编码器，处理 datetime 和 date 类型
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        # 处理 datetime 对象
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
            # return obj.isoformat()
        # 处理 date 对象
        elif isinstance(obj, date):
            # return obj.isoformat()
            return obj.strftime('%Y-%m-%d')
        return super().default(obj)

class JsonUtils:
    """ JSON 工具类 """
    @staticmethod
    def load(json_file: str) -> Any:
        """ 加载文件数据 """
        with open(json_file, 'r') as f:
            return json.load(f)
        
    @staticmethod
    def dump(json_file: str, data: Dict[str, Any]):
        """ 保存数据到文件 """
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=2)
            
    @staticmethod
    def json_decode(json_str: str) -> dict[str, Any]:
        return json_decode(json_str)

    @staticmethod
    def json_encode(value: dict[str, Any]) -> str:
        return json.dumps(value, ensure_ascii=False, cls=DateTimeEncoder)