from config import Config
from termcolor import colored
import time
import requests
import re

class Monitor:
    def __init__(self, config):
        self.config = config
        self.configs = []
        for config in self.config:
            headers = {}
            for header in config['headers']:
                headers[header['key']] = header['value']
            mode = config['mode']
            p = re.compile(config['regex'])
            url = config['url']
            r = requests.get(url, headers=headers)
            t = r.text
            m = p.search(t)
            sort = config['sort']
            data = re.compile(config['data'])
            f = config['format']
            _trigger = config['trigger']
            if m:
                trigger = m.group(1)
                self.configs.append(Config(url, trigger, p, headers, mode, data, sort, _trigger, f))

    def display(self):
        while True:
            for config in self.configs:
                headers = config.get_headers()
                url = config.get_url()
                r = requests.get(url, headers=headers)
                t = r.text
                x = config.validate(t)
                mode = config.get_mode()
                if x:
                    msg = config.get_data(t)
                    if mode == 'success':
                        print(colored(msg, 'green'))
                    elif mode == 'warning':
                        print(colored(msg, 'orange'))
                    elif mode == 'error':
                        print(colored(msg, 'red'))
                    else:
                        print(colored(msg, 'white'))
            time.sleep(10)
