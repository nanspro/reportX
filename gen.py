import json, requests
import os, pprint                                                                                                                               
from jinja2 import Environment, PackageLoader

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

USERNAME = os.environ['MYTHX_ETH_ADDRESS']
PASS = os.environ['MYTHX_PASSWORD']

API_ENDPOINT = 'https://api.mythx.io/v1/auth/login'

r = requests.post(url = API_ENDPOINT, data = {'ethAddress' : USERNAME, 'password' : PASS})
response = json.loads(r.text)
jwtTokens = response["jwtTokens"]

ACCESS_TOKEN = jwtTokens["access"]
REFRESH_TOKEN = jwtTokens["refresh"]

bearer_token = 'Bearer ' + ACCESS_TOKEN
header = {'Authorization': bearer_token}

print(ACCESS_TOKEN, header)
# API_ENDPOINT = 'https://api.mythx.io/v1/analyses'

# data = {
#   'bytecode': '0x6080604052602060405190810160405280600060010260001916600019168152506000906001610030929190610043565b5034801561003d57600080fd5b506100bb565b828054828255906000526020600020908101928215610085579160200282015b82811115610084578251829060001916905591602001919060010190610063565b5b5090506100929190610096565b5090565b6100b891905b808211156100b457600081600090555060010161009c565b5090565b90565b60d8806100c96000396000f300608060405260043610603f576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063017a9105146044575b600080fd5b348015604f57600080fd5b50606c60048036038101908080359060200190929190505050608a565b60405180826000191660001916815260200191505060405180910390f35b600081815481101515609857fe5b9060005260206000200160009150905054815600a165627a7a72305820d1c4ab8874b5f3cc139613c225a5908ed916e813f5ccdf9a9de97ce28420ca090029'
# }
# m = requests.post(url = API_ENDPOINT, json = data, headers = header)
# print(m)

@app.route('/', methods= ["GET", "POST"])
def hello():
    if request.method == 'POST':
        bytecode = request.form.get("bytecode")
        uuid = request.form.get("uuid")
        uuid_result = request.form.get("uuid_result")

        if bytecode:
            data = {
                "bytecode": bytecode
            }
            print(data)
            API_ENDPOINT = 'https://api.mythx.io/v1/analyses'
            m = requests.post(url = API_ENDPOINT, data = data, headers = header)
            print(m.error)
        elif uuid:
            API_ENDPOINT = 'https://api.mythx.io/v1/analyses' + '/' + uuid
            m = requests.get(url = API_ENDPOINT, headers = header)
            print(m)
            # return jsonify(result='Input needed')
        elif uuid_result:
            API_ENDPOINT = 'https://api.mythx.io/v1/analyses' + '/' + uuid_result + '/' + 'issues'
            m = requests.get(url = API_ENDPOINT, headers = header)
            print(m)

    return render_template('index.html')


# # API_ENDPOINT = 'https://api.mythx.io/v1/analyses/04892277-7197-4a3d-b3fb-dceb6b7ab8ac/issues'
# # m = requests.get(url = API_ENDPOINT, headers = header)

# with open('1.json', 'r') as f:
#     text = f.read()
#     text = text.replace("'", '"')
#     text = text.replace("None", '""')
#     r = json.loads(text)

# print(r)
# report = {}

# # # Preparing data to be presented
# report['source_type'] = r["sourceType"]
# report['source_format'] = r["sourceFormat"]
# report['source_list'] = r["sourceList"]

# #meta
# if "coveredInstructions" in r["meta"].keys():
#     report['n_ins']@app.route('/', methods= ["GET", "POST"])
# def hello():
#     if request.method == 'POST':
#         story = request.form.get("bytecode")
#         if story:
#             data = {
#                 "bytecode": story
#             }
#             print(data)
#             API_ENDPOINT = 'https://api.mythx.io/v1/analyses'
#             m = requests.post(url = API_ENDPOINT, data = data, headers = header)
#             print(m.error)
#         else:
#             return jsonify(result='Input needed')
#     return render_template('index.html') = r["meta"]["coveredInstructions"]
# if "coveredPaths" in r["meta"].keys():
#     report['n_paths'] = r["meta"]["coveredPaths"]
# if "selectedCompiler" in r["meta"].keys():
#     report['compiler'] = r["meta"]["selectedCompiler"]

# #issues
# r = r["issues"][0]
# report['source_map'] = r["locations"][0]["sourceMap"]
# report['severity'] = r["severity"]
# report['swc_id'] = r["swcID"]
# report['swc_title'] = r["swcTitle"]
# report['summary'] = r["description"]["head"]
# report['detail'] = r["description"]["tail"]

# output = template.render(h1 = report['source_type'], descr = report['source_format'])
# print(output)