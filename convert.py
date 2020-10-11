""" A small script to convert covid notifications from Android phone to csv """
import json, sys

# Read the input file
try:
    INPUT_FILE=(sys.argv[1])
except:
    print("No file supplied, please give filename as first argument")
    exit(1)


if INPUT_FILE:
    OUTPUT = ""
    with open(INPUT_FILE, 'r') as f:
        EXPOSURE_CHECKS = json.loads(f.read())
        HEADER = []
        OUTPUTS = []
    for c in EXPOSURE_CHECKS:
        # TODO potential bug if header changes
        HEADER = c.keys()
        OUTPUTS.append(list(c.values()))

    LINES = []
    for o in OUTPUTS:
        line = ', '.join(['"{}"'.format(x) for x in o])
        LINES.append(line)
        print("\n".join(LINES))
        OUT = '"' + '","'.join(HEADER) + '"\n' + "\n".join(LINES)
        print(f'{OUT}')
    with open('output.csv', 'w') as f:
        f.write(OUT)
