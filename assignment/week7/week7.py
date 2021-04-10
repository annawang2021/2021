from flask import Flask, request, redirect, render_template, session, url_for, flash, jsonify
import mysql.connector, json

app= Flask (__name__, static_folder="static", static_url_path="/static")

app.secret_key = b'\xc1@\xbbnla\x8a8\x97\xc4\x97e(K\xea\n'

mydb = mysql.connector.connect(
  host="localhost",
  user=,
  password=,
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
    realname = session.get('realName')
    return render_template("week7_member.html", realname=realname) 

@app.route("/error/")
def error():
    message = request.args.get ("message", "帳號或密碼輸入錯誤")
    return render_template("week7_error.html", failLogin=message )


@app.route("/signup", methods=["POST"])
def signup():
    realName = request.form["realName"]
    userName = request.form["userName"] 
    password = request.form["password"]

    # check = "SELECT * FROM user WHERE userName = %s" %(userName) #格式化字串%g語法： %s(字串)，%d (十進位整數)，%f(小數點)
    check = f"select * from user where userName='{userName}'" #格式化字串f-string語法
    # check ="select * from user where username={k}" .format(k=userName) #格式化字串.formant()語法
    print (check)

    mycursor.execute(check)

    result = mycursor.fetchall()
    # print (result)

    count = len (result)
    # print (count)
    
    if count > 0:
        # flash('帳號已經被註冊')
        return redirect(url_for("error"))

    else:
        sql = "INSERT INTO user (realName, userName, password) VALUES (%s, %s, %s)"
        val = (realName, userName, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for("home"))
      

@app.route("/signin", methods=["POST"])
def signin():
    userName = request.form["userName"]
    password= request.form["password"]

    check = f"select * from user where userName='{userName}' and password = '{password}'"
    # print (check)
    mycursor.execute(check)
    result = mycursor.fetchall() 
    # print (result) 
    count = len (result)
    # print (count)#1
    
    if (count > 0) and (request.method == "POST"):
        info = f"select * from user where userName ='{userName}' and password = '{password}'"
        mycursor.execute(info)
        result= mycursor.fetchall()
        # print (result[0][1]) 
        
        session["userName"] = userName
        session["realName"] = result[0][1]
        # flash(result[0][1])
        return redirect(url_for("member") )

    else:
        return redirect(url_for("error") ) 
    

@app.route("/signout")
def signout():
    session.pop("userName", None)
    session.pop("password", None)
    return redirect(url_for ("home"))

@app.route("/api/users")
def api():
    username = request.args.get ("username", None)
    info = f"select id, realName, userName from user where userName ='{username}'"
    mycursor.execute(info)
    result= mycursor.fetchall()
    # print (result)
    count=len(result)
    # print(count)
    if count >0:
        final = {
            "data":{
                "id" :result[0][0],
                "name" :result[0][1],
                "username" :result[0][2]
            }
        }
        final = json.dumps(final, ensure_ascii=False)#轉換中文字的方法: ensure_ascii=False
        # print (final)
        return final
    else:
        no_result={
            "data":"null"
        }
        no_result= json.dumps(no_result, ensure_ascii=False)#轉換中文字的方法: ensure_ascii=False
        # print (no_result)
        return no_result




if __name__ == "__main__":
    app.run (port=3000,debug=True)
