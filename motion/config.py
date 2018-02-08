class Config:
    def __init__(self, url, trigger, regex, headers, mode):
        self.url = url
        self.trigger = trigger
        self.regex = regex
        self.headers = headers
        self.mode = mode

    def get_trigger(self):
        return self.trigger

    def set_trigger(self, trigger):
        self.trigger = trigger

    def get_headers(self):
        return self.headers
    
    def get_url(self):
        return self.url
    
    def get_mode(self):
        return self.mode

    def validate(self, data):
        p = self.regex.search(data)
        if p:
            trigger = p.group(1)
            msg = p.group(2)
            if self.trigger != trigger:
                self.trigger = trigger
                return msg
        return False