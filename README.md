romdownloader
=======
A simple web crawler based on `Scrapy`.

How to use
--------
1. clone repo, then cd to `romdownloader` dir
2. run crawler to download rom urls to json file
3. run download script to download roms to `roms` directory

Install
--------
```
$ apt-get install python-dev
$ wget https://bootstrap.pypa.io/get-pip.py   
$ python get-pip.py  #install pip
$ pip install Scrapy
```

Example
--------
Clone repo
```
$ git clone http://github.com/Dongdongshe/romdownloader
$ cd romdownloader
```
Download nexus roms
```
$ scrapy crawl nexus -o nexus.json
$ python download.py nexus.json
```
Download Cyanogenmod roms
```
$ scrapy crawl Cyanogenmod -o Cyanogenmod.json
$ python download.py Cyanogenmod.json
```
