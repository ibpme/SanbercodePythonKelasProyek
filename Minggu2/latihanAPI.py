from urllib.request import urlopen
import json 

response = urlopen("https://api.covid19api.com/country/indonesia/status/confirmed?from=2020-07-01T00:00:00Z&to=2020-12-01T00:00:00Z")

def get_confirmed_cases(country):
    cases=[]
    response = urlopen(f"https://api.covid19api.com/country/{country}/status/confirmed?from=2020-07-01T00:00:00Z&to=2020-12-01T00:00:00Z")
    raw_data = json.load(response)
    for data in raw_data :
        cases.append(int(data['Cases']))
    return cases

indonesia_cases = get_confirmed_cases("indonesia")
germany_cases = get_confirmed_cases("germany")
india_cases = get_confirmed_cases("india")



    
