def D(buf):
    buf[0] = buf[0] + " ╓────╖      "
    buf[1] = buf[1] + " ╙╖█╓╖║      "
    buf[2] = buf[2] + " ░║█║║║      "
    buf[3] = buf[3] + " ░║█║║║      "
    buf[4] = buf[4] + " ╓╜█╙╜║      "
    buf[5] = buf[5] + " ╙────╜      "
 
 
s = ["","","","","",""]
D(s)
D(s)
print(*s, sep='\n')