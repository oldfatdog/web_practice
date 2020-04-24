from flask import Flask,redirect,url_for,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import Messageform
from flask_bootstrap import Bootstrap 
from flask_moment import Moment

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///text.db'
app.config['SECRET_KEY'] = 'hard to guess string'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)


@app.route('/',methods=['POST','GET'])
def index():
    form = Messageform()
    if request.method == 'POST':
        user_name = request.form['user_name']
        content = request.form['content']
        message = Message(name=user_name,body=content)
        try:
            db.session.add(message)
            db.session.commit()
            return redirect('/')
        except:
            flash('新的留言已提交')
    else:
        messages = Message.query.order_by(Message.timestamp.desc()).all()
        return render_template('index.html',messages=messages,form=form)

@app.errorhandler(404)
def pag_not_found(e):
    return render_template('errors/404.html')

@app.route('/boot')
def boot():
    return render_template('bootstrap.html')



if __name__ == "__main__":
    app.run(port=4000,debug=True)
