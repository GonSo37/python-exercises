def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    chances = []
    for fisher in fishers:
        prob =  fisher / total_fishers
        chances.append(prob * 100)

    for country, chance in zip(countries, chances):
        print("%s %.2f%%" % (country, chance)) # modify this to print correct results

main()
