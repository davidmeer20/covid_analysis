from enum import Enum
LOCAL_HOST = "mongodb://localhost:27017/"
DB = "test"
COV_COLLECTION = "covid"
COUNTRIES_PATH = 'https://api.covid19api.com/countries'
PATH = 'https://api.covid19api.com/dayone/country/{}/status/{}'


class Status(Enum):
    Confirmed = 1
    Deaths = 2
    Recovered = 3
    Active = 4



