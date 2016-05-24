# Password-Cracking
Password cracking - passCrack.py - Given a string of characters on the command line, find what string hashes to it.  Passwords are sometimes stored in a hashed form, so if the database is breached, the passwords are not easily usable. Assume we have a hash of a password in hex form.  Given this hash on the command line, find what password hashes to it.  Only the first 5 characters of the hash are checked.  Assume passwords are 4 or fewer characters containing only lowercase letters and numbers.   MapReduce  quickly look through all combinations for a match.  Print out the input hash string and the valid passwords which hash to it, if any.  Hashlib md5 hexdigest()and first 5 characters are used.  Here are some passwords to crack: d077f, 0832c, 1a1dc, ee269, 0fe63

Example command line input and corresponding output ---

time python passCrack.py d077f
Attacking d077f

{'found': ['cat', 'gkf9']}

real	0m3.116s
user	0m1.803s
sys	0m0.123s
