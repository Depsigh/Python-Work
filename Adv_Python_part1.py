import os 

def main():
    path = os.mkdir("CyberSecurity-notes")
    for i in range (1,25):
        os.mkdir("CyberSecurity-notes/week") + str(i)

        for j in range (1,4):
            os.mkdir("CyberSecurity-notes/week") + str(i)+'/Day-' + str(j)

main()