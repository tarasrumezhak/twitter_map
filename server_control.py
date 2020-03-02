from flask import Flask, render_template,request
import map_creation
import get_locations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("mainpage.html")

@app.route("/build", methods=["GET", "POST"])
def build():
    if not request.form.get("input"):
        return render_template("failure.html")
    name = request.form.get("input")
    if map_creation.main(get_locations.get_friends_locations(name)) == None:
        return render_template("failure.html")
    map_creation.main(get_locations.get_friends_locations(name))
    return render_template("locations.html")


if __name__ == "__main__":
    app.run(debug=True)