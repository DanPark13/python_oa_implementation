'''
Original Algorithm Implementation
'''

# Test Case #1 from Instructions
reference_trajectory_dict = {
    "C":1,
    "D":2,
    "G":0,
    "F":2,
    "E":3
}

# Test Case #2 from Instructions
# TODO: DEBUG (Nonworking)
reference_trajectory_dict = {
    "C":1,
    "D":2,
    "G":3,
    "F":2,
    "E":0
}

# Print out the Original Reference Trajectory
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

'''
Use bubble sort algorithm to sort
'''
def bubble_sort(array):
    length = len(array)
  
    # Traverse through all array elements
    for i in range(length-1):
    # range(n) also work but outer loop will repeat one time more than needed.
  
        # Last i elements are already in place
        for j in range(0, length-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

# Sort the trajectory value
#sorted_trajs = oa_sort(list(reference_trajectory_dict.values())) # Sort the values using original algorithm sort
sorted_trajs = oa_sort(list(reference_trajectory_dict.values())) # Sort the values using bubble sort
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
print(f"Notes after Sorting: {sorted_notes}\n")

variation_trajectory = [0.5,-1,2,3,4]

'''
Check the numbers in the reference directory against the variation trajectory
and varies it by taking the number to the right of it and assigning the note
associated with that reference value to the variation
if the number in the reference trajectory is less than the variation trajectory number
'''
def variation_sorting(trajectory, note_dict):
    index_added_number = 0
    variation_number_list = []

    # Find the values of trajectory values 
    for num_index, num in enumerate(trajectory):
        for value_index, value in enumerate(list(note_dict.values())[::-1]):
            if (num <= value):
                index_added_number = (list(note_dict.values())[::-1])[-1]
            else:
                # Catch out of bound indeces because index-1 doesn't return error
                if (list(note_dict.values())[::-1])[value_index-1] == (list(note_dict.values())[::-1])[-1]:
                    index_added_number = (list(note_dict.values())[::-1])[0]
                    break
                index_added_number = (list(note_dict.values())[::-1])[value_index-1]
                break
        variation_number_list.append(index_added_number)
    return variation_number_list

variation_sorting = variation_sorting(variation_trajectory, sorted_notes)

'''
Align the Varied Sorted Trajectories along with their respective notes
'''
def variation_note_alignment(variation_sort, note_dict):
    variation_notes = []
    # For each trajectory value
    for varied_traj in variation_sort:
        # For each note
        for note in note_dict.keys():
            # If the trajectory value of the note is equal to the trajectory value found in the sorted array
            if note_dict[note] == varied_traj:
                variation_notes.append(note)
                break
    return variation_notes

print(f"Notes after the variation trajectory sorting: {variation_note_alignment(variation_sorting, sorted_notes)}")
