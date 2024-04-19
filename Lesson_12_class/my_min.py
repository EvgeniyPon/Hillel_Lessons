def my_min(*args):
    min_value = args[0]
    for i in args:
        if i < min_value:
            min_value = i
    return min_value