# custom-pipeline
A CI/CD server that requires no yaml or yml file

## Description

A minimalistic CI/CD server that listens for push events on a set branch and pull the updates, installing it on any desired server. It requires no yml or yaml file.More features would be added when am much free.

## Getting Started
```
git clone https://github.com/marvelous-benji/custom-pipeline.git  
cd custom-pipeline
python -m venv env  
source env/bin/activate
pip install -r requirements.txt
add your secret key to your config.json file with key as "SECRET_KEY"
```

### Dependencies

* Python3, flask, gitpython,github,hashlib,hmac, os
* platform: Linux

## Setup
In your config.json file, set the key "LOCAL_REPO" to the repo containing the .git directory  
where your production or development server is running. You should also enable git-credentials caching,  
check this: https://git-scm.com/docs/git-credential-cache
The value for the key "GITHUB_REPO" is the repo you intend to watch for changes

### Executing program

* To start the server
```
python ci_pipeline.py
```

## Author

Marvelous Benji
