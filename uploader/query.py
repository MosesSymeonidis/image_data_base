from django.db import connection


def querydb(distance, histWeight, numofresults, megaColor, megaTexture):
    cursor = connection.cursor()
    first = 'select * from "Pictures" order by image_' + str(distance) + '("color",\''
    middle = '\', "texture", \''
    last = '\',' + str(histWeight) + ') limit ' + str(numofresults)
    query = first + str(megaColor) + middle + str(megaTexture) + last
    cursor.execute(query)
    filelist = cursor.fetchall()
    cursor.close()
    return filelist

def weighted_dist(megaColor, megaTexture, numofresults,weight_col,weight_tex,histWeight):
    cursor = connection.cursor()
    first = 'select * from "Pictures" order by weightedDist("color",\''
    middle = '\', "texture", \''
    last = '\',\'' + str(weight_col) + " ',' "+str(weight_tex)+'\' ,'+str(histWeight)+') limit ' + str(numofresults)
    query = first + str(megaColor) + middle + str(megaTexture) + last
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