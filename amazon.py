#had to overwrite the intial content in the input.txt (w) cause line 6 was printing on line 5.
#then changed the mode to read and write  (r+) so that i can print the content in input file
f = open("input.txt","r+")

f.write("Min:1,2,3,4,5,6" +"\n")
f.write("Max:1,2,3,4,5,6" +"\n")
f.write("Avg:1,2,3,4,5,6" +"\n")
f.write("p90:1,2,3,4,5,6,7,8,9,10" +"\n")
f.write("sum:1,2,3,4,5,6" + "\n")
f.write("min:1,5,6,14,24" +"\n")
f.write("max:2,3,9" +"\n")
f.write("p70:1,2,3" +"\n")

data = ""
for line in f:
    data = data + line
    print(data)

f.close()


import numpy as np

y = open ("output.txt","w")

num = [1,2,3,4,5,6]
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [1,2,3]
num4 = [1,2,3,5,6]
y.write("The minimum of [1,2,3,4,5,6] is:" +str(min(num))+"\n")
y.write("The maximum of [1,2,3,4,5,6] is:" +str(max(num))+"\n")
y.write("The average of [1,2,3,4,5,6] is:" +str(sum(num)/6)+"\n")
y.write("The 90th percentile of [1,2,3,4,5,6,7,8,9,10] is:" +str(np.percentile(num1,90))+"\n")
y.write("The sum of [1,2,3,4,5,6] is:" + str(sum(num4))+"\n")
y.write("The minimum of [1,5,6,14,24] is:" +str(min(1,5,6,14,24))+"\n")
y.write("The max of [2,3,9] is:" + str(max(2,3,9))+"\n")
y.write("The 70th percentile of [1,2,3] is:" +str(np.percentile(num2,70))+"\n")
        
y.close()        
