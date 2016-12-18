from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)

@app.route('/shopping')
def shopping():
    food=["cheeze", "tuna", "beef"]
    return render_template("shopping.html", food=food)

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        print ('using post')
    return 'method: %s' % request.method

@app.route('/template/<name>')
def template(name):
    return render_template("profile.html", name=name)

@app.route('/tuna')
def tuna():
    return 'tuna'

@app.route('/user/<username>')
def user(username):
    return "hello %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "hello %s" % post_id

if __name__ == '__main__':
    app.run(debug=True)
