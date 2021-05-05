from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
import dns
import os
from werkzeug.utils import secure_filename

PEOPLE_FOLDER = r"static\photos"

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://kathan:ktmehta2000@cluster0.kk42z.mongodb.net/users?retryWrites=true&w=majority'
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/details', methods=['POST'])
def details():
    if 'thumbnail' in request.files:
        thumbnail = request.files['thumbnail']
        # mongo.save_file(thumbnail.filename, thumbnail)
        path = r"static/photos/" + thumbnail.filename
        thumbnail.save(path)
        mongo.db.survey.insert({'description': request.form.get('description'), 'thumbnail': "/" + path,
                               'location':  request.form.get('location'), 'date':  request.form.get('date')})
    return 'Done !'


@ app.route('/view')
def view():
    data = mongo.db.survey.find()
    return render_template('view.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
