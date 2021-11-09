import  requests
import bs4

def get_brands_and_relative_urls():
    url = "https://mklr.pl/marki-samochodow"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, features="html.parser")
    all_marks = soup.find_all('div', {'class':'top'})
    brands_and_relative_urls = {} 
    for mark in all_marks:
        if h2:=mark.h2:
            if a:=h2.a:
                brand_raw = a.text
                brand = brand_raw.lstrip().rstrip()
                link = a['href']
                brands_and_relative_urls[brand] = link
    return brands_and_relative_urls

if __name__ == '__main__':
    print(get_brands_and_relative_urls())
