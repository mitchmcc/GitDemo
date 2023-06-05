# pytest conventions:
# All files must start with test_
# All functions must also start with test_
import pytest


def test_demo1_test1(setup):
    print("Hello")
    # for Git demo
    print("Hello2")
    print("GitDemoX update")
    print("GitDemoX update 2")

@pytest.mark.smoke
def test_demo1_test2_CreditCard(setup):
    print("World")


def test_cross_browser(cross_browser):
    # print(type(cross_browser))
    print("Running for browser:  " + cross_browser)

def test_cross_browser2(cross_browser2):
    print(len(cross_browser2))
    print(cross_browser2[1])
