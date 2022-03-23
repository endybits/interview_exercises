def fizzbuzz(n = 100):
    """ Show the numbers from 1 to n and replace the divisibles by 3 with 'fizz',
        the divisibles by 5 with 'fuzz', 
        and the divisibles by 3 and 5 at the sae time with 'fizzbuzz'

    Args:
        n (int, optional): Limit. Defaults to 100.
    """

    for i in range(1, n):
        divisible_by_three = i % 3 == 0
        divisible_by_five = i % 5 == 0
        if divisible_by_three and divisible_by_five:
            print('fizzbuzz')
        elif divisible_by_three:
            print('fizz')
        elif divisible_by_five:
            print('buzz')
        else:
            print(i)


if __name__ == '__main__':
    fizzbuzz()