#!/usr/bin/python

# Set up variables
tuition = 10000
years = 0
increase = 0.07

# while loop to increase tuition and years
while tuition < 20000:
    tuition += (tuition * increase)
    years += 1

# print statements for output
print("Tuition will be doubled in %i years" % (years))
print("Tuition will be $%.2f in %i years" % (tuition, years))
