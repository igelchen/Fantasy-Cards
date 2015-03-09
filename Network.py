import socket
import Queue
import threading

class Connection(threading.Thread):

	def __init__(self, server_ip=None, port=50000):
		threading.Thread.__init__(self)
		self._server_ip = server_ip
		self._port = port
		self._closed = False
		self._actions = Queue.Queue()
		if server_ip == None:
			self._remote_addr = None
		else:
			self._remote_addr = (server_ip, port)
		self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		if server_ip == None:
			#start as server
			self._sock.bind(("", port))
		self.start()

	def run(self):
		try:
			self._sock.settimeout(1)
			while not self._closed:
				try:
					data, addr = self._sock.recvfrom(2048)
				except:
					continue
				if self._remote_addr == None:
					self._remote_addr = addr
				self._actions.put(MessageAction(data))
		except Exception, e:
			if not self._closed:
				raise e

	def send(self, message):
		if self._remote_addr == None:
			raise Exceeption("Fehler beim Senden: die Gegenstelle ist nicht bekannt! Bevor etwas gesendet wird muss von der Gegenstelle etwas empfangen werden!")
		self._sock.sendto(message, self._remote_addr)

	def close(self):
		self._closed = True
		self._sock.close()

	def get_action(self):
		return self._actions.get()


class Action():

    def __init__(self, type):
        self._type = type

    def get_type(self):
          return self._type


class MessageAction(Action):

    def __init__(self, message):
        Action.__init__(self, "message")
        self._message = message

    def get_message(self):
        return self._message
