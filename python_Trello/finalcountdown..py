import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("BOOM!")

print("Vanaf hoeveel seconden moet de countdown aftellen?:")
seconds = input()
while not seconds.isdigit():
    print("Error")
    seconds = input()
seconds = int(seconds)
countdown(seconds)
