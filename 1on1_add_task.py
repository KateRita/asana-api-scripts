import os
import asana

from argparse import ArgumentParser
from oneononeprojects import projects

# projects is an array of objects in the following format

# projects = [
#     { 'name': 'KateTest',         #user-friendly name
#       'id': '<projectId>',        # string, project id
#       'userid': '<userEmail>',    # string, email address of the other user who should be assigned tasks in this project
#       'group': 'self'},            # group name. matches list of groups
# ]

def get_user_selected_group(groups):
    """Promppt user to select project group."""

    for i, group in enumerate(groups):
        print i, ': ' + group
    print i + 1, ': all'
    print i + 2, ': choose'

    return raw_input('Select (name) which projects or groups to add task to: ')


def get_user_task_title():
    "Prompt user for task title, and return result."

    return raw_input("Enter task title: ")

def get_user_task_description():
    """Prompt user for task description. return as a string."""

    print("Enter task description: (Ctrl-D to finish)")
    contents = []
    while True:
        try:
            line = raw_input("")
        except EOFError:
            break
        contents.append(line)
    return '\n'.join(contents)


def get_projects_by_user_select(projects):
    """Prompts the user for each project to determine whether to add task to that project.

    :param projects: (list) all projects for the user to select from
    :return: (list) all projects selected by the user
    """

    selected_projects = []
    for project in projects:
        add_to_project = raw_input('Add to ' + project['name'] + ' [y/n]? ')
        if(add_to_project == 'y'):
            selected_projects.append(project)
    return selected_projects


def get_user_selected_projects(projects):
    """Prompts the user to select which projects to modify, and then returns the appropriate projects

    :param projects: (list) project objects for the user to choose from
    :return: (list) selected projects
    """

    groups = {project['group'] for project in projects}
    selected_group = get_user_selected_group(groups)

    if selected_group == 'all':
        return projects

    elif selected_group == 'choose':
        return get_projects_by_user_select(projects)

    elif selected_group in groups:
        projects_for_selected_group = [project for project in projects if project['group'] == selected_group]
        return projects_for_selected_group

    else:
        print('Unknown group: ' + selected_group)
        print('Known groups: ' + ', '.join(groups))
        quit()

def get_assignee(assign_pref, project):
    """Get the userId of the assignee

    :param assign_pref: (string) one of 'me', 'them', or 'none'
    :param project: (object) project
    :return: (string) userId/email of the user who should be assigned the task.
    """
    if assign_pref == 'me':
        return me['id']
    elif assign_pref == 'them':
        return project['userid']
    else:
        return None


###########
# Main
###########
parser = ArgumentParser("Add task to 1on1 projects.")
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

# create a client with a Personal Access Token
client = asana.Client.access_token(os.environ['ASANA_ACCESS_TOKEN'])
me = client.users.me()

# get user selections
user_selected_projects = get_user_selected_projects(projects)
task_name = get_user_task_title()
task_notes = get_user_task_description()
assignee_type = raw_input('Choose Task Assignee (me/them/none): ')

print
print("Creating tasks...")
print
print("Adding to " + str(len(user_selected_projects)) + " projects.")

for project in user_selected_projects:

    assignee = get_assignee(assignee_type, project)

    print('Adding to ' + project['name'] + ' ...')

    task = {
        'projects': project['id'],
        'name': task_name,
        'notes': task_notes
    }

    if assignee is not None:
        task['assignee'] = assignee

    if not args.dry_run:
        result = client.tasks.create(task)
        print('    ' + result['projects'][0]['name'] + '-> Done!')
        print
    else:
        print('    ' + project['name'] + '-> Dry Run!')
        print


