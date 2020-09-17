from flask import Blueprint

blog_ab = Blueprint('blog',__name__)

@blog_ab.route('/blog1')
def blog():
    return "TEST Blueprint"