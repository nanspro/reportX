import json
import os, pprint
from jinja2 import Environment, PackageLoader

pp = pprint.PrettyPrinter(indent=4)
env = Environment(loader=PackageLoader('app', 'templates'))
template = env.get_template('index.html')

root = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(root, 'reports', 'index.html')

# API_ENDPOINT = 'https://api.mythx.io/v1/auth/login'

USERNAME = os.environ['MYTHX_ETH_ADDRESS']
PASS = os.environ['MYTHX_PASSWORD']

# r = requests.post(url = API_ENDPOINT, data = {'ethAddress' : USERNAME, 'password' : PASS})
# response = json.loads(r.text)
# jwtTokens = response["jwtTokens"]

# ACCESS_TOKEN = jwtTokens["access"]
# REFRESH_TOKEN = jwtTokens["refresh"]

# bearer_token = 'Bearer ' + ACCESS_TOKEN
# header = {'Authorization': bearer_token}

# # API_ENDPOINT = 'https://api.mythx.io/v1/analyses'
# # m = requests.get(url = API_ENDPOINT, headers = header)
# # response = json.loads(m.text)
# # pp.pprint(response)

# API_ENDPOINT = 'https://api.mythx.io/v1/analyses/04892277-7197-4a3d-b3fb-dceb6b7ab8ac/issues'
# m = requests.get(url = API_ENDPOINT, headers = header)

with open('1.json', 'r') as f:
    text = f.read()
    text = text.replace("'", '"')
    text = text.replace("None", '""')
    r = json.loads(text)

print(r)
report = {}

# # Preparing data to be presented
report['source_type'] = r["sourceType"]
report['source_format'] = r["sourceFormat"]
report['source_list'] = r["sourceList"]

#meta
if "coveredInstructions" in r["meta"].keys():
    report['n_ins'] = r["meta"]["coveredInstructions"]
if "coveredPaths" in r["meta"].keys():
    report['n_paths'] = r["meta"]["coveredPaths"]
if "selectedCompiler" in r["meta"].keys():
    report['compiler'] = r["meta"]["selectedCompiler"]

#issues
r = r["issues"][0]
report['source_map'] = r["locations"][0]["sourceMap"]
report['severity'] = r["severity"]
report['swc_id'] = r["swcID"]
report['swc_title'] = r["swcTitle"]
report['summary'] = r["description"]["head"]
report['detail'] = r["description"]["tail"]

output = template.render(h1 = report['source_type'], descr = report['source_format'])
print(output)