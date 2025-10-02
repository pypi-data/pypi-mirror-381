# -*- coding: utf-8 -*-
import logging
from os import path
from typing import Optional, Union
from tornado import options, log as tornado_log
from rich.console import Console
from rich.logging import RichHandler
from yitool.const import __PKG__


logger = logging.getLogger(__PKG__)

def setup_logging(
    terminal_width: Union[int, None] = None, level: int = logging.INFO
) -> None:    
    console = Console(width=terminal_width) if terminal_width else None
    rich_handler = RichHandler(
        show_time=True,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        markup=True,
        show_path=True,
        console=console,
    )
    rich_handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(rich_handler)
    logger.setLevel(level)
    logger.propagate = False
    