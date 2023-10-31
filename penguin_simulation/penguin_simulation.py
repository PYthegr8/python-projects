'''Papa Yaw Owusu Nti
    10/12/2023
    this program simulates the growth of penguins over a specified number of years.
    I computed the initial population with the function initPopulation, simulated a year of growth
    with the function simulateYear, run the simulation over a specified number of years with the function
    runSimulation, computed the cumulative extinction probability with the function computeCEPD
    and defined a main function that takes in command line arguments to ran multiple simulations specifying
    years between El-Nino whether 3,5 or 7
'''

import random
import sys
import pylab as plt



#function to initialize population
def initPopulation(N, probFemale):
    '''
    this function initializes a population of penguins
    with a specified size(n) and gender distribution(probFemale i.e. probability of being a female).
    '''
    population = []
    
    for i in range(N):
        random_float = random.random()
        if random_float < probFemale:
            population.append('f')
        else:
            population.append('m')
    return population


#function to simulateYear                  
def simulateYear(pop,elNinoProb ,stdRho ,elNinoRho , probFemale, maxCapacity):
    '''
    The function simulates a year of the population growth by 
    taking the current population (pop), probability of el-Nino, standard growth probability, el-Nino growth probability
    probability of Female and Max carrying capacity respectively and returns a new population 
    '''
    newpop = []
    elNinoYear = False
    if random.random() < elNinoProb:
        elNinoYear = True
    
    for penguin in pop:
        # if the length of the new population list is greater than maxCapacity,break,
        if len(newpop) > maxCapacity:
            break
    # if it is an El Nino year
        # if random.random() is less than the El Nino growth/reduction factor,append the penguin to the new population list
        if elNinoYear == True:
            if random.random() < elNinoRho:
                newpop.append(penguin)
        else:
        # append the penguin to the new population list
            # if random.random() is less than the standard growth factor - 1.0
                # if random.random() is less than the probability of a female, append an 'f' to the new population list
                # else append an 'm to the new population list
            newpop.append(penguin)
            if random.random() < (stdRho-1.0) :
                if random.random() < probFemale:
                    newpop.append('f')
                else:
                    newpop.append('m')
    return newpop


#test 
def test():
    ''' the test functions is testing to see if the previous functions previously defined are working accurately'''
    popsize = 10
    probFemale = 0.5
    pop = initPopulation(popsize, probFemale)

    newpop = simulateYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)
    print( "El Nino year" )
    print( newpop )

    newpop = simulateYear(pop, 0.0, 1.188, 0.4, 0.5, 2000)
    print( "Standard year" )
    print( newpop )



def runSimulation(N,initPopSize,probFemale,elNinoProb,stdRho,elNinoRho,maxCapacity,minViable ):  
    '''
    this function simulates the penguin population over N years. It uses the simulateYear function to compute the population, 
    tracks male and female penguins, and checks for population viability. The function returns the year awhen simulation ends.
    '''
    
    population = initPopulation(initPopSize, probFemale)
    
    for i in range(N):
        newPopulation = list(simulateYear(population,elNinoProb ,stdRho ,elNinoRho , probFemale, maxCapacity))
        
        # Count the number of male and female penguins in the new population
        males = newPopulation.count('m')
        females = newPopulation.count('f')
        
        # If viability conditions are met, update the population else break
        if len(newPopulation) < minViable or males <0 or females <0:
            endDate = i
            break
        else:
            endDate = N
            population= newPopulation
            # print (len(population))
    return endDate
    
 
runSimulation(201,500,0.5,1.0/7.0,1.188,0.41,2000,10)

def computeCEPD(endDate, N ):
    '''
this function computes the Cumulative Extinction Probability Distribution over multiple simulations. 
It takes a list of simulation end years and the total number of years (N) and returns a list of CEPD values for each year.
'''
    CEPD= []
    # Initialize CEPD list by filling it up with zeros for N years
    for i in range(N):
        CEPD.append(0)
    
    # Increase the CEPD value for each year 
    for year in endDate:
        if year < N:
            for i in range(year, len(CEPD)):
                CEPD[i] += 1
  
            
    # compute CEPD values by dividing by the length of years list
    for i in range(N):
        CEPD[i] /= len(endDate)
    return CEPD


def main(argv):
    '''
    this function accepts command-line arguments as parameters, runs user specified number of simulations, 
    calculates the survival probability of the population, computes the CEPD, and plots the CEPD over every 10 years.
    '''
    if len(argv) < 3:
        print('Usage statement:error')
        sys.exit()
    
    #assign command-line arguments    
    filename = argv[0]
    NSim= int(sys.argv[1])
    Years_Between_ElNino= int(sys.argv[2])
    

    # Set standard parameters    
    N_yr= 201
    IniPopSize=500
    ProbaFemales=0.5
    ProbaElNino= 1.0/ Years_Between_ElNino
    GrowthStd =1.188
    GrowthElNino=0.41
    MaxCap=2000
    MiniViaPop=10
    simulation_years =[]
    results_count = 0
  
    # record the year when simulations ends 
    for i in range(NSim):
        extinction_years = runSimulation(N_yr,IniPopSize,ProbaFemales, ProbaElNino, GrowthStd, GrowthElNino, MaxCap, MiniViaPop)
        simulation_years.append(extinction_years)
        
    # Compute the number of simulations where the population survived   
    for results in simulation_years:
            if results <= N_yr:
                results_count+=1
                
            
    # Calculate the survival probability    
    survival_probability = results_count / NSim  
    print(f"The survival probability of the population was {survival_probability}")
        
         
    # Print CEPD values for every 10 years
    CEPD = (computeCEPD(simulation_years, N_yr)) 
    for i in range(1, len(CEPD)):
        if i%10 == 0:
             print(f" CEPD for Year {i}: {CEPD[i]}")
    
    
    #EXTENSION 1: save computed values to csv file
    fp = open ("CEPD values.csv", "w")
    fp.write(str('years') + ', ' + str('CEPD') + '\n')
    for i in range(len(CEPD)):
        fp.write(str(i) + ',' + str(CEPD[i]) + '\n')  
    fp.close()
       

    # set x-values to the length of CEPD list for plotting
    x_values = []
    x_values = list(range(len(CEPD))) 


    ##Add title/axes labels etc to the plot
    plt.title( 'Plot of CEPD of penguin population for 201 years' )
    plt.xlabel( 'Year' )
    plt.ylabel( 'CEPD' )
    plt.plot( x_values , CEPD , color='b' , marker='' )    
    ##Save, then show the plot
    plt.show()  
    


    
        
if __name__ == "__main__":
    main(sys.argv)
   
   

    

    

    









    