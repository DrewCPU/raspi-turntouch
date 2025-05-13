import json
import logging
import kasa
import os
import subprocess

from .base_controller import BaseController


class KasaController(BaseController):

    def perform(self, action):
        if action['action'] == 'toggle':
           self.log(subprocess.check_output('kasa --alias ' + action['alias'] + ' toggle',
                                          shell=True
            ).decode('utf-8').strip())

    @classmethod
    def help(cls):
      return """
Hue Module - Control Nest Thermostats

Usage:

north_press:
  type: nest
  action: set_temp
  structure: Home     # Run setup to see names. Optional if only one structure
  device: Kitchen     # Run setup to see names. Optional if only one device
  temperature: 21     # In ºF or ºC, as your thermostat is set

north_press:
  type: nest
  action: adjust_temp
  structure: Home     # Run setup to see names. Optional if only one structure
  device: Kitchen     # Run setup to see names. Optional if only one device
  direction: up       # or down
"""
