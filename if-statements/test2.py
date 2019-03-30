with open("Belmullet.txt", "r") as f:

# readlines will read all lines of text
    lines = f.readlines()

# use of strip() removes space between lines
    desired_lines = [x.strip() for x in lines[1::2]]

print(desired_lines)