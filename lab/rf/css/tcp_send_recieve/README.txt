READ FIRST:
https://dev.to/cwprogram/python-networking-tcp-and-udp-4i3l
https://www.pynetlabs.com/transmission-control-protocol-tcp-header/


https://www.kytta.dev/blog/tcp-packets-from-scratch-in-python-3/
https://kytta.medium.com/tcp-packets-from-scratch-in-python-3a63f0cd59fe


https://gist.github.com/kytta/b06520e3cb458ac7264cab1c51fa33d6



UDP:
https://abdesol.medium.com/udp-protocol-with-a-header-implementation-in-python-b3d8dae9a74b


Python:struct
https://docs.python.org/3/library/struct.html#format-characters

Python:  '\x00'

The leading \x escape sequence means the next two characters are interpreted as hex digits for the character code, so \xaa equals chr(0xaa),
i.e., chr(16 * 10 + 10) -- a small raised lowercase 'a' character.

from this https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
it says :  \xhh  Character with hex value hh (see 3 and 4)

3- Unlike in Standard C, exactly two hex digits are required.

4- In a bytes literal, hexadecimal and octal escapes denote the byte with the given value.
In a string literal, these escapes denote a Unicode character with the given value.

