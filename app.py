from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# class Todo(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#
#     def __repr__(self) -> str:
#         return f"{self.sno}-{self.name}"


@app.route('/')
def hello_world():  # put application's code here
    name = "Avtar"
    return render_template('index.html', name = name )

if __name__ == '__main__':
    app.run(debug=True)  #to run the application
