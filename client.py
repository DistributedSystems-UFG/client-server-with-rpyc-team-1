import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  continu = True
  while continu == True:
    print ('commands: delete_at_index, ordenate, add, delete_element, count, search, leave')
    what_do = input()
    if what_do == 'delete_at_index':
      print('which index?')
      value = int(input())
      conn.root.exposed_delete(value)
    elif what_do == 'ordenate':
      conn.root.exposed_ordenate()
    elif what_do == 'add':
      print('which value?')
      value = int(input())
      conn.root.exposed_append(value)
    elif what_do == 'delete_element':
      print('which value?')
      value = int(input())
      conn.root.exposed_delete_element(value)
    elif what_do == 'count':
      print('which value?')
      value = int(input())
      print(conn.root.exposed_count(value))
      print ('\n')
      continue
    elif what_do == 'search':
      print('which value?')
      value = int(input())
      print(conn.root.exposed_search(value))
      print ('\n')
      continue
    elif what_do == 'leave':
      continu = False
    print (conn.root.exposed_value())   # Print the result
    print ('\n')
