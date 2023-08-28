"""
This script is made to convert json format to html form data and be used to test if the end point doesn't distinguish between json and form data. This might be expanded to convert to other formats like GET parameters
"""

import sys,json

input = open(sys.argv[1])
ijson = json.loads(input.read())
output = ''
for key in ijson:
	output += '&'+str(key)+'='+str(ijson[key])
output = output[1:]
print(output)
