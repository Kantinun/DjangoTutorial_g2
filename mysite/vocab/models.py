from django.db import models

class Vocab(models.Model):
    vocab_text = models.CharField(max_length=200)   #คำศัพท์

    def __str__(self):
        return self.vocab_text #แสดงคำศัพท์

class Definition(models.Model):
    def_text = models.CharField(max_length=200) #ความหมาย
    vocab = models.ForeignKey(Vocab, on_delete=models.CASCADE) # เก็บว่าเป็นความหมายของคำศัพท์ใด

    def __str__(self):
        return self.def_text #แสดงคำศัพท์