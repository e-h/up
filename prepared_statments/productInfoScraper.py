import urllib2
import json as simplejson
import random
import websql as db

productIds = []
apiKeys = ["ef236b29aaf1de879f1167a295b36ddb"]

file = open("productIds3.txt", "r")
for line in file:
	productIds.append(line.strip())
print productIds
file.close()