

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
- github api --> api-token (create api token)

For mysql name and password, you can create a new one refer [here](https://dev.mysql.com/doc/refman/5.7/en/create-user.html)

For data name, you can initialise using sortinghat command explained [here](https://grimoirelab.gitbooks.io/tutorial/grimoireelk/a-dashboard-with-sortinghat.html) with topic name initializing sortinghat

$ 
### Run, how to create a dashboard using the generated file

I am Assuming that you have followed the requirement step and installed grimoirelab in a virtual environment as given [here](https://grimoirelab.gitbooks.io/tutorial/before-you-start/installing-grimoirelab.html)
Before procceding, i will suggest you to read [A GrimoireLab dashboard in one step](https://grimoirelab.gitbooks.io/tutorial/mordred/a-grimoirelab-dashboard-in-one-step.html) , [Mordred in a container](https://grimoirelab.gitbooks.io/tutorial/mordred/mordred-in-a-container.html) , [The projects file](https://grimoirelab.gitbooks.io/tutorial/mordred/the-projects-file.html)
```
# these command is used assuming you have created a virtual envirnoment as mentioned above.

# for initializing sortinghat database, where 'user' and 'XXX' is user name and passord of mysql database.
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

# And that's it. Point your browser to http://localhost:5601, assuming your Kibiter is deployed to serve requests in the standard port (5601). You'll see the produced dashboard.
```
Running mordred command can take time according to the organisation selected, so keep patience