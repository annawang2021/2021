from flask import Flask, request, redirect, render_template, session, url_for, flash
import mysql.connector

app= Flask (__name__, static_folder="static", static_url_path="/static")

app.secret_key = b'\xc1@\xbbnla\x8a8\x97\xc4\x97e(K\xea\n'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="membership"
)

mycursor = mydb.cursor()


@app.route("/")
def home():
    if "userName" in session:
        return redirect(url_for("member")) 
    else:
        return render_template("homepage.html") 
    

@app.route("/member/")
def member():
  return render_template("week6_member.html") 

@app.route("/error/")
def error():
    fail_login = request.args.get ("message", "帳號或密碼輸入錯誤")
    return render_template("week6_error.html" )+ "<h4 align='center'>"+fail_login+"</h4>"


@app.route("/signup", methods=["POST", "GET"])
def signup():
    realName = request.form["realName"]
    userName = request.form["userName"] #type 是 string
    password = request.form["password"]

    mycursor.execute("select * from user")
    result = mycursor.fetchall()
    count = len (result)
    
    for i in range (count):
        userName_db = result[i][2]

        if userName == userName_db:
            # flash('帳號已經被註冊')
            return render_template("week6_error.html", failMessage ="很抱歉，帳號已被註冊，請再試一次")

        elif (i==(count-1)) and (request.method == "POST"): #比到最後一筆，如果沒有相同資料，建立新會員資料+存入資料庫
            sql = "INSERT INTO user (realName, userName, password) VALUES (%s, %s, %s)"
            val = (realName, userName, password)
            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(url_for("home"))
      

@app.route("/signin", methods=["POST"])
def signin():
    userName = request.form["userName"]
    password = request.form["password"]

    mycursor.execute("select * from user")
    result = mycursor.fetchall() #result的資料型態是list包著tuple
    count = len (result) #計算長度

    for i in range (count):
        realName_db = result[i][1]
        userName_db = result[i][2]
        password_db = result[i][3]

        if (userName == userName_db) and (password == password_db) and (request.method == "POST"):
            session["userName"] = userName
            session["password"] = password 
            return render_template("week6_member.html", realname=realName_db)
            # flash(realName_db)
            # return redirect(url_for("member") )

        elif (i==(count-1)) and (request.method == "POST"):
            return redirect(url_for("error") ) 
    

@app.route("/signout")
def signout():
    session.pop("userName", None)
    session.pop("password", None)
    return redirect(url_for ("home"))


if __name__ == "__main__":
    app.run (port=3000,debug=True)
