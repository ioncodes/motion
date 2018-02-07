from __init__ import __version__ as VERSION
import argparse

parser = argparse.ArgumentParser(description='motion')
parser.add_argument('-a', action='store', dest='url', help='Add a new url')
parser.add_argument('-r', action='store', dest='name', help='Remove an url')
parser.add_argument('-v', action='version', version='%(prog)s {0}'.format(VERSION))

def main():
    args = parser.parse_args()
    print(args)