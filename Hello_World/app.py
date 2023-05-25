from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db.init_app(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) # nullable=False, user can't make an empty content
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        # s string that returns the new element
        return '<Task %r>' % self.id

with app.app_context():
    db.create_all()
    
@app.route('/')

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)