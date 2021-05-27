# Write a program to remove empty tuples from a list.
def remove(tuples): 
    # tuples = filter(None, tuples) 
    tuples = [t for t in tuples if t] 
    return tuples 
  
# Driver Code 
t1 = [(), ('SHREYANSH','12','11'), (), ('NISHU', 'RUSHIT'),  
          ('SHREYA','SHIVANI'), ('',''),()] 
print(remove(t1))