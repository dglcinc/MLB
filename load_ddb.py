from __future__ import print_function # Python 2/3 compatibility
import boto3, random, csv, tqdm, time, botocore, uuid
import json, decimal, collections, sys

if len(sys.argv) != 5:
	print("program to load a json file to a DynamoDB table")
	print("usage: ", sys.argv[0], "file tablename gen-uid[true|false] parse-only[parse|load]")
	sys.exit()
filename = sys.argv[1]
gen_uid = sys.argv[3]
parse_only = sys.argv[4]
db_r = boto3.resource('dynamodb')
table = db_r.Table(sys.argv[2])

with open(filename) as json_file:
    items = json.load(json_file,object_pairs_hook=collections.OrderedDict)
    for item in items:
	nb = collections.OrderedDict({})
        if gen_uid == 'true':
		nb['uid'] = str(uuid.uuid1())
	for attr in item:
		nb[attr] = item[attr]

        print("Adding to table(", sys.argv[2], ") item:", nb)

	if parse_only == 'load':
        	table.put_item(Item=nb)
