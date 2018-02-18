from nessie import *
import string

with open('transactions','r') as f:
    for line in f:
        l = line.split(',')
        rv = Purchase.Create("5a88c0af6514d52c7774b549",l[1],'balance',l[0],float(l[2]),'completed',' ')

