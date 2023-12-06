"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    assert students_study(1, True) is False

def test__students_study__night_without_coffee__no_studying():
    assert students_study(1, False) is False
    
def test__students_study__day_with_coffee__no_studying():
    assert students_study(5, True) is True

def test__students_study__day_without_coffee__no_studying():
    assert students_study(5, False) is False
    
def test__students_study__evening_without_coffee__no_studying():
    assert students_study(18, False) is True
    
def test__students_study__evening_with_coffee__no_studying():
    assert students_study(18, True) is True

def test__students_study__evening_edge_without_coffee__no_studying():
    assert students_study(18, False) == students_study(24, False) is True
    
def test__students_study__evening_edge_with_coffee__no_studying():
    assert students_study(18, True) == students_study(24, True) is True

def test__students_study__night_edge_without_coffee__no_studying():
    assert students_study(1, True) == students_study(4, True) is False
    
def test__students_study__night_edge_with_coffee__no_studying():
    assert students_study(1, False) == students_study(4, False) is False
    
def test__students_study__day_edge_without_coffee__no_studying():
    assert students_study(5, True) == students_study(17, True) is True
    
def test__students_study__day_edge_with_coffee__no_studying():
    assert students_study(5, False) == students_study(17, False) is False
    

def test__lottery__all_fives():
    assert lottery(5,5,5) is 10

def test__lottery__all_samepos():
    assert lottery(4,4,4) is 5
    
def test__lottery__all_sameneg():
    assert lottery(-4,-4,-4) is 5
    
def test__lottery__all_samezer():
    assert lottery(0,0,0) is 5
    
def test__lottery__all_cdiff():
    assert lottery(2,2,1) is 0

def test__lottery__all_bdiff():
    assert lottery(2,1,2) is 0
    
def test__lottery__all_adiff():
    assert lottery(1,2,2) is 1

def test__lottery__all_diff():
    assert lottery(1,2,3) is 1
    

def test__fruit_order__all_zero():
    assert fruit_order(0, 0, 0) == 0

def test__fruit_order__zero_big():
    assert fruit_order(5, 0, 0) == 0

def test__fruit_order__zero_small():
    assert fruit_order(0, 3, 0) == 0

def test__fruit_order__others_not_zero():
    assert fruit_order(4, 1, 0) == 0

def test__fruit_order__only_big_exact_match():
    assert fruit_order(0, 6, 30) == 0

def test__fruit_order__only_big_not_enough_but_multiple_of_5():
    assert fruit_order(0, 10, 50) == 0

def test__fruit_order__only_big_not_enough():
    assert fruit_order(0, 3, 25) == -1

def test__fruit_order__only_big_more_than_required_match():
    assert fruit_order(0, 10, 20) == 0

def test__fruit_order__only_big_more_than_required_no_match():
    assert fruit_order(0, 9, 27) == -1

def test__fruit_order__only_small_match_more_than_5_smalls():
    assert fruit_order(9, 0, 9) == 9

def test__fruit_order__only_small_not_enough_more_than_5_smalls():
    assert fruit_order(8, 0, 9) == -1

def test__fruit_order__only_small_exact_match():
    assert fruit_order(1, 0, 1) == 1

def test__fruit_order__only_small_not_enough():
    assert fruit_order(1, 0, 3) == -1

def test__fruit_order__only_small_more_than_required():
    assert fruit_order(5, 0, 3) == 3

def test__fruit_order__match_with_more_than_5_smalls():
    assert fruit_order(10, 10, 60) == 10

def test__fruit_order__all_positive_exact_match():
    assert fruit_order(50, 10, 100) == 50

def test__fruit_order__use_all_smalls_some_bigs():
    assert fruit_order(1, 1, 1) == 1

def test__fruit_order__use_some_smalls_some_bigs():
    assert fruit_order(120, 120, 124) == 4

def test__fruit_order__not_enough():
    assert fruit_order(1, 1, 60) == -1

def test__fruit_order__enough_bigs_not_enough_smalls():
    assert fruit_order(4, 11, 55) == 0

def test__fruit_order__enough_smalls_not_enough_bigs():
    assert fruit_order(10, 1, 19) == -1

def test__fruit_order__not_enough_with_more_than_5_smalls():
    assert fruit_order(30, 1, 60) == -1

def test__fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    assert fruit_order(2, 600, 1158) == -1

def test__fruit_order__match_large_numbers():
    assert fruit_order(200, 200, 1200) == 200
