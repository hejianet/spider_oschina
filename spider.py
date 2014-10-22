#! /usr/bin/python
#coding:utf-8

import sys,os,string
from sgmllib import SGMLParser
class GetIdList(SGMLParser):
	def reset(self):
		self.IDlist = []
		self.flag = False
		self.getdata = False
		self.verbatim = 0
		SGMLParser.reset(self)
		
	def start_head(self, attrs):
		self.flag = True
		return

	def end_head(self):#遇到</div>
		self.flag = False

	def start_title(self, attrs):
		if self.flag == False:
			return
		self.getdata = True
		
	def end_title(self):#遇到</p>
		if self.getdata:
			self.getdata = False

	def handle_data(self, text):#处理文本
		if self.getdata:
			self.IDlist.append(text)
			
	def printID(self):
		mstr= '%s' % self.IDlist[0]
		return mstr	

if __name__ == '__main__':
	m=GetIdList()
	current_files = os.listdir("./blog/")
	raw_input("Press any key to exit!") 
	all_files = []
	for file_name in current_files:
		m.reset()
		full_file_name = os.path.join("./blog/", file_name)
		print full_file_name
		file_object = open(full_file_name,'r');
		m.feed(file_object.read())
		print(m.printID())
		
		new_name=m.printID().replace(" -  强子哥哥 - 开源中国社区","")
		new_name=new_name.replace("/","#")
		new_name = os.path.join("./blog/", new_name)
		print new_name
		os.rename(full_file_name,new_name);
		
	m.close()
##import urllib2
##import datetime
##vrg = (datetime.date(2012,2,19) - datetime.date.today()).days
##strUrl = 'http://www.nod32id.org/nod32id/%d.html'%(200+vrg)
##req = urllib2.Request(strUrl)#通过网络获取网页
##response = urllib2.urlopen(req)
##the_page = response.read()
