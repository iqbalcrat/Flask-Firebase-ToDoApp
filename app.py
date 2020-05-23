import pyrebase
from flask import Flask, render_template, request, redirect


config = {
    'apiKey': 'AIzaSyBXva8f3SMu42TWhcpqls5B1C218iPv-yU',
    'authDomain': 'test-cb399.firebaseapp.com',
    'databaseURL': 'https://test-cb399.firebaseio.com/messages',
    'projectId': 'test-cb399',
    'storageBucket': 'test-cb399.appspot.com',
    'messagingSenderId': '938425930701',
    'appId': '1:938425930701:web:ed34381b90c751c92bea84',
    'measurementId': 'G-NJJ16VLT6F'
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