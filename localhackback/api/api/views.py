from django.shortcuts import render, HttpResponse
# Create your views here.
import json
import pandas as pd
from .models import Day


def cases(request):
    df = pd.read_csv('/home/artur/Desktop/Local_Hack_files/Local_Hack/Cases.csv')
    data = {}
    for col in df.columns:
        if 'Unnamed' not in col:
            data[col] = []
            for i in range(len(df)):
                data[col].append({'time': df['Unnamed: 0'][i], 'cases': int(df[col][i])})
    return HttpResponse(json.dumps(data), status=200)


def deaths(request):
    df = pd.read_csv('/home/artur/Desktop/Local_Hack_files/Local_Hack/Deaths.csv' )
    data = {}
    for col in df.columns:
        if 'Unnamed' not in col:
            data[col] = []
            for i in range(len(df)):
                data[col].append({'time': df['Unnamed: 0'][i], 'cases': int(df[col][i])})
    return HttpResponse(json.dumps(data), status=200)


def recoveries(request):
    df = pd.read_csv('/home/artur/Desktop/Local_Hack_files/Local_Hack/Recovery.csv')
    data = {}
    for col in df.columns:
        if 'Unnamed' not in col:
            data[col] = []
            for i in range(len(df)):
                data[col].append({'time': df['Unnamed: 0'][i], 'cases': int(df[col][i])})
    return HttpResponse(json.dumps(data), status=200)

def graph(request,day_id):
    country_name = get_object_or_404(Day, pk=day_id)
    countries = Day.objects.all().filter(name=country_name)
    for i in countries:
        print(i.deaths,i.recoveries,i.cases)

def index(request):
    return render(request, 'index.html')

#
# def bd(request):
#     recoveries = pd.read_csv('C:\\Users\\hp\\Downloads\\recovery.csv')
#     cases = pd.read_csv('C:\\Users\\hp\\Downloads\\cases.csv')
#     deaths = pd.read_csv('C:\\Users\\hp\\Downloads\\deaths.csv')
#     for i in range(len(recoveries)):
#         for col in recoveries.columns:
#             if 'Unnamed' not in col:
#                 a = Day()
#                 a.name = col
#                 a.cases = cases[col][i]
#                 a.deaths = deaths[col][i]
#                 a.recoveries = recoveries[col][i]
#                 a.date = cases['Unnamed: 0'][i]
#                 a.save()
