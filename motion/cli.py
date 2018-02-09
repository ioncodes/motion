from __init__ import __version__ as VERSION
from configmanager import ConfigManager
from monitor import Monitor
import argparse

parser = argparse.ArgumentParser(description='motion')
parser.add_argument('--add', action='store_true', default=False, dest='add', help='Add a new url')
parser.add_argument('--name', action='store', dest='name', help='Name of the config')
parser.add_argument('--regex', action='store', dest='regex', help='Regex for the config')
parser.add_argument('--mode', action='store', dest='mode', help='The output mode (coloring)')
parser.add_argument('--data', action='store', dest='data', help='Regex for data output')
parser.add_argument('--data-sorting', action='store', dest='data_sorting', help='Data regex group sorting')
parser.add_argument('--trigger', action='store', dest='trigger', help='Condition to trigger')
parser.add_argument('--format', action='store', dest='format', help='String format (with %)')
parser.add_argument('--url', action='store', dest='url', help='Url to use')
parser.add_argument('--headers', action='store', dest='headers', help='Headers to use')
parser.add_argument('--remove', action='store_true', default=False, dest='remove', help='Remove an url')
parser.add_argument('--example', action='store_true', default=False, help='Show me an example!')
parser.add_argument('--version', action='version', version='%(prog)s {0}'.format(VERSION))

def main():
    args = parser.parse_args()
    if args.example:
        print("""python3 motion/ --add --name 'jellyfish' --regex 'last(.+)' --url 'https://api.random.api/api/status' --headers 'Accept:application/json' --mode 'success' --trigger 'online' --data '(.+)' --data-sorting '1' --format '% is online!'""")
    else:
        manager = ConfigManager()
        if args.add or args.remove:
            if args.add and args.name and args.regex and args.url and args.mode and args.data and args.data_sorting and args.trigger and args.format:
                manager.add(args.name, args.url, args.regex, args.headers, args.mode, args.data, args.data_sorting, args.trigger, args.format)
            elif args.remove and args.name:
                manager.remove(args.name)
            else:
                print('Invalid argument combination!')
        else:
            monitor = Monitor(manager.read())
            monitor.display()