from django.shortcuts import render, redirect, get_object_or_404
from .forms import RagaForm
from .models import Raga, Song, Varnam, Comparisons, DoItYourself


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
    ragas = Raga.objects.all().order_by('name')
    if not ragas.exists():
        context = {'message': 'There are no ragas yet.'}
    else:
        context = {'ragas': ragas}
    return render(request, 'ragas.html', context)
    
def raga_detail(request, name):
    # Get the raga by name
    raga = get_object_or_404(Raga, name__iexact=name)

    next_raga = Raga.objects.filter(name__gt=raga.name).order_by('name').first()
    prev_raga = Raga.objects.filter(name__lt=raga.name).order_by('-name').first()

    return render(request, 'raga_detail.html', {
        'raga': raga,
        'next_raga': next_raga,
        'prev_raga': prev_raga,
    })



def AllSongs(request):
    songs = Song.objects.all().order_by('name')
    if not songs.exists():
        context = {'message': 'There are no songs yet.'}
    else:
        context = {'songs': songs}
    return render(request, 'songs.html', context)

def song_detail(request, name):
    
    song = get_object_or_404(Song, name__iexact=name)

    next_song = Song.objects.filter(name__gt=song.name).order_by('name').first()
    prev_song = Song.objects.filter(name__lt=song.name).order_by('-name').first()

    return render(request, 'song_detail.html', {
        'song': song,
        'next_song': next_song,
        'prev_song': prev_song,
        })

def AllVarnams(request):
    varnams = Varnam.objects.all().order_by('name')
    if not varnams.exists():
        context = {'message': 'There are no varnams yet.'}
    else:
        context = {'varnams': varnams}
    return render(request, 'varnams.html', context)

def varnam_detail(request, name):
    
    varnam = get_object_or_404(Varnam, name__iexact=name)

    next_varnam = Varnam.objects.filter(name__gt=varnam.name).order_by('name').first()
    prev_varnam = Varnam.objects.filter(name__lt=varnam.name).order_by('-name').first()

    return render(request, 'varnam_detail.html', {
        'varnam': varnam,
        'next_varnam': next_varnam,
        'prev_varnam': prev_varnam,
        })  

def AllComparisons(request):
    comparisons = Comparisons.objects.all()
    if not comparisons.exists():
        context = {'message': 'There are no comparisons yet.'}
    else:
        context = {'comparisons': comparisons}
    return render(request, 'comparisons.html', context)

def AllDoItYourself(request):
    do_it_yourself = DoItYourself.objects.all()
    if not do_it_yourself.exists():
        context = {'message': 'There are no do it yourself yet.'}
    else:
        context = {'diys': do_it_yourself}
    return render(request, 'diy.html', context)

def diy_detail(request, name):
    do_it_yourself = get_object_or_404(DoItYourself, name=name)
    
    parts = do_it_yourself.name.rsplit(' ', 1)
    
    if len(parts) == 2:
        heading = f"{parts[0]} swara sthanas {parts[1]}"
    else:
        heading = do_it_yourself.name

    question1_answer = do_it_yourself.question1_answer
    question2_answer = do_it_yourself.question2_answer
    question3_answer = do_it_yourself.question3_answer      
    
    return render(request, 'diy_detail.html', {
        'do_it_yourself': do_it_yourself, 
        'heading': heading,
        'question1_answer': question1_answer,
        'question2_answer': question2_answer,
        'question3_answer': question3_answer
        })