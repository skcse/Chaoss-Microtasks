from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import pandas as pd
import configparser, os

def get_index_name(cfg):
	config = configparser.ConfigParser()
	config.read_file(open(CONFIG_FILE))
	arr=[]
	arr.append(config.get('git','enriched_index'))
	arr.append(config.get('github','enriched_index'))
	arr.append(config.get('git','raw_index'))
	arr.append(config.get('github','raw_index'))
	return arr

def delete_repository(arr):
	es = Elasticsearch('http://localhost:9200', verify_certs=False)
	
	s = Search(using=es, index='git_test-raw')
	s.aggs.bucket('repository', 'terms', field='origin')
	result=s.execute()
	buckets_result = result['aggregations']['repository']['buckets']

	i=-1
	for repo in buckets_result:
		i=i+1
		print(i,repo.key)
	index=int(input("\nEnter the Index of repository which you want to delete\n"))
	delete_repo=buckets_result[index]['key']
	
	for i in arr:
		print(i)
		s=Search(using=es,index=i).query("match",origin=delete_repo)
		response = s.delete()

if __name__ == '__main__':
	cfg=input("Enter the name of config file which is associated with current dashboard\n")
	try:
		CONFIG_FILE=cfg
		arr=get_index_name(cfg)
		delete_repository(arr)
		print("Repository deleted successfully")
	except:
		print("This config file does not exit")