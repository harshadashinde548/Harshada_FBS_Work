
A=int(input("Enter value of A:"))
B=int(input("Enter value of B:"))
C=int(input("Enter value of C:"))
#calculate discriminant
D=B*B-4*A*C
Root1=(-B+(D**0.5))/(2*A)
Root2=(-B-(D**0.5))/(2*A)
print(f'Root1:{Root1},Root2:{Root2}')
