from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

def getAverageScore(termOne, termTwo):
    terms = [termOne, termTwo]
    pytrends.build_payload(terms, timeframe='today 3-m', geo='', gprop='')
    res = pytrends.interest_over_time()

    return {"scoreOne": round(res[termOne].mean()), "scoreTwo": round(res[termTwo].mean())}