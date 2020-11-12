
import sys


NAME = ["Heinz Frühschicht", "Heinz Spätschicht", "Heinz Nachtschicht", "Frida Frühschicht", "Frida Spätschicht", "Fritz Frühschicht",
"Fritz Spätschicht", "Udo Frühschicht", "Udo Spätschicht", "Udo Nachtschicht", "Ira Frühschicht", "Ira Spätschicht", "Nora Nachtschicht",
"Heinz Frühschicht", "Heinz Spätschicht", "Heinz Nachtschicht", "Frida Frühschicht", "Frida Spätschicht", "Fritz Frühschicht",
"Fritz Spätschicht",  "Udo Frühschicht", "Udo Spätschicht", "Udo Nachtschicht", "Ira Frühschicht", "Ira Spätschicht", "Nora Nachtschicht"]

ASDF = ["fritz früh eins", "fritz spät eins", "frida früh eins", "frida spät eins", "udo früh eins", "udo spät eins", "udo nachts eins", "ira früh eins", "ira spät eins", "heinz früh eins", "heinz spät eins", "heinz nachts eins", "nora nachts eins", "fritz früh", "fritz spät", "frida früh", "frida spät", "udo früh", "udo spät", "udo nacht", "ira früh", "ira spät", "heinz früh", "heinz spät", "heinz nacht", "nora nacht"]

def main():

    try:
        f = open(sys.argv[1],"r")

    except FileNotFoundError:
        print("Invalid file or file path! Exiting...")
        exit(1)

    content = f.readlines()

    for i, line in enumerate(content[1:]):
    	print("Belegung %d:" % (i))
    	line = line.split(" ")
    	for n, char in enumerate(line[:-1]):

    		if n == 13:
    			print("--------------")

    		if char[0] != "-":
    			print(ASDF[int(char)-1] + " " + char)

    		

    	print("\n")


if __name__ == '__main__':
    main()