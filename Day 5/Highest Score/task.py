# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

student_scores = [8, 65, 89, 86, 55, 91, 64, 89]
counter1 = 0
counter2 = 0

for score in student_scores:
    if score > counter1:
        counter1 = score

print(counter1)
    # if score > student_scores[score.__index__()+1]:
    #     counter1 = score
    # if score.__index__() < (len(student_scores) - 1):
    #     print(student_scores[score.__index__()])
    # print(score.__index__())
    # print(f"{score}  {student_scores.index(score)}")
