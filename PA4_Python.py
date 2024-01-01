import random
'''
* Perform one instance of the Monty Hall Problem
*
* should_switch: set to true if running an experiment where the contestant should
*    switch their guess every time. Set to false if not
*
* Returns true if the contestant selected the door with the car behind it. Returns
*    false otherwise.
'''
def run_trial(should_switch) -> bool:
  car = random.randint(1,3)
  pick = random.randint(1,3)
  shown_door = open_door(car, pick)
  if should_switch == True:
    pick = switch(shown_door, pick)
  if pick == car:
    return True
  return False

'''
* Reveal a goat door
* Car is the door with a car behind it
* Pick is the players choice door
'''
def open_door(car, pick):
  i = 1
  while (i == car or i == pick):
    i = (i+1)
  return i

'''
* Switch your pick to a different one.
'''
def switch(shown_door, pick):
  i = 1
  while (i == shown_door or i == pick):
    i = (i+1)
  return i

'''
* Execute an entire experiment (i.e., execute the specified number of trials)
* and return the desired results
* 
* num_trials: number of trials to execute in this experiment
* should_switch: set to true if running an experiment where the contestant should
*    switch their guess every time. Set to false if not
*
* Returns the percentage of games won (i.e., number of wins / number of trials)
'''
def run_experiment(num_trials: int, should_switch: bool) -> float:
  wins = 0
  for i in range(0, num_trials):
    result = run_trial(should_switch)
    if result == True: wins+=1
  return wins/num_trials

'''
* This is a stub that you can use to test the rest of the program. The code in this
* method will not be executed during grading, so you don't need to worry about user
* input.
'''
def main():
  num_trials = 1000
  should_switch = True
  
  prob = run_experiment(num_trials, should_switch)
  print(prob)

main()