import requests
import json
import csv
import time

#parameters to pass into Google Custom Search JSON API



parameters = {
    "cx" : "c6e3001bf986f4943",
    "exactTerms" : "high energy physics particle accelerator",
    "start" : "1"

}

#Loop to repeatedly call API obtaining top 100 search results
for i in range(1,100,10):
    for key, value in parameters.items():
        if key == 'start':
            parameters[key] =str(i)
    #print(parameters)
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
    fileName = 'output_csv/high_energy_physics_particle_accelerator.csv'

    #writing to csv file ignoring keys not appearing in fields
    with open(fileName, mode = 'a', newline='', encoding='utf-8') as accelerator_review:
        accWriter = csv.DictWriter(accelerator_review, fieldnames=fields, extrasaction='ignore')
        if i == 1:
            accWriter.writeheader()
        accWriter.writerows(lay1) 
    time.sleep(1)

    


       
