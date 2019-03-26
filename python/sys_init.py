#!/bin/env python
#time:2019-03-26 16:43:24
#auth:victor
#func:dns hostname profile rc.local sysctl rootpasswd sshpubkey servicedir zbxclient
#
import argparse,parser
import subprocess
import os

def get_options():
  parser = argparse.ArgumentParser(
        description='Created By Victor nu11point007@gmail.com')
  parser.add_argument('-d', '--dns', action='store',
                        help='DNS config.', type=str, default="192.168.0.1")
  config = parser.parse_args()
  return config
def config_dns(dnsargv):
  if os.access("/etc/resolv.conf",os.W_OK) != True:
    print "resolv file read only, chattr -i..."
    os.system('chattr -i /etc/resolv.conf')
  fd = open('/etc/resolv.conf',"w")
  dns = "nameserver " + dnsargv
  fd.write(dns)
  fd.close()
def main():
  opts = get_options()
  print opts
  config_dns(opts.dns)
if __name__ == '__main__':  
  main()
