import pyrebase  
from flask import Flask,render_template,request
app=Flask(__name__)
firebaseConfig = {
  "apiKey": "AIzaSyC1wrWQHWbgNwaoAA71KQ7eGWVMWBF_aCg",
  "authDomain": "webdev-2b668.firebaseapp.com",
  "databaseURL": "https://webdev-2b668-default-rtdb.firebaseio.com",
  "projectId": "webdev-2b668",
  "storageBucket": "webdev-2b668.appspot.com",
  "messagingSenderId": "1016661166433",
  "appId": "1:1016661166433:web:5b734459e9aac88f835d20",
  "measurementId": "G-0Z8YZ55MEC"
};
firebase=pyrebase.initialize_app(firebaseConfig)
rdb=firebase.database()
sdb=firebase.storage()

@app.route("/", methods={"GET","POST"})
def hi():

    if(request.form):
        click=request.form["btn"]
        if(click=="loginbtn"):
          return render_template("login.html")
        elif(click=="signupbtn"):
            return render_template("signup.html")
          
        elif(click=="signupsubmit"):
            uname=request.form["username"]
            
            pwd=request.form["password"]
            uname=uname.lower()
            details={"name":uname,
                    
                     "password":pwd
                     
                }
            data=rdb.get().val()
            if(uname in data):
              return render_template("signup.html",msg={"user exist"})
            else:
                rdb.child(uname).update(details)
                #rdb.update({"age":"20"})
                return render_template("login.html")
           
        elif(click=="loginsubmit"):
          lname=request.form["luname"].lower()
          lpwd=request.form["lpassword"]
          dname=rdb.child(lname).child("name").get().val()
          dpwd=rdb.child(lname).child("password").get().val()
          if(lname==dname and lpwd==dpwd):
              sdb.child(lname).download(path="gs:///"+firebaseConfig["storageBucket"]+"/",filename="static/"+lname+".png") 
              return render_template("1mainpage.html",msg="login successful", pic="static/"+lname+".png")
        elif (click=="Contact"):
          return render_template("contact.html")
        elif(click=="view details"):
                return render_template("2Wedding.html") 
        elif(click=="view details2"):
                return render_template("3Musicalc.html")
        elif(click=="view details3"):
                return render_template("4Tech.html")
        
              
    return render_template("index.html",name="Saba")



app.run(debug=True,port=5021)