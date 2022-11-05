polynomial = 0xEDB88320
table = []
for byte in range(256):
    crc = 0
    for bit in range(8):
        if (byte ^ crc) & 1:
            crc = (crc >> 1) ^ polynomial
        else:
            crc >>= 1
        byte >>= 1
    table.append(crc)
def crc32(string):
    value = 0xffffffff
    for x in string:
        value = table[(ord(x) ^ value) & 0xff] ^ (value >> 8)
    return -1 - value
while True:
    i=str(input('Input the string you wanna hash. Enter "0!" if you want to end the program.\n'))
    if (i=='0!'): print ('The program is over.')
    if (i=='0!'): break 
    j=crc32(i)
    print ('%08x' % (j & 0xffffffff))
