import sys
import math

transition_prob = [[math.log10(0.8),math.log10(0.2)],[math.log10(0.7),math.log10(0.3)]]
emission_prob = [0.1,0.1,0.1,0.1,0.1,0.5]

# perform viterbi
def viterbi(observations):
    # v is a matrix that store result as (max_prob,prev_dice_index,dice_type)
    v = [[0 for x in range(len(observations))] for y in range(2)]
    path = []

    # initialization
    v[0][0] = (math.log10(0.5*emission_prob[observations[0]-1]),None,"F")   #v[0] = F
    v[1][0] = (math.log10(0.5*emission_prob[observations[0]-1]),None,"L")   #v[1] = L

    # recursion
    for i in range(1,len(observations)):
        max = v[0][i-1][0]+transition_prob[0][0]
        prev = v[0][i-1]
        if v[1][i-1][0]+transition_prob[1][0] > max:
            max = v[1][i-1][0]+transition_prob[1][0]
            prev = v[1][i-1]
        v[0][i] = (math.log10(1/6)+max,prev,"F")
        
        max = v[0][i-1][0]+transition_prob[0][1]
        prev = v[0][i-1]
        if v[1][i-1][0]+transition_prob[1][1] > max:
            max = v[1][i-1][0]+transition_prob[1][1]
            prev = v[1][i-1]
        v[1][i] = (math.log10(emission_prob[observations[i]-1])+max,prev,"L")

    # termination
    max = v[0][len(observations)-1][0]
    current = v[0][len(observations)-1]
    if v[1][len(observations)-1][0] > max:
        max = v[1][len(observations)-1][0]
        current = v[1][len(observations)-1]
    
    for i in range(0,len(observations)):
        path = [current[2]]+path
        current = current[1]
    return path