from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db, bcrypt
from .models import User
from flask_login import login_user, logout_user, current_user, login_required

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    # TODO: Add form logic
    return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    # TODO: Add form logic
    return render_template('auth/register.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.index'))
