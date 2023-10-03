# https://www.codewars.com/kata/541a354c39c5efa5fa001372/train/python
def ip_to_num(ip):
    octets = ip.split(".")
    binary = str()
    for octet in octets:
        value = bin(int(octet))[2:]
        #format(1, '#010b')
        binary += ("0"*(8-len(value))) + value
    
    return int(binary, 2)