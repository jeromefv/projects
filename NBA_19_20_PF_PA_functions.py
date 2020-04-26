def bin_maker(start, stop, num):
    """
    This function will create bins for a matplotlib item.
    start = left-most bin edge
    stop = right-most bin edge
    num = number of bins
    """
    table = []
    dx = (stop - start) / (num)
    table.append(start)
    for i in range(1, num):
        step = i * dx
        table.append(start+step)
    table.append(stop)
    return table

def min_finder(data_set):
    val = data_set[0]
    for i in data_set:
        if i < val:
            val = i
    return val

def max_finder(data_set):
    val = data_set[0]
    for i in data_set:
        if i > val:
            val = i
    return val

def smart_bin(data_set, num):
    bin_set = bin_maker(min_finder(data_set), max_finder(data_set), num)
    return bin_set