
from django.shortcuts import render,redirect

from django.contrib import messages

import pandas,json
# Create your views here.

def home(request):

    return render(request,'home.html')

def task(request):
    

    return render(request,'task.html')


def data(request):
    fName=request.user 
    #print(fName)
    file=open(f'{fName}.csv','r')
    df=pandas.read_csv(file)
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    #print(data)
    context = {"page_obj": data}

        

    return render(request,'data.html',context)
