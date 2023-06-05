import pytest


@pytest.fixture(scope="class")
def setup():
    print("(setup) I will be executed first")
    yield
    print("(setup) I will be executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Mitchell", "McConnell", "rahulshettyacademy.com"]


@pytest.fixture(params=["chrome", "firefox"])
def cross_browser(request):
    return request.param


# to pass multiple params, passed as tuples

@pytest.fixture(params=[("chrome", "rahul", "shetty"), ("firefox", "rahul", "shetty"), ("IE", "foo")])
def cross_browser2(request):
    return request.param
