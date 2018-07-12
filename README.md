# Fibonacci-series
Fibonacci series can be generated by adding the shallow diagonals of the pascal triangle. 
---
Please refer to below image to see the fibonacci series generated from the pascal triangle. Numbers in sequence are shown in blue color
![fibonacci series](https://user-images.githubusercontent.com/3431730/42612297-32c9de20-85b8-11e8-8157-6c2cc9c90922.png)

---

Sequence can also be generated using the below code
```
a=0;          #let us fix the first term
b=1;          #let us fix the second term so that we can define a logic to generate the next sequence
#Now to make the program, let us code to make user to enter how many numbers are generated as the output or number of sequence
n = int(input("Enter the number which defines terms in the sequence: "))
#apply some conditions so that one can understand all the cases in such series
if n==0:
    print("Invalid input as series must contains atleast two numbers")
elif n==1:
    print("{}".format(a))
elif n==2:
    print("{},{}".format(a,b))
elif n>=2:
    print('{},{}'.format(a,b),end='')
    for i in range(2,n):
        c = a+b;
        print(',{}'.format(c),end='')
        a=b;
        b=c;
```

---

Please refer to **Fibonacci series.py** for more comments and details of the code written. Though different programming languges can be used to implement the same series but logic remain same in all the programming languages. This code in implemeted using Pycharm and Python 3.5.
