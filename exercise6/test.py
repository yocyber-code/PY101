import math

N = int(input())
V = []
D = []
C = []
sum_of_all_people_of_party_list = 0
for i in range(N):
    s = input()
    ss = s.split(' ')
    V.append(int(ss[0]))
    D.append(int(ss[1]))
    C.append(int(ss[2]))
    if C[i] > 0:
        sum_of_all_people_of_party_list += V[i]

number_of_people_per_ss = sum_of_all_people_of_party_list / 500.0

target_ss = []
for i in range(N):
    target_ss.append(V[i] / number_of_people_per_ss)

v_per_target_ss = []
for i in range(N):
    if target_ss[i] > 0:
        v_per_target_ss.append(V[i] / target_ss[i])
    else:
        v_per_target_ss.append(0)

party_list_step_1 = []
for i in range(N):
    party_list_step_1.append(target_ss[i] - D[i])
    if party_list_step_1[i] <= 0:
        party_list_step_1[i] = 0

party_list_step_2 = []
for i in range(N):
    party_list_step_2.append(math.floor(party_list_step_1[i]))

party_list_step_3 = []
for i in range(N):
    party_list_step_3.append(
        min(party_list_step_2[i], math.floor(target_ss[i])))
sum_step_3 = sum(party_list_step_3)

if sum_step_3 <= 150:
    party_list_step_2_not_integer = []  # เศษที่เหลือ
    for i in range(N):
        party_list_step_2_not_integer.append(party_list_step_1[i] % 1)

    party_list_step_2_not_integer_copy = []  # เศษที่เหลือ copy
    for i in range(N):
        party_list_step_2_not_integer_copy.append(
            party_list_step_2_not_integer[i])

    num_of_party_list = int(sum_step_3)

    while num_of_party_list < 150:
        max_index = 0
        max_indeies = []
        max_indeies.append(0)
        for i in range(1, N):
            if party_list_step_2_not_integer_copy[max_index] == party_list_step_2_not_integer_copy[i]:
                max_indeies.append(i)
            elif party_list_step_2_not_integer_copy[max_index] < party_list_step_2_not_integer_copy[i]:
                max_index = i
                max_indeies.clear()
                max_indeies.append(i)

        if len(max_indeies) == 1:  # กรณีมีเศษที่มากกว่า
            if party_list_step_3[max_index] + 1 <= target_ss[max_index]:
                party_list_step_3[max_index] += 1
                num_of_party_list += 1
            party_list_step_2_not_integer_copy[max_index] = -100
        elif len(max_indeies) > 1:  # กรณีเศษเท่ากัน
            v_per_target_ss_copy_only_max_above = []
            for i in max_indeies:
                v_per_target_ss_copy_only_max_above.append(
                    v_per_target_ss[i])

            target_max_index = 0
            target_max_indeies = []
            target_max_indeies.append(0)
            for i in range(len(v_per_target_ss_copy_only_max_above)):
                if v_per_target_ss_copy_only_max_above[target_max_index] == v_per_target_ss_copy_only_max_above[i]:
                    target_max_indeies.append(i)
                elif v_per_target_ss_copy_only_max_above[target_max_index] < v_per_target_ss_copy_only_max_above[i]:
                    target_max_index = i
                    target_max_indeies.clear()
                    target_max_indeies.append(i)

            if len(target_max_indeies) >= 1:
                party_list_step_3[target_max_indeies[0]] += 1
                num_of_party_list += 1
                party_list_step_2_not_integer_copy[target_max_indeies[0]] = -100

    for i in range(N):
        print(party_list_step_3[i] + D[i])

elif sum_step_3 > 150:
    party_list_step_4 = []
    party_list_step_4_not_integer = []
    for i in range(N):
        cal = party_list_step_3[i] * 150 / N
        party_list_step_4.append(math.floor(cal))
        party_list_step_4_not_integer.append(cal % 1)

    sum_step_4 = sum(party_list_step_4)

    party_list_step_4_not_integer_copy = []  # เศษที่เหลือ copy
    for i in range(N):
        party_list_step_4_not_integer_copy.append(
            party_list_step_4_not_integer[i])

    num_of_party_list = int(sum_step_4)

    while num_of_party_list < 150:
        max_index = 0
        max_indeies = []
        max_indeies.append(0)
        for i in range(1, N):
            if party_list_step_4_not_integer_copy[max_index] == party_list_step_4_not_integer_copy[i]:
                max_indeies.append(i)
            elif party_list_step_4_not_integer_copy[max_index] < party_list_step_4_not_integer_copy[i]:
                max_index = i
                max_indeies.clear()
                max_indeies.append(i)

        if len(max_indeies) == 1:  # กรณีมีเศษที่มากกว่า
            if party_list_step_4[max_index] + 1 <= target_ss[max_index]:
                party_list_step_4[max_index] += 1
                num_of_party_list += 1
            party_list_step_4_not_integer_copy[max_index] = -100
        elif len(max_indeies) > 1:  # กรณีเศษเท่ากัน
            v_per_target_ss_copy_only_max_above = []
            for i in max_indeies:
                v_per_target_ss_copy_only_max_above.append(
                    v_per_target_ss[i])

            target_max_index = 0
            target_max_indeies = []
            target_max_indeies.append(0)
            for i in range(len(v_per_target_ss_copy_only_max_above)):
                if v_per_target_ss_copy_only_max_above[target_max_index] == v_per_target_ss_copy_only_max_above[i]:
                    target_max_indeies.append(i)
                elif v_per_target_ss_copy_only_max_above[target_max_index] < v_per_target_ss_copy_only_max_above[i]:
                    target_max_index = i
                    target_max_indeies.clear()
                    target_max_indeies.append(i)

            if len(target_max_indeies) >= 1:
                party_list_step_4[target_max_indeies[0]] += 1
                num_of_party_list += 1
                party_list_step_4_not_integer_copy[target_max_indeies[0]] = -100
            else:
                raise Exception("ERROR BY NT 04")
        else:
            raise Exception("ERROR BY NT 03")

    for i in range(N):
        print(party_list_step_4[i] + D[i])
