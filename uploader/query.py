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