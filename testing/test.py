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