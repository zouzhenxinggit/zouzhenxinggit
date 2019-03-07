#!/usr/bin/python
#coding=utf-8

# 队列库
from Queue import Queue
# 线程库
import threading
# 解析库
from lxml import etree
# 请求处理
import requests
# json处理
import json
import time


CRAWL_EXIT = False
PARSE_EXIT = False

class ThreadCrawl(threading.Thread):
	"""
		采集线程
	"""
	def __init__(self, threadName, pageQueue, dataQueue):
		super(ThreadCrawl, self).__init__()
		
		# 线程名
		self.threadName = threadName
		# 页面队列
		self.pageQueue = pageQueue
		# 数据队列
		self.dataQueue = dataQueue
		
		self.headers = {
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
		}	

	def run(self):
		print "采集线程" + self.threadName
		while not CRAWL_EXIT:
			try:
				# 可选参数block，默认值为True
                #1. 如果对列为空，block为True的话，不会结束，会进入阻塞状态，直到队列有新的数据
                #2. 如果队列为空，block为False的话，就弹出一个Queue.empty()异常，
				page = self.pageQueue.get(False)
				# print page
				url = "http://www.qiushibaike.com/8hr/page/" + str(page) + '/'
				content = requests.get(url, headers = self.headers).text
				time.sleep(1)
				self.dataQueue.put(content)
				# print content
			except:
				pass



class ThreadParse(threading.Thread):
	"""
		解析线程
	"""
	def __init__(self, threadName, dataQueue, filename, lock):
		super(ThreadParse, self).__init__()
		
		# 线程名
		self.threadName = threadName
		# 数据队列
		self.dataQueue = dataQueue
		# 保存解析后数据的文件名
		self.filename = filename
		# 锁
		self.lock = lock
		
		self.headers = {
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
		}	

	def run(self):
		print "解析线程" + self.threadName
		while not PARSE_EXIT:
			try:
				html = self.dataQueue.get(False)
				self.parse(html)
			except:
				pass

	def parse(self, sion):
		content = etree.HTML(sion)
		node_list = content.xpath('//li[contains(@id, "qiushi_tag")]')									

		for node in node_list:
			username = node.xpath('./div//@alt')[0]
			image = node.xpath('.//img//@src')[0]
			content = node.xpath('.//div[@class="recmd-right"]/a')[0].text
			zan = node.xpath('.//span')[0].text
			comments = node.xpath('.//span')[3].text

			# print username, image, content, zan, comments
			items = {
				"username": username,
				"image": "https:" + image,
				"content": content,
				"zan": zan,
				"comments": comments
			}

			# print items['username']
			# with 后面有两个必须执行的操作：__enter__ 和 _exit__
			# 不管里面的操作结果如何，都会执行打开、关闭
			# 打开锁、处理内容、释放锁
			with self.lock:
				# 写入存储的解析后的数据
				self.filename.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")



def main():
	# 创建队列，表示20个页面
	pageQueue = Queue(20)

	# 采集队列
	for i in range(2, 20, 2):
		pageQueue.put(i)

	# 采集结果 HTML源码 的数据队列，参数为空表示不限制
	dataQueue = Queue()

	# 打开文件
	filename = open("threadduanzi.json", "a")

	# 创建锁
	lock = threading.Lock()

	# 三个采集线程的名字
	crawlList = ["crawl-1","crawl-2","crawl-3"]
	# 存储三个采集线程的列表集合
	threadcrawl = []
	for threadName in crawlList:
		thread = ThreadCrawl(threadName, pageQueue, dataQueue)
		thread.start()
		threadcrawl.append(thread)

	# 三个解析线程的名字
	parseList = ["parser-1", "parser-2", "parser-3"]
	threadparse = []
	#存储三个解析线程
	for threadName in parseList:
		thread = ThreadParse(threadName, dataQueue, filename, lock)
		thread.start()
		threadparse.append(thread)

	# 等待采集队列为空
	while not pageQueue.empty():
		pass

	global CRAWL_EXIT
	CRAWL_EXIT = True
	print "pageQueue为空"

	# 等待采集线程结束后在执行主线程
	for thread in threadcrawl:
		thread.join()

	# 等待解析队列为空
	while not dataQueue.empty():
		pass

	global PARSE_EXIT
	PARSE_EXIT = True
	print "parseQueue为空"

	# 等待解析线程结束后在执行主线程
	for thread in threadparse:
		thread.join()	

	with lock:
		filename.close()

	print "谢谢使用！"
main()



