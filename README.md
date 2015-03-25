romdownloader
=======
A simple web crawler based on `Scrapy`.

Usage
-------
install Scrapy
```
$ apt-get install python-dev
$ wget https://bootstrap.pypa.io/get-pip.py   
$ python get-pip.py  #install pip
$ pip install Scrapy
```
clone repo
```
$ git clone http://github.com/Dongdongshe/romdownloader
```
cd to `romdownloader` dir
```
$ cd romdownloader
```
run crawler to download all nexus rom urls, direct output to `roms.json`
```
$ scrapy crawl nexus -o roms.json
```
run download script to download roms to `roms` directory
```
$ python download.py
```
