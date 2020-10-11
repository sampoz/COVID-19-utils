""" A small script to convert covid notifications from Android phone to csv """
import json

print("test")
OUTPUT = ""
with open('all-exposure-checks.json', 'r') as f:
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
