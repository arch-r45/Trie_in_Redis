from flask import Flask, render_template, session, redirect, url_for
from flask import request
from collections import deque
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
                session["word"] = deque()
            else:
                session["word"] = deque(session["word"])
            temp_set = set(session.get("word", []))
            """
            I know this next part may be a potential bottleneck for someone with a very large session. 
            I want to make it a deque in order to keep it in FIFO order but deques arent JSON serializable.
            I cannot read lists in reverse in Jinga so I have to keep switching between a deque and list 
            which is 0(N) operation. If I dont use a deque and reverse the list every time it correctly 
            brings the most recent element to the front, but it jumbles all the other elements because I am 
            reversing the list every single time. I cannot call reverse in Jinga either.
            
            """
            if (data, word) not in temp_set:
                session["word"].appendleft((data, word))
                session.modified = True
            else:
                session["word"] = list(session["word"])
                index = session["word"].index((data, word))
                new_data, new_word = session["word"].pop(index)
                session["word"] = deque(session["word"])
                session["word"].appendleft((new_data, new_word))
            session["word"] = list(session["word"])
            print(session)
        return render_template('speed.html', words=session.get("word", []))
    return render_template('speed.html')
app.config['SECRET_KEY'] = 'ppepe'
