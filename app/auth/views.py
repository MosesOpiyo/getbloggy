from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,logout_user
from app.auth.forms import LoginForm,RegistrationForm
from app.models import User
from app.auth import auth
from .. import db,login_manager

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

@auth.route('/login',methods = ["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.index'))

        flash('Invalid password or user name')
            
    return render_template('auth/login.html',login_form = login_form)

@auth.route('/signup',methods = ["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()   

        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html',registration_form = form)  

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.index"))
