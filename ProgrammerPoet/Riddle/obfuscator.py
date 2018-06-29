# simple functions used to create the "numerized" versions of strings used in the main script

def numerize_string(s):
    return [ord(c) for c in s]

def numerize_poem(poem):
    return [numerize_string(line) for line in poem.split("\n")]

def numerize_arr(arr):
    return [numerize_string(row) for row in arr]
