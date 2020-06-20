import subprocess
subprocess.run('ifconfig eth1 hw ether 00:11:22:33:44:55', shell=True)
