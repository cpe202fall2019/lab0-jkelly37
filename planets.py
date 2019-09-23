def weight_on_planets():
    x = float(input("What do you weigh on earth? " + '\n'))

    y = [x*0.38,x*2.34]
    print("On Mars you would weigh " + y[0].__str__() + " pounds." + '\n' + "On Jupiter you would weigh " + y[1].__str__() + " pounds.")

if __name__ == '__main__':
   weight_on_planets()