#dictionary comprehension
square={num:num**2 for num in range(1,11)}
                   #or
#square={f"square of {num} is":num**2 for num in range(1,11)}
                   #or
#for k,v in square.items():
    #print(f"{k}:{v}")
       

#print(square)


#string="harshit"
#word_count={char:string.count(char) for char in string}
#print(word_count)

even_odd={i:('even'if i%2==0 else'odd') for i in range (1,11)}
print(even_odd)
