import pytest
 
#defining a function with parameter x
def func(x):
    return x+5
 
#defining an another function  
def test_method():
#check whether 3+5 = 8 or not by passing 3 as an argument in function x
    assert func(3) == 8
 
def test_answer1():
  a = 5*2
  b = 10
  assert a==b
   
def test_answer2():
  c = 15
  d = 3*5
  assert c==d