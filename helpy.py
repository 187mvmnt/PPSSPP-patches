#!python3

import pyperclip
import time


"""
it is a simple as subtracting 0x08800000 are you sure you have the correct base address
_L 0x203B3B58 0x3F800000
"""

PROGRAM_NAME = "Helpy"
MAGIC = 0x08800000
VAL = 1

def is_input_valid(s):
	if(s[:1].isdigit() and (len(s) > 6) and (int(s, 16) > 0)):
		return True
	return False

def toaddr32(num): return '0x{0:08X}'.format(num)

def gen_pay(s):
	si = int(s, 16)
	assert si > 0
	
	si = si - MAGIC
	
	# https://stackoverflow.com/a/28650911
	pay = "_L "
	pay += toaddr32(si)
	pay += " "
	pay += toaddr32(VAL)
	return pay



def main():
	HOW_TO = """Just copy stuff to clipboard!"""
	
	print(PROGRAM_NAME+" "+"greets you!")
	print("How to: "+HOW_TO)
	
	try:
		while True:
			paste = pyperclip.paste().strip()
			
			# check for valid input 
			if(is_input_valid(paste)):
				print("*Valid in: "+paste)
				# gen pay
				pay = gen_pay(paste)
				print("*Out: "+pay)
				pyperclip.copy(pay+chr(10))
			#else:
				#print("*Inv: "+paste)
			time.sleep(0.1)
	except KeyboardInterrupt:
		print('cya!')


if __name__ == '__main__':
	main()