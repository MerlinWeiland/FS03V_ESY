#!/usr/bin/python3

#python Porgramm

def clear():
  os.system("clear")
  auswahl(num)

def pi_berechnen():
  print("no Pi 3,141")

def weiter():
  strg = input("Owllen Sei iene ewitere ebrechnung rduchfuehren")
  if strg == "J":
    menu()
  elif strg == "N":
    clear()


def main():
  print("was geht")
  menu()

def menu():
  print("1: berechne pi")
  print("2: berechne x quadrte")
  num = input()
  auswahl(num)

def auswahl(value):
  clear()
  if value == 1:
    #erstmal NOIX!
    pi_berechnen()
  elif value == 2:
    #hält die Frasse
  else
    pass

  weiter()

  



if __name__ == "__main__":
  main()


