from flask import Flask, flash, render_template, request

#imported data from weather data module
from weather_data import data

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/", methods=["POST", "GET"])
def input():
    if request.method == "POST":
        city = request.form["city"]
        
        error = None
        if error is None:
            try:    
                dt = data(city)
                icon_image = dt["icon"]
                return render_template("index.html", dt=dt, icon=icon_image)

            except KeyError:
                error = f'Data for "{city}" not available'
        
        flash(error)

    return render_template("get_city.html")

if __name__ == "__main__":
    app.run(debug=True) 


