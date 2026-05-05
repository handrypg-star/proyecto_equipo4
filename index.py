from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "clave_secreta_menteactiva"

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")

    user = ["ADMIN", "PSICOLOGO", "ESTUDIANTE"]

    for i in user:
        if usuario.upper() == i and clave == "1234":
            session["usuario"] = usuario.upper()
            return redirect(url_for("dashboard"))

    return render_template("login.html", mensaje="Usuario o contraseña incorrectos")

@app.route("/dashboard")
def dashboard():
    if 'usuario' in session:
        return render_template("dashboard.html", usuario=session['usuario'])
    else:
        return redirect(url_for('inicio'))

@app.route("/diario")
def diario():
    # Verificamos que el usuario haya iniciado sesión
    if 'usuario' in session:
        return render_template("diario.html", usuario=session['usuario'])
    else:
        return redirect(url_for('inicio'))

@app.route("/capsulas")
def capsulas():
    if 'usuario' in session:
        return render_template("capsulas.html", usuario=session['usuario'])
    else:
        return redirect(url_for('inicio'))
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)