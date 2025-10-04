from demo_greeter_pkg.greet import greet

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet(None) == "Hello, World!"