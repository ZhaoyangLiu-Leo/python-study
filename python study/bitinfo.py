# -*- coding:utf-8 -*-
'''
	judge the file is a bmp file or not, 
	if true, read the size and the number of color of the photo. 
'''

import struct

HEAD_SIZE = 30

file_path = raw_input('Please input the file name:')

with open(file_path, 'rb') as f:
	s = f.read(HEAD_SIZE)

bmp_tuple = struct.unpack('<ccIIIIIIHH', s)

if bmp_tuple[0] == 'B' and bmp_tuple[1] == 'M':
	print 'True, bmp file'
	print 'Size: %s * %s' % (bmp_tuple[6], bmp_tuple[7])
	print 'Color number:', bmp_tuple[9]
else:
	print 'False'

