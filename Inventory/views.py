from django.shortcuts import render, redirect, get_object_or_404
from .forms import RagaForm
from .models import Raga

def HomePage(request):

    return render(request, 'home.html')

def AboutPage(request):

    return render(request, 'about.html')

def BlogPage(request):

    return render(request, 'blog.html')

def FaqPage(request):

    return render(request, 'faq.html')

def SpecialPage(request):

    return render(request, 'special.html')

def RagaAdd(request):
    context = {
        'raga_form': RagaForm()
    }

    if request.method == "POST":
        raga_form = RagaForm(request.POST)

        if raga_form.is_valid():
            raga_form.save()
            return redirect('raga_list')  
        else:
            print(raga_form.errors)  

    return render(request, 'raga_add.html', context)
 
def AllRagas(request):
    ragas = Raga.objects.all()
    if not ragas.exists():
        context = {'message': 'There are no ragas yet.'}
    else:
        context = {'ragas': ragas}
    return render(request, 'ragas.html', context)
    
def raga_detail(request, id):
    raga = get_object_or_404(Raga, id=id)
    return render(request, 'raga_detail.html', {'raga': raga})

