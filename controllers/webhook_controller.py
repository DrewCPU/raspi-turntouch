import logging
import subprocess
import requests

from .base_controller import BaseController

class WebhookController(BaseController):

    def perform(self, action):
        try:
            self.log(action['command'])
            self.log(requests.get(action['command']))
        except Exception as e:
            self.log("Something went wrong: {}".format(e), logging.ERROR)

    @classmethod
    def help(cls):
      return """
Bash Module - Run commands in the shell

Usage:

north_press:
  type: webhook
  command: echo "Hello North"
"""

