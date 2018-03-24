import json
import requests

def check_repo_url(org_url,repo_url):
	r = requests.get(org_url)
	org_file=r.json()
	# print(repo_url)
	for repo in org_file:
		# print(repo)
		if repo['url'] == repo_url:
			return True
	return False 

def check_repo_already_there(org,repo_html_url,data):
	# print(repo_html_url)
	for i in data[org]['git']:
		# print(i)
		if i == repo_html_url:
			return True
		
	return False

def add_repo(org,repo_html_url):
	project=input("Enter the name of json file like 'project.json'\n")
	# print(project)
	with open(project, 'r+') as f:
		data = json.load(f)
		
		if not org in data:
			# print('yeah')
			data[org]={}
			data[org]['git']=[]
			data[org]['github']=[]

		if check_repo_already_there(org,repo_html_url,data) ==True:
			print("This repository already exits!!")
			return

		data[org]['git'].append(repo_html_url)
		data[org]['github'].append(repo_html_url)
		f.seek(0)
		json.dump(data,f,default=str)
		print("repository successfully added")


if __name__ == '__main__':
	org=input("Enter organisation name\n")
	rr=requests.get('https://api.github.com/orgs/'+ org)
	if not 'id' in rr.json():
		print("this organisation does not exit")
	else:	
		repo=input("Enter name of repository\n")
		org_url='https://api.github.com/orgs/'+ org +'/repos'
		repo_url='https://api.github.com/repos/'+org+'/'+repo
		repo_html_url='https://github.com/'+org+'/'+repo

	
		if check_repo_url(org_url,repo_url) ==True:
			add_repo(org,repo_html_url)
		else:
			print("This repository does not exit in this organisation")