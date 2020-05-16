from django.shortcuts import render
from .models import Origin
import requests
# Create your views here.
def Welcome(request):
    return render(request,'CoronaWeb/Welcome.html')


def Symptoms(request):
    return render(request,'CoronaWeb/symptoms.html')



def origin(request):
    my_obj = Origin.objects.all()
    my_dict = {'data':my_obj}
    return render(request,'CoronaWeb/Origin.html',my_dict)


def figures(request):
    url = "https://covid-19-data.p.rapidapi.com/totals"
    querystring = {"format":"undefined"}
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "0afbcbdfa3mshb239ddddf311962p17ef70jsnc23948e229e7"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_obj=response.json()
    confirm=json_obj[0]["confirmed"]
    recovered=json_obj[0]["recovered"]
    critical=json_obj[0]["critical"]
    death=json_obj[0]["deaths"]

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    querystring = {"country":"India"}
    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "0afbcbdfa3mshb239ddddf311962p17ef70jsnc23948e229e7"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_obj=response.json()
    confirmedC=json_obj["data"]["covid19Stats"][0]["confirmed"]
    deathC=json_obj["data"]["covid19Stats"][0]["deaths"]
    recoveredC=json_obj["data"]["covid19Stats"][0]["recovered"]
    my_dict={'confirm':confirm,'recovered':recovered,'critical':critical,'death':death,'confirmc':confirmedC,'recoveredC':recoveredC,'deathC':deathC}
    return render(request,'CoronaWeb/Data.html',my_dict)
