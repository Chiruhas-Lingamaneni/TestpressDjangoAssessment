from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectTemplateResponseMixin
from testapp.models import  Quiz
from django.contrib.auth import logout
from user_app.views import responsesave
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
questionno,score=0,0
questionlist,answerlist=[],[]
# Create your views here.

class Index(LoginRequiredMixin ,ListView):
    
    global questionno
    questionno=0
    model=Quiz
class Details(LoginRequiredMixin ,DetailView):
    global questionno
    questionno=0
    context_object_name='test_details'
    model=Quiz
    
    template_name='testapp/test_details.html'

@login_required
def quiz(request,pk):
    global questionno,quiz,starttime,questionlist,question
    
    if questionno==0:
        starttime=time.time()
        quiz=Quiz.objects.get(pk=pk).get_questions()

    if Quiz.objects.get(pk=pk).number_of_questions==questionno:
        stoptime=time.time()
        return(result(request,pk,int(stoptime-starttime)))
    eachquestion=quiz[questionno]
    questionlist.append(eachquestion.id)
    question=eachquestion.question
    options=eachquestion.get_answers()

    questionno+=1
    return render(request,"testapp/quiz.html",{'multy':True,'question':question,'options':options,'pk':pk,'questionno':questionno})

@login_required
def solution(request,pk):
    global quiz,answerlist
    
    if request.method=="POST":
        eachquestion=quiz[questionno-1]
        arr=[]
        result=[]
        temp=list(dict(request.POST.items()).keys())[1:]
        answerlist.append(temp)
        for x in eachquestion.get_answers():
            key=str(x.pk)
            
            if x.correct==True and request.POST.get(key)=='on':
                arr.append(1)
                result.append(1)
            elif x.correct==True:
                arr.append(1)
                result.append(2)
            elif x.correct==False and request.POST.get(key)=='on':
                arr.append(2)
                result.append(2)
            else:
                arr.append(3)
                result.append(3)
        question=eachquestion.question
        options=[]
        for x in eachquestion.get_answers():
            options.append(x.option)
        response(result)
        return render(request,"testapp/solution.html",{'question':question,
                                                    'option0':options[0],'option1':options[1],'option2':options[2],'option3':options[3],
                                                    'arr0':str(arr[0]),'arr1':str(arr[1]),'arr2':str(arr[2]),'arr3':str(arr[3]),
                                                    'pk':pk,})
def response(arr,):
    global score 
    if 1 in arr and 2 not in arr:
        score+=1
@login_required
def result(request,pk,timetaken):
    global score,questionno,questionlist,answerlist
    questionno=0
    yourscore=score
    if yourscore<Quiz.objects.get(pk=pk).score_to_pass:
        text="You did not cleared the test, better luck next time"
    else :
        text="Congrats, you cleared the test"
    responsesave(request,pk,questionlist,answerlist,yourscore,text,timetaken)
    return render(request,"testapp/result.html",{'timetaken':timetaken,'yourscore':yourscore,'scoretopass':Quiz.objects.get(pk=pk).score_to_pass,'text':text})
@login_required
def submession(request):
    return render(request,"testapp/submession.html")
@login_required
def userlogout(request):
    logout(request)
    return redirect('/')