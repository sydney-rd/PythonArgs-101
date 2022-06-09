# Argparse tutorial for Python3

# Run input.py

From terminal, run:
$ python3 input.py


# Run argparse.py

From the terminal, run:

$ python argparse.py -r 10

$ python argparse.py --radius 10

The following will trigger an error cause we didn't give 
a value to the '-r' flag even

$ python argparse.py -r


# Run advanced.py

From the terminal, run:

$ python advanced.py -r 5 -r2 6 -r3 4

$ python advanced.py --radius 5 --radius2 6 --radius3 4

The following will trigger an error cause we didn't give 
a value to the '-r' flag even

$ python argparse.py -r -r2 -r3
