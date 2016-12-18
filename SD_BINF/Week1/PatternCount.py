#Goal: check the pattern of an input string 
#input = 'GCGCG' #should print out 2 patterns
#pattern = GCG -> this case only 
input = 'GACCATCAAAACTGATAAACTACTTAAAAATCAGT'
def PatternCount(text, Pattern): 
    count = []
    for i in range(len(text) - len(Pattern) + 1): #should go up to 2 
        if text[i:len(Pattern)+i] == Pattern:
            count.append(i) 
    return count

print ( PatternCount(input, 'AAA') ) 
