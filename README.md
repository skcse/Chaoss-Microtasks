

## Microtask -1
Produce a Python script that produces configuration files for Mordred to analyze a complete GitHub organization, excluding repositories that are forks from other GitHub repositories. Test it with at least two GitHub organizations, producing screenshots of the resulting dashboard.
#### Requirements
- [Python3 and some python modules](https://grimoirelab.gitbooks.io/tutorial/before-you-start/supporting-systems.html)
- [Docker](https://docs.docker.com/install/)
- [Grimoirelab](https://grimoirelab.gitbooks.io/tutorial/before-you-start/installing-grimoirelab.html) 

### Run, how to generate configuration.cfg and project.json file
```
# Clone this repository
$ git clone https://github.com/skcse/Chaoss-Microtasks.git

# Change directory into the cloned repository
$ cd Chaoss-Microtasks

# Change directory into task folder of your choice, let say task1
$ cd task1

# For running the python script 
$ python3 task1.py

# then it will ask for valid organisation you want to test
# And will generate configuration.cfg file and projects.json file
```

Before using configuration.cfg file have to enter four things:
- sortinghat --> user (mysql user name)
- sortinghat --> password (mysql user password)
- sortinghat --> database (mysql database name)
- github api --> api-token ([create api token](https://help.github.com/articles/authorizing-a-personal-access-token-for-use-with-a-saml-single-sign-on-organization/))

For mysql name and password, you can create a new one refer [here](https://dev.mysql.com/doc/refman/5.7/en/create-user.html)

For database name, you can initialise using sortinghat command explained [here](https://grimoirelab.gitbooks.io/tutorial/grimoireelk/a-dashboard-with-sortinghat.html) with topic name 'initializing sortinghat'
 
### Run, how to create a dashboard using the generated file

I am Assuming that you have followed the requirement step and installed grimoirelab in a virtual environment as given [here](https://grimoirelab.gitbooks.io/tutorial/before-you-start/installing-grimoirelab.html)
Before procceding, i will suggest you to read [A GrimoireLab dashboard in one step](https://grimoirelab.gitbooks.io/tutorial/mordred/a-grimoirelab-dashboard-in-one-step.html) , [Mordred in a container](https://grimoirelab.gitbooks.io/tutorial/mordred/mordred-in-a-container.html) , [The projects file](https://grimoirelab.gitbooks.io/tutorial/mordred/the-projects-file.html)

these command is used assuming you have created a virtual envirnoment as mentioned above.
```

# for initializing sortinghat database, where 'user' and 'XXX' is user name and passord of mysql database. 'shdb' is database name
$ sortinghat -u user -p XXX  init shdb
 
# Docker container run Elasticsearch, MariaDB, Kibiter and also Grimoirelab tools and keep the mordred config file unconfigure.
$ sudo docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:5601:5601  -e RUN_MORDRED=NO -t grimoirelab/full

# Clone panels repository explained [here](https://grimoirelab.gitbooks.io/tutorial/mordred/a-grimoirelab-dashboard-in-one-step.html).
$ git clone https://github.com/grimoirelab/panels

# Change directory into the cloned repository
$ cd panels/panels

# Download menu.yaml from [here](https://grimoirelab.gitbooks.io/tutorial/mordred/files/menu.yaml)

# move the above generated configuration file and project.json file in the current directory

# Run mordred command with appropriate configuration.cfg file, let say configuration.cfg file is config.cfg
$ mordred -c config.cfg

```
And that's it. Point your browser to http://localhost:5601, assuming your Kibiter is deployed to serve requests in the standard port (5601). You'll see the produced dashboard.

Running mordred command can take time according to the organisation selected, so keep patience

### Results

- There is separate folder for each microtask.
- These folder contain a python script, menu.yaml and organisation folder.
- And organisation folder contains screenshots, config.cfg and projects.json file produced by python script.

## Microtask -2
Produce a Python script that adds a new GitHub repository (git and GitHub issues / pull requests) to a given set of Mordred configuration files. Test it by adding at least two repositories (in two separate steps) to a GrimoireLab dashboard, producing screenshots of the results.

This script adds repositories in the given set of mordred configuration file, or in other terms we can say this python script modifies the projects.json file of the given organisation.

For this script to run we requires mordred configuration file and projects.json file which was generated in microtask-1

After running this script the projects.json file will be modified, hence for generating dashboard you can see the microtask1 readme (Run, how to create a dashboard using the generated file)


### How to run this script
Commands for adding repository, for this let say organisation name is 'bytedeco' and repository name is 'javacpp' and we are adding this repository to a organisation named 'so-fancy'. so, the projects.json file is 'projects_so-fancy.json'.This json file was created in microtask-1 
```
$ python3 task2.py
Enter organisation name
bytedeco
Enter name of repository
javacpp
Enter the name of json file like 'project.json'
projects_so-fancy.json
repository successfully added


# For screenshot, i have added repository 'bytedeco/javacpp' and 'fastlane/ci'
```

### Results
- Task-2 folder contain three folder namely 'initial dashboard','1st repo added','2nd repo added'.
- Initial dashboard folder contains screenshots and mordred config files 
- Folder '1st repo added' contains screenshots and mordred config files after a repository of another organisation is added.
- Folder '2nd repo added' contains screenshots and mordred config files after 2nd repository of another organisation is added.


## Microtask -3
Produce a Python script that removes a GitHub repository (git and GitHub issues / pull requests) from a working GrimoireLab dashboard, by modifying the needed Mordred configuration files, and fixing the raw and enriched indexes to remove the items for the removed repository. Test it by removing at least two repositories (in two separate steps) from a GrimoireLab dashboard, producing screenshots of the results.

For this script to run you need config file which was generated in microtask-1 and both of this file and script should be in the same folder.
Then this script will show the repository which are present in dashboard and then you will be asked for chosing the index for deleting that repository
After that it will show the index of git and github which are present in dashboard. 
### How to run this script
Commands for using for this script, assuming config file which was generated in microtask-1 is 'config_bytedeco.cfg'
```
(grimoirelab) $ python3 task3.py
Enter the name of config file which is associated with current dashboard
config_bytedeco.cfg
0 https://github.com/bytedeco/javacpp-presets
1 https://github.com/bytedeco/javacpp
2 https://github.com/bytedeco/javacv
3 https://github.com/bytedeco/javacv-examples
4 https://github.com/bytedeco/sbt-javacv
5 https://github.com/bytedeco/procamcalib
6 https://github.com/bytedeco/procamtracker
7 https://github.com/bytedeco/sbt-javacpp
8 https://github.com/bytedeco/bytedeco.github.io
9 https://github.com/bytedeco/sample-projects

Enter the Index of repository which you want to delete
2
git_test
github_test
git_test-raw
github_test-raw
Repository deleted successfully

# For screenshot, i have deleted the 2nd and 1st repository 

```

### Results
- Task-3 folder contains mordred configuration files, script and three folder for storing screenshots
- Folder 'Initial dashboard' contain screeenshot of initial dashboard.
- Folder 'Second repo deleted' contain screeenshot of dashboard after second repository is deleted.
