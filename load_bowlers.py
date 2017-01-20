from __future__ import print_function # Python 2/3 compatibility
import boto3, random, csv, tqdm, time, botocore, uuid
import json, decimal, collections, sys

if len(sys.argv) != 3:
	print("program to load a json file to a DynamoDB table")
	print("usage: ", sys.argv[0], "file tablename")
	sys.exit()
db_r = boto3.resource('dynamodb')
table = db_r.Table(sys.argv[2])

with open(sys.argv[1]) as json_file:
    items = json.load(json_file,object_pairs_hook=collections.OrderedDict)
    for item in items:
	nb = {}
        nb['uid'] = str(uuid.uuid1())
	for attr in item:
		nb[attr] = item[attr]

        print("Adding to table(", sys.argv[2], ") item:", item)

#        table.put_item(nb)
