import asana
import csv
from dev import private_access_token

client = asana.Client.access_token(private_access_token)
me = client.users.me()
TASKS = ['Graveyard (**ONLY IF YOU REJECT COMPANY"" ELSE MARK COMPLETE):', 'Leads:', 'Applied:', 'Phone Screen Scheduled:', 'Phone Screen Completed:', 'Technical Screen Scheduled:', 'Technical Screen Completed:', 'Coding Challenge Recieved:', 'Coding Challenge Completed:', 'On-Site Interview Scheduled:', 'On-Site Interview Completed:', 'Offers Recieved:', 'Working Area (NOT Companies):',]
# Grab workspace id for Reactor Education Group
reactor_workspace_id = me['workspaces'][0]['id']

# Grab the team names
teams = client.teams.find_by_organization(reactor_workspace_id)
team = next(team for team in teams if team['name'] == 'Testing tools')

file_to_open = 'testing_new_names.csv'
with open(file_to_open) as csvfile:
	print 'in the open'
	reader = csv.DictReader(csvfile)
	for row in reader:
		if len(row['Name']) > 5:
			create_project = client.projects.create_in_workspace(reactor_workspace_id, {'team': team['id'],  'name': row['Name']})			
			print "Created project with id: " + str(create_project['id'])
			for i in TASKS:
				task = client.tasks.create_in_workspace(reactor_workspace_id, {'projects': [create_project['id']], 'name': i})