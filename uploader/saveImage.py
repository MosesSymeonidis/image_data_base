def saveImage(f):
    destination = open('/home/dgi/name.jpg', 'w+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
