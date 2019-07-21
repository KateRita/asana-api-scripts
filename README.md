# asana-api-scripts

Setup:
1. Get a personal access token ([Quick Start](https://asana.com/developers/documentation/getting-started/quick-start), see 'Authentication')
2. Set an environment variable: `export ASANA_ACCESS_TOKEN='<accesstoken>'`

## 1on1 Add Task

Define a task title & body, create copies of that task in multiple 1 on 1 projects.

**Options:**
- use command line option `--dry-run` to see which projects would have tasks added w/o actually adding them.
- prompt user for task title & description
- add task to all projects, to all projects for a given team, or prompt the user to add to each project
- assign to me, to other member of 1:1 project, or to no one

**Usage:**
Create a file called oneononeprojects.py that contains an array of objects in this format:

```
projects = [
     { 'name': 'KateTest',         # user-friendly name
       'id': '<projectId>',        # string, project id
       'userid': '<userEmail>',    # string, email address of the other user who should be assigned tasks in this project
       'group': 'self'},           # group name. 
]
```

`python 1on1_add_task.py`

or

`python 1on1_add_task.py --dry-run`

### References
Quick Start:
https://asana.com/developers/documentation/getting-started/quick-start

python library:
https://github.com/Asana/python-asana/

Documentation:
https://asana.com/developers/api-reference/tasks#create
