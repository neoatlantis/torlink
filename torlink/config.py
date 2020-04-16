#!/usr/bin/env python3

import yaml

class Config:

    def __init__(self, filename):
        self.filename = filename
        self._yaml = yaml.load(open(self.filename, "r").read())

    def get(self, name):
        if name in self._yaml:
            return self._yaml[name]
        return None
