import re

def arithmetic_arranger(problemList, showAwnser=False):
    returnDict = dict({})
    if len(problemList) > 5:
        return ("Error: Too many problems.")
    for index in range(len(problemList)):
        reString = re.match('([0-9a-zA-Z]+)\W([/+-])\W([0-9a-zA-Z]+)', problemList[index])
        if reString.group(2) == '/':
            return "Error: Operator must be '+' or '-'."
        try:
            int(reString.group(1))
            int(reString.group(3))
        except ValueError:
            return "Error: Numbers must only contain digits."
        if len(reString.group(1)) > 4 or len(reString.group(3)) > 4:
            return "Error: Numbers cannot be more than four digits."
        returnDict[index] = {'num1': reString.group(1), 'operator': reString.group(2), 'num2': reString.group(3)}
    line1, line2, line3, line4 = '', '', '', '' # empty lines that we are going to append to
    for key in returnDict:
        num1Len, num2Len = len(returnDict[key]["num1"]), len(returnDict[key]["num2"])
        if num1Len == 1 and num2Len == 1:
            line1Format = 3
            line2Format = 1
        elif num1Len == 1 and num2Len == 4:
            line1Format = 6
            line2Format = 1
        elif num1Len == 2 and num2Len == 1:
            line1Format = 4
            line2Format = 2
        elif num1Len == 2 and num2Len == 2:
            line1Format = 4
            line2Format = 2
        elif num1Len == 4 and num2Len == 1:
            line1Format = 6
            line2Format = 4
        elif num1Len == 4 and num2Len == 4:
            line1Format = 6
            line2Format = 4
        else:
            line1Format = 5
            line2Format = 3
        temp1 = f'{returnDict[key]["num1"]:>{line1Format}}'
        line1 += temp1 + '    '
        temp2 = f'{returnDict[key]["operator"]} {returnDict[key]["num2"]:>{line2Format}}'
        line2 += temp2 + '    '
        temp3 = '-' * max(len(temp1), len(temp2)) + '    '
        line3 += temp3
        temp4 = f'{eval(returnDict[key]["num1"] + returnDict[key]["operator"] + returnDict[key]["num2"]):>5}    '
        if len(str(eval(returnDict[key]["num1"] + returnDict[key]["operator"] + returnDict[key]["num2"]))) == 5:
            temp4 = f'{eval(returnDict[key]["num1"] + returnDict[key]["operator"] + returnDict[key]["num2"]):>6}   '
        line4 += temp4
    if showAwnser:
        return line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4] + '\n' + line4[:-4]
    else:
        return line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4]