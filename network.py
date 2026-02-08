#Programmer's Note: This was one of my very first projects, written during my introduction to programming (2021 Pre-AI era).
# I'm keeping it as a milestone, a reminder of where I started.

import sys

with open("output.txt","w") as output: 
    output.write("Welcome to Assignment 3\n-------------------------------\n")
with open(sys.argv[1],"r") as smnfile:
    network={}
    lineslist=smnfile.readlines()
    for line in lineslist:
        nline=line.strip().split(":")        
        user=nline[0]
        friends=nline[1].split(" ")
        network[user]=friends
    userlist=network.keys()

#adds a new user to network, prints error if user already exists in network
def anu(usr):  
    if usr not in userlist:
        network[usr]=[]
        output.write("User '{}' has been added to the social network successfully\n".format(usr))
    else:
        output.write("ERROR: Wrong input type! for 'ANU'! -- This user already exists!!\n") 

#deletes a user and all his/her relations from network, prints error if there is no such user in network
def deu(usr):
    if usr in   userlist:
        frends=network[usr]
        for fr in frends:
            network[fr].remove(usr)
        network.pop(usr)
        output.write("User '{}' and his/her all relations have been deleted successfully\n".format(usr))
    else:
        output.write("ERROR: Wrong input type! for 'DEU'!--There is no user named '{}'!!\n".format(usr))   

#adds a relation between two users, prints error if there is no such user in network or if there is already a relation between them
def anf(user,friend):
    if (user in userlist) and (friend not in network):
        output.write("ERROR: Wrong input type! for'ANF'! -- No user named '{}' found!!\n".format(friend))
    elif (user not in userlist) and (friend in network):
        output.write("ERROR: Wrong input type! for'ANF'! -- No user named '{}' found!!\n".format(user))
    elif  (user not in userlist) and (friend not in network): 
        output.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{}' and '{}' found!\n".format(user,friend))
    elif friend in network[user]:
        output.write("ERROR: A relation between '{}' and '{}' already exists!!\n".format(user,friend))
    else:
        network[user].append(friend)
        network[friend].append(user)
        output.write("Relation between '{}' and '{}' has been added successfully\n".format(user,friend))

#deletes a relation between two users, prints error if there is no such user in network or if there is no relation between them
def deff(user,friend):
    if (user in userlist) and (friend not in network):
        output.write("ERROR: Wrong input type! for'DEF'! -- No user named '{}' found!!\n".format(friend))
    elif (user not in userlist) and (friend in network):
        output.write("ERROR: Wrong input type! for'DEF'! -- No user named '{}' found!!\n".format(user))
    elif  (user not in userlist) and (friend not in network): 
        output.write("ERROR: Wrong input type! for 'DEF'! -- No user named '{}' and '{}' found!\n".format(user,friend))
    elif friend not in network[user]:
        output.write("ERROR: No relation between '{}' and '{}' found!!\n".format(user,friend))
    else:
        network[user].remove(friend)
        network[friend].remove(user)
        output.write(f"Relation between '{user}' and '{friend}' has been deleted successfully\n")

# counts the number of friends of a user, prints error if there is no such user in network
def countf(usr):
    if usr in   userlist:
        output.write("User '{}' has '{}' friends\n".format(usr,len(network[usr])))
    else:
        output.write("ERROR: Wrong input type! for 'CF'!--No user named  '{}' found!\n".format(usr))

#finds possible friends of a user with maximum distance 1,2 or 3
# prints error if there is no such user in network or if the maximum distance is out of range
def fpf(usr, maxd):
    if usr in userlist:
        if maxd == 1:
            output.write("User '{}' has {} possible friends when maximum distance is 1\n".format(usr, len(network[usr])))
            output.write("These possible friends: {}\n ".format(str(sorted(network[usr])).replace("[","{").replace("]","}")))
        elif maxd == 2:
            friendslist2 = network[usr].copy()
            for frnd in network[usr]:
                friendslist2 += network[frnd]
            possible_fr = set(friendslist2)
            possible_fr.remove(usr)
            possible_fr = sorted(possible_fr)
            output.write("User '{}' has {} possible friends when maximum distance is 2\n".format(usr, len(possible_fr)))
            output.write("These possible friends: {}\n ".format(str(possible_fr).replace("[","{").replace("]","}")))
        elif maxd==3:
            friendslist3 = network[usr].copy()
            for frnd in network[usr]:
                friendslist3 += network[frnd]
            friendslist3 = set(friendslist3)
            friendslist3.remove(usr)
            poss_fr=set()
            for fr in sorted(friendslist3):
                for friend3 in network[fr]:
                    poss_fr.add(friend3)
            possible_friend=friendslist3|poss_fr
            possible_friend.remove(usr)
            output.write("User '{}' has {} possible friends when maximum distance is 3\n".format(usr, len(sorted(possible_friend))))
            output.write("These possible friends: {} \n".format(str(sorted(possible_friend)).replace("[","{").replace("]","}")))
        else:
            output.write("ERROR: Maximum distance is out of range!!\n")
    else:
        output.write("ERROR: Wrong input type! for 'FPF'! -- No user named '{}' found!\n".format(usr))

#suggests friends for a user with mutually degree 2 or 3
# prints error if there is no such user in network or if the mutually degree is out of range

def sf(usr,md):
    if usr in userlist:
        if md in [2,3]:           
            sflist=[]
            for frnd in network[usr]:
                friendsfriends=network[frnd].copy()
                friendsfriends.pop(friendsfriends.index(usr))
                sflist.extend(friendsfriends)
                md3list=[]
                md2list=[]
                for fr in sflist:
                    if sflist.count(fr)==3:
                        md3list.append(fr)
                    elif sflist.count(fr)==2:
                        md2list.append(fr)  
            md3list=set(md3list)
            md3list=sorted(md3list)
            md2list=set(md2list)
            md2list=sorted(md2list)
            if md==3:
                output.write("Suggestion List for '{}' (when MD is 3):\n".format(usr))
                for i in md3list:
                    output.write("'{}' has 3 mutual friends with '{}'\n".format(usr,i))
                output.write("The suggested friends for '{}': {}\n".format(usr,str(md3list)[1:-1]))
            if md==2:
                if len(md3list)==0:
                    output.write("Suggestion List for '{}' (when MD is 2):\n".format(usr))
                    for k in md2list:
                        output.write("'{}' has 2 mutual friends with '{}'\n".format(usr,k))
                    output.write("The suggested friends for '{}': {}\n".format(usr,str(md2list)[1:-1]))

                else:
                    mdlist=md2list+md3list
                    mdlist.sort()
                    output.write("Suggestion List for '{}' (when MD is 2):\n".format(usr))
                    for k in md2list:
                        output.write("'{}' has 2 mutual friends with '{}'\n".format(usr,k))
                    for i in md3list:
                        output.write("'{}' has 3 mutual friends with '{}'\n".format(usr,i))
                    output.write("The suggested friends for '{}': {}\n".format(usr,str(mdlist)[1:-1]))
        else:
            output.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")        
    else:
        output.write(f"ERROR: Wrong input type! for 'SF'! -- No user named '{usr}' found!!\n")


with open(sys.argv[2],"r") as cmdfile:
     cmdlines=cmdfile.readlines()
     for line in cmdlines:
        cmdlines[cmdlines.index(line)]=line.strip().split(" ")
with open("output.txt","a") as output:
    for cmd in cmdlines:
        if cmd[0]=="ANU":
            anu(cmd[1])
        elif cmd[0]=="DEU":
            deu(cmd[1])
        elif cmd[0]=="ANF":
            anf(cmd[1],cmd[2])
        elif cmd[0]=="DEF":
            deff(cmd[1],cmd[2])
        elif cmd[0]=="CF":
            countf(cmd[1])
        elif cmd[0]=="FPF":
            fpf(cmd[1],int(cmd[2]))
        elif cmd[0]=="SF":
            sf(cmd[1],int(cmd[2]))
