# to calculate the GC content of the given DNA sequence

print("GC content calculator")
dna = input("Enter the sequence: ")
dna = dna.upper()

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")
print(f"A:{a}, T:{t}, G:{g}, C:{c}")

gc_content = round(((g+c)/(a+t+g+c))*100, 3)
print(f"The GC-content for the given sequence is: {gc_content}%")
