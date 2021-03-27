from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import request
import ast
app = Flask(__name__)
api = Api(app)
# from firestore_connect import FirebaseDB 
# from bucket_connect import storage_bucket


import base64
from io import BytesIO
from PIL import Image

import subprocess


class Users(Resource):

    def get(self):
        return 'Hello World', 200  # return data and 200 OK code



    # def post(self):
    #     parser = reqparse.RequestParser()  # initialize
        
    #     parser.add_argument('userId', required=True)  # add args
    #     parser.add_argument('version', required=True)
        
    #     args = parser.parse_args()  # parse arguments to dictionary
        
    #     # create new dataframe containing new values
    #     new_data = pd.DataFrame({
    #         'userId': args['userId'],
    #         'version': args['version'],
    #     })
    #     # read our CSV
    #     data = pd.read_csv('users.csv')
    #     # add the newly provided values
    #     data = data.append(new_data, ignore_index=True)
    #     # save back to CSV
    #     data.to_csv('users.csv', index=False)
    #     return {'data': data.to_dict()}, 200  # return data with 200 OK

api.add_resource(Users, '/users')  # '/users' is our entry point


# # New route
# @app.route('', methods=['POST'])
# def api_all():
#     return 'This is test message'

@app.route("/api/v1/create_model", methods=["POST"])
def process_image():
    print(request.data)

    payload = request.get_json()
    email = payload['email']
    gender = payload['gender']
    im_b64 = payload['image']

    im = Image.open(BytesIO(base64.b64decode(im_b64)))
    im.save('../Automate-results/Input/image.png', 'PNG')
    p = subprocess.Popen(['bash', '../Automate/main.sh', '-s', 'http://35.194.162.133:80/',
        '-f', 'http://34.80.223.160:80/', '-i', '../Automate-results/Input/image.png', 
        '-o', '../Automate-results/Output', '-c', '../Common-files-Automate', '-b', 'unity-test-9a5f8.appspot.com', '-u', email,
        '-g', gender
        ])


    return 'JSON Object Example'

if __name__ == '__main__':
    app.run(debug=True)