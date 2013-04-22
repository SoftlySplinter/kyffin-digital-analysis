from flask import Flask, render_template, request
from kyffin.analyser import Analyser

app = Flask("Kyffin")
analyser = Analyser(None, None, None, None, None)
default_path = "database.csv"


@app.route('/')
def show_years():
    years = []
    counts = {}
    for painting in analyser.paintings:
        if painting.year not in years:
            years.append(painting.year)
        if painting.year not in counts:
            counts[painting.year] = 0
        counts[painting.year] = counts[painting.year] + 1
    years.sort()
    return render_template("index.html", years=years, counts=counts)

@app.route('/paintings')
def show_paintings():
    year = request.args['year']
    paintings = [painting for painting in analyser.paintings if painting.year == year]
    return render_template("painting.html", paintings=paintings, year=year, no_paintings=len(paintings))
    

def main():
    analyser.loadPaintings(default_path)
    app.run(debug=True)
