from orbit.net.streaming import UdpTranceiver

net = UdpTranceiver(1360, '127.0.0.1', 1630, '127.0.0.1')

net.recv_all(lambda msg: net.send(bytes(reversed(msg))))
