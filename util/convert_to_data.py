import sys
import json
file_to_convert = str(sys.argv[1])
list_before = open(file_to_convert).read().split("\n")
years = []
minutes = []
combined = {}
for itemset in list_before:
    split_object = itemset.split(",")
    year = split_object[0]
    minute = split_object[1]
    years.append(year)
    minutes.append(minute)
    combined[str(year)] = minute
with open("exported.json", "w+") as out:
    to_export = {"years": years, "minutes": minutes, "data": combined}
    json.dump(to_export, out)
    out.close()