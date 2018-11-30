from flask import render_template, request, Blueprint, redirect, url_for
from flaskblog.models import Post
from flaskblog.posts.forms import SearchForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    form = SearchForm()

    text = request.args.get('text')
    if text:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter(Post.content.contains(text)).paginate(page=page, per_page=5)
        
        return render_template('home.html', posts=posts, form=form)

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, form=form)

@main.route("/about")
def about():
    form = SearchForm()
    return render_template('about.html', title='About', form=form)
