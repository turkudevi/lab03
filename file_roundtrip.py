path = "rt.txt"
f = open(path, "w", encoding="utf-8")
f.write("hello")
f.close()
f = open(path, "r", encoding="utf-8")
data = f.read()
f.close()
if data == "hello":
    print("ROUNDTRIP OK")
else:
    print("ROUNDTRIP FAIL")