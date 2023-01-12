T = int(input()); case = []; cnt = 1; new_number = 0; answer = []
numbers = ["no","no","no","no","no","no","no","no","no","no"]
for i in range(T): case.append(input())
for i in range(len(case)):
    while "no" in numbers:
        new_number = str(int(case[i]) * cnt)
        for j in range(len(new_number)):
            if numbers[int(new_number[j])] == "no": numbers[int(new_number[j])] = "yes"
        cnt += 1
    answer.append((cnt-1) * int(case[i]))
    cnt = 1; new_number = 0
    for j in range(len(numbers)): numbers[j] = "no"
for i in range(len(answer)): print("#{} {}".format(i+1, answer[i]))