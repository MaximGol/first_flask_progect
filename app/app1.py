from flask import Flask, render_template, request, url_for , flash
from werkzeug.utils import redirect

from config import Config
from forms1 import MessageForm

app = Flask(__name__)
app.config.from_object(Config)



coord = [0,0]

@app.route('/', methods=['GET', 'POST'])
@app.route('/message', methods=['GET', 'POST'])
@app.route('/message/', methods=['GET', 'POST'])
def message():
    def calc(coord, side):
        side = side.split(',')
        for i in range(len(coord)):
            coord[i] += int(side[i])*count_steps
        return coord
    name = ''
    email = ''
    text = ''
    form = MessageForm()
    
    if form.validate_on_submit():
        '''name = form.name.data
        email = form.email.data
        text = form.message.data'''
        course = form.course.data
        count_steps = form.count_steps.data

        global coord
        coord = calc(coord,course)
        if coord ==[1,1]:
            flash(f'Вы на балконе')
        
        flash(f'Сообщение отправлено {coord}')

        print('\nData received. Now redirection...1')
        #return redirect(url_for('message'))

    return render_template(
        'index1.html',
        form=form,
        #name=name,
        #email=email,
        #text=text,
    )
if __name__ == "__main__":
    
    app.run(debug=True)
