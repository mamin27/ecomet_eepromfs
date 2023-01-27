#!/usr/bin/env python3
#import sys
#sys.path.append("..")

import eepromfs

toc = eepromfs.EEPROM_FS()

filename = 'data/AT.pdf'
rc = toc.load_eepromfs(filename)

print ("RC: {}".format(rc))