from Api import app

@app.route("/usuario")
def usuario():
    return "Usuário";

