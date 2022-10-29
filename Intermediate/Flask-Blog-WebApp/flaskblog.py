from flask import Flask, render_template, url_for
app = Flask(__name__) # creating Flask Object

# static posts content
posts = [
    {
        'author':'Jay',
        'title':'Blog Post 1',
        'content':'This is my first post with sample content',
        'date_posted':'15th Oct 2020'
    },
    {
        'author':'Prakash',
        'title':'Second Blog Post',
        'content':'This is my 2nd post with dummy content',
        'date_posted':'16th Oct 2020'
    },
    {
        'author':'Aluri',
        'title':'Third Blog Post',
        'content':'This is my third post with general content',
        'date_posted':'17th Oct 2020'
    }

]

@app.route('/')
def Home():
    return render_template('home.html', title="Prakash Blog - 2022", posts=posts)


@app.route('/about')
def About():
    return render_template('about.html', title="About Us")

if __name__ == ('__main__'):
    app.run(port=5000, debug=True)