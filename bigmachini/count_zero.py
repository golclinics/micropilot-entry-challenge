def count_zero(data):
    if len(data) == 0 or 0 not in data:
        return 0
    else:
        # use the count feature for python as we are only counting one item
        return data.count(0)
