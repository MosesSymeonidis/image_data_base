# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from uploader.forms import UploadFileForm, QueryFileForm
from uploader.models import Pictures
from histEx import histogram
from django.db import connection
import StringIO
import cv2
from PIL import Image
import numpy as np
#from uploader.models import Document
from saveImage import saveImage

def list(request):
    # Handle file upload

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for afile in request.FILES.getlist('file'):
                color,texture=histogram(afile)
                b=Pictures(str(afile),str(tuple(color)),str(tuple(texture)),afile)
                b.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('uploader.views.list'))
    else:
        form = UploadFileForm() # A empty, unbound form

    # Load documents for the list page
    #documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'uploader/list.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def query(request):
    # Handle file upload
    if request.method == 'POST':
        form = QueryFileForm(request.POST, request.FILES)
        if form.is_valid():

            numofresults=request.POST['text']

            megaColor=[0]*343
            megaTexture=[0]*343
            totalFiles=0
            print(1)

            for afile in request.FILES.getlist('file'):

                color,texture = histogram(afile)
                totalFiles+=1
                for i in range(0,343):
                    megaColor[i]+=color[i]
                    megaTexture[i]+=texture[i]
               # b.histogram=str(tuple(hist))
               # b.save()

            megaColor=[el/float(totalFiles) for el in megaColor]
            megaTexture=[el/float(totalFiles) for el in megaTexture]
            megaColor=tuple(megaColor)
            megaTexture=tuple(megaTexture)
            numofresults=int(numofresults)
            cursor=connection.cursor()
            if (Pictures.objects.count()<numofresults):
                numofresults=Pictures.objects.count()
            arxiko = 'select * from "Pictures" order by image_distance("color",\''
            mesaio='\', "texture", \''
            teliko = '\',0.5) limit '+str(numofresults)

            query = arxiko +str(megaColor)+ mesaio+str(megaTexture)+teliko

            print(query)
            cursor.execute(query)

            filelist = cursor.fetchall()

            # Redirect to the document query after POST
            #return HttpResponseRedirect(reverse('uploader.views.results'), filelist)
            return render_to_response(
                 'uploader/results.html',
                 {'filelist': filelist},
                  context_instance=RequestContext(request)
             )
    else:
        form = UploadFileForm()

    # Render list page with the documents and the form
    return render_to_response(
        'uploader/query.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def results(request):
    a = 0
    return HttpResponseRedirect(reverse('uploader.views.results'))

