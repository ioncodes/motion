class Config:
    def __init__(self, url, trigger, regex, headers, mode, data, sort, condition, f):
        self.url = url
        self.trigger = trigger
        self.regex = regex
        self.headers = headers
        self.mode = mode
        self.data = data
        self.sort = sort
        self.condition = condition
        self.format = f

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

    def get_data(self, data):
        p = self.data.search(data)
        s = self.format
        for i in self.sort:
            s = s.replace('%', p.group(i), 1)
        return s

    def validate(self, data):
        p = self.regex.search(data)
        if p:
            trigger = p.group(1)
            msg = p.group(2)
            if self.trigger != trigger and self.condition == msg:
                self.trigger = trigger
                return True
        return False