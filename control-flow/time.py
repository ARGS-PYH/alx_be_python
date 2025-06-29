import time
#print(time.ctime(1000000))
#print(time.time())

time_object = time.localtime()
print(time_object)
new_time = time.strftime("%B %c ", time_object)
print(new_time)