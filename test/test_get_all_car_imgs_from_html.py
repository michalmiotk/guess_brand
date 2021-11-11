import pytest

from get_img import get_all_car_imgs_from_html

def test_get_all_car_imgs_get_all_car_imgs_from_html():
    webpage = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            </head>
            <body>
                <div class="pictureImage ">
                    <a>
                        <img src="tajne_dane" />
                    </a>
                </div>
            </body>
            </html>
            """
    
    assert get_all_car_imgs_from_html(webpage) == "tajne_dane"