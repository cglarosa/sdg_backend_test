from flask import Flask, jsonify, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os
import psycopg2
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost/postgres'
CORS(app)
app.secret_key = 'my_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer, unique=True,primary_key = True,autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    primary_aff = db.Column(db.String(80))
    secondary_aff = db.Column(db.String(80))
    educ_attain = db.Column(db.String(80), nullable=False)
    yrs_exp = db.Column(db.String(80),nullable=False)
    name = db.Column(db.String(80),nullable=False)
    acknowledge = db.Column(db.Boolean, nullable=False)
    pending = db.Column(db.Boolean,nullable=False)
    contact_person = db.Column(db.String(80),nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    def __repr__(self):
        return '<User %r>' % self.username

class Sdg_goals(db.Model):
    goal_id = db.Column(db.String(80),primary_key=True)
    subgoal_id = db.Column(db.String(80),primary_key=True)
    body = db.Column(db.String(1000),unique=True,primary_key=True)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User_to_sdg(db.Model):
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'),primary_key = True)
    goal_id = db.Column(db.Integer,primary_key = True)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Survey_answers(db.Model):
    target1_goal = db.Column(db.String(80),primary_key=True)
    target1_subgoal = db.Column(db.String(80), primary_key=True)
    target2_goal = db.Column(db.String(80), primary_key=True)
    target2_subgoal = db.Column(db.String(80), primary_key=True)
    score = db.Column(db.Integer)
    reason = db.Column(db.String(1000))
    username = db.Column(db.String(80))
    finished = db.Column(db.Boolean)
    time_answered = db.Column(db.Integer)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@app.route("/survey/answer",methods=["POST"])
@cross_origin()
def add_survey_answer():
    data = request.get_json()
    target1_subgoal = data[0]['target1_subgoal']
    target1_goal = data[0]['target1_goal']
    target2_subgoal = data[0]['target2_subgoal']
    target2_goal = data[0]['target2_goal']
    score = data[0]['score']
    reason = data[0]['reason']
    username = data[0]['username']
    finished = data[0]['finished']
    time_answered = data[0]['time_answered']
    answer = Survey_answers(target1_goal=target1_goal,target1_subgoal=target1_subgoal,target2_subgoal=target2_subgoal,target2_goal=target2_goal,score=score,
        reason=reason,username=username,finished=finished,time_answered=time_answered)
    try:
        db.session.add(answer)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(success=False,status_code = 400,body='Duplicate answer')
    else:
        return jsonify(success=True,status_code = 200)

@app.route("/survey/answer/single",methods=["POST"])
@cross_origin()
def get_survey_answer():
    data = request.get_json()
    target1_subgoal = data[0]['target1_subgoal']
    target1_goal = data[0]['target1_goal']
    target2_subgoal = data[0]['target2_subgoal']
    target2_goal = data[0]['target2_goal']

    answer = Survey_answers.query.filter_by(target1_goal=target1_goal,target1_subgoal=target1_subgoal,target2_subgoal=target2_subgoal,target2_goal=target2_goal).first()
    if answer is None:
        abort(404)

    return jsonify(success=True,status_code = 200,target1_goal=target1_goal,target1_subgoal=target1_subgoal,target2_subgoal=target2_subgoal,target2_goal=target2_goal,score=answer.score,
        reason=answer.reason,username=answer.username,finished=answer.finished,time_answered=answer.time_answered)





@app.route("/survey/answer/update",methods=["PUT"])
@cross_origin()
def update_survey_answer():
    data = request.get_json()
    target1_subgoal = data[0]['target1_subgoal']
    target1_goal = data[0]['target1_goal']
    target2_subgoal = data[0]['target2_subgoal']
    target2_goal = data[0]['target2_goal']
    score = data[0]['score']
    reason = data[0]['reason']
    username = data[0]['username']
    finished = True
    time_answered = data[0]['time_answered']

    answer=Survey_answers.query.filter_by(target1_subgoal=target1_subgoal,target1_goal=target1_goal,target2_goal=target2_goal,target2_subgoal=target2_subgoal).first()
    answer.score = score
    answer.reason = reason
    answer.username = username
    answer.finished = finished
    answer.time_answered = time_answered
    db.session.commit()
    return jsonify(success=True,status_code = 200)



@app.route("/survey/answers",methods=["GET"])
@cross_origin()
def display_answers():
    answers = Survey_answers.query.all()
    list_answers = []
    for answer in answers:
        list_answers.append(answer.as_dict())
    return jsonify(list_answers)

@app.route("/survey/answers/user",methods=["POST"])
@cross_origin()
def display_user_answers():
    data = request.get_json()
    username = data[0]['username']
    answers = Survey_answers.query.filter_by(username=username).all()
    list_answers = []
    for answer in answers:
        list_answers.append(answer.as_dict())
    return jsonify(list_answers)

@app.route("/")
@cross_origin()
def hello():
    return "Hello World!"

@app.route("/users",methods=["GET"])
@cross_origin()
def users():
    users = User.query.all()
    list_users = []
    for user in users:
    	list_users.append(user.as_dict())
    return jsonify(list_users)

@app.route("/users/delete",methods=["POST"])
@cross_origin()
def delete_users():
    data = request.get_json()
    username = data[0]['username']
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify(success=True,status_code = 200)

@app.route("/users/delete/cascade",methods=["POST"])
@cross_origin()
def delete_users_cascade():
    data = request.get_json()
    username = data[0]['username']
    user_id = data[0]['user_id']
    
    goals = User_to_sdg.query.filter_by(user_id=user_id).all()
    if goals is not None:
        for goal in goals:
            db.session.delete(goal)
    db.session.commit()

    user = User.query.filter_by(username=username,user_id=user_id).first()
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()

    answers = Survey_answers.query.filter_by(username=username).all()
    if answers is not None:
        for answer in answers:
            db.session.delete(answer)
    db.session.commit()
    return jsonify(success=True,status_code = 200)

@app.route("/users/grant",methods=["PUT"])
@cross_origin()
def grant_user():
    data = request.get_json()
    username = data[0]['username']
    user = User.query.filter_by(username=username).first()
    user.pending = False
    db.session.commit()
    return jsonify(success=True,status_code = 200)

@app.route("/users/confirm",methods=["POST"])
@cross_origin()
def confirm():
    data = request.get_json()
    username = data[0]['username']
    password = data[0]['password']
    user = User.query.filter_by(username=username,password = password,pending=False).first()
    if user is None:
        abort(404)
    return jsonify(success=True,status_code = 200,user_id=user.user_id,username=user.username)


@app.route("/users/change/password",methods=["POST"])
@cross_origin()
def change_password():
    data = request.get_json()
    username = data[0]['username']
    new_password = data[0]['new_password']
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    user.password = new_password
    db.session.commit()
    return jsonify(success=True,status_code=200)

@app.route("/goals/main",methods=["GET"])
@cross_origin()
def main_goals():
    goals = Sdg_goals.query.filter_by(subgoal_id="0")
    list_goals = []
    for goal in goals:
        list_goals.append(goal.as_dict())
    return jsonify(list_goals)

@app.route("/goals/sub",methods=["POST"])
@cross_origin()
def get_subgoals():
    data = request.get_json()
    goal_id = data[0]['goal_id']
    subgoals = Sdg_goals.query.filter_by(goal_id=goal_id)
    list_subgoals = []
    for subgoal in subgoals:
        list_subgoals.append(subgoal.as_dict())
    return jsonify(list_subgoals)


@app.route("/goals",methods=["POST"])
@cross_origin()
def get_goal():
    data = request.get_json()
    goal_id = data[0]['goal_id']
    subgoal_id = data[0]['subgoal_id']
    goal = Sdg_goals.query.filter_by(goal_id=goal_id,subgoal_id=subgoal_id).first()
    if goal is None:
        abort(404)
    return jsonify(goal.as_dict())

@app.route("/goals/all",methods=["GET"])
@cross_origin()
def get_all_goals():
    goals = Sdg_goals.query.all()
    list_goals = []
    for goal in goals:
        list_goals.append(goal.as_dict())
    return jsonify(list_goals)

@app.route("/goals/body",methods=["POST"])
@cross_origin()
def get_body_goal():
    data = request.get_json()
    goal_id = data[0]['goal_id']
    subgoal_id = data[0]['subgoal_id']
    goal = Sdg_goals.query.filter_by(goal_id=goal_id,subgoal_id=subgoal_id).first()
    if goal is None:
        abort(404)
    return jsonify(goal.body)


@app.route("/users/add",methods=["POST"])
@cross_origin()
def add():
    data = request.get_json()
    username = data[0]['username']
    password = data[0]['password']
    educ_attain = data[0]['educ_attain']
    name = data[0]['name']
    yrs_exp = data[0]['yrs_exp']
    primary_aff = data[0]['primary_aff']
    secondary_aff = data[0]['secondary_aff']
    contact_person = data[0]['contact_person']
    acknowledge = data[0]['acknowledge']
    pending = data[0]['pending']
    user = User(username=username,password=password,educ_attain=educ_attain,name=name,yrs_exp=yrs_exp,primary_aff=primary_aff,secondary_aff=secondary_aff,acknowledge=acknowledge,pending=pending,contact_person=contact_person)
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(success=False,status_code = 400,body='Duplicate username')
    else:
        return jsonify(success=True,status_code = 200)

@app.route("/users/add/sdg",methods=["POST"])
@cross_origin()
def add_sdg():
    data = request.get_json()
    user_id = data[0]['user_id']
    sdg_id = data[0]['goal_id']
    user_to_sdg = User_to_sdg(user_id=user_id,goal_id=sdg_id)
    try:
        db.session.add(user_to_sdg)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(success=False,status_code = 400,body='Duplicate SDG')
    else:
        return jsonify(success=True,status_code = 200)

@app.route("/users/goals",methods=["POST"])
@cross_origin()
def user_sdg():
    data = request.get_json()
    user_id = data[0]['user_id']
    goals = User_to_sdg.query.filter_by(user_id=user_id).all()
    if goals == []:
        return jsonify(success=False,status_code = 400,body='No goals')
    list_goals = []
    for goal in goals:
        list_goals.append(goal.goal_id)
    return jsonify(list_goals)

if __name__ == "__main__":
    app.run()