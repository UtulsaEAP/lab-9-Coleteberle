def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   #write your code here
   cost = (miles_driven/miles_per_gallon) * dollars_per_gallon
   return cost

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    #print your costs here like example below
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
   