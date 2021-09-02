## Copyright tlegx 2021 under MIT License
## Use at your own risk, no warranty provided!

import time
import readchar
import sys
import os
import random

def main():
	os.system("cls")
	print("===== 3x+1 =====")
	print("3x+1, also known as the 'Collatz conjecture' is a conjecture in mathematics that left an unsolved problem in mathematics")
	print("You can read more about this on the Wikipedia article: https://en.wikipedia.org/wiki/Collatz_conjecture")
	print("This is a program which automatically apply numbers to this conjecture and return results. Useful for demoing and learning purposes")
	print("[S]tart/[C]redits/[Q]uit (or press any key): ")
	choice = readchar.readkey()
	if choice == "s" or choice == "S":
		os.system("cls")
		math()
	elif choice == "c" or choice == "C":
		os.system("cls")
		credits()
	else:
		print("Bye!")
		sys.exit()

def math():
	print("===== 3x+1 =====")
	mathChoice = input("Enter a positive integer or [R]andom number from 1 to 1000 exclusive: ")
	if mathChoice == "r" or mathChoice == "R":
		mathNum = int(random.randrange(1, 1000))
		print("The number is " + str(mathNum) + ". Do you wish to continue? [Y]es/[N]o (or press any key): ")
		randomMath = readchar.readkey()
		if randomMath == "n" or randomMath == "N":
			print("Operation cancelled")
			sys.exit()
	else:
		try:
			mathNum = int(mathChoice)
			if mathNum == 0:
				print("The 'Collatz conjecture' does not apply for this number as it is not a positive integer. Please try again!\n")
				math()
			elif mathNum > 1000:
				isMathOver1000Confirm = input("You are about to execute an operation which will do a lot of math operations and may hang some old computers. If you wish to continue, type 'Yes, I understand the risk' (case sensitive!): ")
				if isMathOver1000Confirm != "Yes, I understand the risk":
					print("Operation cancelled")
					sys.exit()
			elif mathNum < 0:
				print("The 'Collatz conjecture' does not apply for this number as it is not a positive integer. Please try again!\n")
				math()
		except ValueError:
			print("The 'Collatz conjecture' does not apply for this number as it is not a positive integer. Please try again!\n")
			math()

	do3xplus1(mathNum)
		
def do3xplus1(number):
	i = 0
	while i < 6:
		number = int(number)
		if number % 2 == 0:
			number = number / 2
			print(int(number))
			time.sleep(0.5)
		elif number % 2 != 0:
			number = number * 3 + 1
			print(int(number))
			time.sleep(0.5)
		if number == 1:
			i += 1
	print("The loop is complete. Continue running will result in the '4, 2, 1' loop indefinitely.")

def credits():
	print("===== 3x+1 =====")
	print("Copyright 2021 tlegx under MIT License")
	print("For more information, (such as: open-source, license, bug reporting, etc.) please visit: https://github.com/tlegx/3xplus1")
	print("[B]ack/[Q]uit (or press any key): ")
	creditsChoice = readchar.readkey()
	if creditsChoice == "b" or creditsChoice == "B":
		main()
	else:
		print("Bye!")
		sys.exit()

main()