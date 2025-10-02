import json
from urllib import response

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado
import requests
import os
import uuid
import datetime
from zoneinfo import ZoneInfo


def read_config_file():
    """
    reads config.json file
    :return: dict
    """
    config_file = os.path.join(os.getcwd() ,"Exercises",'config.json')
    if os.path.exists(config_file):
        f=open(config_file)
        return json.load(f)
    return {}

def create_initial_files():
    print('======================================')
    print("Check and Create Initial Files:")
    print('======================================')
    current_dir = os.getcwd()
    print(current_dir)
    if "Exercises" not in os.listdir():
        os.makedirs(os.path.join(current_dir,"Exercises"))
   
    # Create config.json file
    config_path = os.path.join(current_dir,"Exercises","config.json")
    if not os.path.isfile(config_path):
        config_data = {}
        config_data['name'] = "John Smith"
        config_data['server'] = "http://141.225.10.71:8081"
        config_data['carpo_version'] = "0.2.9"
        # Write default config
        with open(config_path, "w") as config_file:
            config_file.write(json.dumps(config_data, indent=4))
    
    # Create blank notebook
    notebook_path = os.path.join(current_dir,"Exercises","Welcome.ipynb")
    if not os.path.isfile(notebook_path):
        content = {
                        "cells": [],
                        "metadata": {
                            "kernelspec": {
                                "display_name": "Python 3 (ipykernel)",
                                "language": "python",
                                "name": "python3"
                                },
                            "language_info": {
                            "codemirror_mode": {
                                "name": "ipython",
                                "version": 3
                                },
                            "file_extension": ".py",
                            "mimetype": "text/x-python",
                            "name": "python",
                            "nbconvert_exporter": "python",
                            "pygments_lexer": "ipython3",
                            "version": "3.10"
                            }
                        },
                        "nbformat": 4,
                        "nbformat_minor": 5
                    }

        content["cells"].append({
                                "cell_type": "markdown",
                                "id": str(uuid.uuid4()),
                                "metadata": {},
                                "source": [ "\
#### (Optional) To register on carpo, do these steps: \n \
1. Click on Carpo Menu -> Register. \n \
2. Enter the server URL. Click Ok. \n \
#### To download exercises: \n \
1. Click on Active Learning Menu -> Download Exercise. \n \
It will download the exercise notebooks inside Exercises Directory. \n \
                                    "],
                                "outputs": []
                                })

        with open(notebook_path, "w") as file:
            file.write(json.dumps(content, indent = 4))


class RegistrationHandler(APIHandler):
    def initialize(self,config_files):
        self.config_files = config_files

    @tornado.web.authenticated
    def post(self):

        config_data = read_config_file()

        if config_data == {}:
            create_initial_files()
            self.set_status(500)
            self.finish(json.dumps({'message': "Update your User Name and Server address in Exercises/config.json file and register again."}))
            return 
            
        if not {'name','server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "Invalid config.json file. Please check your config file."}))
            return
        
        if 'id' in config_data.keys() and 'name' in config_data.keys():
            self.set_status(200)
            self.finish(json.dumps({'message':'User already registered.', 'name': config_data['name']}))
            return
    
        # get name from jupyterhub username
        input_data = self.get_json_body()
        serverUrl = input_data['serverUrl']
        hubUserName = os.environ.get('USER')
        userName = hubUserName.replace("jupyter-", "")

        # To register user based on the config file. Uncomment the following.
        # userName = config_data['name'] 

        url = serverUrl + "/users"

        body = {}
        body['name'] = userName
        body['role'] = 2 # Role 2 is student

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        
        try:
            response = requests.post(url, data=json.dumps(body),headers=headers,timeout=5).json()
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': "Carpo Server Error. {}".format(e)}))
            return

        config_data['id'] = response['id']
        config_data['server'] = serverUrl
        config_data['name'] = userName
        # Write id to the json file.
        with open(os.path.join(os.getcwd(),"Exercises",'config.json'), "w") as config_file:
            config_file.write(json.dumps(config_data, indent=4))

        self.finish(json.dumps(response))

class QuestionRouteHandler(APIHandler):
    @tornado.web.authenticated
    def get(self):

        config_data = read_config_file()

        if not {'id','server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return

        # url = config_data['server'] + "/problem?student_id="+str(config_data['id'])
        url = config_data['server'] + "/problems/students/"+str(config_data['id'])
        try:
            resp = requests.get(url,timeout=5).json()
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': "Carpo Server Error. {}".format(e)}))
            return

        # Write questions to individual Notebook
        file_paths = self.question_file(resp['data'])
        msg = ""
        # print(file_paths)
        if file_paths['new_download']:
            msg = "New Problem downloaded and placed in notebook " + ', '.join(file_paths['new_download']) + '.'

        if file_paths['already_downloaded']:
            msg += "\nProblem already downloaded and placed in notebook " + ', '.join(file_paths['already_downloaded']) + '.'

        if len(resp['data']) == 0: 
            msg = "You have got 0 new problems. Please check again later."
    
        self.finish(json.dumps({'msg': msg}))

    def question_file(self, data):
        file_paths = {}
        file_paths['new_download'] = []
        file_paths['already_downloaded'] = []
        for res in data:
            file_path = os.path.join(os.getcwd(),"Exercises","ex{:03d}".format( res['id']) + ".ipynb")

            if not os.path.exists(file_path):
                file_paths['new_download'].append("ex{:03d}".format( res['id']) + ".ipynb")
                content = {
                        "cells": [],
                        "metadata": {
                            "kernelspec": {
                                "display_name": "Python 3 (ipykernel)",
                                "language": "python",
                                "name": "python3"
                                },
                            "language_info": {
                            "codemirror_mode": {
                                "name": "ipython",
                                "version": 3
                                },
                            "file_extension": ".py",
                            "mimetype": "text/x-python",
                            "name": "python",
                            "nbconvert_exporter": "python",
                            "pygments_lexer": "ipython3",
                            "version": "3.8.10"
                            }
                        },
                        "nbformat": 4,
                        "nbformat_minor": 5
                    }

                content["cells"].append({
                                "cell_type": "markdown",
                                "id": str(uuid.uuid4()),
                                "metadata": {},
                                "source": [ f"### In-class Exercises: {res['id']} \n" ],
                                "outputs": []
                                })
                content["cells"].append({
                                "cell_type": res['format'],
                                "execution_count": 0,
                                "id": str(uuid.uuid4()),
                                "metadata": { 
                                    "problem": res['id']
                                    },
                                "source": [ x+"\n" for x in res['question'].split("\n") ],
                                "outputs": []
                                })
                content["cells"].append({
                                "cell_type": "code",
                                "id": str(uuid.uuid4()),
                                "metadata": {"editable": False},
                                "source": [],
                                "outputs": []
                                })

                # Serializing json 
                json_object = json.dumps(content, indent = 4)

                with open(file_path, "w") as file:
                    file.write(json_object)
            else:
                file_paths['already_downloaded'].append("ex{:03d}".format( res['id']) + ".ipynb")


        return file_paths

class SolutionRouteHandler(APIHandler):
    @tornado.web.authenticated
    def get(self):

        config_data = read_config_file()

        if not {'id','server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return


        url = config_data['server'] + "/solution"
        try:
            resp = requests.get(url,timeout=5).json()
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': "Carpo Server Error. {}".format(e)}))
            return

        # Write solutions to individual Notebook
        file_paths = self.solutions_files(resp['data'])
        msg = ""
        if file_paths['new_download']:
            msg = "New Solution(s) downloaded and placed in notebook(s) " + ', '.join(file_paths['new_download']) + '. '

        # if file_paths['already_downloaded']:
        #     msg += "Solution(s) already downloaded and placed in notebook(s) " + ', '.join(file_paths['already_downloaded']) + '.'

        if len(file_paths['new_download'] + file_paths['already_downloaded'] )  == 0: 
            msg = "There are no new solutions. Please check again later."
    
        self.finish(json.dumps({'msg': msg}))

    def solutions_files(self, data):
        file_paths = {}
        file_paths['new_download'] = []
        file_paths['already_downloaded'] = []
        for res in data:
            file_path = os.path.join(os.getcwd(),"Exercises","ex{:03d}".format( res['problem_id']) + "_sol.ipynb")

            if not os.path.exists(file_path):
                file_paths['new_download'].append("ex{:03d}".format( res['problem_id']) + "_sol.ipynb")
                content = {
                        "cells": [],
                        "metadata": {
                            "kernelspec": {
                                "display_name": "Python 3 (ipykernel)",
                                "language": "python",
                                "name": "python3"
                                },
                            "language_info": {
                            "codemirror_mode": {
                                "name": "ipython",
                                "version": 3
                                },
                            "file_extension": ".py",
                            "mimetype": "text/x-python",
                            "name": "python",
                            "nbconvert_exporter": "python",
                            "pygments_lexer": "ipython3",
                            "version": "3.8.10"
                            }
                        },
                        "nbformat": 4,
                        "nbformat_minor": 5
                    }

                content["cells"].append({
                                "cell_type": res['format'],
                                "execution_count": 0,
                                "id": str(uuid.uuid4()),
                                "metadata": {},
                                "source":  [ x+"\n" for x in res['solution'].split("\n") ],
                                "outputs": []
                                })

                # Serializing json 
                json_object = json.dumps(content, indent = 4)

                with open(file_path, "w") as file:
                    file.write(json_object)
            else:
                file_paths['already_downloaded'].append("ex{:03d}".format( res['problem_id']) + "_sol.ipynb")

        return file_paths

class FeedbackRouteHandler(APIHandler):
    @tornado.web.authenticated
    def get(self):
        config_data = read_config_file()

        if not {'id','server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return

        url = config_data['server'] + "/students/get_submission_feedbacks?student_id="+str(config_data['id'])
        
        try:
            response = requests.get(url,timeout=5).json()
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': "Carpo Server Error. {}".format(e)}))
            return

        if len(response['data']) == 0:
            self.finish(json.dumps({
                "msg": "No Feedback available at the moment. Please check again later.",
                "hard-reload": -1
            }))
            return
        
        # Write feedbacks to individual Notebook
        file_paths,reload = self.feedback_file(response['data'])
        if file_paths:
            msg = "Feedback placed in " + ','.join(file_paths) + '.'
        
        self.finish(json.dumps({'msg':msg, 'hard-reload': reload}))

    def feedback_file(self, data):
        file_paths = []
        reload = 0
        for res in data:
            dir_path = os.path.join("Exercises","Feedback")
            file_path = "ex{:03d}_{:03d}".format(res['problem_id'],res['id']) + ".ipynb"
            file_paths.append("Feedback/" + file_path)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            feedback_file = os.path.join(dir_path, file_path)
            if os.path.exists(feedback_file):
                os.remove(feedback_file)
                reload = 1

            if not os.path.exists(feedback_file):
                content = {
                        "cells": [],
                        "metadata": {
                            "kernelspec": {
                                "display_name": "Python 3 (ipykernel)",
                                "language": "python",
                                "name": "python3"
                                },
                            "language_info": {
                            "codemirror_mode": {
                                "name": "ipython",
                                "version": 3
                                },
                            "file_extension": ".py",
                            "mimetype": "text/x-python",
                            "name": "python",
                            "nbconvert_exporter": "python",
                            "pygments_lexer": "ipython3",
                            "version": "3.8.10"
                            }
                        },
                        "nbformat": 4,
                        "nbformat_minor": 5
                    }
               
                content["cells"].append({
                        "cell_type": "markdown",
                        "id": str(uuid.uuid4()),
                        "metadata": {},
                        "source": [ x+"\n" for x in res['message'].split("\n") ]
                        })


                content["cells"].append({
                        "cell_type": "code",
                        "execution_count": 0,
                        "id": str(uuid.uuid4()),
                        "metadata": {},
                        "source": [ x+"\n" for x in res['code_feedback'].split("\n") ],
                        "outputs": []
                        })

                content["cells"].append({
                        "cell_type": "markdown",
                        "id": str(uuid.uuid4()),
                        "metadata": {},
                        "source": [ x+"\n" for x in res['comment'].split("\n") ]
                        })

                # Serializing json 
                json_object = json.dumps(content, indent = 4)

                with open(feedback_file, "w") as file:
                    file.write(json_object)
        return file_paths, reload
class SubmissionRouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server

    @tornado.web.authenticated
    def post(self):
        # input_data is a dictionary with a key "name"
        input_data = self.get_json_body()

        config_data = read_config_file()

        if not {'id', 'name', 'server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return

        input_data['student_id'] = config_data['id']
        url = config_data['server'] + "/submissions/students/" + str(config_data['id'] )


        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        try:
            response = requests.post(url, data=json.dumps(input_data),headers=headers).json()
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': "Carpo Server Error. {}".format(e)}))
            return

        self.finish(response)

class RaiseHandRouteHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        # input_data is a dictionary with a key "name"
        input_data = self.get_json_body()

        config_data = read_config_file()

        if not {'id', 'name', 'server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return

        input_data['student_id'] = config_data['id']
        url = config_data['server'] + "/students/" + str(input_data['student_id']) +"/ask_for_help"


        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        try:
            response = requests.post(url, data=json.dumps(input_data),headers=headers).json()
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': "Carpo Server Error. {}".format(e)}))
            return

        self.finish(response)

class ViewStatusRouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server

    @tornado.web.authenticated
    def get(self):
        # input_data is a dictionary with a key "name"
        input_data = self.get_json_body()

        config_data = read_config_file()

        if not {'id', 'name', 'server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return

        id = config_data['id']
        name = config_data['name']
        student_status_url = config_data['server'] + "/students/status" + "?student_id=" + str(id) + "&student_name=" + name

        self.finish({"url":student_status_url })

class ViewProblemStatusRouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server

    @tornado.web.authenticated
    def get(self):
        # input_data is a dictionary with a key "name"
        input_data = self.get_json_body()

        config_data = read_config_file()

        if not {'id', 'name', 'server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return

        problems_status_url = config_data['server'] + "/problems/status"

        self.finish({"url":problems_status_url })

class WidgetFeedbackHandler(APIHandler):
    """Handler for the floating feedback widget to get feedback content as JSON"""
    
    @tornado.web.authenticated
    def get(self):
        config_data = read_config_file()

        if not {'id','server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return

        # Get problem_id from query parameter, default to 1 if not provided
        problem_id = self.get_argument('problem_id', '1')
        
        try:
            problem_id = int(problem_id)
        except ValueError:
            problem_id = 1

        url = config_data['server'] + "/students/"+ str(config_data['id'])+ "/problems/"+ str(problem_id) + "/feedbacks"

        try:
            response = requests.get(url,timeout=5).json()
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': "Carpo Server Error. {}".format(e)}))
            return

        if len(response['data']) == 0:
            self.finish(json.dumps({
                "msg": "No feedback available yet. Your submissions are being reviewed."
            }))
            return
        
        else:
            self.finish(json.dumps(response))

class ConfigHandler(APIHandler):
    """Handler to serve the config.json file"""
    
    @tornado.web.authenticated
    def get(self):
        config_data = read_config_file()
        
        if not config_data:
            self.set_status(404)
            self.finish(json.dumps({'message': "Config file not found"}))
            return
        
        self.finish(json.dumps(config_data))

class FeedbackRatingHandler(APIHandler):
    """Handler for feedback ratings - PUT /feedback-ratings"""
    
    @tornado.web.authenticated
    def put(self):
        # Get the rating from request body
        input_data = self.get_json_body()
        
        if 'id' not in input_data:
            self.set_status(400)
            self.finish(json.dumps({'message': "Missing id field in request body"}))
            return
            
        rating = input_data['rating']
        
        # Validate rating value
        if rating not in [-1, 0, 1]:
            self.set_status(400)
            self.finish(json.dumps({'message': "Rating must be -1, 0, or 1"}))
            return
        
        config_data = read_config_file()

        if not {'id','server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return

        # Prepare the request body for the backend server
        body = {
            'rating': rating,
            'id': input_data['id']
        }

        url = config_data['server'] + "/feedback-ratings"
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        
        try:
            response = requests.put(url, data=json.dumps(body), headers=headers, timeout=5)
            
            if response.status_code == 200:
                response_data = response.json()
                self.finish(json.dumps(response_data))
            else:
                self.set_status(response.status_code)
                self.finish(json.dumps({'message': f"Server returned status {response.status_code}"}))
                
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': f"Carpo Server Error. {e}"}))
            return

class SolutionDownloadHandler(APIHandler):
    """Handler for downloading solutions - GET /solutions/problem/:problem_id"""
    
    @tornado.web.authenticated
    def get(self, problem_id):
        config_data = read_config_file()

        if not {'id','server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return

        # Validate problem_id
        try:
            problem_id = int(problem_id)
        except ValueError:
            self.set_status(400)
            self.finish(json.dumps({'message': "Invalid problem_id. Must be a number."}))
            return

        url = config_data['server'] + f"/solutions/problem/{problem_id}"
        
        try:
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                response_data = response.json()
                self.finish(json.dumps(response_data))
            elif response.status_code == 404:
                self.set_status(404)
                self.finish(json.dumps({'message': f"No solution available for problem {problem_id}"}))
            else:
                self.set_status(response.status_code)
                self.finish(json.dumps({'message': f"Server returned status {response.status_code}"}))
                
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': f"Carpo Server Error. {e}"}))
            return

class DownloadNotebooksHandler(APIHandler):
    """Handler for downloading notebooks - GET /download_notebooks"""
    
    @tornado.web.authenticated
    def get(self):
        file_paths = {}
        file_paths['new_download'] = []
        file_paths['already_downloaded'] = []

        config_data = read_config_file()

        if not {'id','server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return
        
        mode = self.get_argument("type", None, True)
        if mode not in ('assignment', 'exam'):
            self.set_status(500)
            self.finish(json.dumps({'message': 'Notebook type not found.'}))
            return

        user_id = config_data['id']
        url = config_data['server'] + f"/notebooks/students/{user_id}/download?type={mode}"
        # msg = ''
        msg_2 = []
        
        try:
            response = requests.get(url, timeout=30)
            
            if response.status_code == 200:
                resp_data = response.json()
                
                if 'data' in resp_data and len(resp_data['data']) > 0:
                    for item in resp_data['data']:
                        # Create directory if it doesn't exist
                        directory = "Assignments" if item['mode'] == 1 else "Exams" 
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        
                        # filename = f"{file_path}.ipynb"
                        # Save file with as the path
                        name = os.path.basename(item['path'])
                        filename = os.path.join(directory, name)
                        if  os.path.exists(filename):
                            file_paths['already_downloaded'].append(filename)
                            msg_2.append(f'Notebook already downloaded and placed to {filename}.')
                            continue

                        # Download individual notebook file
                        file_url = config_data['server'] + f"/notebooks/file?file_path={item['path']}"
                        
                        try:
                            file_response = requests.get(file_url, timeout=30)
                            
                            if file_response.status_code == 200:

                                #Decode the bytes to a string using UTF-8 encoding
                                json_string = file_response.content.decode('utf-8')

                                #Parse the JSON string into a Python dictionary
                                json_object = json.loads(json_string)
                                json_object['metadata']['notebook_id'] = item['id'] 
                                json_object['metadata']['notebook_uuid'] = item['notebook_uuid'] 

                                # Serializing json 
                                json_serial = json.dumps(json_object, indent = 4)

                                # with open(filename, 'wb') as f:
                                    # f.write(file_response.content)
                                with open(filename, 'w') as f:
                                    f.write(json_serial)
                                
                                file_paths['new_download'].append(filename)
                                msg_2.append(f'New Notebook downloaded to {filename}.')
                                                                
                        except requests.exceptions.RequestException as e:
                            self.set_status(file_response.status_code)
                            self.finish(json.dumps({'message': f"Server File returned status {file_response.status_code}"}))
                    self.finish(json.dumps({
                        'message': msg_2,
                    }))
                else:
                    self.finish(json.dumps({'message': ['No notebooks to download.']}))

            else:
                self.set_status(response.status_code)
                self.finish(json.dumps({'message': f"Server returned status {response.status_code}"}))
                
        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': f"Carpo Server Error. {e}"}))
            return

class SubmitNotebookHandler(APIHandler):
    """Handler for submitting notebooks - POST /submit_notebook"""
    
    @tornado.web.authenticated
    def post(self):
        # Get the request data
        input_data = self.get_json_body()
        
        if 'title' not in input_data or 'path' not in input_data or 'notebookID' not in input_data:
            self.set_status(400)
            self.finish(json.dumps({'message': "Cannot submit Notebook. Missing required fields."}))
            return
        
        title = input_data['title']
        path = input_data['path']
        status = input_data['status']
        notebook_id = input_data['notebookID']
        
        # Get file creation time
        try:
            if not os.path.exists(path):
                self.set_status(404)
                self.finish(json.dumps({'message': f"File not found at path: {path}"}))
                return
                
            # Get file stats
            file_stats = os.stat(path)
            target_timezone = ZoneInfo('America/Chicago')

            creation_time = datetime.datetime.fromtimestamp(file_stats.st_ctime, tz=target_timezone)
            creation_time_str = creation_time.isoformat()
            
        except OSError as e:
            self.set_status(500)
            self.finish(json.dumps({'message': f"Error accessing file: {e}"}))
            return
        
        config_data = read_config_file()
        if not {'id','server'}.issubset(config_data):
            self.set_status(500)
            self.finish(json.dumps({'message': "User is not registered. Please Register User."}))
            return
        
        user_id = config_data['id']
        name = config_data['name']
        
        # Read notebook file content
        try:
            with open(path, 'rb') as notebook_file:
                notebook_content = notebook_file.read()
        except IOError as e:
            self.set_status(500)
            self.finish(json.dumps({'message': f"Error reading notebook file: {e}"}))
            return

        # Prepare form data and files for multipart upload
        data = {
            'title': f"{name}_{title}",
            'path': path,
            'status': status,
            'notebook_id': notebook_id,
            'created_at': creation_time_str
        }
        
        files = {
            'filecontent': (title, notebook_content, 'application/json')
        }

        url = config_data['server'] +  f"/notebooks/students/{user_id}/submit"
        
        try:
            response = requests.post(url, data=data, files=files, timeout=30)
            
            if response.status_code == 200:
                response_data = response.json()
                self.finish(json.dumps({'message': response_data['message']}))
            else:
                self.set_status(500)
                self.finish(json.dumps({'message': f"Error. {response.json()}"}))

        except requests.exceptions.RequestException as e:
            self.set_status(500)
            self.finish(json.dumps({'message': f"Carpo Server Error. {e}"}))
            return

def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    route_pattern = url_path_join(base_url, "carpo-student", "submissions")
    handlers = [(route_pattern, SubmissionRouteHandler)]
    web_app.add_handlers(host_pattern, handlers)

    route_pattern_register =  url_path_join(web_app.settings['base_url'], "carpo-student", "register")
    web_app.add_handlers(host_pattern, [(route_pattern_register, RegistrationHandler, dict(config_files = create_initial_files()))])

    route_pattern_question =  url_path_join(web_app.settings['base_url'], "carpo-student", "question")
    web_app.add_handlers(host_pattern, [(route_pattern_question, QuestionRouteHandler)])


    route_pattern_feedback =  url_path_join(web_app.settings['base_url'], "carpo-student", "feedback")
    web_app.add_handlers(host_pattern, [(route_pattern_feedback, FeedbackRouteHandler)])

    route_pattern_view_status =  url_path_join(web_app.settings['base_url'], "carpo-student", "view_student_status")
    web_app.add_handlers(host_pattern, [(route_pattern_view_status, ViewStatusRouteHandler)])

    route_pattern_problems_status =  url_path_join(web_app.settings['base_url'], "carpo-student", "view_problem_list")
    web_app.add_handlers(host_pattern, [(route_pattern_problems_status, ViewProblemStatusRouteHandler)])

    route_pattern_problems_status =  url_path_join(web_app.settings['base_url'], "carpo-student", "solution")
    web_app.add_handlers(host_pattern, [(route_pattern_problems_status, SolutionRouteHandler)])

    route_pattern_problems_status =  url_path_join(web_app.settings['base_url'], "carpo-student", "ask_for_help")
    web_app.add_handlers(host_pattern, [(route_pattern_problems_status, RaiseHandRouteHandler)])

    # Widget feedback endpoint for floating feedback widget
    route_pattern_widget_feedback =  url_path_join(web_app.settings['base_url'], "carpo-student", "widget-feedback")
    web_app.add_handlers(host_pattern, [(route_pattern_widget_feedback, WidgetFeedbackHandler)])

    # Config endpoint to serve config.json
    route_pattern_config =  url_path_join(web_app.settings['base_url'], "carpo-student", "config")
    web_app.add_handlers(host_pattern, [(route_pattern_config, ConfigHandler)])

    # Feedback ratings endpoint
    route_pattern_ratings =  url_path_join(web_app.settings['base_url'], "carpo-student", "feedback-ratings")
    web_app.add_handlers(host_pattern, [(route_pattern_ratings, FeedbackRatingHandler)])

    # Solution download endpoint
    route_pattern_solutions =  url_path_join(web_app.settings['base_url'], "carpo-student", "solutions", "problem", r"(\d+)")
    web_app.add_handlers(host_pattern, [(route_pattern_solutions, SolutionDownloadHandler)])

    # Download notebooks endpoint
    route_pattern_download_notebooks =  url_path_join(web_app.settings['base_url'], "carpo-student", "download_notebooks")
    web_app.add_handlers(host_pattern, [(route_pattern_download_notebooks, DownloadNotebooksHandler)])

    # Submit notebook endpoint
    route_pattern_submit_notebook =  url_path_join(web_app.settings['base_url'], "carpo-student", "submit_notebook")
    web_app.add_handlers(host_pattern, [(route_pattern_submit_notebook, SubmitNotebookHandler)])
