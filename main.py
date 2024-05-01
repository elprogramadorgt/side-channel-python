import time
import timeit
secret = "secret"


def verify_secret(password):

    for i in range(len(password)):
        time.sleep(0.1)
        if i >= len(password) or password[i] != secret[i]:
            return False
    return True


def attack():

    password = ["a"]*len(secret)

    for position in range(len(password)):
        attemps = []
        for char in "abcdefghijklmnopqrstuvwxyz":

            temp_password = password[:]
            temp_password[position] = char

            start_time = timeit.default_timer()

            verify_secret("".join(temp_password))

            total_time = timeit.default_timer() - start_time

            attemps.append((char, total_time))
            # print(char, total_time)

        # print(attemps)
        char, t = max(attemps, key=lambda x: x[1])
        print(char, t)
        password[position] = char
        # break


attack()
