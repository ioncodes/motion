from pathlib import Path
import os.path
import json

class ConfigManager:
    def __init__(self):
        self.config = str(Path.home()) + '/.motion.json'
        self.check_config()

    def check_config(self):
        f = Path(self.config)
        if not f.is_file():
            with open(self.config, 'w') as stream:
                json.dump([], stream)

    def read(self):
        with open(self.config, 'r') as stream:
            return json.load(stream)
    
    def write(self, config):
        with open(self.config, 'w') as stream:
            json.dump(config, stream)

    def add(self, name, url, regex, headers, mode):
        config = self.read()
        _headers = []
        if headers:
            for header in headers.split(','):
                data = header.split(':')
                _headers.append({'key': data[0], 'value': data[1]})
        config.append({'name': name, 'url': url, 'regex': regex, 'headers': _headers, 'mode': mode})
        self.write(config)

    def remove(self, name):
        config = self.read()
        config = [c for c in config if c['name'] != name]
        self.write(config)
