import matplotlib.pyplot as plt


def calculate_emissions():
    emissions = 0

    car = int(input("Do you drive a car? (1-yes, 0-no): "))
    if car:
        fuel_economy = 10.6286  # km/liter
        distance = float(input("How long do you drive in km?: "))
        gas_per_fuel = 2.3
        emissions += distance/fuel_economy * gas_per_fuel

    # Home Energy
    natural_gas = float(input("How much gas does your home use? (kg): ")) * 1.9
    electricity = float(input("How much electricity does your home use? (kWh): ")) * 0.709
    emissions += natural_gas + electricity

    # Waste
    cans = float(input("Roughly how many aluminum cans do you throw away?: ")) * 0.155
    plastic = float(input("Roughly how much plastic do you throw away? (in kg): ")) * 6.02
    glass = float(input("Roughly how much glass do you throw away (in kg): ")) * 8.4
    paper = float(input("Roughly how much paper do you throw away? (in kg): ")) * 0.028
    emissions += cans + plastic + glass + paper

    print("Your total greenhouse gas emissions:", emissions, "kg")
    return emissions


num_days = int(input("For how many days would you like this program to calculate your greenhouse gas emissions?: "))
record = []
for i in range(num_days):
    print("DAY", i+1, "----------------------------------------------------")
    result = calculate_emissions()
    record.append(result)


x = list(i for i in range(1, num_days+1))
average = [26.57]*num_days
plt.plot(x, record, 'r-', label="Your Emissions")
plt.plot(x, average, 'b-', label="Japan's Average")
plt.xlabel("Days")
plt.ylabel("Greenhouse gas emissions (kg)")
plt.title('Your Greenhouse Gas Emissions')
plt.legend()
plt.show()
