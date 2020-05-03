from flask_restful import Resource


class Task(Resource):

    def get(self):
        return {"Message" : "Inside get method"},200

    def post(self):
        return {"Message" : "Inside post method"},200

    def put(self):
        return {"Message" : "Inside put method"},200

    def delete(self):
        return {"Message": "Inside delete method"},200
