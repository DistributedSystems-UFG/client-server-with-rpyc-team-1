import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [int(data)]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_delete(self, data):
    self.value.pop(int(data))
    return self.value

  def exposed_ordenate(self):
    self.value.sort()
    return self.value

  def exposed_delete_element(self, data):
    self.value.remove(int(data))
    return self.value

  def exposed_count(self, data):
    return self.value.count(int(data))

  def exposed_search(self, data):
    return self.value.index(int(data))

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()
