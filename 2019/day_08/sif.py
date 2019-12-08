import numpy as np
from collections import Counter

width = 25
height = 6

white = chr(9608)


def split_sif(sif, width, height):
    layer_size = width * height
    layers = np.array_split(sif, len(sif) / layer_size)

    layer_counters = [Counter(l) for l in layers]
    least_zeros = sorted(layer_counters, key=lambda x: x[0])[0]

    print(f"Validation Code: {int(least_zeros[1]) * int(least_zeros[2])}")

    return layers


def decode_layers(layers, height):
    """0 is black
       1 is white
       2 is transparent"""
    decoded_message = []

    # Transpose the layers
    layers = [list(layer) for layer in zip(*layers)]

    for layer in layers:
        black_index = 100
        white_index = 100
        if 0 in layer:
            black_index = layer.index(0)
        if 1 in layer:
            white_index = layer.index(1)
        if black_index < white_index:
            decoded_message.append(" ")
        else:
            decoded_message.append(white)

    message = np.array_split(decoded_message, height)

    for line in message:
        print("".join(str(n) for n in line))


with open("input.txt", "r") as f:
    sif = f.read()
    sif = [int(n) for n in sif.strip()]

layers = split_sif(sif, width, height)
decode_layers(layers, height)

