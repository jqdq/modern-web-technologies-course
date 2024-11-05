# Use this script to generate a random alphabet permutation to be used as a rotor/reflector translation in the Enigma machine.

import random
import string

def generate_permutation():
    alphabet = list(string.ascii_uppercase)
    permutation = [None] * 26
    shuffled = alphabet[:]
    random.shuffle(shuffled)

    while shuffled:
        new1 = shuffled.pop()
        new2 = shuffled.pop()
        permutation[alphabet.index(new1)] = new2
        permutation[alphabet.index(new2)] = new1

    return ''.join(permutation)

if __name__ == "__main__":
    permutation = generate_permutation()

    for n, i in enumerate(string.ascii_uppercase):
        n_2 = string.ascii_uppercase.index(permutation[n])
        print(f"{i} -> {n} -> {permutation[n]} -> {n_2} -> {permutation[n_2]}\t{i == permutation[n_2]}")

    print(permutation)