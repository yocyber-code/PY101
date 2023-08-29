import math

total_party = int(input())
votes = []
while len(votes) < total_party:
    party_vote = str(input()).split(' ')
    for i in range(len(party_vote)):
        party_vote[i] = int(party_vote[i])
    votes.append(party_vote)

total_vote = 0
for party_vote in votes:
    if party_vote[2] != 0:
        total_vote += party_vote[0]

quota_score = total_vote / 500
target_parliament_member = []

for party_vote in votes:
    target_parliament_member.append(party_vote[0] / quota_score)

partyList_Step_1 = []
for i in range(total_party):
    partyList = target_parliament_member[i] - votes[i][1]
    if partyList < 0:
        partyList = 0
    partyList_Step_1.append(partyList)

partyList_Step_2 = []
party_list_not_integer = []
for party_list in partyList_Step_1:
    partyList_Step_2.append(math.floor(party_list))
    party_list_not_integer.append(party_list % 1)

partyList_Step_3 = []
for i in range(len(partyList_Step_2)):
    min1 = min(math.floor(target_parliament_member[i]), partyList_Step_2[i])
    partyList_Step_3.append(min1)

total_party_list = sum(partyList_Step_2)

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

party_list_not_integer_temp = party_list_not_integer.copy()
if total_party_list < 150:
    multiple = 1
    while total_party_list < 150:
        # if (sum(party_list_not_integer) == 0):
        #     break
        max1 = max(party_list_not_integer)
        max_index_list = []
        for i in range(len(party_list_not_integer)):
            if party_list_not_integer[i] == max1:
                max_index_list.append(i)
        if len(max_index_list) == total_party:
            multiple += 1
        if len(max_index_list) > 1:
            avg_target = 0
            max_index_list_temp = max_index_list.copy()
            max_index_list.clear()
            for i in max_index_list_temp:
                avg_temp = votes[i][0] / (votes[i][0] / quota_score)
                if avg_temp >= avg_target:
                    avg_target = avg_temp
                    max_index_list.append(i)
            # v_max = []
            # for i in range(total_party):
            #     v_max.append(votes[i][0] / (votes[i][0] / quota_score))

            # max_target = 0
            # target_max_index = [0]
            # for i in range(1, total_party, 1):
            #     if i in max_index_list:
            #         if v_max[max_target] == v_max[i]:
            #             target_max_index.append(i)
            #         else:
            #             max_target = i
            #             target_max_index.clear()
            #             target_max_index.append(i)

            # if len(target_max_index) >= 1:
            #     for i in target_max_index:
            #         if partyList_Step_3[i] + 1 <= target_parliament_member[i]:
            #             max_index_list[0] = i
            #             break
        for index in max_index_list:
            if partyList_Step_3[index] + 1 <= target_parliament_member[index]:
                partyList_Step_3[index] += 1
                total_party_list += 1
                break
            else:
                party_list_not_integer[index] = -100 * multiple
        party_list_not_integer[index] = -100 * multiple

for i in range(total_party):
    print(votes[i][1] + partyList_Step_3[i])
 