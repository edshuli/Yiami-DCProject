import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_manager'
app.config["MONGO_URI"] = 'mongodb+srv://tokyo_ghoul:edna@myfirstcluster-uvyys.mongodb.net/recipe_manager?retryWrites=true&w=majority'
app.config['SECRET_KEY']=os.environ.get("SECRET_KEY")

# Set Randome Key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


#All Recipes
all_recipes = mongo.db.recipes

#All Users
users=mongo.db.users
#Homepage

@app.route('/')
@app.route('/main')
def main():
    recipes = all_recipes.find()

    if 'username' in session:
        flash('You are logged in as ' + session['username']) 
        return render_template('main.html', username=session['username'], username_id=users['_id'])
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


#Sign In
@app.route('/signIn', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username' : request.form['username']})
    password = request.form['password']


    if login_user:
        if check_password_hash(users['password'], password):
            session['username'] = request.form['username']
            flash('Logged in as {username}!')
            return redirect(url_for('get_recipes'))
    
    flash('Invalid username/password combination') 
    return render_template('signInUp.html')   

# Sign Up
@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    if request.method == 'POST':
        existing_user = users.find_one({'username': request.form['username']})
        if existing_user is None:
            pw_hash =  generate_password_hash(request.form['password'])
            users.insert_one({'username': request.form['username'], 'email': request.form['email'],'password': pw_hash })
            session['username'] = request.form['username']
            flash("Welcome session['username']!") 
            return redirect(url_for('main'))
        flash("Sorry username already exists!")
    return render_template('signInUp.html')

#Log Out
@app.route('/logout')
def logout():
    session.pop('username')
    flash("Successfully logged out")
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)