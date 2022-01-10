choice = input("CHOOSE VERSION (SEE FILES IF UNSURE):\n[1] (NEWEST VERION, RECOMMENDED) OR [2]\n>>> ")
if choice == "1":
  exec(open("./MainVersion.py").read())
elif choice == "2":
  exec(open("./AlternativeVersion.py").read())
