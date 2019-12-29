import os
import sys
import logging 
import time

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s", filename="/Users/username/github-local/dns-detector-12-31/logs/dns_detector.log")

class DnsDetector():
    def __init__(self, subnet, range1, range2):
        self.subnet = subnet
        self.range1 = range1
        self.range2 = range2

    #def subnet_splitter(self):
     #   print str(self.subnet)
    
    def scan_range(self):
        try:
            range3 = self.range2 + 1
            range_master = range(self.range1, range3)
            #print(self.subnet)
            iplist = []
            for i in range_master:
                s = ".";
                s1 = str(self.subnet)
                s2 = str(i)
                seq = (s1, s2)
                print s.join( seq )
                ipaddress = s.join( seq )
                iplist.append(ipaddress)
            print(iplist)
        except:
            print("some error")

    def nslookup(self):
        try:
            socket.gethostnamebyname(hostname)
            return 1
        except: socket.error:
            return 0
            

