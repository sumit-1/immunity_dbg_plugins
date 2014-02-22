#!/usr/bin/env python

"""
Sumit Kumar
Badchar Hunter: Hunt for badchar in an exe.

Alpha Version

"""

__VERSION__ = '0.1'

DESC="""Hunt down badchars"""

import immlib
import struct
import binascii

imm = immlib.Debugger()

def usage():
	imm.log("!bchunter reg array_of_badchar")
	imm.log("ex: !bchunter ESP \"\\x00\\x01\\x0a\"", focus=1)

def filterBC(buf, badchar):
	for c in badchar:
		buf = buf.replace(c, '')
	return buf

def compare(buf, mem_buf):
	for i in range(len(buf)):
		if buf[i] != mem_buf[i]:
			return buf[i]
	return True

def byteArray():
	buf = ''
	for i in range(0, 255):
		c = struct.pack('h', i)[0]
		buf += c
	return buf

def convertToHex(badchar):
	a = ''
	for i in xrange(0, len(badchar), 4):
		a += badchar[i+3:i+5]
	return binascii.unhexlify(a)

def main(args):
	if len(args) < 1:
		usage()
		return 'Try Harder!'
	reg = args[0]
	if len(args) < 2:
		badchar = convertToHex(args[1])
		imm.log('Badchars entered: %d' % (len(badchar)))
	else:
		badchar = ''
	buf = filterBC(byteArray(), badchar)
	mem_buf = imm.readMemory(imm.getRegs()[reg], len(buf))
	res = compare(buf, mem_buf)
	if res != True:
		return 'New Badchar Identified : \\x%s' % (binascii.hexlify(res))
	else:
		return 'All Badchars identified'
