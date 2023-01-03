# user-generated file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request, 'index2.html')

def analyze(request):
    submittedtext= (request.POST.get('submittedtext', 'default'))
    removepunc= (request.POST.get('removepunc', 'off'))
    fullcaps= (request.POST.get('fullcaps', 'off'))
    charcount= (request.POST.get('charcount', 'off'))
    count=0
    
    print(submittedtext)
    print(removepunc)
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=submittedtext
    purpose=""
    
    if removepunc=="on":
        purpose+="Remove Punctuations "
        analyzed=''
        
        for char in submittedtext:
            if char not in punctuations:
                analyzed=analyzed+char
                
    if fullcaps=="on":
        
        purpose+="Capitalize "
        analyzed=analyzed.upper()
        
    if charcount=="on":
        purpose+="Character Count "
        for char in submittedtext:
            count+=1
        
        analyzed+=f' char count {count}'
    
    print(analyzed)
    
    if len(analyzed)==0 and charcount!="on":
        analyzed="Analysis unchecked!"
        submittedtext="None"
    
    params={'purpose': purpose, 'submittedtext': submittedtext, 'analyzedtext': analyzed}
    return render(request, 'analyze.html', params)

