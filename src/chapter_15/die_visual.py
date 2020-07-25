from die import Die

die = Die()

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)