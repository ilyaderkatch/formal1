import pytest
import main

def test_basic():
    assert main.find_answer(['ab+c.aba.*.bac.+.+*', '5', '1']) == 'YES'  # ((a + b)c + a(ba)*(b + ac))*
    assert main.find_answer(['ab+c.aba.*.bac.+.+*', '1', '5']) == 'NO'  # ((a + b)c + a(ba)*(b + ac))*
    assert main.find_answer(['acb..bab.c.*.ab.ba.+.+*a.', '4', '0']) == 'YES'  # (acb + b(abc)*(ab + ba))*a
    assert main.find_answer(['acb..bab.c.*.ab.ba.+.+*a.', '5', '0']) == 'YES'  # (acb + b(abc)*(ab + ba))*a
    assert main.find_answer(['acb..bab.c.*.ab.ba.+.+*a.', '14', '13']) == 'YES'  # (acb + b(abc)*(ab + ba))*a

def test_error_a_lot_of_letters():
    assert main.find_answer(['aaa+', '5', '1']) == 'ERROR'
    assert main.find_answer(['a*aa1bc.+aaa+..*', '4', '1']) == 'ERROR'
    assert main.find_answer(['aa', '1', '5']) == 'ERROR'

def test_error_a_lot_of_operators():
    assert main.find_answer(['a+a', '3', '2']) == 'ERROR'
    assert main.find_answer(['a*b*c*1*++++*', '5', '1']) == 'ERROR'


