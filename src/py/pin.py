pin = 4851
attempts = 3
inp = int(None)

print("***Vítejte v naší bance***")
print("Pro přístup k vašemu účtu je nutné zadat čtyřmístný PIN")
print("V případě zadání tří neplatných hodnot bude účet zablokován\n")
for i in range(0,attempts-1):
    print("Zadejte PIN")
    inp = input()
    if inp == pin:
        break
