import csv
from flask import Flask, render_template, request, redirect, url_for
import requests
from pager import Pager
import json
import pickle


def read_table(url):
    """Return a list of dict"""
    # r = requests.get(url)
    with open(url) as f:
        return [row for row in csv.DictReader(f.readlines())]


APPNAME = "FashionIQ-Image-Viewer"
STATIC_FOLDER = ''
# TABLE_FILE = "example/fakecatalog.csv"
diction = open("dress.test.json.pt", 'rb')
diction = pickle.load(diction)

n = len(diction)
print('the length of diction is: ',)
asin_array = []

for asin in diction:
    asin_array.append(asin)



# table = read_table(TABLE_FILE)
pager = Pager(n)


app = Flask(__name__, static_folder=STATIC_FOLDER)
app.config.update(
    APPNAME=APPNAME,
    )


@app.route('/')
def index():
    return redirect('/0')


@app.route('/<int:ind>/')
def image_view(ind=None):
    if ind >= pager.count:
        return render_template("404.html"), 404
    else:
        pager.current = ind
        print(diction[asin_array[ind]])
        u1 = diction[asin_array[ind]]['imUrl']
        u2 = None
        # if len(diction[asin_array[ind]]['imUrl']) > 0:
        #     u1 = diction[asin_array[ind]]['imUrl'][0] 
        # if len(diction[asin_array[ind]]['imUrl']) > 1:
        #     u2 = diction[asin_array[ind]]['imUrl'][1]
        # print()
        return render_template(
            'imageview.html',
            index=ind,
            pager=pager,
            data=diction[asin_array[ind]],
            url1=u1,
            asin=asin_array[ind]
            # url2=u2
            )


@app.route('/goto', methods=['POST', 'GET'])    
def goto():
    return redirect('/' + request.form['index'])


if __name__ == '__main__':
    app.run(host='169.46.81.178')
