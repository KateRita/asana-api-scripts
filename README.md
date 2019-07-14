# asana-api-scripts

Scripts that 
Setup:
1. Get a personal access token
2. Set an environment variable: `export ASANA_ACCESS_TOKEN='<accesstoken>'`

## 1on1 Add Task

Add copies of a single task to multiple 1 on 1 projects.

basic features:
- prompt user for task title & description
- add task to all projects, to all projects for a given team, or prompt the user to add to each project
- assign to me, to other member of 1:1 project, or to no one

Note: This is based on the assumption that the 1:1 projects won't change that often, so Ids can be hardcoded to save time/reduce API calls.

### References
Quick Start:
https://asana.com/developers/documentation/getting-started/quick-start

python library:
https://github.com/Asana/python-asana/

Documentation:
https://asana.com/developers/api-reference/tasks#create

New website:
