"""numbers = list(map(int, input("Enter integer")))

#calculate sum and average
total = sum(numbers)
average = total/len(numbers)

#save to file
with open ('numbers_data.txt','w') as f:
    f.write('Numbers: '+ str(numbers) +'\n')
    f.write(f'sum: {total}\n')
    f.write(f'Average : {average} \n')

#Read back and display
with open('numbers_data.txt','r') as f:
  print(f.read)"""