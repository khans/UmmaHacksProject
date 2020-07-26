# UmmaHacksProject - MuQu

### Backend Demo:
Available at https://khansafa.pythonanywhere.com/"
Github files at: https://github.com/khans/UmmaHacksProject.git

### Backend: Trivia Generator 

When a player clicks on the play button, a randomly generated trivia form is presewnte. The player can choose the answers from the options provided and can use the hints provided below the option as well.
Once submit is clicked, the score is shown on the results page along wiotha  list of references and bibliography

### Frontend: Search UI
For testing I created sample templates for the following
Welcome Page
Quiz/Trivia Page
Results Page
I used html and css.

### Prerequisites:
Python 3 <br>
    https://www.python.org/downloads/ <br>
Flask - Web framework for Python <br>
    command: pip3 install Flask <br>
Editor: <br>
    Sublime Text <br> 

### Working:
1) The github repository is at https://github.com/khans/UmmaHacksProject.git which can be cloned to your local machine.
2) To run the flask application, on the mac terminal, navigate to the directory and run the command: 
    python3 server.py
3) The application will run on port 5000. 
4) The welcome page has a simple button to start the quiz.
5) This navigates to the quiz page which has randomly selected questions. 
6) You can choose from the options and this can be submitted to the server.
7) The server calculates the score by comparing the options chosen with the answer set.
8) The results page is simply printing the score and shows the links to the references of the topics covered in the questions.
P.S: The questions and answers are stored in datastructures, refer structures.py.

### Resources: 
Flask: https://www.tutorialspoint.com/flask/index.htm <br>
HTML, CSS: https://www.w3schools.com/ <br>
Hosting: https://www.pythonanywhere.com/ <br>
