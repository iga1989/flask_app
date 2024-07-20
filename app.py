from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user for login
users = {"admin": "password"}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('select_camera'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/select_camera')
def select_camera():
    return render_template('camera_selection.html')

@app.route('/order/<camera>', methods=['GET', 'POST'])
def order(camera):
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        quantity = request.form['quantity']
        return render_template('success.html', name=name, camera=camera, city=city, quantity=quantity)
    return render_template('order_form.html', camera=camera)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)