from django.db import connection


def querydb(distance, histWeight, numofresults, megaColor, megaTexture):
    cursor = connection.cursor()
    arxiko = 'select * from "Pictures" order by image_' + str(distance) + '("color",\''
    mesaio = '\', "texture", \''
    teliko = '\',' + str(histWeight) + ') limit ' + str(numofresults)
    query = arxiko + str(megaColor) + mesaio + str(megaTexture) + teliko
    cursor.execute(query)
    filelist = cursor.fetchall()
    cursor.close()
    return filelist

def weighted_dist(megaColor, megaTexture, numofresults,weight_col,weight_tex,histWeight):
    cursor = connection.cursor()
    arxiko = 'select * from "Pictures" order by weightedDist("color",\''
    mesaio = '\', "texture", \''
    teliko = '\',\'' + str(weight_col) + " ',' "+str(weight_tex)+'\' ,'+str(histWeight)+') limit ' + str(numofresults)
    query = arxiko + str(megaColor) + mesaio + str(megaTexture) + teliko
    cursor.execute(query)
    filelist = cursor.fetchall()
    cursor.close()
    return filelist

def get_all():
    cursor = connection.cursor()
    cursor.execute('select * from "Pictures"')
    filelist = cursor.fetchall()
    cursor.close()
    return filelist