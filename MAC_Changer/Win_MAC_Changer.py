#!/usr/bin/env python3

import subprocess 
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        #code to execute
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        #code to execute
        parser.error("[-] Please specify a new mac, use --help for more info")
    return options
def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for: " + interface +" to: "  + new_mac)

    #Secure Way to call subprocess:
    subprocess.call(["C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "Set-NetAdapter", "-name", interface, "-macaddress", new_mac]) 
    

options = get_arguments()
change_mac(options.interface, options.new_mac)
