from biisis.models import Biisi
from django.http import Http404

from django.http import HttpResponse
from django.shortcuts import render,  redirect, get_object_or_404
from django.template import RequestContext, loader

def index(request):
    biisis = Biisi.objects.all()
    context = {'biisis': biisis}
    return render(request, 'biisis/index.html', context)

def detail(request, biisi_id):
    try:
        biisi = Biisi.objects.get(pk=biisi_id)
        splittaus = biisi.soinnut.split(', ')
    except Biisi.DoesNotExist:
        raise Http404
    return render(request, 'biisis/detail.html', {'biisi': biisi, 'splittaus': splittaus})

def create_biisi(request):
    new = Biisi(nimi="default nimi", esittaja="default esittaja", soinnut="default soinnut")
    esittaja = request.GET['esittaja']
    nimi = request.GET['nimi']
    soinnut = request.GET['soinnut']
    linkki = request.GET['linkki']
    new.esittaja = esittaja
    new.nimi = nimi
    new.soinnut = soinnut
    new.linkki = linkki
    new.save()

    return redirect('/biisis')

def change_laji(request, biisi_id):
    b = get_object_or_404(Biisi, pk=biisi_id)
    aste = request.GET['aste']
    splitit = b.soinnut.split(', ')
    kaikki = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
    uudetsoinnut = ""
    pituus = len(splitit)
    i = 0
    for sointu in splitit:
        i = i + 1
        if sointu.find("m") != -1:
            mollipois = sointu.replace("m", "")
            m_oli = 1
        else:
            mollipois = sointu
            m_oli = 0
        indeksi = kaikki.index(mollipois)
        kokonais = indeksi + int(aste)
        uusi = kokonais % 12
        uusisointu = kaikki[uusi]
        if m_oli == 1:
            uusisointu = uusisointu + "m"
        uudetsoinnut += uusisointu
        if i != pituus:
            uudetsoinnut += ", "
    b.soinnut = uudetsoinnut
    b.save()
    #splittaus = b.soinnut.split(', ')
    return redirect('/biisis/' + str(b.id))
    




    
    