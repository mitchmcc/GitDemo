import pytest


@pytest.mark.smoke
def test_demo2_test1():
    a = 3
    b = 5

    assert a == b, "A does not equal B"


def test_demo2_CreditCard(setup):
    print("Ca va?")


def test_demo2_fixtureDemo(setup):
    print()
    print("I will execute steps in fixtureDemo method")

