'''
Fibonacci series in a simple way using if and else statement
'''

#fibonacci series can be generated by adding the shallow diagonals of the pascal triangle
#another way is after writing first and second term, third term is sum of first two
#In more generalized form , one can say that next term is the sum of two previous terms
#So it would be convenient to fix first two terms so that one can find the rest term easily

#0,1,1,2,3.......................................is a fibonacci series
#1,1,2,3,5........................................is another fibonacci series

a=0;          #let us fix the first term
b=1;          #let us fix the second term so that we can define a logic to generate the next sequence
#Now to make the program, let us code to make user to enter how many numbers are generated as the output or number of sequence
n = int(input("Enter the number which defines terms in the sequence: "))
#apply some conditions so that one can understand all the cases in such series
if n==0:
    print("Invalid input as series must contains atleast two numbers")
elif n==1:
    print("Please print{}".format(a))
elif n==2:
    print("Sequence is {},{}".format(a,b))
elif n>=2:
    print('{},{}'.format(a,b),end='')
    for i in range(2,n):
        c = a+b;
        print(',{}'.format(c),end='')
        a=b;
        b=c;



