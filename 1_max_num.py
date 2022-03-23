def which_max(n1: int, n2: int):
    """Given two numbers return the maximun

    Args:
        n1 (int): First value
        n2 (int): Secound value

    Returns:
        int: The maximun value
    """
    
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n1 == n2:
        raise Exception('The values are the same')
    else:
        raise Exception('Oops! Something went wrong.')

if __name__ == '__main__':
    print(which_max(54, 54))