population = int(input())
infected = int(input())
infection_rate = int(input())

days = 0
to_be_infected = infected

while not to_be_infected > population:
    days = days + 1
    infected = infected * infection_rate
    to_be_infected = to_be_infected + infected
    # print("Infected: ", infected, "Days: " , days, "To be infected: ", to_be_infected)

print(days)