import requests
from bs4 import BeautifulSoup

def is_match_exactly_this_class(bs4tag):
    return True if len(bs4tag['class']) == 1 else False

def get_all_car_imgs_urls(*, relative_path):
    r = requests.get('https://mklr.pl'+relative_path)
    return get_all_car_imgs_from_html(r.content.decode("utf-8"))

def get_all_car_imgs_from_html(html_text):
    soup = BeautifulSoup(html_text, features="html.parser")
    div_with_imgs = soup.find_all("div",{"class": 'pictureImage'})
    relative_urls = []
    for div in div_with_imgs:
        if is_match_exactly_this_class(div):
            if div.a.img is not None:
                img_src = div.a.img['src']
                relative_urls.append(img_src)
    return relative_urls

def get_car_from_list(car_imgs_relative_url):
    forbidden_url = "/uimages/services/motokiller/i18n/pl_PL/201403/1394231039_by_Charakterek.jpg?1394336707"
    if len(car_imgs_relative_url):
        for url in car_imgs_relative_url:
            if url != forbidden_url:
                return url 
        
    return None

def get_one_img_url(page_relative_path):
    car_imgs_relative_url = get_all_car_imgs_urls(relative_path=page_relative_path)
    car_relative_url = get_car_from_list(car_imgs_relative_url)
    if car_relative_url is None:
        return None
    return 'https://mklr.pl' + car_relative_url

   
if __name__=='__main__':
    print(get_one_img_url('/Mercedes-Benz-81-marka'))