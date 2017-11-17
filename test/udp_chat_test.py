from orbit.net.streaming import UdpTranceiver

net = UdpTranceiver(1630, '127.0.0.1', 1360, '127.0.0.1')

while True:
    net.send(bytes(input('>'), 'utf8'))
    print(':' + str(net.recv(), 'utf8'))
