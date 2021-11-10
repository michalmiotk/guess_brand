import requests
from bs4 import BeautifulSoup
import re

def is_match_exactly_this_class(bs4tag):
    return True if len(bs4tag['class']) == 1 else False

def get_all_car_imgs_relative_url(relative_path):
    r = requests.get('https://mklr.pl'+relative_path)
    soup = BeautifulSoup(r.content, features="html.parser")
    div_with_imgs = soup.find_all("div",{"class": 'pictureImage'})
    relative_urls = []
    for div in div_with_imgs:
        if is_match_exactly_this_class(div):
            img_src = div.a.img['src']
            relative_urls.append(img_src)
    return relative_urls

def get_one_img_url(page_relative_path):
    car_imgs_relative_url = get_all_car_imgs_relative_url(page_relative_path)
    car_relative_url = car_imgs_relative_url[0]
    car_img_full_url = 'https://mklr.pl' + car_relative_url
    return car_img_full_url

    
if __name__=='__main__':
    print(get_one_img_url('/Mercedes-Benz-81-marka'))