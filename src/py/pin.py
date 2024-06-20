pin = 4851
attempts = 3
inp = int(None)
corr = bool(None)

print("***Vítejte v naší bance***")
print("Pro přístup k vašemu účtu je nutné zadat čtyřmístný PIN")
print("V případě zadání tří neplatných hodnot bude účet zablokován\n")
if not corr:
    for i in range(0,attempts-1):
        print("Zadejte PIN")
        inp = input()
        if inp == pin:
            corr = 1
            break

if not corr:
    print("Třirát jste zadali nesprávný PIN, váš účet je zablokován")
else:
    print("Jupí jste ve svém účtě!!!")