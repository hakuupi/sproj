import time
from playsound import playsound #dependency: PyObjC


BPM = 60  # starting tempo in beats per minute
INCREASE_AMOUNT = 5  # amount to increase tempo per iteration
ITERATIONS = 10  # number of tempo increases to make

# calculate the delay between clicks based on current tempo
def get_delay(bpm):
    return 60.0 / bpm

# loop through iterations, increasing tempo and playing clicks
for i in range(ITERATIONS):
    print("Tempo:", BPM)

    # calculate delay between clicks based on current tempo
    delay = get_delay(BPM)

    # play click sound
    playsound("click.wav")
    time.sleep(delay)

    # increase tempo for next iteration
    BPM += INCREASE_AMOUNT

print("Finished")
