import pytest

from get_img import get_car_from_list
@pytest.fixture
def forbidden_url():
    return "/uimages/services/motokiller/i18n/pl_PL/201403/1394231039_by_Charakterek.jpg?1394336707"

def test_GIVEN_empty_list_EXPECT_return_None():
    assert get_car_from_list([]) is None

def test_GIVEN_list_with_one_url_EXPECT_return_address_contating_than_url():
    some_url = "abc"
    assert some_url in get_car_from_list([some_url])

def test_GIVEN_list_with_forbidden_url_EXPECT_return_None(forbidden_url):
    assert get_car_from_list([forbidden_url]) is None

def test_GIVEN_list_with_forbidden_url_and_normal_url_EXPECT_return_url_containing_normal_url(forbidden_url):
    some_url = "abc"
    assert some_url in get_car_from_list([some_url, forbidden_url])


def test_GIVEN_list_with_forbidden_url_and_normal_url_but_in_other_order_EXPECT_return_url_containing_normal_url(forbidden_url):
    some_url = "abc"
    assert some_url in get_car_from_list([forbidden_url, some_url])