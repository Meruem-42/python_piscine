from types import FunctionType

def ft_reduce(function_to_apply, iterable) :
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    if not isinstance(function_to_apply, FunctionType) :
        raise TypeError(f"{type(function_to_apply)} is not callable")
    if not hasattr(iterable, '__iter__') :
        raise TypeError(f"{type(iterable)} is not iterable")
    try :
        u = iterable[0]
        for elem in iterable[1::] :
            u = function_to_apply(u, elem)
        return u
    except Exception as e :
        return None

def main() :
    lst = []
    lst2 = [1, 2, 3, 4]
    print(ft_reduce(lambda x,y: x + y, lst))

main()