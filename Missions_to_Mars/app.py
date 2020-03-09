from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri = "mongodb://localhost:27017/Scrape_Mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # 1. 
    Latest_New = mongo.db.Latest_New.find_one()
    # 2. 
    featured_image = mongo.db.featured_image.find_one()
    # 3. 
    mars_weather = mongo.db.mars_weather.find_one()
    # 4. 
    mars_facts = mongo.db.mars_facts.find_one()
    # 5. 
    mars_hemispheres = mongo.db.mars_hemispheres.find_one()
    
    # Return template and data
    return render_template("index.html", Latest_New = Latest_New, 
                           featured_image = featured_image, mars_weather = mars_weather, 
                           mars_facts = mars_facts, mars_hemispheres =  mars_hemispheres)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # 1.
    # Run the Latest New scrape function:
    Latest_New = scrape_mars.NASA_Mars_News()

    # Update the Mongo database using update and upsert=True
    mongo.db.Latest_New.update({}, Latest_New, upsert = True)

    # 2.
    # Run the featured image scrape function:
    featured_image = scrape_mars.featured_image()

    # Update the Mongo database using update and upsert=True
    mongo.db.featured_image.update({}, featured_image, upsert = True)

    # 3.
    # Run the weather scrape function:
    mars_weather = scrape_mars.mars_weather()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_weather.update({}, mars_weather, upsert = True)

    # 4.
    # Run the facts scrape function:
    mars_facts = scrape_mars.mars_facts()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_facts.update({}, mars_facts, upsert = True)

    # 5.
    # Run the hemispheres scrape function:
    mars_hemispheres = scrape_mars.mars_hemispheres()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_hemispheres.update({}, mars_hemispheres, upsert = True)

    # Redirect back to home page
    return redirect("/")

#

if __name__ == "__main__":
    app.run(debug=True)
