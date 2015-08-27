This python script is currently being utilized to handle repetitive duplication of an asana template. 
It requires a csv with names from which it will duplicate the parent template.

##Setup

Install requirements

`pip install requirements.txt`

## Usage
Currently the script runs from the command line.

It requires a few command line inputs from the user in order to properly duplicate the template.
* The URL of the template to duplicate
* The current users Asana login credentials
* The csv file name that will provide the student names for their projects
* You will be asked if the duplication process has finished, Y if so, N if not

##Running

From the command line run:
`python duplicate_templates.py`

##TODO

* Handle input errors gracefully
* Handle Asana timeout/erros gracefully

