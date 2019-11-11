from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm): #내부적으로 class meta를 가지고 있음
    class Meta:
        model = GuessNumbers #moedel.py에서 불러오는 것
        fields = ('name', 'text', ) # 5개의 열 중 어떤걸 받을 건지 결정
