# to count the number of A, T, G, C in a given DNA sequence

print("Counting Bases")
dna = input("Enter the sequence: ")
dna = dna.lower()

print(f"No. of As: {dna.count("a")}")
print(f"No. of Ts: {dna.count("t")}")
print(f"No. of Gs: {dna.count("g")}")
print(f"No. of Cs: {dna.count("c")}")
print(f"No. of Ns: {dna.count("n")}")

