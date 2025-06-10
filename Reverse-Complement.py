# to print the reverse complement of the given sequence

print("Reverse Complement")
dna = input("Enter the sequence: ")
dna = dna.upper()
comp = ""
complement = {'A':'T',
              'T':'A',
              'G':'C',
              'C':'G'}
comp = ''.join(complement[base] for base in dna)
print(f"Result: {comp[::-1]}")