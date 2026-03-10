from pytrends.request import TrendReq

pytrend = TrendReq()

def get_trends(keyword):

    pytrend.build_payload([keyword])

    data = pytrend.interest_over_time()

    return data
