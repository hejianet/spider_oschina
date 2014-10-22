spider_oschina
==============

spider blogs of oschina by python,wget

To crawl all the blogs of oschina(I think csdn,chinaunix 
are the same or similar), the basic thoughts are as below:
1. Use wget to mirror all the webpages of that blog sites
The cmd I used is wget -np -r -k -x   \
http://my.oschina.net/qiangzigege/ -U "Mozilla/5.0 (Windows NT 5.2) \
AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"
I also think this crawling operation can be done by python, this
might be the next what I want to do ;)
2. Use spide.py to find the title field of each blogs. Rename them
to the readable ones.

