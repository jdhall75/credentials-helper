import pathlib

import pytest

from credentials_helper import get_credentials


@pytest.fixture
def bad_file():
    """generate a file with the wrong permisions"""
    tmp_path = pathlib.Path(".credentails")
    tmp_path.write_text("USERNAME=xyz\nPASSWORD=secret\n")
    tmp_path.chmod(0o666)
    yield str(tmp_path)
    tmp_path.unlink()


@pytest.fixture
def good_file():
    """generate a file with the wrong permisions"""
    tmp_path = pathlib.Path(".credentails")
    tmp_path.write_text("USERNAME=xyz\nPASSWORD=secret\n")
    tmp_path.chmod(0o600)
    yield str(tmp_path)
    tmp_path.unlink()


def test_with_bad_file_perms(bad_file):
    """Bad file with bad permisions raises the proper exception"""
    with pytest.raises(PermissionError):
        username, password = get_credentials(file=bad_file)


def test_with_good_file_perms(good_file):
    username, password = get_credentials(file=good_file)
    assert isinstance(username, str)
    assert isinstance(password, str)
