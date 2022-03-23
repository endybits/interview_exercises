
def custom_except(equals = True):
    """Raise custo Exceptions

    Args:
        equals (bool, optional): Raise exception to same values. Defaults to True.

    Raises:
        Exception: Sae values
        Exception: Another error
    """
    if equals:
        return "Values maximun cann't be the same"
    else:
        return 'Oops! Something went wrong.'


def which_max(n1: int, n2: int):
    """Given two numbers return the maximun

    Args:
        n1 (int): First value
        n2 (int): Secound value

    Returns:
        int: The maximun value
        bool: Equal values
    """
    
    if n1 > n2:
        return n1, False
    elif n2 > n1:
        return n2, False
    elif n1 == n2:
        return n1, True


def max_of_three_nums(n1: int, n2: int, n3:int):
    """Given three numbers return the maximun

    Args:
        n1 (int): first value
        n2 (int): secound
        n3 (int): _description_

    Logic: 
        if n1 > n2 & n2 > n3: then n1 > n3
    Returns:
        _type_: _description_
    """
    n, equals = which_max(n1, n2)

    if not equals:
        max, equals = which_max(n, n3)
        if equals == False:
            return max
        else:
            raise Exception(custom_except(True))
    else:
        max, equals = which_max(n, n3)
        if max != n:
            return max
        else:
            raise Exception(custom_except(True))


if __name__ == '__main__':
    
    mx = max_of_three_nums(2, -2, -3)
    print(mx)