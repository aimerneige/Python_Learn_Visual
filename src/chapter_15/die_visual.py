from die import Die

die = Die()

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)