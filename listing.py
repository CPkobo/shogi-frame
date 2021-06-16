import os

files = os.listdir("./docs/resources/")
with open("./docs/js/files_.js", "w", encoding="utf-8") as f:
  f.write("const files = [" + "\n")
  for file in files:
    f.write(f'"{file}",' + "\n")
  f.write("]")

