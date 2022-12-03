import os

def task1():
    inputFile = open(os.getcwd() + "\\AOC\\2022\\day1\\day1input.txt")
    answer = [ 0 ]
    biggestAnswer = 0
    index = 0
    
    for line in inputFile:
        if line == "\n":
            index += 1
            answer.append(0)
        else:
            answer[index] += int(line)
            if biggestAnswer < answer[index]:
                biggestAnswer = answer[index]
    inputFile.close()
    return biggestAnswer

def task2():
    inputFile = open(os.getcwd() + "\\AOC\\2022\\day1\\day1input.txt")
    answer = [ 0 ]
    biggestAnswers = [ 0, 0, 0 ]
    index = 0
    
    for line in inputFile:
        if line == "\n":                    
            if biggestAnswers[0] < answer[index]:
                biggestAnswers[0] = answer[index]
                biggestAnswers.sort()
            index += 1
            answer.append(0)
        else:
            answer[index] += int(line)
    
    inputFile.close()
    return biggestAnswers[0] + biggestAnswers[1] + biggestAnswers[2]

print(task1())
print(task2())