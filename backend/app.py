from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
from flask_restx import Api,Resource,fields

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
import os
from datetime import datetime

basedir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'tasktracker.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ECHO']= True

api = Api(app)

db = SQLAlchemy(app)

class Task(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    text = db.Column(db.String(25),nullable=False)
    day = db.Column(db.Date)
    reminder=db.Column(db.Boolean(),default= False)

    def __repr__(self):
        return self.name

task_model = api.model(
    'Task',
    {
        'id':fields.Integer(),
        'text':fields.String(),
        'day':fields.String(),
        'reminder':fields.Boolean()
    }
)



@api.route('/tasks')
class task(Resource):
    @cross_origin()
    @api.marshal_list_with(task_model,code=200,envelope='tasks')
    def get(self):
        tasks= Task.query.all()
        
        return tasks
    @api.marshal_with(task_model,code=200,envelope='task')
    def post(self):
        data = request.get_json()
        text = data.get('text')
        day =datetime.now()
        print(day,'dayyy')

        reminder= data.get('reminder')
        new_task = Task(text=text,day=day,reminder=reminder)
        db.session.add(new_task)
        db.session.commit()
        return new_task
        

@api.route('/tasks/<int:id>')
class TaskDetail(Resource):
    @cross_origin()
    @api.marshal_with(task_model,code=200,envelope='task')
    def get(self,id):
        task =Task.query.get_or_404(id)
        return task
    @api.marshal_with(task_model,code=200,envelope='task')
    def put(self,id):
        task_to_update =Task.query.get_or_404(id)
        data =request.get_json()
        task_to_update.reminder = data.get('reminder')

        db.session.commit()
        return task_to_update,200
    @cross_origin()
    @api.marshal_with(task_model,envelope='Task is deleted',code=200)    
    def delete(self,id):
        task_to_delete = Task.query.get_or_404(id)
        db.session.delete(task_to_delete)
        db.session.commit()
        return task_to_delete
 

@app.shell_context_processor
def make_shell_context():
    return {
        'db':db,
        'Task':Task
    }

if __name__ == "__main__":
    app.run(debug=True)