import json
import urllib2
import sys
import os

# function to download file 
def download(url, file_name):
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,
    
    f.close()

# check if roms dir exists, else mkdir roms
a=os.getcwd()+'/roms'
if not os.path.exists(a):
    os.makedirs(a)
    
for arg in sys.argv:
    if arg == 'download.py':
        continue

    with open(arg) as data_file:    
        data = json.load(data_file)

    if arg == 'nexus.json':
        for i in range(len(data)):
            if not data[i]['url']:
                continue
        
            url=data[i]['url'].pop().encode('ascii', errors='ignore')
            file_name = url.split('/')[-1]
            file_name = 'roms/' + file_name
            download(url, file_name)


    if arg == 'Cyanogenmod.json':
        for i in range(len(data)):
            if not data[i]['url']:
                continue
        
            url=data[i]['url'].encode('ascii', errors='ignore')
            url='http://download.cyanogenmod.org/'+url
            print url
            file_name = url.split('/')[-1]
            file_name = 'roms/' + file_name
            download(url, file_name)


    
