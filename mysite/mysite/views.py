# i have created this file
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("About is written in website url at end point")

def navigator(request):
    return HttpResponse('''<h1>Personal Navigator</h1>
                        <a href="https://replit.com/@ajaygogavale101/python-tutorial#main.py"> Replet </a><br>
                        <a href="https://www.hackerrank.com/dashboard"> Hackerrank </a><br>
                        <a href="https://chatgpt.com/"> Chatgpt </a>''')

def removepunc(request):
    return HttpResponse("Remove Punc ")

def capitalizefirst(request):
    return HttpResponse("capitalize first <a href='/'>back</a>") # back button added

def newlineremove(request):
    return HttpResponse("new line remove")

def spaceremove(request):
    return HttpResponse("space remove")

def charcount(request):
    return HttpResponse("char count")

#exeresize 1 
def exe1(request):
    nav = '''
            
            <h1>Home</h1>
    
             <li><a href="removepunc">Remove Punctuation <a href='/'>back</a> </a></li>
             <li><a href="capitalizefirst">Capitalization</a></li>
             <li><a href="newlineremove">New Line Remover</a></li>
             <li><a href="spaceremove">Space Remover</a></li>
             <li><a href="charcount">Character Counter</a></li>
                       '''
    return HttpResponse(nav)

#template
from django.shortcuts import render

def ind23(request):
    params={'name':'harry','place':'mars'}#add dict using this function
    return render (request,'index.html',params)

# creating homepage
def ind111(request):
    return render (request,'index.html')

# def removepunc111(request):
#     # print(request.GET.get('text','default')) #if write something in text box then this will print
#     #if dont write text box then this will print default
#     djtext=request.GET.get('text','default')
#     print(djtext) # o/p -> written text shown
#     #return HttpResponse("Remove punc <a href='/'>back</a>")
#     return HttpResponse("Remove punc ")
def analyze111(request):
    # get the text
    # dtext=request.GET.get('text','Default')
    dtext=request.POST.get('text','Default') # use for privacy
    #chekbox values
    # removepunc=request.GET.get('removepunc','off')
    # fullcaps=request.GET.get("fullcaps",'off')
    # newlineremover=request.GET.get("newlineremover",'off')
    # extraspaceremover=request.GET.get("extraspaceremover",'off')
    # charactercounter=request.GET.get("charactercounter",'off')

    # for security reason all get post converted into post request for use url=index2.html only 
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get("fullcaps",'off')
    newlineremover=request.POST.get("newlineremover",'off')
    extraspaceremover=request.POST.get("extraspaceremover",'off')
    charactercounter=request.POST.get("charactercounter",'off')
    print(removepunc)
    print(dtext)

#check which chekbox on /////////////////////////////////////
    if removepunc=='on':
       punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
       analyzed=''
       for char in dtext:
          if char not in punctuations:
              analyzed=analyzed+char
       params={'purpose':'Removing punctuations','analyzed_text':analyzed}
       #analyzed the text
       return render(request,'analyze.html',params)
    # else:
    #     return HttpResponse ("error") for sinle check box run only
   
#check which chekbox on /////////////////////////////////////
    elif(fullcaps=="on"):
        analyzed=""
        for char in dtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to UPPERCASE','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
#check which chekbox on /////////////////////////////////////    
    elif(newlineremover=='on'):
       analyzed=''
       for char in dtext:
          if char != "\n" and char!="\r":
              analyzed=analyzed+char
       params={'purpose':'Removed New Line','analyzed_text':analyzed}
       #analyzed the text
       return render(request,'analyze.html',params)
    
#check which chekbox on /////////////////////////////////////    
    elif(extraspaceremover=='on'):
       analyzed=''
       for index, char in enumerate (dtext):
           if not (dtext[index] == " " and dtext[index+1] == " "):
              analyzed=analyzed+char
        # or  if dtext == " " and dtext[index+1] == " ":
        #       pass
        #   else:
        #       analyzed=analyzed+char
       params={'purpose':'Extra spaces removed..','analyzed_text':analyzed}
       #analyzed the text
       return render(request,'analyze.html',params)

#check which chekbox on /////////////////////////////////////   
    elif charactercounter=='on':
        analyzed=''
        count=0
        for char in dtext:
            if char.isalpha():
                count=count+1
                analyzed=count
        params={'purpose':'Character Count','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    
    else:
        return HttpResponse ("error")
    
#bootstrap website index...
def index2(request):
    return render(request,'index2.html')


    
