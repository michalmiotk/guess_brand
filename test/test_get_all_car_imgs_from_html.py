import pytest

from get_img import get_all_car_imgs_from_html



@pytest.fixture
def header():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        </head>
        """

def test_get_all_car_imgs_from_html(header):
    webpage = header + """
        <body>
            <div class="pictureImage ">
                <a>
                    <img src="tajne_dane" />
                </a>
            </div>
        </body>
        </html>
        """

    assert get_all_car_imgs_from_html(webpage) == ["tajne_dane"]

def test_get_all_car_imgs_from_html_When_two_images_are(header):
    webpage = header + """
        <body>
            <div class="pictureImage ">
                <a>
                    <img src="tajny_adres1" />
                </a>
            </div>
            <div class="pictureImage ">
                <a>
                    <img src="tajny_adres2" />
                </a>
            </div>
        </body>
        </html>
        """

    assert get_all_car_imgs_from_html(webpage) == ["tajny_adres1", 'tajny_adres2']


def test_get_all_car_imgs_from_html_When_not_typical_images_are(header):
    webpage = header + """
        <body>
            <img src="logo" />
            <div class="pictureImage ">
                <a>
                    <img src="tajny_adres1" />
                </a>
            </div>
            <div class="pictureImage ">
                <a>
                    <img src="tajny_adres2" />
                </a>
            </div>
        </body>
        </html>
        """
    assert get_all_car_imgs_from_html(webpage) == ["tajny_adres1", 'tajny_adres2']