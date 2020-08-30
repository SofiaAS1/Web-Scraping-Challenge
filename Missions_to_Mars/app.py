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
   
    # news_title = "NASA Engineers Checking InSight's Weather Sensors"
    # news_p = "An electronics issue is suspected to be preventing the sensors from sharing their data about Mars weather with the spacecraft."
    # featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA08003_hires.jpg" 
    # img1_title = 'Cerberus Hemisphere Enhanced'
    # img1_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    # img2_title = 'Schiaparelli Hemisphere Enhanced'
    # img2_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    # img3_title = 'Syrtis Major Hemisphere Enhanced'
    # img3_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    # img4_title = 'Valles Marineris Hemisphere Enhanced'
    # img4_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    # mars_data = {
    #     "news_title": news_title,
    #     "news_p": news_p,
    #     "featured_image_url": featured_image_url,
    #     "img1_title": img1_title,
    #     "img1_url": img1_url,
    #     "img2_title": img2_title,
    #     "img2_url": img2_url,
    #     "img3_title":img3_title,
    #     "img3_url": img3_url,
    #     "img4_title": img4_title,
    #     "img4_url": img4_url,
    # }
    
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
