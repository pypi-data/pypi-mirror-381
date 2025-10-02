# -*- coding: utf-8 -*-
from cachetools import cached
import _humps

class StrUtils(object):
    """字符串工具类"""
    
    @staticmethod
    @cached({})
    def camelize(str_or_iter: str) -> str:
        return _humps.camelize(str_or_iter)