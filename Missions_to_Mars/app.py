from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    
    # Find one record of data from the mongo database
    mission_data = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mission=mission_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    # Run the scrape function
    # mars_data = scrape_mars.scrape_info()
    news_title = "NASA Engineers Checking InSight's Weather Sensors"
    news_p = "An electronics issue is suspected to be preventing the sensors from sharing their data about Mars weather with the spacecraft."

    mars_data = {
    "news_title": news_title,
    "news_p": news_p,
    }

    # Update the Mongo database using update and upsert=True
    mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
