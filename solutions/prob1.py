def is_prime(x):
    if x<2:
        return False
    for n in range(2,x-1):
        if x%n == 0:
            return False
            break
    else:
        return True

f=open('/Users/megan/Code/code-golf-spring-2017/inputs/1.txt', 'r')
nums = []
for line in f:
    full = line.split()
    justnum = int(full[0])
    nums.append(justnum)
print nums
out = open('/Users/megan/Code/code-golf-spring-2017/answers/1.txt', 'w')
for num in nums:
    print num
    primes = 0
    for x in range(1, num+1):
        if is_prime(x):
            primes+=1
    print primes
    prime = str(primes)
    out.write(prime + '\n')
