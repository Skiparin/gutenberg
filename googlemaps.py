from flask import Flask, render_template, request, redirect, url_for
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from psql_queries import get_cities_for_title, get_titles_for_city, get_titles_and_cords_for_author, get_title_for_cords
from flask import flash

app = Flask(__name__, template_folder=".")
app.secret_key = 'some secret key'
GoogleMaps(app)

@app.route('/')
def index():
    return render_template('html/index.html')

@app.route('/map',methods=['POST'])
def map_post():
    title = request.form['title']
    result = get_cities_for_title(title)
    if not title:
        flash('Please enter a book title')
        return redirect(url_for('index'))
    elif not result:
        flash("Can't find a book title with that name")
        return redirect(url_for('index'))
    else:
        mymap = Map(
            identifier="view-side",
            lat=0,
            lng=0,
            markers=result,
            optimized=False
        )
        return render_template('html/map.html', mymap=mymap)

@app.route('/titles',methods=['POST'])
def titles():
    city = request.form['city']
    result = get_titles_for_city(city)
    if not city:
        flash('Please enter a city name')
        return redirect(url_for('index'))
    elif not result:
        flash("Can't find titles mentioning that city")
        return redirect(url_for('index'))
    else:
        return render_template('html/titles.html', result=result)

@app.route('/authors',methods=['POST'])
def authors():
    author = request.form['author']
    result = get_titles_and_cords_for_author(author)
    if not author:
        flash('Please enter an author name')
        return redirect(url_for('index'))
    elif not result["titles"]:
        flash("Can't find an author with that name")
        return redirect(url_for('index'))
    else:
        mymap = Map(
            identifier="view-side",
            lat=0,
            lng=0,
            markers=result["cords"]
        )
        return render_template('html/authors.html', mymap=mymap, result=result["titles"])

@app.route('/radius',methods=['POST'])
def radius():
    x = request.form['x']
    y = request.form['y']
    r = request.form['r']
    if not x or not y or not r:
        flash('Please enter x and y coordinates with a radius')
        return redirect(url_for('index'))
    try:
        if float(r) > 1:
            flash('Please enter enter a radius at 1 or less')
            return redirect(url_for('index'))
        result = get_title_for_cords(x, y, r)
    except:
        flash("Please enter valid numbers")
        return redirect(url_for('index'))

    if not result:
        flash("No titles were found in this area")
        return redirect(url_for('index'))

    else:
        return render_template('html/radius.html', result=result)
