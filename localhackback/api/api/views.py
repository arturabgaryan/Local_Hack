from django.shortcuts import render, HttpResponse
from django.forms.models import model_to_dict
# Create your views here.
import json
import pandas as pd
from .models import Day


def cases(request):
    df = pd.read_csv('..\..\\Cases.csv')
    data = {}
    obj = Day.objects.all()
    for o in obj:
        if o.name not in data.keys():
            data[o.name] = []
        data[o.name].append({'time': str(o.date), 'cases': o.cases})
    return HttpResponse(json.dumps(data), status=200)


def deaths(request):
    df = pd.read_csv('Deaths.csv')
    data = {}
    for col in df.columns:
        if 'Unnamed' not in col:
            data[col] = []
            for i in range(len(df)):
                data[col].append({'time': df['Unnamed: 0'][i], 'cases': int(df[col][i])})
    return HttpResponse(json.dumps(data), status=200)


def recoveries(request):
    df = pd.read_csv('..\..\\Recovery.csv')
    data = {}
    for col in df.columns:
        if 'Unnamed' not in col:
            data[col] = []
            for i in range(len(df)):
                data[col].append({'time': df['Unnamed: 0'][i], 'cases': int(df[col][i])})
    return HttpResponse(json.dumps(data), status=200)


def index(request):
    return render(request, 'index.html')


#
# def bd(request):
#     recoveries = pd.read_csv('..\..\\Recovery.csv')
#     cases = pd.read_csv('..\..\\Cases.csv')
#     deaths = pd.read_csv('..\..\\Deaths.csv')
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


def graph(request):
    name = request.GET.get('country', None)
    day = request.GET.get('day', None)
    countries = Day.objects.filter(name=name)
    data = []
    for i in range(int(day)):
        data.append({'cases': countries[i].cases, 'deaths': countries[i].deaths, 'recoveries': countries[i].recoveries})

    return HttpResponse(status=200, content=json.dumps(data))


def predict(request):
    df = pd.read_csv('..\..\\predictions.csv')
    cases = df[0:7]
    deaths = df[7:14]
    recoveries = df[14:21]
    data = []
    for i in range(7):
        for col in cases.columns:
            if 'Unnamed' not in col:
                data.append([col, int(cases[col][i]), int(deaths[col][i + 7]), int(recoveries[col][i + 14])])
    return HttpResponse(status=200, content=json.dumps(data))
