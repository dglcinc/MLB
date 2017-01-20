from __future__ import print_function # Python 2/3 compatibility
import boto3, random, csv, tqdm, time, botocore, uuid, json, decimal

db_r = boto3.resource('dynamodb')

table = db_r.Table('mlb_bowler')

with open("bowlers.json") as json_file:
    bowlers = json.load(json_file, parse_float = decimal.Decimal)
    for bowler in bowlers:
        uid = str(uuid.uuid1())
        firstname = bowler['firstname']
        lastname = bowler['lastname']
        clubmember = bowler['clubmember']
        team = int(bowler['team'])
        address = bowler['address']
        city = bowler['city']
        state = bowler['state']
        zipcode = bowler['zip']
        cellphone = bowler['cellphone']
        email = bowler['email']
        shirts = bowler['shirts']
        roles = bowler['roles']

        print("Adding bowler:", firstname, lastname)
        print("Adding bowler:", bowler)

        table.put_item(
           Item={
	       'uid': uid,
               'fname': firstname,
               'lastname': lastname,
               'member': clubmember,
               'team': team,
               'addr': address,
               'city': city,
               'st': state,
               'zip': zipcode,
               'cell': cellphone,
               'email': email,
               'shirts': shirts,
               'roles': roles,
            }
        )
