def best_score(a_dictionary):
    # returns a key with the biggest integer value.
    if not a_dictionary.values():
        return None
    best_score = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == best_score:
            return key
