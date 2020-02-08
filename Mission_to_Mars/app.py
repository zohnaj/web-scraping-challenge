from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app=Flask(__name__)

mongo=PyMongo(app, uri="mongodb://localhost:27017/mars_results")

@app.route("/")
def index():
    mars_results = mongo.db.mars_results.find_one()
    return render_template("index.html", mars_results=mars_results)

@app.route("/scrape")
def scrape():
    mars_data= scrape_mars.scrape()
    mongo.db.mars_results.update({}, mars_data, upsert=True)
    return "Complete"

if __name__ == "__main__":
    app.run(debug=True)