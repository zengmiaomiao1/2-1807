from multiprocessing import Pool
import time

def show():
	for i in range(5):
		time.sleep(0.5)
		print('哇哈哈')

p=Pool()#创建一个池子，可以装无限个进程
for i in range(3):
	p.apply_async(show)#添加一个进程到池子里面 非阻塞添加进程  3个进程同时执行
	#p.apply(show)#阻塞添加
	print('添加成功')

p.close()#关闭池子
p.join()#不支持传超时时间
print('呵呵')


