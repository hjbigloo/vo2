import flask
from flask import Flask, render_template
from flask import request, session, jsonify
import dataconn 
app = Flask(__name__)
app.secret_key = b'fr3umr349uft0374]43_'
dataConn = dataconn.DataConn("demo.db")

@app.route("/api/login", methods=['POST'])
def loginApi():
    payload = request.json
    username = payload['username']
    password = payload['password']
    loginUid= dataConn.check_login(username, password)
    if loginUid is not None:
        session['user_id'] = loginUid
        return jsonify({'code': 200, 
                        'payload':{'username': username,
                                   'user_id': 1}})
    else:
        return jsonify({'code': 403})

@app.route("/api/logout")
def logoutApi():
    session.pop('user_id')
    return jsonify({'code': 200})

@app.route("/api/getCurrentUser")
def getCurrentUserApi():
    if 'user_id' in session:
        return jsonify({'code': 200, 'payload':{
                'user_id': session['user_id'],
                'username': 'admin'
            }})
    else:
        return jsonify({'code': 200, 'payload': None})

@app.route("/api/getProjectsList")
def getProjectsListApi():
    if not ('user_id' in session):
        return jsonify({'code': 403})
    user_id = session['user_id']
    pj_list = dataConn.get_projects_of_user(user_id)
    payload = {'projects': pj_list}
    return jsonify({'code': 200, 'payload': payload})

@app.route("/api/addProject", methods=['POST'])
def addProjectApi():
    if not ('user_id' in session):
        return jsonify({'code': 403})
    user_id = session['user_id']
    payload = request.json
    name = payload['name']
    pj_list = dataConn.get_projects_of_user(user_id)
    for item in pj_list:
        if name == item['name']:
            return jsonify({'code': 400})
    dataConn.add_project(name, user_id)
    return jsonify({'code': 200})

@app.route("/api/getLayersList", methods=['POST'])
def getLayersListApi():
    if not ('user_id' in session):
        return jsonify({'code': 403})
    payload = request.json
    pid = payload['pid']
    layers = dataConn.get_layers_of_project(pid)
    return jsonify({'code': 200, 'payload': {'layers': layers}})

@app.route("/api/addLayer", methods=['POST'])
def addLayerApi():
    if not ('user_id' in session):
        return jsonify({'code': 403})
    payload = request.json
    name = payload['name']
    url = payload['url']
    layer_type = payload['type']
    location = payload['location']
    pid = payload['pid']
    dataConn.add_layer(name, url, layer_type, location, pid)
    return jsonify({'code': 200})

@app.route("/")
def index():
    with open("index.html") as f:
        html_source = f.read()
    return html_source

if __name__ == "__main__":
    app.run("localhost", 9802, True)
