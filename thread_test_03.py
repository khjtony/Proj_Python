import threading

import time

class Producer(threading.Thread):

    def __init__(self, t_name):

        threading.Thread.__init__(self, name=t_name)

 

    def run(self):

        global x
        return 0
    def sell(self):
        global x
        con.acquire()

        if x > 0:

            con.wait()

        else:

            for i in range(5):

                x=x+1

                print ("producing..." + str(x))

            con.notify()

        print (x)

        con.release()

 

class Consumer(threading.Thread):

    def __init__(self, t_name):

        threading.Thread.__init__(self, name=t_name)

    def run(self):
        return 0
        
    def buy(self):
        global x
        con.acquire()

        if x == 0:

            print ('consumer wait1')

            con.wait()

        else:

            for i in range(5):

                x=x-1

                print ("consuming..." + str(x))

            con.notify()

        print (x)

        con.release()

 

con = threading.Condition()

x=0

print ('start consumer')

c=Consumer('consumer')

print ('start producer')

p=Producer('producer')

p.start()

c.start()

while True:


    p.sell()

    c.buy()
    time.sleep(1)
print (x)
