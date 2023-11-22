"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if time >= 1 and time <= 4:
        return False
    elif time >= 5 and time <= 17 and coffee_needed:
        return True
    elif time >= 18 and time <= 24:
        return True
    return False
        
print(students_study(1,True))
def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b and b == c and a == 5:
        return 10
    elif a == b and b == c and a != 5:
        return 5
    elif b == a or a == c:
        return 0
    else:
        return 1

def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if small_baskets + (5*big_baskets) == ordered_amount:
        return ordered_amount - (5*big_baskets)
    else:
        return -1
print(fruit_order(3,1,10))
