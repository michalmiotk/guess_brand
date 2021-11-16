from flask import Flask, render_template
from get_img import get_one_img_url
import random
from brands import brands


app = Flask(__name__)

@app.route('/')
def main_page():
    true_brand = random.choice(list(brands.keys()))
    brand_url = brands[true_brand]
    car_img_link = get_one_img_url(brand_url)
    car_brands = list(brands.keys())
    js = render_template('js/index.js', true_brand=true_brand)
    return render_template('index.html', car_img_link=car_img_link, car_brands=car_brands, true_brand=true_brand, js=js)

if __name__ == "__main__":
  app.run()