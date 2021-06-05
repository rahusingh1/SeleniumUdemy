import pytest
import sys

@pytest.mark.skip(reason='this test not include in this build')
def test_demp1():
    assert True

@pytest.mark.skipif(sys.version_info < (3, 9), reason="requires python3.9 or higher")
def test_demo2():
    assert True

def test_demo3():
    assert True

@pytest.mark.windows
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.linux
def test_linux_1():
    assert True

@pytest.mark.linux
def test_linux_2():
    assert True
