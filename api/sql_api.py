import flask
import flask.ext.sqlalchemy
import flask.ext.restless


app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/app.db'

db = flask.ext.sqlalchemy.SQLAlchemy(app)


class Journalist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return '<Journalist {}>'.format(self.name)


db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Journalist,
                   methods=['GET'],
                   max_results_per_page=1000)

app.run()
