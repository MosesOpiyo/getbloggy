from flask import render_template,redirect,url_for,abort,request,flash
from flask_login import current_user,login_required
from app.models import User,Post,Comment
from app import db,photos
from app.models import Blog
from app.main import main
from app.main.forms import BlogForm,CommentForm

@main.route('/')
def index():
    title = 'blogposting'
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html')

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    posts = Post.get_user_posts(
        user.id).order_by(Post.created_at.desc()).all()
    # get all comments created by other users on current user posts
    comments = Comment.get_my_posts_comments(user.id)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/blogs/new/', methods = ['GET', 'POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    blogs = Blog.query.all()
    if blog_form.validate_on_submit():
        description = blog_form.description.data
        title = blog_form.title.data
        owner_id = current_user
        new_pitch = Blog(user_id=current_user.id, title=title, description=description)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('pitches.html', form=blog_form, blogs = blogs)

@main.route('/pitches/fashion_blogs',methods=['GET','POST'])
def fashion_blogs():
    form = CommentForm()
    blogs = Blog.query.filter_by(category = 'fashion')

    return render_template("fashion.html", blogs = blogs,form = form)

@main.route('/blogs/food_blogs',methods=['GET','POST'])
def food_blogs():
    form = CommentForm()
    blogs = Blog.query.filter_by(category = 'food')

    return render_template("food.html", blogs = blogs,form = form)

@main.route('/blogs/music_blogs',methods=['GET','POST'])
def music_blogs():
    form  = CommentForm()
    blogs = Blog.query.filter_by(category = 'music')

    return render_template("music.html", blogs = blogs,form = form)

@main.route('/blogs/lifestyle_blogs',methods=['GET','POST'])
def lifestyle_blogs():
    form  = CommentForm()
    blogs = Blog.query.filter_by(category = 'lifestyle')

    return render_template("lifestyle.html", blogs = blogs,form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/post/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_post(id):
    """
        View update post function that returns the update post page and its data
    """
    post = Post.get_post(id)
    title = request.args.get('title')
    category_id = request.args.get('category_id')
    content = request.args.get('content')
    user_id = request.args.get('user_id')
    # update post
    post.title = title
    post.content = content
    post.category_id = category_id
    post.user_id = user_id
    db.session.commit()
    return redirect(url_for('main.profile', username=current_user.username))

@main.route('/post/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    """
        View delete post function that returns the delete post page and its data
    """
    post = Post.get_post(id)
    db.session.delete(post)
    db.session.commit()
    flash('You have successfully deleted the post', 'success')
    return redirect(url_for('main.profile', username=current_user.username))

@main.route('/comment/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_comment(id):
    """
        View delete comment function that returns the delete comment page and its data
    """
    comment = Comment.get_comment(id)
    db.session.delete(comment)
    db.session.commit()
    flash('You have successfully deleted the comment', 'success')
    return redirect(url_for('main.profile', username=current_user.username))

