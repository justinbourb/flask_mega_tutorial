import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or r'\xbbM\xe8\xbeXZ\x03\xa5\xd5r\x1aq\xc1\x01PY\x18\x16'
