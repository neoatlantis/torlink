#!/usr/bin/env python3

import getpass
import sys
import time

from .hidden_service import TorHiddenService
from .link_terminal import LinkTerminalServer
from .config import Config
from .port_map import PortMap


ports = PortMap()
config = Config(sys.argv[1])


with TorHiddenService(
    ports,
    privateKey=config.get("tor-private-key"),
) as hs, LinkTerminalServer(('', ports.torHiddenService)) as hsserver:

    while True:
        time.sleep(10)
        print(".")
