# Write a function to open and read data from access.log.
# Use a regular expression to find IP addresses
#
# The function will return a list of all IP addresses. If the same IP address appears multiple times,
# only one should be reported.


import re


def count_IP_addresses(text):

    ipRegex= re.compile(r'''
    \d\d?\d?
    \.
    \d\d?\d?
    \.
    \d\d?\d?
    \.
    \d\d?\d?
    ''',re.VERBOSE)

    ip = ipRegex.findall(text)
    ip = list(set(ip))

    result = ("\n").join(ip)

    print result

with open("access.log",'r') as file:
    text = file.read()

    count_IP_addresses(text)
