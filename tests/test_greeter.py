from lib.greet import greet

def test_greet():
    print (greet("Bruno"))
    assert "Hello, Bruno!"
