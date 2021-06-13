def divide_sequence(sequence):
    if len(sequence) <= 1:  #condition to stop my recursive at a stage where i get single element sequences
        return sequence
    mid = len(sequence)//2
    #Divide your sequnce into 2 sequences
    sequence1 = sequence[:mid]
    sequence2 = sequence[mid:]
    # Divide recursively untill u get a sequence which you can sort easily
    sequence1 = divide_sequence(sequence1)
    sequence2 = divide_sequence(sequence2)
    return mergeSort(sequence1, sequence2)

def mergeSort(sequence1, sequence2):
    
    sorted_sequence = []
    i = 0 
    j = 0
    while i < len(sequence1) and j < len(sequence2):
        if sequence1[i] > sequence2[j]:
            sorted_sequence.append(sequence2[j])
            j += 1
        elif sequence1[i] < sequence2[j]:
            sorted_sequence.append(sequence1[i])
            i += 1
    while i<len(sequence1):
        sorted_sequence.append(sequence1[i])
        i+=1
    while j<len(sequence2):
        sorted_sequence.append(sequence2[j])
        j+=1
    return sorted_sequence
            

print(divide_sequence([5,2,3,4,6,1]))
