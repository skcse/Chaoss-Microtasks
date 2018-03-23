import configparser
import os
import json
import requests

def config_file(org):
	cfile= configparser.ConfigParser()
	cfile['general']={
						'short_name':'Girmoirelab',
						'update' :'false',
						'sleep':' 0',
						'min_update_delay ':' 10',
						'debug':' true',
						'logs_dir':'/tmp/',
						'kibana':'"6"'
					}
	cfile['projects']={'projects_file':get_repo(org)}
	cfile['es_collection']={
							'url':'http://127.0.0.1:9200',
							'user':'',
							'password':''
							}
	cfile['es_enrichment']={
							'url':'http://127.0.0.1:9200',
							'user':' ',
							'password':' ',
							'autorefresh': 'false',
							
							}
	cfile['sortinghat']={
						'host' : 'localhost',
						'user' : 'XXXX',
						'password' : 'XXXX',
						'database' : 'XXXX',
						'load_orgs' : 'false',
						'unify_method':'',
						'unaffiliated_group' : 'Unknown',
						'affiliate' : 'True',
						'autoprofile' : '[customer,git,github]',
						'matching' : '[email]',
						'sleep_for' : '0',
						'bots_names' : '[Beloved Bot]'
						}
	cfile['panels']={
					'kibiter_time_from': '"now-180d"',
					'kibiter_default_index':'"git"'	
					}
	cfile['phases']={
					'collection' : 'true',
					'identities' : 'true',
					'enrichment' : 'true',
					'panels' : 'true'
					}
	cfile['git']={
				'raw_index' : 'git_test-raw',
				'enriched_index' : 'git_test'
				}
	cfile['github']={
					'raw_index' : 'github_test-raw',
					'enriched_index' : 'github_test',
					'api-token' : 'XXXX',
					'sleep-for-rate' : 'true'
					}
	with open('config_'+org+'.cfg','w') as configfile:
		cfile.write(configfile)


def get_repo(org):
	org_url='https://api.github.com/orgs/'+org+'/repos'
	data={}
	data[org]={}
	data[org]['git']=[]
	data[org]['github']=[]
	r = requests.get(org_url)
	org_file=r.json()
	# print(org_file)
	for repo in org_file:
		# print(repo)
		# print(" ")
		if repo['fork']==False:
			repo_url=repo['html_url']
			data[org]['git'].append(
				repo_url
				)
			data[org]['github'].append(
				repo_url
				)

	with open('projects_'+org+'.json','w') as outfile:
		json.dump(data,outfile,default=str)
		return 'projects_'+org+'.json'



if __name__ == '__main__':
	org=input("Enter organisation name\n")
	config_file(org)