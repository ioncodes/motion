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
            if m:
                trigger = m.group(1)
                self.configs.append(Config(url, trigger, p, headers, mode))

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
                    if mode == 'success':
                        print(colored(x, 'green'))
                    elif mode == 'warning':
                        print(colored(x, 'orange'))
                    elif mode == 'error':
                        print(colored(x, 'red'))
                    else:
                        print(colored(x, 'white'))
                else:
                    config.set_trigger('lol') # debug
            time.sleep(1)
