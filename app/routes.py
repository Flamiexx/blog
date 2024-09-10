from flask import render_template, request, redirect, url_for, Blueprint
from app import db
from app.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('home.html', posts=posts)


@main.route('/post/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('create_post.html')
