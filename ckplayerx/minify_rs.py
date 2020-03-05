import re
import sys
t = open(sys.argv[1], "rb").read().decode()
t = re.sub(r"  +", " ", t)
t = re.sub(r"\n", "", t)
open(sys.argv[1].replace(".draft", ""), "wb").write(t.encode())
