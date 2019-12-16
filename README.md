# laughing-octo-engine

route: POST /survey/answer
input: target1_subgoal, target1_goal, target2_subgoal, target2_goal, score(int), reason, username, finished(boolean), time_answered
output: success, statuscode

route: POST /survey/answer/single
input: target1_subgoal, target1_goal, target2_subgoal, target2_goal
output: target1_subgoal, target1_goal, target2_subgoal, target2_goal, score(int), reason, username, finished(boolean), time_answered

route: PUT /survey/answer/update
input: target1_subgoal, target1_goal, target2_subgoal, target2_goal, score(int), reason, username, finished(boolean), time_answered
output: success, statuscode

route: GET /survey/answers
input:
output: list of all answers

route: POST /survey/answers/user
input: username
output: list of all answers of that user

route: GET /users
input: 
output: list of all users

route: DELETE /users/delete
input: user_id
output: success if deleted

route: DELETE /users/delete/cascade
input: user_id,username
output: success if deleted

route: PUT /users/grant
input: username
output: success

route: POST /users/confirm
input: username, password
output: success, status, username, user_id

route: GET /goals/main
input:
output: goal descriptions

route: POST /goals/sub
input: goal_id
output: list of all subgoals of goal

route: POST /goals
input: goal_id,subgoal_id
output: returns subgoal of goal

route: GET /goals/all
input:
output: returns all goals and subgoals

route: POST /goals/body
input: goal_id, subgoal_id
output: returns body of goal

route: POST /users/add
input: username,password,educ_attain,name,yrs_exp,primary_aff,secondary_aff,acknowledge(boolean),contact_person
output: success or duplicate username

route: POST /users/add/sdg
input: user_id,goal_id
output: success or duplicate sdg

route POST /users/add/goal
input: user_id
output: list of all goals selected by user