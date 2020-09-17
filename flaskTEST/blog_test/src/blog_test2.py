from flask import Blueprint

blog_ab2 = Blueprint('blog2',__name__)

@blog_ab2.route("/blog2")
def blog():
    return "TEST blogs2"