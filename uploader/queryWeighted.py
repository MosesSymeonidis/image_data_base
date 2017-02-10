from numpy import *
def weightMed(filelist,file):

    colorall=[]
    textureall=[]
    texturenew=[]
    colornew=[]
    for f in filelist:
        c = str(f[2])[1:-1].split(',')
        c = [int(i) for i in c]
        colorall.append(c)
        c = str(f[3])[1:-1].split(',')
        c = [int(i) for i in c]
        textureall.append(c)
    for f in file:
        c = str(f[2])[1:-1].split(',')
        c = [int(i) for i in c]
        colornew.append(c)
        c = str(f[3])[1:-1].split(',')
        c = [int(i) for i in c]
        texturenew.append(c)


    colorallstd=std(array(colorall),0)
    textureallstd=std(array(textureall),0)
    colornewstd=std(array(colornew),0)
    texturenewstd=std(array(texturenew),0)
    weightColor=[]
    weightTex=[]

    for i in range(0,len(colorallstd)):
        weightColor.append(colorallstd[i]/colornewstd[i])
        if math.isinf(weightColor[i]):
            weightColor[i]=-1.0
    for i in range(0,len(weightColor)):
        if weightColor[i]<0:
            if max(weightColor)<0:
                weightColor[i] = 1.0
            else:
                weightColor[i]=max(weightColor)
        elif math.isnan(weightColor[i]):
            weightColor[i]=1.0

    for i in range(0,len(textureallstd)):
        weightTex.append(textureallstd[i]/texturenewstd[i])

        if math.isinf(weightTex[i]):
            weightTex[i]=-1.0

    for i in range(0,len(weightTex)):
        if weightTex[i]<0:
            if max(weightTex)<0:
                weightTex[i] = 1.0
            else:
                weightTex[i]=max(weightTex)
        elif math.isnan(weightTex[i]):
            weightTex[i]=1.0
    sc=sum(weightColor)
    st=sum(weightTex)
    weightC=[]
    weightT=[]
    for i in weightColor:
        weightC.append(i/sc)
    for i in weightTex:
        weightT.append(i/st)
    return tuple(weightC), tuple(weightT)