romdownloader
=======
A simple web crawler based on `Scrapy`.

Usage
-------
1. Install Scrapy
```
$ apt-get install python-dev
$ wget https://bootstrap.pypa.io/get-pip.py   
$ python get-pip.py  #install pip
$ pip install Scrapy
```
2. Clone repo
```
$ git clone http://github.com/Dongdongshe/romdownloader
```
3. cd to `romdownloader` dir
```
$ cd romdownloader
```
4. run crawler to download all nexus rom urls, direct output to `roms.json`
```
$ scrapy crawl nexus -o roms.json
```
5. run download script to download roms to `roms` directory
```
$ python download.py
```
