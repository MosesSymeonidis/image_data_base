# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django import forms
from query import querydb
from queryRocchio import rocMeth
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from uploader.models import Pictures
from histEx import histogram
from django import shortcuts


def upload(request):
    # Handle file upload

    if request.method == 'POST':
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            for afile in request.FILES.getlist('file'):
                color, texture = histogram(afile)
                b = Pictures(str(afile), str(tuple(color)), str(tuple(texture)), afile)
                b.save()
                # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('uploader.views.upload'))
    else:
        form = forms.Form() # A empty, unbound form

    return render_to_response(
        'uploader/upload.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def query(request):
    # Handle file upload
    if request.method == 'POST':
        form = forms.Form(request.POST, request.FILES)

        if form.is_valid():

            numofresults = request.POST['text']
            histWeight = request.POST['optionsHist']
            distance = request.POST['optionsDist']

            megaColor = [0] * 512
            megaTexture = [0] * 256
            totalFiles = 0

            for afile in request.FILES.getlist('file'):
                color, texture = histogram(afile)
                totalFiles += 1
                for i in range(0, 512):
                    megaColor[i] += color[i]
                for i in range(0, 256):
                    megaTexture[i] += texture[i]

            megaColor = [el / float(totalFiles) for el in megaColor]
            megaTexture = [el / float(totalFiles) for el in megaTexture]
            megaColor = tuple(megaColor)
            megaTexture = tuple(megaTexture)
            numofresults = int(numofresults)

            if (Pictures.objects.count() < numofresults):
                numofresults = Pictures.objects.count()
            request.session['colorHistogram'] = megaColor
            request.session['textureHistogram'] = megaTexture
            filelist = querydb(distance, histWeight, numofresults, megaColor, megaTexture)
            request.session['filelist'] = filelist

            return HttpResponseRedirect(
                '/results/')


    else:
        form = forms.Form()

    # Render list page with the documents and the form
    return render_to_response(
        'uploader/query.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def results(request):
    try:
        filelist = request.session['filelist']
    except KeyError:
        return shortcuts.redirect('/query/')

    if request.method == 'POST':
        Qdict = request.POST

        files = []

        for file in filelist:
            if Qdict.__contains__(str(file[1])):
                files.append(file)
        numofresults = request.POST['text']

        histWeight = request.POST['optionsHist']
        distance = request.POST['optionsDist']
        if (len(files) != 0):
            megaColor, megaTexture = rocMeth(request.session.get('colorHistogram'),
                                             request.session.get('textureHistogram'), files, 8, 8)
            filelist = querydb(distance, histWeight, numofresults, megaColor, megaTexture)
            request.session['filelist'] = filelist

    return render_to_response('uploader/results.html', {'filelist': filelist}, context_instance=RequestContext(request))
