import math
from Evaluator import evaluate

defVars = {}
premise_list = "p^q"
operators = ['^', 'V', '~', '>']

def generate_combinations(letters):
    result = []
    for i in range(2**len(letters)):
        combination = {}
        for j, letter in enumerate(letters):
            combination[letter] = (i & (1 << j)) != 0
        result.append(combination)
    return result

defVars = generate_combinations(['p', 'q'])

def evaluatePremiseList(premiseList, combinations):
    result = []
    for dictionary in combinations:
        result.append(evaluate(premiseList, **dictionary))
    return result


# testDict = {'p': True, 'q': False}
# sss = evaluatePremiseList("pVq", generate_combinations(['p','q']))
# conclusion = ["q"]
# print(evaluatePremiseList("q", generate_combinations(['q'])))

# # premise = ["pVq", "p"]
# conclusion = ["p"]
# #print(evaluatePremiseList( ("(" + str(premise[0]) + ")" + "(" + str(premise[1]) + ")" + ">" + str(conclusion)), sss))
# #print(evaluatePremiseList("((pVq)(p))>p", generate_combinations(['p','q'])))

# urmom = generate_combinations(['p','q'])
# print(urmom)
# urdad = generate_combinations(['p'])
# #urmom.append(urdad)
# print(urmom)
# print(urdad)
# print(evaluatePremiseList("((pVq)^p)>p", urmom))
# print(evaluatePremiseList("(pVq)^p", urmom))

premise_list = ["pVq", "p"]
operators = ["V", "^", "~", ">"]
# lettersList = []
# for premise in premise_list:
#     for char in premise:
#         if char.isalpha() and char not in (lettersList and operators):
#             lettersList.append(char)

# print(lettersList)

def reformat(premise_list, conclusion):
 builder = "("
 for premise in premise_list:
    builder += "("
    builder += premise
    builder += ")^"
 builder = builder[:-1]
 builder += ")>("+ conclusion + ")"
 return builder

print(reformat(["pVq", "p"], "p"))
