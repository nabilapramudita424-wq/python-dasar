x = "global"
def tes():
    x = "lokal"     # hanya didalam test()
    print(x)       # lokal
tes()
print(x)             # global   