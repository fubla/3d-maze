
class Error(Exception):
    
    pass

class CorruptFileError(Error):
    
    def __init__(self):
        Exception.__init__(self, 'Corrupt or inconsistent input file. Aborting...')
        
