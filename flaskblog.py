from flask import Flask,render_template

app = Flask(__name__)

posts = [
    {'author': 'Sutskever et al',
     'title': 'Sequence to sequence learning with neural networks',
     'content': 'https://arxiv.org/pdf/1406.1078.pdf',
     'datepost': '2014'
     },

    {'author': 'Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio',
     'title': 'Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation',
     'content': 'https://arxiv.org/pdf/1704.04368.pdf',
     'datepost': '3 Sep 2014'
     }
]

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return """
    <h1>About page</h1>
    """


if __name__ == "__main__":
    app.run(debug=True)
