#!/usr/bin/python

# commitment.py
# June 2015 - ben.dale@gmail.com
# Take a list of IP addresses of Junos devices and force a commit on each of them
# Used to trigger a configuration backup via system archival

import sys
import shlex
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

def main(argv):
    sys.stdout.write("commitment\n\n")
    if len(sys.argv) != 2:
        sys.stdout.write("Error: Missing parameter\n")
        sys.stdout.write("Usage: commitment.py <device-list.txt>\n")
        sys.exit()
    username = raw_input('Username: ')
    password = getpass('Password (leave blank to use SSH Key): ')
    hostsfile = open(str(sys.argv[1]),'r')
    for address in hostsfile:
		if password != '':
			dev = Device(host=address.rstrip('\n'),user=username,passwd=password)
		else:
			dev = Device(host=address.rstrip('\n'),user=username)
		print "Opening :" + str(dev.hostname)
		dev.open()
		print "Opened :" + str(dev.hostname)
		print "Opening config"
		dev.bind(cf=Config)
		print "Locking config"
		dev.cf.lock()
		print "Committing config"
		dev.cf.commit()
		print "Unlocking config"
		dev.cf.unlock
		print "Closing: " + str(dev.hostname)
		dev.close()
		print "Closed :" + str(dev.hostname)
    hostsfile.close()

if __name__ == "__main__":
   main(sys.argv[1:])
