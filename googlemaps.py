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
    if r > 5
        flash('Please enter enter a smaller radius')
        return redirect(url_for('index'))
    try:
        result = get_title_for_cords(x, y, r)
    except:
        flash("Please enter valid numbers")
        return redirect(url_for('index'))
    if not result:
        flash("No titles were found in this area")
        return redirect(url_for('index'))
    else:
        return render_template('html/radius.html', result=result)

@app.route("/map")
def mapview(la, lo):
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=float(la),
        lng=float(lo),
        markers=[(la, lo),(float(la)-1,float(lo)-1)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=la,
        lng=lo,
        fit_markers_to_bounds = True,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': la,
             'lng': lo,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 42.98339,
             'lng': -81.23306,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('html/example.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
