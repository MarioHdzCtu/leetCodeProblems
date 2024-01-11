"""Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true."""

def FizzBuzz(n: int) -> list:
    l = [i+1 for i in range(n)]
    a = []
    for i in l:
        output = ''
        if (i % 3 == 0 and i % 5 == 0):
            output = 'FizzBuzz'
        elif i % 3 == 0:
            output += 'Fizz'
        elif i % 5 == 0:
            output += 'Buzz'
        else:
            output = f'{i}'
        a.append(output)
    return a
        
print(FizzBuzz(15))

