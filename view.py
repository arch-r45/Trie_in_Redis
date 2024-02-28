from flask import Flask, render_template, session, redirect, url_for
from flask import request
app = Flask(__name__)
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
@app.route('/', methods=['GET'])
def post_comment():
    if request.method == 'GET':
        word = ""
        data = request.args.get("Review", "").strip().upper()
        print(data)
        if data:
            word = r.get(data)
            session[data] = f"{data}: {word}"
        else:
            session[data] = ""
        print(session)
        return render_template('speed.html', word=session)
    return render_template('speed.html')
app.config['SECRET_KEY'] = 'ered'