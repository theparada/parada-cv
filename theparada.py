from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, SigninForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8bd291a47f6a3be7db6301436aba07a0'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/registor", methods=['GET', 'POST'])
def registor():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created. welcome, {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registor.html', title='registor', form=form)
    
@app.route("/signin")
def signin():
    form = SigninForm()
    return render_template('signin.html', title='signin', form=form)

if __name__=='__main__':
    app.run(port=8000, debug=True)