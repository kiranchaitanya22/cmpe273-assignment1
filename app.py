from flask import Flask
from github import Github
import base64
import sys
import yaml
import json

app = Flask(__name__)

g=Github()

url=sys.argv[1].split("/")
for i in url:
    if 'github' in i:
        username= url[url.index(i)+1]
        repository=url[url.index(i)+2]
        break
repo=g.get_user(username).get_repo(repository)


@app.route("/v1/<filename>")
def h1(filename):
    if filename.endswith('.yml'):
        out1=base64.b64decode(repo.get_file_contents(filename).content)
    
    elif filename.endswith('.json'):
        name = filename[:-5] + ".yml"
        out1 = base64.b64decode(repo.get_file_contents(name).content)
        out1 = json.dumps(yaml.load(out1), indent=2)
    
    return out1

@app.route("/")
def h2():
    return "Hello from Dockerized Flask App"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
