import os
import asana
import pprint
from oneononeprojects import projects

pp = pprint.PrettyPrinter()

# create a client with a Personal Access Token
client = asana.Client.access_token(os.environ['ASANA_ACCESS_TOKEN'])
me = client.users.me()

for project in projects:
    result=client.projects.find_by_id(project['id'])

    members = result['members']
    for member in members:
        if member['id'] != me['id']:
            pp.pprint(member)