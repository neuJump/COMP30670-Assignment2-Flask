# -*- coding: utf-8 -*-

"""Top-level package for First Flask Platform."""

__author__ = """Timothy Madigan"""
__email__ = 'timothy.madigan@ucdconnect.ie'
__version__ = '1.0'

from flask import Flask
app = Flask(__name__.split('.')[0])
from app import views
