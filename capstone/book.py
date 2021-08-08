
from extract_book_info import extract_isbn, image_parsing
from flask import Flask, render_template, request, make_response
from functools import wraps, update_wrapper
from datetime import datetime
from rating import final_compare
import os
import cv2

r = ''

def nocache(view):
  @wraps(view)
  def no_cache(*args, **kwargs):
    response = make_response(view(*args, **kwargs))

    response.headers['Last-Modified'] = datetime.now()
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response
  return update_wrapper(no_cache, view)

app = Flask(__name__)

@app.route("/isbn", methods=['GET', 'POST', 'PUT'])
@nocache
def get_image():
    isbn = request.args.to_dict()['isbn']
    bookinfo = extract_isbn(isbn)
    print(bookinfo)
    img = image_parsing(bookinfo['thumbnail'])
    #os.remove('static/image/test2.jpeg')
    cv2.imwrite('static/image/test2.jpeg', img)
    return "test"

@nocache
@app.route("/show")
def show_image():
    return render_template("result.html", image_file='image/test2.jpeg')

@app.route("/distinguish", methods=['GET'])
def distinguish():
    global r
    r = final_compare('static/image/test.jpg', 'static/image/test2.jpeg')
    os.remove('static/image/test.jpg')
    os.remove('static/image/test2.jpeg')
    return "test"

@app.route("/grade")
def grade():
    return render_template("grade_result.html", grade=r)

if __name__ == "__main__":
    app.run(host="serverIp", port="5000", debug=True)