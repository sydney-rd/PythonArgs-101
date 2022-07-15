# Argparse tutorial for Python3

A small tutorial project to demonstrate argparse vs input during runtime in Python3

# Requirements

&nbsp;&nbsp; $ sudo apt-get install python3.6

# Run input.py

From terminal, run:

&nbsp;&nbsp; $ python3 input.py


# Run args.py

From the terminal, run:

&nbsp;&nbsp; $ python args.py -r 10

&nbsp;&nbsp; $ python args.py --radius 10

The following will trigger an error cause we didn't give 
a value to the '-r' flag even

&nbsp;&nbsp; $ python args.py -r


# Run advanced.py

From the terminal, run:

&nbsp;&nbsp; $ python advanced.py -r 5 -r2 6 -r3 4

&nbsp;&nbsp; $ python advanced.py --radius 5 --radius2 6 --radius3 4

The following will trigger an error cause we didn't give 
a value to the '-r' flag even

&nbsp;&nbsp; $ python advanced.py -r -r2 -r3
