def trend_score(search_growth,velocity,competition):

    if competition == 0:

        competition = 1

    score = (search_growth * velocity) / competition

    return score
