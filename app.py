#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

app = Flask(__name__)

#Set up Authentication - user:pwd=archit:ahlawat
'''
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'archit':
        return 'ahlawat'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
'''
tasks = [
    {
        'id': 1,
        'ani': u'917042723503',
        'dnis': u'8001234567',
        'cv1': u'12345***********************************',
        'cv2': u'12345***********************************',
        'cv3': u'12345***********************************',
        'cv4': u'12345***********************************',
        'cv5': u'12345***********************************',
        'cv6': u'12345***********************************',
        'cv7': u'12345***********************************',
        'cv8': u'12345***********************************',
        'cv9': u'12345***********************************',
        'cv10': u'12345***********************************',
        'ecc1': u'12345***********************************12345***********************************12345***********************************12345***********************************12345*********************************************',
        'ecc2': u'12345***********************************12345***********************************12345***********************************12345***********************************12345*********************************************',
        'ecc3': u'12345***********************************12345***********************************12345***********************************12345***********************************12345*********************************************',
        'ecc4': u'12345***********************************12345***********************************12345***********************************12345***********************************12345*********************************************',
        'app_authenticated': u'yes', 
        'transfer_escalation': False,
        'done': False
    },
    {
        'id': 2,
        'ani': u'918745032469',
        'dnis': u'8001234567',
        'cv1': u'98765***********************************',
        'cv2': u'98765***********************************',
        'cv3': u'98765***********************************',
        'cv4': u'98765***********************************',
        'cv5': u'98765***********************************',
        'cv6': u'98765***********************************',
        'cv7': u'98765***********************************',
        'cv8': u'98765***********************************',
        'cv9': u'98765***********************************',
        'cv10': u'98765***********************************',
        'ecc1': u'98765***********************************98765***********************************98765***********************************98765***********************************98765*********************************************',
        'ecc2': u'98765***********************************98765***********************************98765***********************************98765***********************************98765*********************************************',
        'ecc3': u'98765***********************************98765***********************************98765***********************************98765***********************************98765*********************************************',
        'ecc4': u'98765***********************************98765***********************************98765***********************************98765***********************************98765*********************************************',
        'app_authenticated': u'yes', 
        'transfer_escalation': True,
        'done': False
    }
]

@app.route('/icmservice/api/v1.0/tasks', methods=['GET'])
#@auth.login_required
def get_tasks():
    #return jsonify({'tasks': tasks})
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

'''@app.route('/icmservice/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})'''

@app.route('/icmservice/api/v1.0/tasks/<cust_ani>', methods=['GET'])
def get_task1(cust_ani):
    task = [task for task in tasks if task['ani'] == cust_ani]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/icmservice/api/v1.0/tasks',methods=['POST'])
def create_task():
    if not request.json or not 'ani' in request.json:
        abort(400)
    task = {
    'id': tasks[-1]['id']+1,
    'ani': request.json['ani'],
    'dnis': request.json['dnis'],
    'cv1': request.json['cv1'],
    'cv2': request.json['cv2'],
    'cv3': request.json['cv3'],
    'cv4': request.json['cv4'],
    'cv5': request.json['cv5'],
    'cv6': request.json['cv6'],
    'cv7': request.json['cv7'],
    'cv8': request.json['cv8'],
    'cv9': request.json['cv9'],
    'cv10': request.json['cv10'],
    'ecc1': request.json['ecc1'],
    'ecc2': request.json['ecc2'],
    'ecc3': request.json['ecc3'],
    'ecc4': request.json['ecc4'],
    'app_authenticated': request.json['app_authenticated'],
    'transfer_escalation': request.json.get('transfer_escalation',""),
    'done': False
    }
    tasks.append(task)
    return jsonify({'task':task}),201

@app.route('/icmservice/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'ani' in request.json and type(request.json['ani']) != unicode:
        abort(400)
    if 'dnis' in request.json and type(request.json['dnis']) != unicode:
        abort(400)
    if 'cv1' in request.json and type(request.json['cv1']) is not unicode:
        abort(400)
    if 'cv2' in request.json and type(request.json['cv2']) is not unicode:
        abort(400)
    if 'cv3' in request.json and type(request.json['cv3']) is not unicode:
        abort(400)
    if 'cv4' in request.json and type(request.json['cv4']) is not unicode:
        abort(400)
    if 'cv5' in request.json and type(request.json['cv5']) is not unicode:
        abort(400)
    if 'cv6' in request.json and type(request.json['cv6']) is not unicode:
        abort(400)
    if 'cv7' in request.json and type(request.json['cv7']) is not unicode:
        abort(400)
    if 'cv8' in request.json and type(request.json['cv8']) is not unicode:
        abort(400)
    if 'cv9' in request.json and type(request.json['cv9']) is not unicode:
        abort(400)
    if 'cv10' in request.json and type(request.json['cv10']) is not unicode:
        abort(400)
    if 'ecc1' in request.json and type(request.json['ecc1']) is not unicode:
        abort(400)
    if 'ecc2' in request.json and type(request.json['ecc2']) is not unicode:
        abort(400)
    if 'ecc3' in request.json and type(request.json['ecc3']) is not unicode:
        abort(400)
    if 'ecc4' in request.json and type(request.json['ecc4']) is not unicode:
        abort(400)
    if 'app_authenticated' in request.json and type(request.json['app_authenticated']) is not unicode:
        abort(400)
    if 'transfer_escalation' in request.json and type(request.json['transfer_escalation']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['ani'] = request.json.get('ani', task[0]['ani'])
    task[0]['dnis'] = request.json.get('dnis', task[0]['dnis'])
    task[0]['cv1'] = request.json.get('cv1', task[0]['cv1'])
    task[0]['cv2'] = request.json.get('cv2', task[0]['cv2'])
    task[0]['cv3'] = request.json.get('cv3', task[0]['cv3'])
    task[0]['cv4'] = request.json.get('cv4', task[0]['cv4'])
    task[0]['cv5'] = request.json.get('cv5', task[0]['cv5'])
    task[0]['cv6'] = request.json.get('cv6', task[0]['cv6'])
    task[0]['cv7'] = request.json.get('cv7', task[0]['cv7'])
    task[0]['cv8'] = request.json.get('cv8', task[0]['cv8'])
    task[0]['cv9'] = request.json.get('cv9', task[0]['cv9'])
    task[0]['cv10'] = request.json.get('cv10', task[0]['cv10'])
    task[0]['ecc1'] = request.json.get('ecc1', task[0]['ecc1'])
    task[0]['ecc2'] = request.json.get('ecc2', task[0]['ecc2'])
    task[0]['ecc3'] = request.json.get('ecc3', task[0]['ecc3'])
    task[0]['ecc4'] = request.json.get('ecc4', task[0]['ecc4'])
    task[0]['app_authenticated'] = request.json.get('app_authenticated', task[0]['app_authenticated'])
    task[0]['transfer_escalation'] = request.json.get('transfer_escalation', task[0]['transfer_escalation'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/icmservice/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


if __name__ == '__main__':
    app.run(host='0.0.0.0')



