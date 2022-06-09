# Argparse tutorial for Python3

# Run input.py

From terminal, run:

$ python3 input.py


# Run args.py

From the terminal, run:

$ python args.py -r 10

$ python args.py --radius 10

The following will trigger an error cause we didn't give 
a value to the '-r' flag even

$ python args.py -r


# Run advanced.py

From the terminal, run:

$ python advanced.py -r 5 -r2 6 -r3 4

$ python advanced.py --radius 5 --radius2 6 --radius3 4

The following will trigger an error cause we didn't give 
a value to the '-r' flag even

$ python advanced.py -r -r2 -r3
