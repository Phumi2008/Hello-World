#Function that identifies DNA sequence and returns the Amino Acid
def translate(DNA):
    ATTATCATA = ""
    I = "ATTATCATA"
    CTTCTCCTACTGTTATTG = ""
    L = "CTTCTCCTACTGTTATTG"
    GTTGTCGTAGTG = ""
    V = "GTTGTCGTAGTG"
    TTTTTC = ""
    F = "TTTTTC"
    ATG = ""
    M = "ATG"
    # x variable for all the other DNA sequence that are not declared
    x = ""
    # Getting the DNA codons to identify the related Amino Acid 
    DNA = input("Please enter the DNA codons: ")
    # Using while loop to get the length of DNA sequence divisable by 3
    while len(DNA) % 3 == 0:
        if DNA == I:
            print ("The Amino Acid is Isoleucine")
            break

        elif DNA == L:
            print ("The Amino Acid is Leucine")
            break
            
        elif DNA == V:
            print ("The Amino Acid is Valine")
            break
            
        elif DNA == F:
            print ("The Amino Acid is Phenylalanine")
            break
            
        elif DNA == M:
            print("The Amino Acid is Methionine")
            break

        else:
            if DNA == x:
                print ("sequence is not loaded")

    return DNA

# Calling the translate function
DNA = input("please enter the DNA codons: ")
aminoAcid = translate(DNA)
print(aminoAcid)

#Function that read DNA file and identify the first occurrence of "a" and return the position of a
def mutate(read):
    mfile = open("DNA.txt","r")
    contents = mfile.read()
    letterAPos = contents.find("a")
    print(letterAPos)
    return contents

#Calling the mutate function
mfile = open("DNA.txt","r")
contents =""
modified = mutate(contents)
print(modified)

mfile.close()

#copying a file into another file(copying DNA into normalDNA file)

y = open("DNA.txt","r")
f = open("normalDNA.txt","w")
file = ["normalDNA.txt"]
# Using the for loop to replace a with A    
for line in y:
    f.write(line.replace("a","A"))
    print(line)
y.close()
f.close()

# Copying file and replacing a character(a with T)
y = open("DNA.txt","r")
h = open("mutateDNA.txt","w")
for line in y:
    h.write(line.replace("a","T"))
    print(line)
    
y.close()
h.close()

#Function that call the translate function to take in text file input
def txtTranslate (DNA):
    output = translate(0)
    return output
#calling the txtTranslate function to get the Amino Acid in file normalDNA
output = txtTranslate
f = open("normalDNA.txt","r")
line =f.read()
DNA = input("please enter the DNA sequence:")
print(output(DNA))
      
f.close()
#calling the txtTranslate function to get the Amino Acid in file mutateDNA

h = open("mutateDNA.txt","r")
line = h.read()
DNA = input("please enter the DNA sequence:")
print(output(DNA))

h.close()
    
                         
                         
        

