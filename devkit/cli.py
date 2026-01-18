"""CLI entry point for devkit."""
import sys
import argparse
from devkit.json_format import format_json_file


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Developer toolkit utilities')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # JSON formatter
    json_parser = subparsers.add_parser('json-format', help='Format JSON files')
    json_parser.add_argument('file', help='JSON file to format')
    json_parser.add_argument('--indent', type=int, default=2, help='Indentation spaces')
    json_parser.add_argument('--no-sort', action='store_true', help='Do not sort keys')
    
    args = parser.parse_args()
    
    if args.command == 'json-format':
        success = format_json_file(args.file, args.indent, not args.no_sort)
        sys.exit(0 if success else 1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
