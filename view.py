from flask import Flask, render_template, session, redirect, url_for
from flask import request
app = Flask(__name__)

dictionary = {
    "homogeneous": "similar, or the same as something else.",
    "blunt": "Having a thick edge or point, as an instrument; not sharp.",
}
@app.route('/', methods=['GET'])
def post_comment():
    if request.method == 'GET':
        word = ""
        data = request.args.get("Review", "").strip()
        print(request.headers["Cookie"])
        if data:
            word = dictionary.get(data, "Does Not Exist")
        session[data] = word
        print(session)
        return render_template('speed.html', word=session)
    return render_template('speed.html')
app.config['SECRET_KEY'] = 'eerenad'


