from mazegen.config_parser import parse_config, ConfigParseError
import pytest

def test_parse_valid_config() -> None:
	"""Test parsing a valid configuration file."""
	config = parse_config("config.txt")
	assert config['WIDTH'] == 20
	assert config['HEIGHT'] == 15
	assert config['ENTRY'] == (0, 0)
	assert config['EXIT'] == (19, 14)
	assert config['PERFECT'] is True

def test_invalid_dimensions() -> None:
	"""Test that invalid dimensions raise error."""
	pass