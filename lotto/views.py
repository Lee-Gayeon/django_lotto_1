from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all() # DB에 저장된 GuessNumbers 객체 모두를 가져온다.
    ## site_!\lotto\templates\lotto\deault.html
    return render(request, 'lotto/default.html', {'lottos':lottos}) # {}에 데이터를 넣어줄 것, 그 데이터를 재활용 가능, 'lottos'는 key값, <p>{{ lottos }}</p>에 대

    # html 만들고 보여주기,
    ## html 파일은 site_!\lotto\templates\lotto\deault.html -> 나중에 웹서버에 올릴 때 templates라는 하나의 폴더에
    ## 다 모아야 하므로 새로운 폴더를 하나 더 만드는 것
    ## site_!\lotto\static

    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음

    # return HttpResponse('<h1>Hello, world! </h1>')

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):
    if request.method == "POST":
        # 사용자로부터 넘겨져 온 POST 요청 데이터를 담아 PostForm 객체 생성
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False) # DB 저장은 아래 generate 함수의 .save()로 처리
            lotto.generate()
            return redirect('index') # urls.py의 name='index'에 해당
            # -> 상단 from django.shortcuts import render, redirect 수정
    else:
        form = PostForm()
        return render(request, "lotto/form.html", {"form": form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})
    
