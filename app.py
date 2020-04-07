import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_manager'
app.config["MONGO_URI"] = 'mongodb+srv://tokyo_ghoul:edna@myfirstcluster-uvyys.mongodb.net/recipe_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_posts')
def get_posts():
    return render_template("main.html", posts=mongo.db.posts.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)