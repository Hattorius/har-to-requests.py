import json

with open('input.har') as f:
    har = json.loads(f.read())

output = open('output.py', 'w+')
output.write("import requests\n\n")

for entry in har['log']['entries']:
    request = entry['request']

    r = 'requests.'
    r += request['method'].lower() + '("'
    r += request['url'] + '"'
    if len(request['headers']) > 0:
        r += ', headers='
        headers = {}
        for header in request['headers']:
            headers[header['name']] = header['value']
        r += str(headers)

    output.write(r + ')\n\n')
