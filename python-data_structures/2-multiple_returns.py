def multiple_returns(sentence):
    try:
        return len(sentence), sentence[0]
    except:
        return len(sentence), None
