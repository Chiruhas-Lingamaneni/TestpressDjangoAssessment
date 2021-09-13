from django.shortcuts import render,redirect
from user_app.forms import CreateUserForm
from django.contrib.auth import authenticate,login
from user_app.models import QuestionsList, UserResponse,ResponseList
from django.contrib.auth.models import User
from testapp.models import Questions,Answers
from django.contrib.auth.decorators import login_required
# Create your views here.
def registerpage(request):
    form=CreateUserForm()
    registered=False
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            registered=True

    context={'form':form,'registered':registered}
    return render(request,'user_app/register.html',context)

def loginpage(request):
    cradestials=False
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user =authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/school/')
        else:
            cradestials=True
    return render(request,'user_app/login.html',{'cradentials':cradestials})

def homepage(request):
    return render(request,'user_app/home.html')

@login_required
def responsesave(request,quizid,questionid,anslist,score,result,time):
    userlist=UserResponse(username=request.user,quizid=quizid,score=score,timetaken=time,
                           result=result )
    userlist.save()
    for i,j in enumerate(questionid):
        uresponse=QuestionsList(questionid=j,quizname=userlist)
        uresponse.save()
        for mark in anslist[i]:
            response=ResponseList(answerid=mark,questionname=uresponse)
            response.save()
        
    
    #p = Person(name="Fred Flintstone", shirt_size="L")
    # p.save()

def uresponse(request):
    return render(request,'user_app/response.html')
@login_required
def userresponse(request):
    a=User.objects.get(username=request.user)
    return render(request,'user_app/userresponse_list.html',{'object_list':a})
@login_required
def detailans(request,pk):
    a=User.objects.get(username=request.user)

    questions=Questions.objects.all()
    options=Answers.objects.all()
    qlist,alist=[],[]
    for x in a.usermodel.all()[pk].getuserresponse():
        qlist.append(Questions.objects.get(id=x.questionid))
        temp=[]
        for y in x.getquestionlist():
            temp.append(Answers.objects.get(id=y.answerid).option)
        alist.append(temp)

    qlist=list(zip(qlist,alist)) 
    objectlist={'questions':qlist}
    return render(request,"user_app/detailans.html",objectlist)