from mafh.commons.utils import *
import pytest


@pytest.fixture()
def setup():
    xx = UtilityFunctions()
    yield xx
