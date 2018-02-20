#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `First_Flask_Platform` package."""


import unittest
from click.testing import CliRunner

from First_Flask_Platform import First_Flask_Platform
from First_Flask_Platform import cli


class TestFirst_flask_platform(unittest.TestCase):
    """Tests for `First_Flask_Platform` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'First_Flask_Platform.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
