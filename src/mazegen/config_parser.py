from typing import Dict, Any, Tuple

class ConfigParseError(Exception):
	"""Exception raised for configuration parsing errors."""
	pass

def parse_config(filepath: str) -> Dict[str, Any]:
	"""
	Parse maze configuration from file.

	Args:
		filepath: Path to configuration file

	Returns:
		ConfigParseError: If file cannot be read or parsed
		FileNotFoundError: If configuration file doesn't exist
	"""

	config: Dict[str, Any] = {}
	required_keys = {'WIDTH', 'HEIGHT', 'ENTRY', 'EXIT', 'OUTPUT_FILE', 'PERFECT'}

	try:
		with open(filepath, 'r') as f:
			for line_num, line in enumerate(f, 1):
				line = line.strip()

				# Skip empty lines and comments
				if not line or line.startswith('#'):
					continue
					
				# Parse Key=Value
				if '=' not in line:
					raise ConfigParseError(
						f"Line {line_num}: Invalid format (Expected KEY=VALUE)"
					)
				
				key, value = line.split('=', 1)
				key = key.strip()
				value = value.strip()

				# Parse specific types
				if key in ('WIDTH', 'HEIGHT', 'SEED'):
					config[key] = int(value)

				elif key in ('ENTRY', 'EXIT'):
					config[key] = _parse_coordinates(value, key, line_num)
				
				elif key == 'PERFECT':
					config[key] = _parse_boolean(value, line_num)
				
				else:
					# String values
					config[key] = value		
	except FileNotFoundError:
		raise FileNotFoundError(f"Configuration file not found: {filepath}")
	except ConfigParseError as e:
		raise ConfigParseError(f"Line {line_num}: {str(e)}")
	
	# Validate required keys
	missing_keys = required_keys - set(config.keys())
	if missing_keys:
		raise ConfigParseError(
			f"Missing required configuration keys: {', '.join(missing_keys)}"
		)

	# Validate values
	_validate_config(config)

	return config

def _parse_coordinates(value: str, key: str, line_num: int) -> Tuple[int, int]:
	"""Parse coordinate string like '0,0' into tuple."""
	try:
		parts = value.split(',')
		if len(parts) != 2:
			raise ValueError(f"{key} must be in format 'x, y'")
		return (int(parts[0].strip()), int(parts[1].strip()))
	except ValueError as e:
		raise ConfigParseError(f"Line {line_num}: Invalid {key} format - {str(e)}")

def _parse_boolean(value: str, line_num: int) -> bool:
	"""Parse boolean value."""

	value_lower = value.lower()
	if value_lower in ('true', '1', 'yes', 'on'):
		return True
	
	elif value_lower in ('false', '0', 'no', 'off'):
		return False
	
	else:
		raise ConfigParseError(
			f"Line {line_num}: Invalid boolean value '{value}' "
			"(use True/False, 1/0, Yes/No, On/Off)"
		)

def _validate_config(config: Dict[str, Any]) -> None:
	"""Validate configuration values."""
	# Validate dimensions
	if config['WIDTH'] < 5 or config['HEIGHT'] < 5:
		raise ConfigParseError("WIDTH and HEIGHT must be at least 5")
	
	if config['WIDTH'] > 200 or config['HEIGHT'] > 200:
		raise ConfigParseError("WIDTH and HEIGHT must not exceed 200")
	
	# Validate coordinates are within bounds
	entry_x, entry_y = config['ENTRY']
	exit_x, exit_y = config['EXIT']

	if not (0 <= entry_x < config['WIDTH'] and 0 <= entry_y < config['HEIGHT']):
		raise ConfigParseError(
			f"ENTRY coordinates ({entry_x},{entry_y} out of bounds)"
		)

	if not (0 <= exit_x < config['WIDTH'] and 0 <= exit_y < config['HEIGHT']):
		raise ConfigParseError(
			f"EXIT coordinates ({exit_x},{exit_y} out of bounds)"
		)
	
	# Validate entry and exit are different:
	if config['ENTRY'] == config['EXIT']:
		raise ConfigParseError("ENTRY and EXIT must be different cells")
	
