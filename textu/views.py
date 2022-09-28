from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index2.html')
def analyze(request):
    txt=request.POST.get('text','default')
    removep=request.POST.get('removepunc','off')
    fullcapes=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removep == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char
        param={'purpose':'Removed punctuation','analyzed_text':analyzed}
        txt=analyzed
    if fullcapes == "on":
        analyzed = ""
        for char in txt:
                analyzed = analyzed + char.upper()
        param={'purpose':'upper case sentense','analyzed_text':analyzed}
        txt=analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in txt:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        param={'purpose':'upper case sentense','analyzed_text':analyzed}
        txt=analyzed
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(txt):
            if not(txt[index] == " " and txt[index+1]==" "):
                analyzed = analyzed + char

        param = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    if(removep != "on" and fullcapes != "on" and newlineremover != "on" and extraspaceremover!="on"):
          return HttpResponse("there a error")
    
    return render(request, 'analyze2.html', param)