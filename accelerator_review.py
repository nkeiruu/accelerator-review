import requests
import json
import csv

#parameters to pass into Google Custom Search JSON API

start_indices= [1,11,21,31,41,51,61,71,81,91]

parameters = {
    "cx" : "c6e3001bf986f4943",
    "exactTerms" : "electrostatic accelerators",
    "start" : "1"

}



#To Do: get top 100 results(might have to write script)

#API request
search_results = requests.get("https://customsearch.googleapis.com/customsearch/v1?key=AIzaSyCyiQ9vR0zdfOOfvKh7NPenIq47CrO45FI", params=parameters)

#Visually appealing/formatted json results
formatted = json.dumps(search_results.json(), indent=4, sort_keys=True)
#print(formatted)
print ("Status code", search_results.status_code)

search_dict = search_results.json()

#Subdictionary with relevant terms
lay1 = search_dict["items"]

#accessing the required info in the search Response object
#i.e. title 
#for i in range(len(lay1)):
    #print(lay1[i]["title"]) 



fields = ['title', 'link', "snippet"] 
fileName = 'output_csv/electrostatic_accelerator.csv'

#writing to csv file ignoring keys not appearing in fields
with open(fileName, mode = 'a', newline='') as accelerator_review:
    accWriter = csv.DictWriter(accelerator_review, fieldnames=fields, extrasaction='ignore')
    #accWriter.writeheader()
    accWriter.writerows(lay1) 
       
