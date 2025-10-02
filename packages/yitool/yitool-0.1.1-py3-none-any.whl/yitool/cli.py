# -*- coding: utf-8 -*-
"""命令行入口"""

import argparse
from os import path
from typing import Optional
from tornado import options
from yitool.log import logger, setup_logging


class Cli:
    def __init__(self):
        logger.info("Welcome to YITECH CLI")
    
    def __call__(self, *args, **kwds):
        parser = argparse.ArgumentParser(description="YITECH CLI")
        parser.add_argument("name", help="The name to greet")
        parser.add_argument("name", help="The name to greet")
        parser.add_argument("--farewell", action="store_true", help="Use farewell instead of greeting")
        
        args = parser.parse_args()
        if args.farewell:
            print(f"Goodbye, {args.name}!")
        else:
            print(f"Hello, {args.name}!")
            
    @staticmethod
    def parse_config_file(file_path: Optional[str] = None):
        if file_path is None or not path.exists(file_path):
            CLI_CONF = 'cli.conf'
            file_path = path.join(path.dirname(__file__), CLI_CONF)
        options.parse_config_file(file_path)
        # setup_logging()
    

if __name__ == "__main__":
    pass