class DataCaller(object):
    """
    Just a data caller base class.
    """
    
    def __init__(self, session):
        self.session = session
    
    def get(self):
        raise NotImplementedError()
    
    def download(self, data):
        raise NotImplementedError()