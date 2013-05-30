#!/usr/bin/python
# coding=UTF-8

import urllib2
import sys
import json
from pymongo import MongoClient

url_extras = "?client_id=******&client_secret=******"
client = MongoClient('localhost', 27017)

if (client):
    print 'Connection is ok!'
else:
    print 'Connection is losed!'
    exit()

db = client.phprepos
if (db):
    print 'DB is ok!'
else:
    print 'DB is losed!'
    exit()

def addSource(data):
    sources = db.sources
    if (sources.find({'name':data['name']}).count()):
        print 'Source was already added!'
    else:
        sources.insert(data)
        print "Source is added!"

def addRepoFromGithub(repo_name):
    # repos/hkulekci/php-the-right-way
    repo_info_str = urllib2.urlopen("https://api.github.com/repos/" + repo_name + url_extras).read()
    repo_info = json.loads(repo_info_str)
    # https://api.github.com/repos/hkulekci/php-the-right-way/tags
    repo_tags_str = urllib2.urlopen("https://api.github.com/repos/" + repo_name + "/tags" + url_extras).read()
    repo_tags = json.loads(repo_tags_str)

    repos = db.repos

    if (repos.find({'seo_url':repo_info['full_name'].replace('/','-')}).count()):
        print "This repo was already saved!";
        return False
    else:
        repo = {}
        repo['seo_url']         = repo_info['full_name'].replace('/','-')
        repo['name']            = repo_info['name']
        repo['description']     = repo_info['description']
        repo['image']           = ''
        repo['requirements']    = ''
        repo['installation']    = ''
        repo['creator']         = ''
        repo['license']         = ''
        repo['tags']            = repo_tags
        repo['home_url']        = repo_info['html_url']

        repo_id = db.repos.insert(repo)
        print 'repo is saved'

def check_repos():

    sources = db.sources
    for source in sources.find({'status':'1'}):
        print source['name']
        if (source['type'] == 'github'):
            addRepoFromGithub(source['name'])
            source['status'] = '1'
            sources.update({'_id':source['_id']}, source, upsert=False)
        else:
            print 'Source Type Not Found!'
    
    # 
    #user_info_str = urllib2.urlopen("https://api.github.com/users/" + username).read()
    #user_info = json.loads(user_info_str)
    #for key in user_info.keys():
    #    print key, " : ", user_info[key]

def main():
    action_name = sys.argv[1]
    action_type = sys.argv[2]
    
    if (action_name == 'source'):
        if (action_type == 'add'):
            data = {}
            data['type'] = sys.argv[3]
            data['name'] = sys.argv[4]
            data['status'] = '0'
            
            addSource(data)
    elif (action_name == 'repo'):
        if (action_type == 'check'):
            check_repos()


if __name__ == "__main__": 
    main()
