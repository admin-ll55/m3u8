import re
import sys
if ".draft" not in sys.argv[1]:
  sys.exit(1)
t = open(sys.argv[1], "rb").read().decode()
t = re.sub(r"(\n|\r)", "", t)
t = re.sub(r"  +", " ", t)
open(sys.argv[1].replace(".draft", ""), "wb").write(t.encode())
