from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def analyze(request):
    text=request.POST.get('text', 'default')
    
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')


    if removepunc =='on':
        punctuations='''!{[}]\|@#$%^&*()_=+;:'"/?.>,<`~'''
        res=""
        for char in text:
            if char not in punctuations:
                res=res+char
        sakib={'purpose':'removepunctuations', 'analyzed_text': res}
        text=res
        
    if fullcaps =='on':
        res=""
        for char in text:
            res=res+char.upper()
        sakib={'purpose':'All Capitals', 'analyzed_text': res}
        text=res
        
    if newlineremover =='on':
        res=""
        for char in text:
            if char !='\n' and char !='\r':
                res=res+char
        sakib={'purpose':'newlineremover', 'analyzed_text': res}
        text=res
        
    if spaceremover =='on':
        res=""
        for index,char in enumerate(text):
            if not(text[index]==" " and text[index+1]==" "):
                res=res+char
        sakib={'purpose':'spaceremover', 'analyzed_text': res}
        text=res

    if charcount =='on':
        res=0
        for char in text:
            if char !=" ":
                res=res+1
        writetext=f'Total no. of char = {res}'
        sakib={'purpose':'charcount', 'analyzed_text': writetext}
        
    if charcount =='off' and spaceremover =='off' and newlineremover =='off' and fullcaps =='off' and removepunc =='off':
        return HttpResponse("Please Select Atleast One Option.")

    return render(request,'analyze.html',sakib)
    