from django import http
from django.http import HttpResponse
from django.shortcuts import render
 
def home(request):
    return render(request,'home.html')


def analyse(request):
# Get the text
    text=request.POST.get('text','default')
#Check the check Box values
    removepunc=request.POST.get("removepun","off")
    capitaliz=request.POST.get("capitalize","off")
    newline=request.POST.get("newline","off")
    extraspace=request.POST.get("extraspace","off")
    charcount=request.POST.get("charcount","off")
# Check if all the checkbox are off
 
# Check which check box is on
    if (removepunc=="on") :
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyse=""
        for char in text:
            if char not in punctuation:
                analyse=analyse+char
        context={'letter': analyse}
        text=analyse
        
  
    if capitaliz=="on":
        analyse=""
        for char in text:
            analyse=analyse+char.upper()
        context={'letter': analyse}
        text=analyse
            

    if(newline=="on"):
        text=text.replace("\r\n"," ").replace("\n"," ")
        analyse=""
        for char in text:
            if char!="\n":
                analyse=analyse+char
        context={'letter': analyse}
        text=analyse
        

    if(extraspace=="on"):
        analyse=""
        for index,char in enumerate(text):
            if not (text[index]==" " and text[index+1]==" "  ):
              analyse=analyse+char
        context={'letter': analyse,}
        text=analyse


    if(charcount=="on"):
        analyse=""
        for char in text:
            analyse=analyse+char
            analysed=len(analyse)
        context={'count': analysed,"letter":analyse,"def":"Number of character in the given string is :"}
      
    if  (charcount!="on" and extraspace!="on" and removepunc!="on" and capitaliz!="on" and newline!="on"):
        return HttpResponse("""<h3> You havent choosen any option ....</h3>
        <a  href="/">HomePage</a>""")
   
    return render(request,'analyse.html',context)

