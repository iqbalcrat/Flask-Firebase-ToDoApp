import pyrebase
from flask import Flask, render_template, request, redirect


config = {
    'apiKey': '',
    'authDomain': '',
    'databaseURL': '',
    'projectId': '',
    'storageBucket': '',
    'messagingSenderId': '',
    'appId': '',
    'measurementId': ''
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def add_todo():
    if request.method == "POST":
        if request.form['submit'] == 'add':
            name = request.form['name']
            db.child("todo").push(name)
            todo = db.child("todo").get()
            to = todo.val()
            return render_template('index.html', t=to.values())
        todo = db.child("todo").get()
        to = todo.val()
        return render_template('index.html', t=to.values())
    todo = db.child("todo").get()
    to = todo.val()
    return render_template('index.html', t=to.values())


@app.route('/del', methods=['GET', 'POST'])
def del_todo():

    del_item = request.form["submit"]
    all_todo = db.child("todo").get().val()
    #print(type(all_todo))
    for key, value in all_todo.items():
        if value == del_item:
            #print("The fucking key is ", key)
            db.child("todo").child(key).remove()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
