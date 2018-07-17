import flask
import flask_sqlalchemy
import flask_restless
from flask_cors import CORS


app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/app.db'
app.config['CORS_ALLOW_HEADERS'] = "Content-Type"
app.config['CORS_RESOURCES'] = {r"/api/*": {"origins": "*"}}

db = flask_sqlalchemy.SQLAlchemy(app)
cors = CORS(app)


class Journalist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return '<Journalist {}>'.format(self.name)


db.create_all()

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Journalist,
                   methods=['GET'],
                   max_results_per_page=1000)

app.run()
