"""JSON formatting and validation utility."""
import json
import sys
from pathlib import Path
from typing import Optional


def format_json_file(filepath: str, indent: int = 2, sort_keys: bool = True) -> bool:
    """
    Format and validate a JSON file.
    
    Args:
        filepath: Path to JSON file
        indent: Indentation spaces (default 2 for readability)
        sort_keys: Whether to sort keys alphabetically
        
    Returns:
        True if successful, False otherwise
    """
    try:
        path = Path(filepath)
        if not path.exists():
            print(f"Error: File not found: {filepath}", file=sys.stderr)
            return False
            
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # ensure_ascii=False preserves unicode characters
        # sort_keys=True makes output consistent and easier to diff
        formatted = json.dumps(data, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
        print(formatted)
        return True
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return False


def validate_json_schema(data: dict, schema: dict) -> tuple[bool, Optional[str]]:
    """
    Basic JSON schema validation.
    
    Args:
        data: JSON data to validate
        schema: Schema definition
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Basic implementation - can be extended
    required_fields = schema.get('required', [])
    
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    
    return True, None
