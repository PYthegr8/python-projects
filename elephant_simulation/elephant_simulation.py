''' Papa Yaw Owusu Nti

    This program simulates the population growth of elephants over a specified number of years 
    using various parameters. It tracks the growth and birth of the elephant population, 
    considering  age, gender, reproduction, and population control. 
    The simulation results are stored, and average population statistics are calculated.
        
'''
import random
import sys

# standard parameters
CalvInterval=3.1
DartProb=0.0
JuvenAge=12
MaxAge=60
CalfSurvivalProb=0.85
AdultSurvivalProb= 0.996
SeniorSurvivalProb=0.20
CarryingCap=7000
NumofYrs=200
parameters = [CalvInterval,DartProb,JuvenAge,MaxAge,CalfSurvivalProb,AdultSurvivalProb,SeniorSurvivalProb,CarryingCap,NumofYrs]

#Indexes for standard parameters
IDXCalvInterval = 0 # put this at the top of your code below the module string and the import statements
IDXDartProb=1
IDXJuvenAge=2
IDXMaxAge=3
IDXCalfSurvivalProb=4
IDXAdultSurvivalProb=5
IDXSeniorSurvivalProb=6
IDXCarryingCap=7
IDXNumofYrs=8

#Indexes for elephant information
IDXGender = 0
IDXAge = 1
IDXMonthsPregnant = 2
IDXMonthsContraceptiveRemaining = 3


    
def newElephant(parameters, age) :
    '''Generates a new elephant with random gender and pregnancy probability based on given parameters.
       Returns A list representing a new elephant with its gender, age, pregnancy status, and contraceptive status.
    '''
    elephant = [0,0,0,0]
    elephant[IDXGender]= random.choice(['f','m'])
    pregProb = 1.0/ parameters[IDXCalvInterval]
    pregProb_permonth = 1.0/ ((parameters[IDXCalvInterval]*12)-22)
    elephant[IDXAge]= age
    
    if elephant[IDXGender] == 'f' and  parameters[IDXJuvenAge] < elephant[IDXAge] <= parameters[IDXMaxAge]:
        if random.random() <= pregProb:
            elephant[IDXMonthsPregnant] = random.randint(1,23)
               
    elephant[IDXMonthsContraceptiveRemaining] = 0 
    return elephant 



def initPopulation(parameters):
    ''' Initializes the elephant population with a specified number of random elephants.
    Returns a list containing the initial population of elephants.'''
    initpopulation = []
    for i in range(CarryingCap):
        new_population = newElephant(parameters, random.randint(1, parameters[IDXMaxAge]))
        initpopulation.append(new_population )
    return initpopulation     
 
    
    
def incrementAge(population):
    '''this function increases the age of every elephant in the population.returns the updated population'''
    for i in range(len(population)):
        population[i][IDXAge]+=1
    return population



def calcSurvival(parameters, population):
    '''Calculates the survival probability for each elephant in the population based on age and gender.
    Returns: A list of surviving elephants in the population after applying survival probabilities.
    '''
    JuvenAge = parameters[IDXJuvenAge]
    MaxAge= parameters[IDXMaxAge]
    new_population = []

    for elephant in population:
        survival_prob = 0

        if elephant[IDXAge] < JuvenAge:
            survival_prob = parameters[IDXCalfSurvivalProb]
        elif elephant[IDXAge] < MaxAge:
            survival_prob = parameters[IDXAdultSurvivalProb]
        else:
            survival_prob = parameters[IDXSeniorSurvivalProb]

        if random.random() < survival_prob:
            new_population.append(elephant)

    return new_population

        
def dartElephants(parameters,population):
    '''Simulates the darting of female elephants and updates their pregnancy and contraceptive status.'''
    DartProb=parameters[IDXDartProb]
    JuvenAge= parameters[IDXJuvenAge]
    MaxAge= parameters[IDXMaxAge]
    for elephant in range(len(population)):
        if population[elephant][IDXGender] =='f' and JuvenAge <= population[elephant][IDXAge] <= MaxAge:
            if random.random() < DartProb:
                population[elephant][IDXMonthsPregnant]=0
                population[elephant][IDXMonthsContraceptiveRemaining]=22
    return population

def cullElephants(parameter, population):
    '''Controls the elephant population size by culling excess elephants if the population size exceeds the carrying capacity.
    Returns: A tuple containing the updated population list and the number of culled elephants.'''
    CarryingCap= parameter[IDXCarryingCap]  
    numCulled = len(population)- CarryingCap 
    

    if numCulled > 0 :
        random.shuffle(population)
        newPopulation= population[:CarryingCap]  
        return newPopulation, numCulled   
    else: 
        return population, numCulled
    
def controlPopulation( parameters, population ):
    '''Manages the population by either calling cullElephants or dartElephants based on the value of DartProb in the parameters.
    Returns a A tuple containing the updated population list and the number of culled elephants.'''
    DartProb = parameters[IDXDartProb]
    # if the parameter value for "percent darted" is zero:
      # call cullElephants, storing the return values in a two  
    if DartProb== 0:
        newpop, numCulled = cullElephants( parameters, population)
        return newpop, numCulled
        
    else:
    # call dartElephants and store the result in a variable 
        newpop = dartElephants(parameters, population)
        numCulled= 0
        return newpop, numCulled

    
def simulateMonth(parameters,population):
    '''Simulates a single month within the population, updating age, pregnancy status, and contraception status of elephants.
    Returns the updated population list after simulating a single month.'''
    CalvInterval = parameters[IDXCalvInterval]
    JuvenAge = parameters[IDXJuvenAge]
    MaxAge= parameters[IDXMaxAge]
    pregProb = 1.0/ (CalvInterval* 12 -22)
    
    for e in range(len(population)):
            # e is the idx'th element in population
            # assign to gender the IDXGender item in e
            # assign to age the IDXAge item in e
            # assign to monthsPregnant the IDXMonthsPregnant item in e
            # assign to monthsContraceptive the IDXMonthsContraceptiveRemaining item in e
        gender= population[e][IDXGender]
        age= population[e][IDXAge]
        monthsPregnant= population[e][IDXMonthsPregnant]
        monthsContraceptive = population[e][IDXMonthsContraceptiveRemaining]
        
        #if gender is female and the elephant is an adult
        if gender=='f' and JuvenAge < age <= MaxAge: 
             # if monthsContraceptive is greater than zero
                #decrement the months of contraceptive left (IDXMonthsContraceptiveRemaining element of e) by one -- make sure this is indexing directly into population!!
            if monthsContraceptive > 0:
                population[e][IDXMonthsContraceptiveRemaining] -= 1
               
     # else if monthsPregnant is greater than zero
          # if monthsPregnant is greater than or equal to 22
               # create a new elephant of age 1 and append it to the population list
               # reset the months pregnant (the IDXMonthsPregnant element of e) to zero -- make sure this is indexing directly into population!!
            elif monthsPregnant > 0:
                if monthsPregnant >= 22:
                    new_elephant = newElephant(parameters,1)
                    population.append(new_elephant)
                    population[e][IDXMonthsPregnant] = 0
                else:
                    population[e][IDXMonthsPregnant] += 1
            else:
                
          # else
               # increment the months pregnant (IDXMonthsPregnant element of e) by 1 -- make sure this is indexing directly into population!!
     # else
          # if the elephant becomes pregnant
               # set months pregnant (IDXMonthsPregnant element of e) to 1 -- make sure this is indexing directly into population!!
                if gender == 'f' and  JuvenAge < age <= MaxAge:
                    if random.random() <= pregProb:
                        population[e][IDXMonthsPregnant] = 1
    return population
    




def simulateYear (parameters, population):
    '''Simulates a full year for the elephant population, accounting for age progression and reproduction.
    Returns The updated population list after simulating a full year'''
    population = calcSurvival(parameters, population)
    population = incrementAge(population)
    
    for i in range(12):
        population = simulateMonth(parameters, population)
    return population


def calcResults(parameters, population, numCulled):
    '''Calculates various population statistics: the number of calves, juveniles, adult males, adult females, and seniors. 
    It also tracks the number of culled elephants.
    Returns alist containing the following population statistics: [total population, number of calves, number of juveniles,
    number of adult males, number of adult females, number of seniors, number culled].'''
    JuvenAge = parameters[IDXJuvenAge]
    MaxAge= parameters[IDXMaxAge]
    Num_Calves = 0
    Num_Juves = 0
    Num_Adult_M = 0
    Num_Adult_F = 0
    Num_Snrs = 0
    
    
    for elephant in population:
        if elephant[IDXAge] == 1:
            Num_Calves+=1
        elif elephant[IDXAge] <= JuvenAge:
            Num_Juves +=1
        elif JuvenAge <= elephant[IDXAge] <=MaxAge and elephant[IDXGender]=='m' :
            Num_Adult_M +=1
        elif JuvenAge < elephant[IDXAge] <=MaxAge and elephant[IDXGender]=='f' :
            Num_Adult_F +=1
        elif  elephant[IDXAge] > MaxAge:
            Num_Snrs +=1
              
    return  [len(population),Num_Calves,Num_Juves,Num_Adult_M ,Num_Adult_F,Num_Snrs, numCulled]



def runSimulation(parameters):
    ''' Runs the elephant population simulation for a specified number of years, considering population control 
    and termination conditions.
    Returns a list of simulation results, where each entry represents the population statistics for a specific year.'''
    popsize = parameters[IDXCarryingCap]

    # init the population
    population = initPopulation( parameters )
    population,numCulled = controlPopulation( parameters, 
    population )

    # run the simulation for N years, storing the results
    results = []
    for i in range(parameters[IDXNumofYrs]):
        population = simulateYear( parameters, population )
        population,numCulled = controlPopulation( parameters, 
         population )
        results.append( calcResults( parameters, population, 
        numCulled ) )
        if results[i][0] > 2 * popsize or results[i][0] == 0 : 
            # cancel early, out of control
            print( 'Terminating early' )
            break
        return results


def main(argv):
    '''The main function that computes the simulation, 
    reads command-line arguments, and computes average population statistics.
    Returns: None. doesn't return a value '''

    if len(argv) < 2:
        print('Usage statement:error')
        sys.exit(1)
    
    #assign command-line arguments    
    filename = argv[0]
    DartProb= float(argv[1])
    
        
    # standard parameters
    CalvInterval=3.1
    JuvenAge=12
    MaxAge=60
    CalfSurvivalProb=0.85
    AdultSurvivalProb= 0.996
    SeniorSurvivalProb=0.20
    
    #EXTENSION 1
    CarryingCap=int(sys.argv[2])
    NumofYrs=int(sys.argv[3])

    parameters = [CalvInterval,DartProb,JuvenAge,MaxAge,CalfSurvivalProb,AdultSurvivalProb,SeniorSurvivalProb,CarryingCap,NumofYrs]

    simulation_results = runSimulation(parameters)
    # print(simulation_results)

    num_simulations = len(simulation_results)
    # print (num_simulations)

    avg_total_population = 0
    avg_num_calves = 0
    avg_num_juveniles = 0
    avg_num_Adult_males = 0
    avg_num_Adult_females = 0
    avg_num_Senior = 0

    for result in simulation_results:
        avg_total_population += result[0]
        avg_num_calves += result[1]
        avg_num_juveniles += result[2]
        avg_num_Adult_males += result[3]
        avg_num_Adult_females += result[4]
        avg_num_Senior += result[5]

    avg_total_population /= num_simulations
    avg_num_calves /= num_simulations
    avg_num_juveniles /= num_simulations
    avg_num_Adult_males /= num_simulations
    avg_num_Adult_females /= num_simulations
    avg_num_Senior /= num_simulations

    print(f"Average Total Population: {avg_total_population:.2f}")
    print(f"Average Number of Calves: {avg_num_calves:.2f}")
    print(f"Average Number of Juveniles: {avg_num_juveniles:.2f}")
    print(f"Average Number of Adult Males: {avg_num_Adult_males:.2f}")
    print(f"Average Number of Adult Females: {avg_num_Adult_females:.2f}")
    print(f"Average Number of Seniors: {avg_num_Senior:.2f}")

if __name__ == "__main__":
    main(sys.argv)





#testfunction commented out below 
    
'''       
def test():

    # assign each parameter from the table above to a variable with an informative name
    CalvInterval=3.1
    DartProb=0.0
    JuvenAge=12
    MaxAge=60
    CalfSurvivalProb=0.85
    AdultSurvivalProb= 0.996
    SeniorSurvivalProb=0.20
    CarryingCap=7000
    NumofYrs=200

    # make the parameter list out of the variables
    parameters = [CalvInterval,DartProb,JuvenAge,MaxAge,CalfSurvivalProb,AdultSurvivalProb,SeniorSurvivalProb,CarryingCap,NumofYrs]
    # print the parameter list
    print (parameters)
    
    
    # test newElephant
    pop = []
    for i in range(10):
        pop.append( newElephant( parameters, random.randint(1, parameters[IDXMaxAge]) ))
    for e in pop:
        print(e)
        
    #test initPopulation()
    testinit= initPopulation(parameters)
    print(testinit)
    
    # test incrementAge()
    testincreAge= incrementAge(testinit)
    print(testincreAge)  
      
if __name__ == "__main__":
    test() 

'''



                       