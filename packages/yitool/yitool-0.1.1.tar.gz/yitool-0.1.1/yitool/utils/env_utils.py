# -*- coding: utf-8 -*-
import os
from pathlib import Path
from typing import Dict, Optional, Union, IO
from dotenv import load_dotenv, dotenv_values

from yitool.const import __ENV__


class EnvUtils(object):
    """系统环境变量工具类"""

    @staticmethod
    def dotenv_values(
        dotenv_path: Union[str, os.PathLike, None] = __ENV__,
        stream: Optional[IO[str]] = None,
        verbose: bool = False,
        interpolate: bool = True,
        encoding: Optional[str] = "utf-8",
    ) -> Dict[str, Optional[str]]:
        """获取dotenv文件内容"""
        return dotenv_values(
            dotenv_path=dotenv_path, stream=stream, verbose=verbose, interpolate=interpolate, encoding=encoding,
        )

    @staticmethod
    def load_env_file(
        dotenv_path: Union[str, os.PathLike, None] = __ENV__,
        stream: Optional[IO[str]] = None,
        verbose: bool = False,
        override: bool = False,
        interpolate: bool = True,
        encoding: Optional[str] = "utf-8",
    ) -> bool:
        """加载dotenv文件到系统环境变量中"""
        return load_dotenv(
            dotenv_path=dotenv_path,
            stream=stream,
            verbose=verbose,
            override=override,
            interpolate=interpolate,
            encoding=encoding,
        )