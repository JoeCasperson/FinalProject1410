#needs adjustment for large file size with the edit and delete features

import os
import ipaddress
import re


class Check_ip: #Mason
  def check_ip(ip):
      '''Ip checker'''

      try:
          x = ipaddress.ip_address(ip)
          return True
      except ValueError:
          return False

class Check_mac: #Joe
  def check_mac(mac):
      '''MAC address checker'''

      z = mac.lower()
      if re.match('[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$', z):
          return True
      else:
          return False

class Create_file:    #Thing is done I presume
  def create():
      name = ''
      while not name:
          print('Please provide some details:')
          print('Be sure to type all inputs correctly')
          name = input('Computer name: ')
          op = input('Operating system: ')
          ip = input('IP address: ')
          mac = input('MAC Address: ')
          user = input('Assigned User: ')
          x = Check_ip.check_ip(ip)
          y = Check_mac.check_mac(mac)

          #another error checker for length and IP/MAC
          if len(name) >= 50 or len(op) >= 50 or len(user) >= 50:
              print('invalid input, please try again')
              name = ''
          elif not y or not x:
              print('The MAC or IP  is incorrect, please try again')
              name = ''

      #this combines the data and makes it one string for input
      data = f'{name} {op} {ip} {mac} {user}'
      with open(os.path.abspath('computer_list.txt'), 'a') as f:
          f.write(data+',') #this makes the data comma delimited
          f.close() #each file is closed in the end for sure
      return


class EditFile: #Joe
        def __init__(self) -> None:
            pass

        def Edit():
            #this edits one of the existing computers in the file

            with open(os.path.abspath('computer_list.txt'), 'r') as r:
                file = r.read()

            text = file.split(',') #this splits the data into computers
            size = len(text) #This is created to give the computers numbers

            print('Here are the available computers to edit:')

            for i in range(size - 1): #there was an extra comma, this works around it
                print(f'[{i + 1}]  {text[i]}')

            print('\n Choose a number you would like to edit: or type 0 to escape')
            choose = '' # this does the error handling
            while not choose:
                choose = input()
                if choose.isdigit() and int(choose) <= size:
                    if choose == '0': #the exit clause
                        return
                    name = '' #this is the same input sequence as in create
                    while not name:
                        print('Please provide some details:')
                        print('Be sure to type all inputs correctly')
                        name = input('Computer name: ')
                        op = input('Operating system: ')
                        ip = input('IP address: ')
                        mac = input('MAC Address: ')
                        user = input('Assigned User: ')
                        x = Check_ip.check_ip(ip)
                        y = Check_mac.check_mac(mac)

                        if len(name) >= 50 or len(op) >= 50:
                            print('invalid input, please try again')
                            name = ''
                        elif not y or len(user) >= 50 or not x:
                            print('invalid input, please try again')
                            name = ''

                    data = f'{name} {op} {ip} {mac} {user}'

                    #this reassigns the computer selected within the list
                    text[int(choose) - 1] = data

                else:
                    print('Sorry, choose a correct file number')
                    choose = ''

                #this uploads and remakes the whole file once again
                print('the computer has been edited.')
                with open(os.path.abspath('computer_list.txt'), 'w') as f:
                    f.write(','.join(text))
                    f.close() #each file is closed in the end for sure
                return

class Delete: #Mathew
    @staticmethod
    def delete(test_choose=None): #test_choose is optional parameter for tests
        '''This function deletes a computer from the file'''

        # Read data from the file
        with open(os.path.abspath('computer_list.txt'), 'r') as r:
            file = r.read()

        # Split data into individual computers
        computers = file.split(',')

        # Display available computers to delete
        print('Here are the available computers to delete:')
        for i, computer in enumerate(computers, 1):
            print(f'[{i}]  {computer}')

        if test_choose is not None:  # Check if test_choose is provided
            choose = test_choose
        else:
            # Prompt user to choose a computer to delete
            print('\n Choose the entry you want to delete: or type 0 to escape')
            choose = input()
            if choose == '0':
                print('Operation canceled.')
                return

        try:
            # Convert input to integer and delete selected computer
            index = int(choose) - 1
            if 0 <= index < len(computers):
                deleted_computer = computers.pop(index)
                print(f'The computer "{deleted_computer}" has been deleted.')
            else:
                print('Invalid input. Please choose a correct file number.')
                return
        except ValueError:
            print('Invalid input. Please choose a correct file number.')
            return

        # Write remaining computers back to the file
        with open(os.path.abspath('computer_list.txt'), 'w') as f:
            f.write(','.join(computers))

class Exit():

  def exit(): #Matthew
      '''This exits the program'''

      Menu.cont = True
      print('Bye Bye!')


class Menu(Create_file, Delete, Exit):

  cont = False
  @classmethod
  def Menu(cls):
    while not cls.cont:
        print()
        print('Hi! Welcome to File Manager!')
        print(' Create a new computer entry [1]')
        print(' Edit a computer entry [2]')
        print(' Delete a computer entry [3]')
        print(' Exit [4]')
        cls.menu = 0
        while not cls.menu:
            cls.menu = input()
            if cls.menu == '1':
                Create_file.create()
            elif cls.menu == '2':
                EditFile.Edit()
            elif cls.menu == '3':
                Delete.delete()
            elif cls.menu == '4':
                Exit.exit()
            else:
                print('Please type a valid input')
                cls.menu = 0

Menu.Menu()




