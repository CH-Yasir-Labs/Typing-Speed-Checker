#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     14/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

print("Press enter to start typing or break a new line:")
print("Press enter twice to finish typing:")
print("--------------------------------------")

# Record the start time
start = time.time()
text = []

while True:
    line = input()
    if not line:
        break
    text.append(line)

# Record the end time
end = time.time()

print("-------------------------------------")

# Display the text the user typed in
print("The text user typed in:")
for line in text:
    print(line)

# Calculate the elapsed time in minutes
elapsed_time = (end - start) / 60

# Calculate character count and word count
char_counts = sum(len(item) for item in text)
word_counts = sum(len(line.split()) for line in text) # Approximate 5 characters per word

# Calculate Words Per Minute (WPM)
wpm = round(word_counts / elapsed_time)

print(f"Your average Words per Minute (WPM) is {wpm}")

# Provide feedback based on the WPM
if wpm < 30:
    print("You need to improve.")
elif wpm < 40:
    print("Not bad.")
elif wpm < 50:
    print("Average.")
elif wpm < 60:
    print("Excellent.")
else:
    print("Brilliant! Outstanding!")










