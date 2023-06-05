import pytest


@pytest.mark.usefixtures("setup")
class FixturesTest:

    def test_fixtures_test1(self):
        a = 3
        b = 5
        assert a == b, "A does not equal B"

    def test_fixtures_test2(self):
        print("fixtures_test2")

    def test_fixtures_test3(self):
        print("fixtures_test3")

    def test_fixtures_test4(self):
        print("fixtures_test4")
