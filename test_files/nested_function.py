def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x)