from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hola mundo desde Flask!</h1><p>Este es el inicio ...</p>"

@app.route("/saludar/<nombre>")
def saludar(nombre):
    return f"Hola {nombre} como estas? \nBienvenido a la app"

@app.route("/postear/<int:post_id>")
def ver_post(post_id):
    return f"Estas leyendo el post numero: {post_id}"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("username")
        if usuario != "NORMAN":
            return f"No esta habilitado {usuario} a nuestro sitio"    
        
        return f"<h1>Sesión iniciada para el usuario {usuario}</h1>"
    
    return """
        <form method='post'>
        Ingrese su usuario <input type='text' name='username'>
        <input type='submit' value='Enviar'>
        </form>
    """


if __name__ == "__main__":
    app.run(debug=True)