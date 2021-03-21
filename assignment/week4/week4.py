from flask import Flask, request, redirect, render_template, session, url_for

app= Flask (__name__, static_folder="static", static_url_path="/static")

app.secret_key = b'\xc1@\xbbnla\x8a8\x97\xc4\x97e(K\xea\n'

@app.route("/")
def home():
    if "userName" in session:
        return redirect(url_for("member")) 
    else:
        return render_template ("week4.html") 

@app.route("/member/")
def member ():
    if "userName" in session:
        return render_template ("week4_member.html")
    else: 
        return redirect(url_for("home")) 

@app.route("/error/")
def error():
    return render_template ("week4_error.html")

@app.route("/signin", methods=["POST"])
def signin():
    userName = request.form["userName"]
    password = request.form["password"]
    
    if (userName=="test") and (password=="test"):
        session["userName"] = userName
        session["password"] = password
        return redirect(url_for("member"))
    else:
        return redirect(url_for("error") ) 
    
@app.route ("/signout")
def signout ():
    session.pop("userName", None)
    session.pop("password", None)
    return redirect(url_for ("home"))

if __name__ == "__main__":
    app.run (port=3000,debug=True)