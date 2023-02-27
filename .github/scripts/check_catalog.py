from github import Github
import yaml
from pathlib import Path
import os

catalog_url = "jungtop/sample_catalog"
#catalog_url = "jungtop/sample_catalog"


def get_catalog(g):
    
    try:
        repo = g.get_repo(catalog_url)
        contents = repo.get_contents(f"./demo.csv")
        catalog = yaml.safe_load(contents.decoded_content.decode())
        return catalog
    except:
        print('Repo Not Found')

def update_catalog(catalog):
    catalog +="new content"+"\n"
    return catalog

def update_repo(g,commit_msg,updated_catalog):
    try:
        repo = g.get_repo(catalog_url)
        contents = repo.get_contents(f"./demo.csv",ref="main")
        repo.update_file(contents.path, commit_msg, updated_catalog, sha=contents.sha, branch="main")
    except Exception as e:
        print(e) 
    

if __name__ == "__main__":
    token = "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"
    g = Github(token)
    commit_msg = "updated catalog"
    catalog = get_catalog(g)
    updated_catalog = update_catalog(catalog)
    update_repo(g,commit_msg,updated_catalog)
