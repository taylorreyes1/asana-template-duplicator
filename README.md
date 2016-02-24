This python script is currently being utilized to handle repetitive duplication of an asana template. 
It requires a csv with names from which it will duplicate the parent template.

##Setup

Install requirements:

`pip install requirements.txt`

You will need to aquire your own personal access token. You can do so here: https://app.asana.com/-/account_api
Be sure to replace 'personal_access_token' in 'create_asana_projects.py' with your personal access token.

##Required 
A CSV file with a column titled 'Name' and 'Email. This can be made more modular later.

## Usage
Currently the script runs from the command line.

It requires a few command line inputs from the user in order to properly duplicate the template.
* The URL of the template to duplicate
* The current users Asana login credentials
* The csv file name that will provide the student names for their projects
* You will be asked if the duplication process has finished, Y if so, N if not

##Running

From the command line run:
`python create_asana_projects.py`

##Use Case
* You have a mundane or repetitive task that requires the duplication of a specific Asana template project (ie Student Projects).
* You have a CSV file of the names of the students who will be recieving projects for their job search.
* In the case of Outcomes we have to create new Asana projects for each individual job seeking student every 6 weeks.
* This can be done manually by copying a master template over and over again for x amount of job seeking students.
* The script works to automate the creation of those projects. It can perform all of the required duplication opertations for you.
* It will loop through a user designated CSV of names and create corresponding Projects based on the 'Name' column.
* Each student will have their very own Job Search project in Asana!

##TODO
* Handle Asana timeout/errors gracefully

