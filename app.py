import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_manager'
app.config["MONGO_URI"] = 'mongodb+srv://tokyo_ghoul:edna@myfirstcluster-uvyys.mongodb.net/recipe_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

#All Recipes
all_recipes = mongo.db.recipes

#Homepage

@app.route('/')
@app.route('/main')
def main():
    recipes = all_recipes.find()
    return render_template('main.html', recipes=recipes)

#Show All Recipes

@app.route('/get_recipes')
def get_recipes():
    recipes = all_recipes.find()
    return render_template("recipes.html", recipes=recipes)

#Sort Recipes
@app.route('/sort_recipes', methods = ['GET','POST'])
def sort_recipes():
    if request.method == 'POST':
        recipes = all_recipes.find({ "$or": [ { "course": request.form["course"] }, { "category": request.form["category"] }] })
        print(request.form)
        return render_template('recipes.html', recipes=recipes)
    return render_template('recipes.html', recipes=recipes)

#Show Each Recipe
@app.route('/recipe/<recipe_id>')   
def recipe(recipe_id):
    recipes = all_recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('eachRecipe.html', recipes=recipes)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)