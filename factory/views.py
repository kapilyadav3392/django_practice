from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from factory.models import data, detail, user
# from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def form(request):
    
    if request.method=="POST":
        name1=request.POST['name']
        bd1=request.POST['Birthdate']
        img=request.FILES['avatar']
        # print(img)
        
        a=data(name=name1,Birthdate=bd1,image=img)
        a.save()
        if a : 
            return redirect('/table/')
    return render (request,'form.html')

def table(request):
    if request.session.get('username'):
        b=data.objects.all()
        # print(b)

        return render (request,'table.html',{'result':b})
    else:
        return redirect('/login')


def delete(request,userid):
    n=data.objects.get(id=userid).delete()
    if(n):
        return redirect('/table')
    
    
    return render (request, 'delete.html')



def update(request,userid):
    u=data.objects.get(id=userid)
    if request.method=="POST":
        name=request.POST['name']
        birthday=request.POST['Birthday']
        img=request.FILES['avatar']

        
        u.name=name
        u.Birthdate=birthday
        u.image=img
        u.save()
        return redirect ('/table')
    return render (request,'update.html',{'result':u})



def signup(request):
    if request.method=="POST":
        username1=request.POST['username']
        name1=request.POST['name']
        password1=request.POST['password']
        
        
        s=user(username=username1,name=name1, password=password1)
        s.save()
        if s:
            return redirect('/login/')
    return render (request,'signup.html')


def login(request):

    
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        try:
      
            fetch = user.objects.get(username =  username2)
       
        
            if(fetch):
           
            
                if (fetch.password== password2):
                    request.session['username']=username2
                    return redirect('/table')
                else:
                    return HttpResponse("wrong pass")
            
        
        except Exception:
            return HttpResponse("wrong user")
       
    return render (request , 'login.html')


def logout(request):
    # z=logout(request)
    del request.session['username']
    if('username' not in request.session):
        return redirect ('/login')

    return render (request,'logout.html')


def details(request,datid):
    # dataid= data.objects.get(id=request['dataid'])
    if datid:
        data1=detail.objects.filter(dataid=datid)
        print(data1)
        # showdetails=detail.objects.all()

        

    return render (request,'details.html',{'data':data1})
        
    
    
        