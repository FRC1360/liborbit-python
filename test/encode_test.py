from orbit.util import encode, decode

print(decode(encode(1.0, -0.7, -3, 49), float, float, int, int))
