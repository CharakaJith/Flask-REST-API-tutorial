from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite.///database.db"
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=True)
    likes = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"

# db.create_all()

video_post_args = reqparse.RequestParser()
video_post_args.add_argument("name", type=str, help="Name of the vidoe is required!", required=True)
video_post_args.add_argument("views", type=str, help="Views of the vidoe")
video_post_args.add_argument("likes", type=str, help="Likes on the vidoe")

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}

# videos = {}

'''
def abort_if_doesnt_exist(id):
    if id not in videos:
        abort(404, message = "Video does not exists with id " + str(id))

def abort_if_exist(id):
    if id in videos:
        abort(409, message = "Video already exists with id " + str(id))
'''

class Sample(Resource):
    def get(self, name, age):
        return {"name": name, "age": age}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        ''' abort_if_doesnt_exist(id)
        return videos[id] '''

        result = VideoModel.query.get(id = id)
        return result

    @marshal_with(resource_fields)
    def post(self, id):
        ''' abort_if_exist(id)
        args = video_post_args.parse_args()
        videos[id] = args
        return videos[id], 201 '''

        args = video_post_args.parse_args()
        video = VideoModel(id = id, name = args["name"], views = args["views"], likes = args["likes"])
        db.session.add(video)
        db.session.commit()
        return {"status": "success", "code": 201, "video": video}

    def delete(self, id):
        abort_if_doesnt_exist(id)
        del videos[id]
        return {"status": "success", "code": 204, "message": "Video deleted under the id " + str(id)}

api.add_resource(Sample, "/sample/<string:name>/<int:age>")
api.add_resource(Video, "/video/<int:id>")

if __name__ == "__main__":
    app.run(debug = True)