def add(a, b):
  return a + b

def sub(a, b):
  return a -b 

def mult (a, b):
  return a * b

def div(a, b):
  if (b != 0):
    return a/b
  return  0


def main():
  while True:
    a = float(input())
    op = input()
    b =float(input())
    if op == "+":
      print ("Result:", add(a,b))
    elif op == "-":
                        print ("Result:", sub(a,b))
    elif op == "/":
                        print ("Result:", div(a,b))
    elif op == "*":
                        print ("Result:", mult(a,b))
    else:
                        print ("Invalid operation")


if __name__ == "__main__":
  main()
