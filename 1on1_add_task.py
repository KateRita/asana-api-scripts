import os
import asana

from oneononeprojects import projects
teams = [ 'api', 'apps', 'test']

# projects is an array of objects

# projects = [
#     { 'name': 'KateTest',         #user-friendly name
#       'id': '<projectId>',        # string, project id
#       'userid': '<userEmail>',    # string, email address of the other user who should be assigned tasks in this project
#       'team': 'self'},            # team name. matches list of teams
# ]

def get_user_task_title():
    return raw_input("Enter task title: ")

def get_user_task_description():
    print("Enter task description: (Ctrl-D to finish)")
    contents = []
    while True:
        try:
            line = raw_input("")
        except EOFError:
            break
        contents.append(line)
    return '\n'.join(contents)

def get_projects_by_team(team):
    selected_projects = []
    for project in projects:
        if project['team'] == team:
            selected_projects.append(project)
    return selected_projects

def get_projects_by_user_select(projects):
    selected_projects = []
    for project in projects:
        add_to_project = raw_input('Add to ' + project['name'] + ' [Y/n]? ')
        if(add_to_project == 'y'):
            selected_projects.append(project)
    return selected_projects


def get_user_selected_projects(projects):

    for i, team in enumerate(teams):
        print i, ': ' + team
    print i + 1, ': all'
    print i + 2, ': choose'

    selected_team = raw_input('Select which projects or teams to add task to: ')

    if selected_team == 'all':
        return projects
    elif selected_team == 'choose':
        return get_projects_by_user_select(projects)
    elif selected_team in teams:
        return get_projects_by_team(selected_team)

    else:
        print('Unknown Team: ' + selected_team)
        print('See list of teams defined in ' + os.path.basename(__file__))
        return []

def get_assignee(assign_pref, project):
    if assign_pref == 'me':
        return me['id']
    elif assign_pref == 'them':
        return project['userid']
    else:
        return None


###########
# Main
###########

# create a client with a Personal Access Token
client = asana.Client.access_token(os.environ['ASANA_ACCESS_TOKEN'])
me = client.users.me()

# get user selections
user_selected_projects = get_user_selected_projects(projects)
task_name = get_user_task_title()
task_notes = get_user_task_description()
assign_string = raw_input('Assign Task? (me/them/none) ')

print
print("Creating tasks...")
print
print("Adding to " + str(len(user_selected_projects)) + " projects.")
for project in user_selected_projects:

    assignee = get_assignee(assign_string, project)

    print('Adding to ' + project['name'] + ' ...')

    task = {
        'projects': project['id'],
        'name': task_name,
        'notes': task_notes
    }

    if assignee is not None:
        task['assignee'] = assignee

    result = client.tasks.create(task)

    print('    ' + result['projects'][0]['name'] + '-> Done!')
    print
