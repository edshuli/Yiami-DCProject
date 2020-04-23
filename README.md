[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/edshuli/Yiami-DCProject) 

# Project Name: Yiami


## Data Centric Development - Code Institute | Project 4
<hr>

### About Yiami-Project

*Yiami is a cooking website, where you can find fresh and healthy recipes. It allows you to access cooking recipes as well as to add
your own recipe. Is your personal online cooking book*

In this proejct I am using <a href="https://www.python.org/">Python 3</a>, <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> and <a href="https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=google&utm_campaign=gs_emea_netherlands_search_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&gclid=EAIaIQobChMIpayiipL-6AIVEOR3Ch2HKwvkEAAYASAAEgK9JfD_BwE">MongoDB Atlas</a>.

## UX
<hr>

*Yiami website's  main focus is to **provide you with healthy and easy to make recipes**. Yiami was created for the food lovers, people who love to cook but they are so busy to stay all day cooking.*
*Here you will find recipes that don't require so much time from your life and also very very tasty.*
*After all Food is Memories, so let's create some!*

As a user you can:

* Browse through all the recipes in the website and you will be able to choose from different categories and courses.
  
  Our Categories are divided such as: 
  * healthy
  * vegetarian
  * vegan

  And we course which is divided such as:
  * main
  * dessert
  * snacks
  * eating on budget

* Register to this website, login.
* Add you own recipe, edit, or delete one.

## Features
<hr>

### Existing Features

* **Navigation**
  * The main logo leads to HomePage.
  * Through recipes item-link all users have access to **All recipes**.
  * SignIn/SignUp buttom allow users to logIn to the exsting acount.
  * If they are not registered then they can create one account. 
  * **Logged In**
    * You are able to access the **Add your own recipe page**
    * You are able to logOut
* **Footer**
  * Social icons that direct user to social media profile  
* **Recipe**
  * Show all recipes
  * There is a sort option, where the user can sort the recipes based on their preferences
* **Recipe**
  * Show the information about the selected recipe
    * Name of the recipe
    * Image
    * Description of Recipe
    * Recipe info
      * Author
      * course
      * category
      * Cook time
      * Yields
    * Ingredients
    * Notes
    * Instructions
  * If user is logged in, there is the option of Editing or Deleting the recipe
* Add your own recipe
  * Allows logged in user to add a recipe
* Edit Recipe  
  * Allow logged in user to edit their recipe
* Delete Recipe
  * Allow logged in user to delete theri recipe

### Features Left to Implement

* Add voting system
* Add comment section
* Newsletter for all the new recipes uploaded

## Technologies Used
<hr>

*The technologies we used to create the website are the follow:*
### **Front End**

<a href="https://dev.w3.org/html5/html-author/"> **HTML 5** </a> 

* Markup language used for structuring and presenting content on the World Wide Web.

<a href="https://jigsaw.w3.org/css-validator/Email.html"> **CSS 3** </a> 

* Style the web documents

<a href="https://getbootstrap.com/docs/4.3/getting-started/download/">**Bootstrap 4.0.0**</a> 

* To make the website more responsive

<a href="https://jquery.com/">**JQuery**</a> 

* For better user experience

### **Back End**

<a href="https://flask.palletsprojects.com/en/1.1.x/">**Flask 1.1.2**</a> 

* A ightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications

<a hfer="https://api.mongodb.com/python/current/tutorial.html">**PyMongo 3.10.1**</a>

* I used to connect with **MongDb**

<a href="https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=google&utm_campaign=gs_emea_netherlands_search_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&gclid=EAIaIQobChMIpayiipL-6AIVEOR3Ch2HKwvkEAAYASAAEgK9JfD_BwE"> **MongoDb**</a>

* A document based database


## Testing
<hr>

I was testing the application manual throughout the process of it.
I used mainly <a href="https://developers.google.com/web/tools/chrome-devtools/">**DEVTOOLS**</a> for my testing. The site was tested on many browser like ( Google Chrome,
Internet Explorer, Safari and Opera ) and mobile devices such as Iphone8,6s, Huaweii P20 Lite, Samsung Galaxy S10, Samsung Galaxy A20 (Chrome, Ipad, Safari) to ensure compatibility and responsiveness.

The screen sizes tested on decision are the below:

* Moto G4 (360 x 640)
* Galaxy S5 (360 x 640)
* Pixel 2  (411 x 731)
* Pixel 2XL (411 x 823)
* iPhone 5/SE (320 x 568)
* iPhone 6/7/8 (375 x 667)
* iPhone 6/7/8 Plus (414 x 736)
* iPhone X (375 x 812)
* iPad (768 x 1024)
* iPad Pro (1024 x 1366)
* Desktop (xl screens)

To validate the HTML code I used <a href="https://validator.w3.org/"> The W3C Markup Validation Service </a> and 
<a href="https://htmlformatter.com/"> HTML Formatter</a> to use the correct format of HTML5. Showed few errors but that is mainly because of the links that we used due to Python and Flask. But the links work perfectly.

To validate CSS 3 code I used <a href="https://jigsaw.w3.org/css-validator/Email.html"> The CSS Validation Service </a>. The validation showed no error and the connection with Bootstrap was very good. 
I created my own JSON file so I used the <a href="https://jsonlint.com/"> The JSon Validotor </a> to correct all the errors that I had.

### NavBar-Footer

The navigation links as well as the social links didn't show any error. My main focus was that the SignIn/SignUp navigation links were working correclty and we linked to the correct page.   

### Sing In - Sign up

Both the Sign In and Sign Up form were tested and they work. The user cannot be registered if the form has an invalid email address,
then an error will be appeared notified the invalid address. Also the required attribute is added to the 'name' and 'password' fileds so if those fields are not filled in then the user will be asked to fill in this fields and the form will not be submitted. 
If all fields are valid then the user will get a flash message on the main page with this Username. If an exsiting user tries to register then a flash message will appear saying that 'Sorry username already exists!' that will appear if the username if taken from another user.

If an exsting user tries to login with an unvalid username or password a flash message will poped-up alerting with the message
'Invalid username/password'.

Add you own recipe form, was also tested to make sure that the input text works correctly for each field, if any field is left bank then the recipe is still added. The recipe is added correctly to database.

Edit recipe was tested if the data was immediately updated both in the site but also in the databe. And test also that the edit button works correctly.

Delete recipe was tested if the data is deleted correctly from the database. Test that the delete button works correctly.

## Deployment
<hr>

#### GitHub :
* To check my website on GitHub click <a href="https://github.com/edshuli/Yiami-DCProject">**here**</a>
* If you want to clone or downloan the repo, you can simply click on the green button "Clone or Download" and then save it in a folder
#### Heroku :
* This website is hosted on Heroku. You can check the live version here: <a href="https://yiami-project.herokuapp.com/">https://yiami-project.herokuapp.com/</a>

##### Deploy project to Heroku
* Create app on Heroku
  * Login to your acount on Heroku and create the project by setting its' name.
  * Under the settings tab you click the button **Reveal Config Vars** and I set the IP to 0.0.0.0 and the PORT to 5000 and later on we add
  MONGO_URI.

I am using  GitPod so I am use the below commands on terminal:
* Login to Heroku: **heroku login**
* Enter your credentials: **email and password**
* Create a new Git repository
  * Initialize a git repository in a new or existing directory
     * $ cd my-project/
     * $ git init
     * $ heroku git:remote -a ednaer     
* Deploy your application
  * Commit your code to the repository and deploy it to Heroku using Git.
    * $ git add .
    * $ git commit -am "make it better"
    * $ git push heroku master  

* Existing Git repository
  * For existing repositories, simply add the heroku remote
    * $ heroku git:remote -a ednaer

#### Database
The database choosen for this website is MongoDB which stores data in JSON format.

## Credits 
<hr>

### Contents
Recipe data and images of the food used in this project are from different website like:
* <a href="https://tasty.co/">Tasty</a>
* <a href="https://www.jamieoliver.com/recipes/">JamieOliver</a>
* <a href="https://akispetretzikis.com/">Akis</a>, where I got the inspiration also :)

### Media
All photos were taken from <a href="https://unsplash.com/t/wallpapers">Unsplash</a> a source for freely usable images.

### Acknoledgements
A **special thanks** to <a href="https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ">Santdex</a> for the guidance of how to creat the loginForm and the registerFormand also to  <a href="https://www.programcreek.com/python/example/51564/forms.LoginForm">https://www.programcreek.com/python/example/51564/forms.LoginForm/RegisterForm</a>.
I got a lot of help from:
* <a href="https://stackoverflow.com/">Stack Overflow</a>
* <a href="https://www.w3schools.com/">W3schools</a>
* <a href="https://slack.com/intl/en-nl/">Slack</a>
* My tutor and all the support from **Code Institute**

**This is for educational use only**
