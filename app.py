from flask import Flask, render_template, jsonify
app = Flask(__name__)

BUSES = [
    {"id":"BUS-01","name":"College Bus 01","driver":"Driver 01","route":"Main Gate → Campus","position":[13.6288,79.4192]},
    {"id":"BUS-02","name":"College Bus 02","driver":"Driver 02","route":"Town → Campus","position":[13.6350,79.4100]}
]

@app.get("/")
def index(): return render_template("index.html")

@app.get("/api/buses")
def buses(): return jsonify(BUSES)

if __name__ == "__main__": app.run(debug=True)
