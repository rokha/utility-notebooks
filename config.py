import os
from dotenv import load_dotenv

load_dotenv('.env')


class Config(object):

    def __init__(self, ):
        self.global_data = dict()

    def set(self):
        self.global_data['mercury_api_key'] = str(
            os.environ.get('MERCURY_API_KEY'))
        self.global_data['mercury_api_key_2'] = str(
            os.environ.get('MERCURY_API_KEY_2'))

    def get(self):
        self.set()
        return self.global_data
