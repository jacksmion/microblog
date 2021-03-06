# -*- coding:utf-8 -*-

from flask import render_template
from app import db
from app.errors import bp


@bp.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 400


@bp.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500