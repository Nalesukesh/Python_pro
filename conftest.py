import pytest
from colorama import Fore


@pytest.fixture(scope='class')
def setup():
    print(Fore.CYAN, "Test Execution Start")
    yield
    print(Fore.CYAN, "Test Execution successfully completed")
