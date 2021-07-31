from consts import LOCAL_HOST, DB, COV_COLLECTION, COUNTRIES_PATH, PATH, Status
from datetime import datetime
import json
import pymongo
import requests


def fetch_and_persist_to_mongo(status = Status.Confirmed.name):
    """
    Fetch COVID data for all
    countries and persist to Mongo
    """
    client = pymongo.MongoClient(LOCAL_HOST)
    testDB = client[DB]
    covidCollection = testDB[COV_COLLECTION]
    response = requests.get(COUNTRIES_PATH)
    allCountries = json.loads(response.text)

    for ct in allCountries:
        response = requests.get(PATH.format(ct['Slug'], status))
        allData = json.loads(response.text)
        currCases = 0
        for dt in allData:
            prevCases = currCases
            dt["Date"] = datetime.strptime(dt["Date"], "%Y-%m-%dT%H:%M:%SZ")
            currCases = dt["Cases"]
            dt['DailyCases'] = currCases - prevCases
            covidCollection.insert_one(dt)


if __name__ == '__main__':
    fetch_and_persist_to_mongo()
