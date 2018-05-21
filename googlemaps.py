from flask import Flask, render_template, request, redirect, url_for
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from database import database
from psql_queries import get_cities_for_title

app = Flask(__name__, template_folder=".")
GoogleMaps(app)

@app.route('/')
def my_form():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def my_form_post():
    lo = request.form['lo']
    la = request.form['la']
    print (la+lo)
    return redirect(url_for('mapview',la = la, lo = lo))
@app.route('/map',methods=['POST'])
def map_post():
    city = request.form['city']
    result = get_cities_for_title(city)
    array = []
    for r in result:
        array.append(r)
    print(str(array))
    mymap = Map(
        identifier="view-side",
        lat=0,
        lng=0,
        markers=array
    )
    return render_template('example.html', mymap=mymap)
@app.route('/array')
def array_view():
    names_of_cities = ["London", "Paris", "Copenhagen","blu"]
    return render_template('city.html', names=names_of_cities)

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
    return render_template('example.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
