print("goodjobbro...")

print("reding is hard")

with open("file1.txt", "r") as f:
    x = f.read()
    if "d" in x:
        print(f"d is in there {x.count("d")} times.")