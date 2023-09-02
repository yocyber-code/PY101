import math
import sys

total_party = int(input())
votes = []
strArr = []
for i in range(total_party):
    party_vote = input()
    strArr.append(party_vote)

for i in range(len(strArr)):
    strSplit = strArr[i].split(" ")
    vote_cast_int = []
    for j in range(len(strSplit)):
        vote_cast_int.append(int(strSplit[j]))
    votes.append(vote_cast_int.copy())

total_vote = 0
for i in range(total_party):
    if votes[i][2] > 0:
        total_vote += votes[i][0]

quota_score = total_vote / 500.0
target_parliament_member = []

for i in range(total_party):
    if votes[i][0] <= 0:
        target_parliament_member.append(0)
    else:
        target_parliament_member.append(votes[i][0] / quota_score)

v_per_target_ss = []
for i in range(total_party):
    if target_parliament_member[i] > 0:
        v_per_target_ss.append(votes[i][0] / target_parliament_member[i])
    else:
        v_per_target_ss.append(0)

partyList_Step_3 = []
party_list_not_integer = []
for i in range(total_party):
    partyList = target_parliament_member[i] - votes[i][1]
    if partyList < 0:
        partyList = 0
    party_list_not_integer.append(partyList % 1)
    partyList_Step_3.append(math.floor(partyList))

total_party_list = sum(partyList_Step_3)

if total_party_list > 150:
    partyList_Step_4 = []
    party_list_not_integer.clear()
    party_list_not_integer = []
    for party_list in partyList_Step_3:
        new_party_list = party_list * 150 / total_party_list
        partyList_Step_4.append(math.floor(new_party_list))
        party_list_not_integer.append(new_party_list % 1)
    partyList_Step_3.clear()
    partyList_Step_3 = partyList_Step_4
    total_party_list = sum(partyList_Step_3)

if total_party_list < 150:
    while total_party_list < 150:
        max1 = max(party_list_not_integer)
        max_index_list = [i for i, val in enumerate(
            party_list_not_integer) if val == max1]
        if len(max_index_list) > 1:
            avg_target = -sys.maxsize - 1
            max_index_list_temp = max_index_list.copy()
            max_index_list.clear()
            for i in max_index_list_temp:
                if v_per_target_ss[i] >= avg_target:
                    avg_target = v_per_target_ss[i]
                    max_index_list.append(i)

        index = max_index_list[0]
        if partyList_Step_3[index] < target_parliament_member[index] and partyList_Step_3[index] < votes[index][2]:
            partyList_Step_3[index] += 1
            total_party_list += 1
        party_list_not_integer[index] = -100

for i in range(total_party):
    print(votes[i][1] + partyList_Step_3[i])
