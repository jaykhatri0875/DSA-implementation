

class message:
	def __init__(self,id,pos_x,pos_y,timestamp,date,sess_time):
		self.id = id,
		self.pos_x = pos_x
		self.pos_y = pos_y
        self.ts = timestamp
        self.date = date
        self.sess_time = sess_time


class buffer:
    def __init__(self,size):
        self.buff = [message]*size
        self.head = None
        self.tail = None
    def add(message_param):
        new_msg = message(message_param)
        self.buff.append(new_msg)   
    def read():
        return self.buff.pop()
    def isempty():
        return len(self.buff)==0
    def isfull():
        return len(self.buff)==size

def producer(buffer,length=10):
    if(not buffer.isfull()):
        for i in range(length):
            buffer.add(message(id=i))
    else:
        raise excp_full 

def consumer(buffer):
    while(not buffer.isempty()):
        message = buffer.read()
        db.insert(message)
    else:
        raise excp_empty
