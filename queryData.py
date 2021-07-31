from consts import LOCAL_HOST, DB, COV_COLLECTION
from datetime import datetime
import matplotlib.pyplot as plt
import pymongo


class CoronaProvider()

    def __init__(self):

def queryData(country = 'Israel', startDate = datetime(2020, 3, 1), endDate = datetime(2020, 6, 30),
              verbose=False, type = 'Daily'):
    """
    :param verbose: True for plot
    :param country:
    :param startDate:
    :param endDate:
    :param type: Cumulative or daily
    :return print a chart with covid data according to the above params from mongoDB:
    """
    client = pymongo.MongoClient(LOCAL_HOST)
    testDB = client[DB]
    covidCollection = testDB[COV_COLLECTION]
    myData = covidCollection.find({"Date": {"$gte": startDate, "$lte": endDate},
             "Country": country, "Province": ""})
    casesCum, casesDaily, dates = zip(*[(d['Cases'], d['DailyCases'], d['Date']) for d in myData])
    #move to a different funciton
    #if verbose:
    #    if type == 'Daily':
    #        plt.plot(dates, casesDaily)
    #    else:  # Cumulative
    #        plt.plot(dates, casesCum)
    #   plt.show()
    return casesDaily, dates

if __name__ == '__main__':
    queryData('Italy')
