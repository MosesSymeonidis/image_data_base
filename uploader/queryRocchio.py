def rocMeth(colorhist, texhist, files, nc, nt):
    newTex = [0] * (2 ** nt)
    newColor = [0] * (nc ** 3)
    megaColor = [0] * (nc ** 3)
    megaTex = [0] * (2 ** nt)
    m = len(files)
    for file in files:
        c = str(file[2])[1:-1].split(',')
        c = [int(i) for i in c]
        t = str(file[3])[1:-1].split(',')
        t = [int(i) for i in t]
        for i in range(0, nc ** 3):
            megaColor[i] += (c[i] / m)
        for i in range(0, 2 ** nt):
            megaTex[i] += (t[i] / m)
    for i in range(0, (nc ** 3)):
        newColor[i] = 0.4 * colorhist[i] + 0.6 * megaColor[i]
    for i in range(0, (2 ** nt)):
        newTex[i] = 0.4 * texhist[i] + 0.6 * megaTex[i]

    return tuple(newColor), tuple(newTex)