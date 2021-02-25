from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Vocab, Definition


def index(request):# เเสดงหน้าคำศัพท์ทั้งหมด
    context = {'vocabList': Vocab.objects.all().order_by('vocab_text')}
    return render(request,"vocab/index.html",context)

def detail(request, vocab_id): # เเสดงหน้าคำที่เราเลือกพร้อมคำแปล
    vocab = get_object_or_404(Vocab,pk=vocab_id)
    context = {'vocab':vocab}
    return render(request,"vocab/detail.html",context)

def addWordPage(request): # เปิดหน้า addword เพื่อเพิ่มคำศัพท์
    return render(request,"vocab/form.html")    

def addWord(request):
    forbiddenList = [""]    #ป้องกันการเพิ่มคำศัพท์โดยที่ไม่ป้อนข้อมูล
    for i in range(1,201):
        forbiddenList.append(" "*i) #ป้องกันการเพิ่มคำศัพท์โดยที่ป้อนข้อมูลโดยการกด spacebar
    vocabText = []  
    for tmp in Vocab.objects.all():
        vocabText.append(tmp.vocab_text)    #เก็บคำศัพท์เคยเพิ่มแล้ว
    if request.POST.get('vocab') not in forbiddenList and  request.POST.get('def') not in forbiddenList:   #ถ้าไม่ป้อนข้อมูลโดยการกด spacebar หรือเว้นว่าง
        if request.POST.get('vocab') not in vocabText:  #ถ้าคำศัพท์นี้ยังไม่เคยถูกเพิ่ม
            word = Vocab(vocab_text = request.POST.get('vocab'))    #เพิ่มคำศัพท์
            defi = Definition(def_text= request.POST.get('def'), vocab = word) #เพิ่มความหมายให้กับคำศัพท์
            word.save() # เพิ่มศัพท์ลงฐานข้อมูล
            defi.save() # บันทึกลง database
            context = {'vocabList': Vocab.objects.all().order_by('vocab_text')}
            return render(request,"vocab/index.html",context)
        else: # ถ้าคำศัพท์นี้เคยถูกเพิ่มแล้ว
            defList = []    
            for tmp in Definition.objects.all():
                defList.append(tmp.def_text)    # เก็บความหมายที่เคยเพิ่มแล้ว
            if request.POST.get('def') not in defList: # ถ้าหากความหมายไม่มีคำซ้ำ
                defi = Definition(def_text= request.POST.get('def'), vocab = Vocab.objects.filter(vocab_text = request.POST.get('vocab'))[0])#เพิ่มความหมาย
                defi.save()# นำความหมายลงฐานข้อมูล
                context = {'vocabList': Vocab.objects.all().order_by('vocab_text')}
                return render(request,"vocab/index.html",context)
            else:
                return HttpResponse("ความหมายนี้ถูกเพิ่มแล้ว>=<")
    return HttpResponse("Please Enter Vocab or Definition")

def search(request): # ค้นหาคำที่เราต้องการ
    word = request.POST.get('searchword')
    if word == "": #ถ้าไม่ได้ใส่คำลงช่อง search
        return index(request)
    else:
        context = {'vocabList': Vocab.objects.filter(vocab_text = word)}
        return render(request,"vocab/index.html",context) 
    