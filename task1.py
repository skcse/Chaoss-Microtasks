import configparser
import os

def config_file():
	cfile= configparser.ConfigParser()
	cfile['general']={
						'short_name':'GrimoireLab',
						'update' :'false',
						'sleep':' 0',
						'min_update_delay ':' 10',
						'debug':' true',
						'logs_dir':'/tmp/logs',
						'kibana':'"5"'
					}
	cfile['projects']={'projects_file':'projects.json'}
	cfile['es_collection']={
							'url':'http://localhost:9200',
							'user':'',
							'password':''
							}
	cfile['es_enrichment']={
							'url':'http://localhost:9200',
							'user':' ',
							'password':' ',
							'autorefresh': 'false'
							}
	cfile['sortinghat']={
						'host' : 'localhost',
						'user' : 'saurabhu',
						'password' : 'saurabhp',
						'database' : 'shdb',
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
					'kibiter_time_from': '"now-90d"',
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
	with open('config.ini','w') as configfile:
		cfile.write(configfile)





if __name__ == '__main__':
	config_file()
