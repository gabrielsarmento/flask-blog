from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flaskblog.posts.forms import SearchForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    form = SearchForm()
    if form.validate_on_submit:
        print(request.args.get('text'))
        
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
        return render_template('home.html', posts=posts, form=form)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, form=form)

@main.route("/about")
def about():
    return render_template('about.html', title='About')
