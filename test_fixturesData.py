import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_edit_profile(self, dataLoad):
        log = self.get_logger

        log.info("Starting test case")
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad)
