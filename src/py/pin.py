pin = 4851
attempts = 3
inp = None
corr = False

print("***Vítejte v naší bance***")
print("Pro přístup k vašemu účtu je nutné zadat čtyřmístný PIN")
print("V případě zadání tří neplatných hodnot bude účet zablokován\n")
if not corr:
    for i in range(0,attempts):
        if i < 0:
            print("Špatný PIN")
        print("Zadejte PIN")
        inp = int(input())
        while len(str(inp)) != 4:
            print("Špatná délka PIN! Vaše délka:", len(str(inp)), ". Očekávaná délka:", len(str(pin)))
            inp = input()
        if inp == pin:
            corr = 1
            break

if not corr:
    print("Třirát jste zadali nesprávný PIN, váš účet je zablokován")
else:
    print("Jupí jste ve svém účtě!!!")