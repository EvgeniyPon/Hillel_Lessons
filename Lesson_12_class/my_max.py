def my_max(*args):
    max_value = args[0]
    for i in args:
        if i > max_value:
            max_value = i
    return max_value
