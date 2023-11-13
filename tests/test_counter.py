from lib.counter import *

def test_counter_number_5():
    
    # to basicly create a test that tells how many numbers have you counted

    counter = Counter()
    counter.add(5) 
    result = counter.report()
    assert result == "Counted to 5 so far."
def test_counter_10():
    counter = Counter()
    counter.add(10) 
    result = counter.report()
    assert result == "Counted to 10 so far."