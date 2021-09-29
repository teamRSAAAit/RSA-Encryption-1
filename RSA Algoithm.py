"""
This code efficiently woks with the numbers up to 1024 digits
So you may have to wait a little bit if you enter more than that
And it only works for numbers and alphabets as a start
"""
import random
alphabet = "1111111111 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


class PrimeGenerator:
    """
    This code below will generate two large random primes using a sequence of codes below
    """
    def sieveOfEratosthenes(self,n):
        """
        Generate the first hundred primes which will help to test the first two primes
        This methode is called the Sieve of Eratosthenes
        """
        prime = [True for i in range(n + 1)]
        p = 2
        first_primes_list = []
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        for p in range(2, n + 1):
            if prime[p]:
                first_primes_list.append(p)
        return first_primes_list


    def nBitRandom(self, n):
        """
        This line will create two large random numbers to be tested as prime or not
        """
        return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


    def getLowLevelPrime(self, n):
        """
        This function will generate the two large numbers using the above function And
        Test them to be prime using the Sieve of Eratostenes
        """
        while True:
            # Obtain a random number
            pc = self.nBitRandom(n)
            # Test divisibility by pre-generated
            # primes
            for divisor in self.sieveOfEratosthenes(500):
                if pc % divisor == 0 and divisor ** 2 <= pc:
                    break
            else:
                return pc


    def isMillerRabinPassed(self, mrc):
        """
        This function will do the final trial to test whether the numbers are prime or not
        This block of code will be executed only if the above test is not succesful
        And it uses the strongest test called the Miller rabbit Test for primes
        """
        maxDivisionsByTwo = 0
        ec = mrc - 1
        while ec % 2 == 0:
            ec >>= 1
            maxDivisionsByTwo += 1
        assert (2 ** maxDivisionsByTwo * ec == mrc - 1)

        def trialComposite(round_tester):
            if pow(round_tester, ec, mrc) == 1:
                return False
            for i in range(maxDivisionsByTwo):
                if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                    return False
            return True

        # Set number of trials here
        numberOfRabinTrials = 20
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, mrc)
            if trialComposite(round_tester):
                return False
        return True

primegenerator = PrimeGenerator()
print("WELCOME TO THE WORLD'S BEST ENCRYPTION MECHANISM CALLED THE RSA ENCRYPTON ALGORITHM\n")
n = int(input("How many digits should the primes be: "))
print("Finding primes...")
if __name__ == '__main__':
    the_two_primes = []
    for i in range(2):
        while True:
            prime_candidate = primegenerator.getLowLevelPrime(n)
            if not primegenerator.isMillerRabinPassed(prime_candidate):
                continue
            else:
                the_two_primes.append(prime_candidate)
                break

p1 = the_two_primes[0]
p2 = the_two_primes[1]
print("P1 = " + str(p1))
print("P2 = " + str(p2))

n = p1 * p2
totient_function_of_n = (p1 - 1) * (p2 - 1)


def gcd(a, b):
    # To find the greatest commom divisor of two numbers
    return b if a % b == 0 else gcd(b, a % b)


lst = list(filter(lambda e: gcd(e, totient_function_of_n) == 1,
                  [i for i in range(totient_function_of_n - 1000, totient_function_of_n)]))
e = random.choice(lst) # e is the public key which is relatively prime to the Euler's totient function of n
print("\nYour public key is: (" + str(e) + ", " + str(n) + ")")


def modInverse(num, mod):
    """
    This function finds the modular multiplicative inverse of two numbers
    """
    m0 = mod
    y = 0
    x = 1
    if (mod == 1):
        return 0
    while (num > 1):
        # q is quotient
        q = num // mod
        t = mod
        # m is remainder now, process
        # same as Euclid's algo
        mod = num % mod
        num = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if (x < 0):
        x = x + m0
    return x


d = modInverse(e, totient_function_of_n) # d is the private key which is the multiplicative inverse of e and n
print("Your private key is: (" + str(d) + ", " + str(n) + ") ")
print("KEEP IT HIDDEN!!!\n")


def modulo(base, exp, mod):
    """
    THis code will find the modulo or the remainder of two numbers in a fraction of seconds
   """
    x = 1
    power = base
    binary = bin(exp)
    for i in binary[:1:-1]:
        if int(i) == 1:
            x = (x * power) % mod
        power = (power * power) % mod
    return x


message = input("Let us check...\nEnter message: ")
padded_message = ""

for i in message:
    padded_message += str(alphabet.index(i))

message_in_numbers = int(padded_message)
encrypted_message = modulo(message_in_numbers, e, n)
decrypted_message = modulo(encrypted_message, d, n)

origional_message = ""
message_to_be_deciphered = str(decrypted_message)
for i in range(0, len(message_to_be_deciphered), 2):
    origional_message += alphabet[int(message_to_be_deciphered[i:i + 2])]


print("Your origional message in numbers is: " + str(message_in_numbers) + "\n")
print("The encrypted message is: " + str(encrypted_message) + "\n")
print("The decrypted message is: " + str(decrypted_message) + "\n")
print("The origional message is: " + origional_message)
