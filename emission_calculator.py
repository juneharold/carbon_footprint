def calculate_emissions():
    emissions = 0

    # transportation
    type_of_vehicle = int(input("What type of vehicle do you use? enter 1 for car: "))
    fuel_economy = 10.6286  # km/liter
    distance = int(input("How long do you drive in km?: "))
    gas_per_fuel = 2.3
    emissions += fuel_economy * distance * gas_per_fuel

    # Home Energy
    natural_gas = int(input("How much gas does your home use? (kg): ")) * 1.9
    electricity = int(input("How much electricity does your home use? (kWh): ")) * 0.709
    emissions += natural_gas + electricity

    # Waste
    cans = int(input("Roughly how many aluminum cans do you throw away?: ")) * 0.155
    plastic = int(input("Roughly how much plastic do you throw away? (in kg): ")) * 6.02
    glass = int(input("Roughly how much glass do you throw away (in kg): ")) * 8.4
    paper = int(input("Roughly how much paper do you throw away? (in kg): ")) * 0.028
    emissions += cans + plastic + glass + paper

    emissions = int(emissions)

    print("Your total greenhouse gas emissions:", emissions, "kg")
    return emissions

record = []

import matplotlib.pyplot as plt
x = ["Monday", "Tuesday", "Wednesday"]
y1 = [123, 141, 103]
y2 = [43, 54, 41]
plt.plot(x, y1, 'r-')
plt.plot(x, y2, 'b-')
plt.xlabel("Days")
plt.ylabel("Greenhouse gas emissions")
plt.title('Your Greenhouse Gas Emissions This Week!')
plt.show()
