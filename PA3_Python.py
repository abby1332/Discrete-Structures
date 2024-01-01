#import numpy as np

class PA3_Python(object):
    '''
    # Multiplies matrix 1 by matrix 2
    '''
    def matrix_mult(mat1, mat2):
        if len(mat1[0]) != len(mat2):
            return 0
        result = [[0]*len(mat2[0]) for i in range(len(mat1))]
        for i in range(len(mat1)):
            # iterate through columns of mat2
            for j in range(len(mat2[0])):
                # iterate through rows of mat2
                for k in range(len(mat2)):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        return result
    '''
    # Make sure the observation follows all the rules
    ''' 
    def validate_observation(observation):
        
        #Can only be R or D
        if set(observation) != set(['R', 'D']):
             raise ValueError("Observation record must only contain 'R' and 'D' characters")
         
        seq_count = {'RR': 0, 'RD': 0, 'DD': 0, 'DR': 0}

        # Iterate over the string and check for each sequence
        for i in range(len(observation)-1):
            if observation[i:i+2] == 'RR':
                 seq_count['RR'] += 1
            elif observation[i:i+2] == 'RD':
                 seq_count['RD'] += 1
            elif observation[i:i+2] == 'DD':
                 seq_count['DD'] += 1
            elif observation[i:i+2] == 'DR':
                seq_count['DR'] += 1

        # # Check that all sequences are present, and raise an error if not
        for seq in seq_count:
            if seq_count[seq] == 0:
                raise ValueError(f"Observation record must include all four possible transitions"
                                  + " (RR, RD, DR, DD) Sequence '{seq}' is missing from observation")
    '''
    # Create the transition matrix from the given observation points
    '''
    def calc_transition_matrix(observation_string):
        PA3_Python.validate_observation(observation_string)
        dd_count = dr_count = rd_count = rr_count = 0

        # Count the transitions
        for i in range(len(observation_string)-1):
            if observation_string[i:i+2] == 'DD':
                dd_count += 1
            elif observation_string[i:i+2] == 'DR':
                dr_count += 1
            elif observation_string[i:i+2] == 'RD':
                rd_count += 1
            elif observation_string[i:i+2] == 'RR':
                rr_count += 1
        
        # Calculate the fractions
        dd_fraction = dd_count / (dd_count + dr_count)
        dr_fraction = dr_count / (dd_count + dr_count)
        rd_fraction = rd_count / (rd_count + rr_count)
        rr_fraction = rr_count / (rd_count + rr_count)
        
        # Create the 2x2 matrix
        transition_matrix = [[dd_fraction, dr_fraction], [rd_fraction, rr_fraction]]
        
        return transition_matrix
    
        
    '''
    # Generates the forecast for the next 7 days given the transition matrix and the current weather
    # The forecast should be a 2x7 matrix where each row is a forecast for a day
    '''
    def generate_forecast(transition_matrix, curr_weather):
        #Find initial state vector
        if(curr_weather == 'D'):
            initial_state_vector = [[1, 0]]
        else:
            initial_state_vector = [[0, 1]]

        #Generate empty 7x2 matrix
        forecast =  [[0] * 2 for i in range(7)]

        #Iterate 7 times to find forecast for the next 7 days
        for day in range(1,8):
            T = transition_matrix
            for i in range(1,day):
                #Raise T to the power of whatever day it is
                if(day > 1):
                    T = PA3_Python.matrix_mult(T, transition_matrix)
            print("Transition matrix to the i power: ", T)
            #Transition matrix ^ power of day * initial state vector
            TP = PA3_Python.matrix_mult(initial_state_vector, T)
            #Put values into the empty matrix
            forecast[day-1][0] = TP[0][0]  
            forecast[day-1][1] = TP[0][1]
        
        return forecast
    
    '''
    # Generates the climate prediction (i.e., steady state vector) given the transition matrix, current 
    # weather, and precision
    '''
    def generate_climate_prediction(transition_matrix, curr_weather, precision):
     #Find initial state vector
     if(curr_weather == 'D'):
            initial_state_vector = [[1, 0]]
     else:
            initial_state_vector = [[0, 1]]
        
     n_rows, n_cols = len(transition_matrix), len(transition_matrix[0])
        # Initialize the state vector
     state_vector = initial_state_vector
        
        # Iterate until the steady-state vector is reached
     while True:
        next_state_vector = PA3_Python.matrix_mult(state_vector, transition_matrix)
        diff = [0,0]
        # Check if the difference between the state vectors is less than the precision
        diff[0] = (abs(next_state_vector[0][0] - state_vector[0][0]))
        diff[1] = (abs(next_state_vector[0][1] - state_vector[0][1]))

        if all(d < precision for d in diff):
            return next_state_vector
                
        state_vector = next_state_vector


    '''
    # Print the forecasted weather predictions 
    '''
    def print_predictions(forecast):
        # Print first line
        print(f'[{forecast[0]},')
        
        # Print middle 5 lines
        for i in range(1, len(forecast) - 1):
            print(f' {forecast[i]},')
        
        # Print the last line
        print(f' {forecast[6]}]')
    
    '''
    # Print the steady state vector containing the climate prediction
    '''
    def print_steady_state(steady_state):
        print(steady_state[0])

observation = 'DDRRRDRDDD'
precision = 0.01

transition_matrix = PA3_Python.calc_transition_matrix(observation)
print("Transition matrix:", transition_matrix)

forecast = PA3_Python.generate_forecast(transition_matrix, 'D')
print("Forecast: ", forecast)

climate = PA3_Python.generate_climate_prediction(transition_matrix, 'D', precision)
print("Climate:", climate)