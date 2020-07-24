'''
    Flask Application for Python. This module server.py will contain the major algorithm for randomly choosing 
    a set of questions for a trivia - Randomization algorithm
'''

from flask import Flask, redirect, url_for, request, render_template
import random,copy
from structures import question_set, answer_set


app = Flask(__name__)





#Base or Root
@app.route('/')
def index():
	return render_template("welcome.html")


# Randomly select 5 questions from our data and display trivia to the user/player
@app.route('/quiz', methods = ['POST'])
def quiz():
    
    q = selection(question_set)
    return render_template("quiz.html", questionset = q)

# helper method to choose questions randomly
def selection(q_list):
	temp_set = []
	i = 0
	while(i<5):
		curr = random.choice(q_list)
		if curr not in temp_set:
			temp_set.append(curr)
			i += 1
	return temp_set

# check the answers, compare them and show the score
@app.route('/checkAnswer', methods = ['POST'])
def check_answer():
    score = 0
    references = []
    
    for key in request.form:
    	val = request.form[key]
    	if val == answer_set[key][0]:
    		score += 1
    	references.append(answer_set[key])
    print("score is %d" %score)
    return render_template('result.html',score = score, references = references)

'''
if __name__ == '__main__':
	app.debug = True;
	EXPLAIN_TEMPLATE_LOADING = True;
	app.run()
	app.run(debug = True)
'''
if __name__ == "__main__":
    app.run()
