from pathlib import Path
path = Path("python-learning-journey/pi_digits.txt")
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

writefile = Path("python-learning-journey/writing file.txt")
texts = "I love programming.\n"
texts += "I love creating new games.\n"
texts += "I also love to learn new languages.\nI also love playing football."
writefile.write_text(texts)
