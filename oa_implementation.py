# Test Case #1 from Instructions
reference_trajectory_dict = {
    "C":1,
    "D":2,
    "G":0,
    "F":2,
    "E":3
}

'''
Original Algorithm Implementation
'''
def oa_sort(array):
    # For every number from first number
    for i in range(len(array)):
        # Compare the number above to each subsequent number after that number
        for j in range(i + 1, len(array)):
            # If the "i" number is greater than the "j" number
            if(array[i] > array[j]):
                # Switch places
                array[i], array[j] = array[j], array[i]
    return array

# Sort the trajectory value
sorted_trajs = oa_sort(list(reference_trajectory_dict.values())) # Sort the values
sorted_note_dict = {}

''' 
Sort the reference trajectory 
'''
def sort_reference_notes(array,dict):
    # For each trajectory value
    for i in array:
        # For each note
        for k in dict.keys():
            # If the trajectory value of the note is equal to the trajectory value found in the sorted array
            if dict[k] == i:
                # Add the note along with its trajectory value to the new dictionary
                sorted_note_dict[k] = dict[k]
    # Return the new dictionary when done
    return sorted_note_dict

# Print the sorted notes along with their corresponding trajectories
print(sort_reference_notes(sorted_trajs, reference_trajectory_dict))