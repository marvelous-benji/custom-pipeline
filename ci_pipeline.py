import hashlib
import hmac
import json
import git
import os

from flask import Flask, request, jsonify



app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')





def check_payload(data,headers):
	key = os.getenv('ACCOUNT-KEYS')
	dk = hmac.new(key=key.encode(), msg=data, digestmod=hashlib.sha256)
	kk = hmac.new(key=key.encode(), msg=data, digestmod=hashlib.sha1)
	result = 'sha256=' + dk.hexdigest()
	return hmac.compare_digest(result,headers)



def git_action():

	repo = git.Repo(os.getenv('LOCAL-REPO'))
	remote_url = os.getenv('GITHUB-REPO')
	repo = repo.remotes.origin
	if repo.active_branch.name != 'master':
		repo.git.checkout('master')
	repo.pull('master')
	return 'success'






@app.route('/pull_repo', methods=['POST'])
def receive_event():
	try:
		data = request.data
		if check_payload(data,request.headers.get('X-Hub-Signature-256')):
			git_action()
			print('Git was processed')
		return jsonify({'status':'success','msg':'event received gracefully'}), 200
	except Exception as e:
		print(e)
		return jsonify({'status':'failed','msg':'An error occured'}), 500




if __name__ == '__main__':
	app.run(debug=True, port=9000)
