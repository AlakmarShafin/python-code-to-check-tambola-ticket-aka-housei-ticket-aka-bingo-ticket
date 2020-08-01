"""
Created on Sun Jul 26 09:46:35 2020

@author: Shafin()
"""

print("How many Ticket You Have?")
n= int(input())
tickets=[]
for i in range(n):
    print("enter your ticket no:")
    tickets.append([input()])
    print("Enter Line 1:")
    tickets[i] = tickets[i]+[["1st Line"]+list(map(int,input().split()))]
    print("Enter Line 2:")
    tickets[i] = tickets[i]+[["2nd Line"]+list(map(int,input().split()))]
    print("Enter Line 3:")
    tickets[i] = tickets[i]+[["3rd Line"]+list(map(int,input().split()))]
    tickets[i] = tickets[i] + [["          ",tickets[i][1][1],tickets[i][1][5],tickets[i][3][1],tickets[i][3][5]]]
    tickets[i] = tickets[i] +[[5]]
print(tickets)
housie=3
fourcorner=1
earlyfi=1
l1=1
l2=1
l3=1
nums=[]
while True:
    try:
        x=int(input().strip())
        for i in tickets:
            for j in range(1,5):
                if type(i[j]) !=type("") and x in i[j]:
                    i[j].remove(x)
                    nums = nums +[x]
                    #i[5][0] = i[5][0]-1
                    print(str(x)+" in "+i[0]+" "+i[j][0])
            if len(i[4]) == 1 and fourcorner !=0 :
                fourcorner = fourcorner -1
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
                print("WON 4 corners"+" in "+i[0]+" ")
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
            #print(i[5][0])
            if len(i[1])+len(i[2])+len(i[3]) == 13 and earlyfi !=0:
                earlyfi = earlyfi -1
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
                print("WON Early 5"+" in "+i[0]+" ")
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
            if len(i[1]) == 1 and l1 != 0 :
                l1 = l1 - 1
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
                print("WON 1st Line in "+i[0])
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
            if len(i[2]) == 1 and l2 != 0 :
                l2 = l2 - 1
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
                print("WON 2nd Line in "+i[0])
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
            if len(i[3]) == 1 and l3 != 0 :
                l3 = l3 - 1
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
                print("WON 3rd Line in "+i[0])
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
            if len(i[1])+len(i[2])+len(i[3]) == 3 and housie != 0:
                housie = housie -1
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
                print("HOUSIE of "+str(i[0]))
                print("::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::::")
    except:
        y = input()
        if y == "quit":
            break
        if y == "nums":
            print(nums)
        if y == "h":
            if housie !=0:
                housie = housie - 1
        if y == "ef":
            if earlyfi !=0:
                earlyfi = earlyfi - 1
        if y == "fc":
            if fourcorner !=0:
                fourcorner = fourcorner - 1
        if y == "l1":
            if l1 !=0:
                l1 = l1 - 1                
        if y == "l2":
            if l2 !=0:
                l2 = l2 - 1
        if y == "l2":
            if l2 !=0:
                l2 = l2 - 1
        continue            
