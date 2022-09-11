from flask import Flask, render_template
from flask import request
from form import MainForm, PlayForm
#from config import sekret_key
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')



@app.route('/game', methods=['post', 'get'])
def game():
    form = PlayForm().submit
    Login = 'jhdfjkshdjk'
    return render_template('game.html',Login =Login)


    
'''@app.route('/', methods=['post', 'get'])
def login():
    message = ''
    username = ''
    password = ''
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')

    if username == 'root' and password == 'pass':
        message = "Correct username and password"
    else:
        message = "Wrong username or password"
    return render_template('login.html', message=message)'''



if __name__ == "__main__":
    
    app.config['SECRET_KEY'] = 'secret key'
    app.run(debug=True)
