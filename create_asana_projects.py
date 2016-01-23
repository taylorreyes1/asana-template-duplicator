import asana
import csv
from dev import private_access_token, followers, instructions, hired, scheduling

TASKS = ['Graveyard (**ONLY IF YOU REJECT COMPANY"" ELSE MARK COMPLETE):', 'Leads:', 'Applied:', 'Phone Screen Scheduled:', 'Phone Screen Completed:', 'Technical Screen Scheduled:', 'Technical Screen Completed:', 'Coding Challenge Recieved:', 'Coding Challenge Completed:', 'On-Site Interview Scheduled:', 'On-Site Interview Completed:', 'Offers Recieved:', 'Scheduling Technical Interview Practice Sessions', 'Getting Started on Hired.com', '$$Instructions - Do Not Modify or Delete', 'Working Area (NOT Companies):',]

client = asana.Client.access_token(private_access_token)
me = client.users.me()

# Grab workspace id for Reactor Education Group
reactor_workspace_id = me['workspaces'][0]['id']

# Grab the team names
teams = client.teams.find_by_organization(reactor_workspace_id)
# This must reference the team you'd like the projects in
team = next(team for team in teams if team['name'] == 'Testing tools')

file_to_open = 'testing_new_names.csv'
with open(file_to_open) as csvfile:
	print 'in the open'
	reader = csv.DictReader(csvfile)
	for row in reader:
		if len(row['Name']) > 5:
			create_project = client.projects.create_in_workspace(reactor_workspace_id, {'team': team['id'],  'name': row['Name']})			
			# client.projects.add_followers(create_project['id'], {'followers': followers})
			
			print "Created project with id: " + str(create_project['id'])
			for i in TASKS:				
				if i == "$$Instructions - Do Not Modify or Delete":
					client.tasks.create_in_workspace(reactor_workspace_id, {'projects': [create_project['id']], 'name': i, 'notes': instructions})
				elif i == "Getting Started on Hired.com":
					client.tasks.create_in_workspace(reactor_workspace_id, {'projects': [create_project['id']], 'name': i, 'notes': hired})
				elif i == "Scheduling Technical Interview Practice Sessions":
					client.tasks.create_in_workspace(reactor_workspace_id, {'projects': [create_project['id']], 'name': i, 'notes': scheduling})
				else:
					client.tasks.create_in_workspace(reactor_workspace_id, {'projects': [create_project['id']], 'name': i})
