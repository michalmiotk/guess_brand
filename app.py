from flask import Flask, render_template, request, url_for, session, redirect
from get_img import get_one_img_url
import random
from brands import brands


app = Flask(__name__)

@app.route('/')
def main_page():
    brand_url = random.choice(list(brands.values()))
    car_img_link = get_one_img_url(brand_url)
    return render_template('index.html', car_img_link=car_img_link)

if __name__ == "__main__":
  app.run()