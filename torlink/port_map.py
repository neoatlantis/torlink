#!/usr/bin/env python3

import random


class PortMap:

    def __init__(self):
        self._base = random.randint(50001, 51000-10)

        self.torControl = self._base
        self.torProxy = self._base + 1
        self.torHiddenService = self._base + 2
        self.torHiddenService = 50000 # TODO dev
