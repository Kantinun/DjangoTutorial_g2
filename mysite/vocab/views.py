from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Vocab, Definition


def index(request):
    context = {'vocabList': Vocab.objects.all().order_by('vocab_text')}
    return render(request,"vocab/index.html",context)

def detail(request, vocab_id):
    vocab = get_object_or_404(Vocab,pk=vocab_id)
    context = {'vocab':vocab}
    return render(request,"vocab/detail.html",context)

def addWordPage(request):
    return render(request,"vocab/form.html")

def addWord(request):
    forbiddenList = [""]
    for i in range(1,201):
        forbiddenList.append(" "*i)
    vocabText = []
    for tmp in Vocab.objects.all():
        vocabText.append(tmp.vocab_text)
    if request.POST.get('vocab') not in forbiddenList and  request.POST.get('def') not in forbiddenList :
        if request.POST.get('vocab') not in vocabText:
            word = Vocab(vocab_text = request.POST.get('vocab'))
            defi = Definition(def_text= request.POST.get('def'), vocab = word)
            word.save()
            defi.save()
            context = {'vocabList': Vocab.objects.all().order_by('vocab_text')}
            return render(request,"vocab/index.html",context)
        else:
            defList = []
            for tmp in Definition.objects.all():
                defList.append(tmp.def_text)
            if request.POST.get('def') not in defList:
                defi = Definition(def_text= request.POST.get('def'), vocab = Vocab.objects.filter(vocab_text = request.POST.get('vocab'))[0])
                defi.save()
                context = {'vocabList': Vocab.objects.all().order_by('vocab_text')}
                return render(request,"vocab/index.html",context)
            else:
                return HttpResponse("ความหมายนี้ถูกเพิ่มแล้ว>=<")
    return HttpResponse("Please Enter Vocab or Definition")

def search(request):
    word = request.POST.get('searchword')
    if word == "":
        return index(request)
    else:
        context = {'vocabList': Vocab.objects.filter(vocab_text = word)}
        return render(request,"vocab/index.html",context) 
    