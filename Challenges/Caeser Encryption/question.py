
from random import *


def normalised_ord(char):

    normalised_char = ord(char)
    normalised_char = normalised_char % 94
    normalised_char = normalised_char-33
    return normalised_char


def normalised_chr(char):

    normalised_char = char % 94
    normalised_char = normalised_char+33
    return chr(normalised_char)


def encrypt(s):
    s1 = ""
    key = randint(
        0, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    for i in range(len(s)):
        a = normalised_ord(s[i])
        a = a + key
        s1 += normalised_chr(a)
    print(s1)
    return s1


def decrypt(s):
    for key in range(95):
        s1 = ""
        for i in range(len(s)):
            a = normalised_ord(s[i])
            a = a-key
            s1 = s1+normalised_chr(a)

        if s1.startswith("ShaastraCTF"):
            return s1
    return None


s = "ShaastraCTF{s!mp1e_crypt0gr@phy_@a1g0r!thm:)}"
e = encrypt(s)
print(e)
print(decrypt(e))
