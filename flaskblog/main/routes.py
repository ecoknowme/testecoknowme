from flask import render_template, request, Blueprint
from flaskblog.models import Post, Comment
from flaskblog.main.forms import Contact
from flask import request
import requests
from flaskblog.users.utils import get_country ,call_api

main = Blueprint('main', __name__)



@main.route("/")
def index():

	return render_template('index.html')

@main.route("/community")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts ,title='Community')


@main.route("/about")
def about():
	form = Contact()
	if form.validate_on_submit():
		flash('Your post has been created!', 'success')
		return redirect(url_for('main.index'))

	return render_template('about.html', title='About' , form=form)

@main.route("/weather")
def weather():
	if request.headers.getlist("X-Forwarded-For"):
		ip = request.headers.getlist("X-Forwarded-For")[0]
	else:		
		ip = request.remote_addr
	country = get_country(ip)
	weather=call_api(country[3],country[4])
	return render_template('weather.html', title='weather' ,country=country,weather=weather)
