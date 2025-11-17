from types import FunctionType

def ft_filter(function_to_apply, iterable) :
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    if not isinstance(function_to_apply, FunctionType) :
        raise TypeError(f"{type(function_to_apply)} is not callable")
    if not hasattr(iterable, '__iter__') :
        raise TypeError(f"{type(iterable)} is not iterable")
    for elem in iterable :
        try :
            if function_to_apply(elem) :
                yield elem
        except Exception as e :
            return None


def main() :
    lst = [1, 2, 3, 4]
    print(list(ft_filter(lambda x: x > 2, lst)))

main()