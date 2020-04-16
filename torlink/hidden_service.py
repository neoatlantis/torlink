#!/usr/bin/env python3

import subprocess
import random
import os

import stem
import stem.connection
from stem.control import Controller
from stem.process import launch_tor_with_config




def hashPassword(password):
    # call Tor to hash a password via `tor --hash-password`
    t = subprocess.check_output(["tor", "--hash-password", password])
    return t.decode("ascii").strip()

def randomPassword():
    return os.urandom(32).hex()




class TorHiddenService:

    def __init__(self, ports, privateKey=None):
        torControlPassword = randomPassword()
        torControlPasswordHashed = hashPassword(torControlPassword)

        self.tor = launch_tor_with_config(
            config={
                "ControlPort": [ports.torControl],
                "HashedControlPassword": [torControlPasswordHashed],
                "SOCKSPort": [ports.torProxy],
                "SOCKSPolicy": [
                    "accept 127.0.0.1",
                    "reject *",
                ],

            },
            take_ownership=True
        )

        self.controller = Controller.from_port(port=ports.torControl)
        self.controller.authenticate(password=torControlPassword)

        options = { "key_type": "ED25519-V3", "key_content": "ED25519-V3" }
        if privateKey:
            options["key_type"], options["key_content"] = privateKey.split(":")

        response = self.controller.create_ephemeral_hidden_service(
            { 80: ports.torHiddenService },
            **options
        )

        self.serviceID = response.service_id
        print(self.serviceID)


    def __enter__(self, *args, **kvargs):
        return self

    def __exit__(self, *args, **kvargs):
        self.controller.close()
