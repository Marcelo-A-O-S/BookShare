from Api import app

@app.route("/")
def index():
    return "Tela inicial";
