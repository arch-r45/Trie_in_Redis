from flask import Flask, render_template, session, redirect, url_for
from flask import request
app = Flask(__name__)
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
@app.route('/', methods=['GET'])
def post_comment():
    if request.method == 'GET':
        data = request.args.get("Review", "").strip().upper()
        if data:
            word = r.get(data)
            print(session)
            if "word" not in session:
                session["word"] = []
            temp_set = set(session.get("word", []))
            if (data, word) not in temp_set:
                session["word"].append((data, word))
                session.modified = True
                session["word"].reverse()
            else:
                index = session["word"].index((data, word))
                new_data, new_word = session["word"].pop(index)
                session["word"].append((new_data, new_word))
                session["word"].reverse()

            print(session)

        return render_template('speed.html', words=session.get("word", []))
    return render_template('speed.html')
app.config['SECRET_KEY'] = 'dleeoppzzzz'
