from collections import defaultdict

# Test Case #1 from Instructions
reference_trajectory_dict = {
    "C":1,
    "D":2,
    "G":0,
    "F":2,
    "E":3
}

print(f"Original Reference Trajectory: {reference_trajectory_dict}\n")

'''
Original Algorithm Implementation
'''
def oa_sort(array):
    # For every number from first number
    for compare in range(len(array)):
        # Compare the number above to each subsequent number after that number
        for compared_to in range(compare + 1, len(array)):
            # If the compare number is greater than the number that is being compared to
            if(array[compare] > array[compared_to]):
                # Switch places
                array[compare], array[compared_to] = array[compared_to], array[compare]
    return array

# Sort the trajectory value
sorted_trajs = oa_sort(list(reference_trajectory_dict.values())) # Sort the values
sorted_note_dict = {}

''' 
Sort the reference trajectory 
'''
def sort_reference_notes(array,dict,empty_dict):
    # For each trajectory value
    for i in array:
        # For each note
        for k in dict.keys():
            # If the trajectory value of the note is equal to the trajectory value found in the sorted array
            if dict[k] == i:
                # Add the note along with its trajectory value to the new dictionary
                empty_dict[k] = dict[k]
    # Return the new dictionary when done
    return empty_dict

# Print the sorted notes along with their corresponding trajectories
sorted_notes = sort_reference_notes(sorted_trajs, reference_trajectory_dict,sorted_note_dict)
print(sorted_notes)

variation_trajectory = [0.5,-1,2,3,4]

index_added_number = 0
variation_number_list = []

# Find the values of trajectory values 
for num_index, num in enumerate(variation_trajectory):
    for value_index, value in enumerate(list(sorted_notes.values())[::-1]):
        if (num <= value):
            index_added_number = (list(sorted_notes.values())[::-1])[-1]
        else:
            # Catch out of bound indeces because index-1 doesn't return error
            if (list(sorted_notes.values())[::-1])[value_index-1] == (list(sorted_notes.values())[::-1])[-1]:
                index_added_number = (list(sorted_notes.values())[::-1])[0]
                break
            index_added_number = (list(sorted_notes.values())[::-1])[value_index-1]
            break
    variation_number_list.append(index_added_number)

variation_notes = []

# For each trajectory value
for i in variation_number_list:
    # For each note
    for k in sorted_notes.keys():
        # If the trajectory value of the note is equal to the trajectory value found in the sorted array
        if sorted_notes[k] == i:
            variation_notes.append(k)
            break

print(variation_notes)
