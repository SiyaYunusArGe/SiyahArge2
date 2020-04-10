#!/usr/bin/env python
import os
os.system("apt.get install figlet")
os.system("clear")
print("""
   _____       _____        _______                                  _          _ 
  / ____|     |  __ \      |__   __|                                (_)        (_)
 | |  __      | |  | |        | |      __ _   _ __    __ _   _   _   _    ___   _ 
 | | |_ |     | |  | |        | |     / _` | | '__|  / _` | | | | | | |  / __| | |
 | |__| |  _  | |__| |  _     | |    | (_| | | |    | (_| | | |_| | | | | (__  | |
  \_____| (_) |_____/  (_)    |_|     \__,_| |_|     \__,_|  \__, | |_|  \___| |_|
                                                              __/ |               
                                                             |___/                



""")
print("""

Guvenlik Duvari Tespit Araci

""")

site = raw_input("Site Adresi: ")

os.system("waff00f " + site)
