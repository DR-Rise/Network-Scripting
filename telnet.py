import getpass
import telnetlib

HOST = "192.168.1.114"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
for x in range(2,6):
    tn.write(b" vlan " + str(x).encode('ascii') +b"\n ")
    tn.write(b"name vlan " + str(x).encode('ascii') + b" test\n ")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
