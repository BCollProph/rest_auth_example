from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, API_USERNAME: str=None, API_PASSWORD: str=None, API_CLIENT_ID: str=None, PAGE_COUNT: int=None):
        self.spark = None
        self.update(API_USERNAME, API_PASSWORD, API_CLIENT_ID, PAGE_COUNT)

    def update(
            self,
            API_USERNAME: str="api-user4@iwt.net", 
            API_PASSWORD: str="b3z0nV0cLO", 
            API_CLIENT_ID: str="0oahdhjkutaGcIK2M4x6", 
            PAGE_COUNT: int=10
    ):
        self.API_USERNAME = API_USERNAME
        self.API_PASSWORD = API_PASSWORD
        self.API_CLIENT_ID = API_CLIENT_ID
        self.PAGE_COUNT = self.get_int_value(PAGE_COUNT)
        pass
