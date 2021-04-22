from django.shortcuts import render,redirect
import pickle
import os
from . models import Prediction

def index(request):
    # res=Prediction.objects.all()
    return render(request, "index.html")

def test(request):
    ppw=int(request.POST['ppw'])
    pn=int(request.POST['pn'])
    mi=int(request.POST['mi'])
    appw=int(request.POST['appw'])
    modulepath=os.path.dirname(__file__)
    path=os.path.join(modulepath,'taxi.pkl')
    model=pickle.load(open(path,'rb'))
    res=str(model.predict([[ppw,pn,mi,appw]])[0].round(2))
    pre=Prediction(ppw=str(ppw),pn=str(pn),mi=str(mi),appm=str(appw),result=res)
    pre.save()
    return render(request,'index.html',{'res':res})
# Create your views here.
