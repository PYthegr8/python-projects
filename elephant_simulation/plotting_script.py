''' Papa Yaw Owusu Nti

    This extension generated a csv file of the and wrote the population data with demographic subsets into it. 
    It then  allows the user to specify the number of years to simulate. 
        
'''

import random
import sys
import pylab as plt
import elephant_simulation

#setting standard variables
CalvInterval=3.1
DartProb=0.0
JuvenAge=12
MaxAge=60
CalfSurvivalProb=0.85
AdultSurvivalProb= 0.996
SeniorSurvivalProb=0.20
CarryingCap=7000
NumofYrs= int(input("enter number of years to Simulate:"))

#setting parameter list
parameters = [CalvInterval,DartProb,JuvenAge,MaxAge,CalfSurvivalProb,AdultSurvivalProb,SeniorSurvivalProb,CarryingCap,NumofYrs]

# Run the simulation and store the results
def runSimulation(parameters):
    '''this function  Run the simulation and return the results'''
    popsize = parameters[elephant_simulation.IDXCarryingCap]

    # init the population
    population = elephant_simulation.initPopulation( parameters )
    population,numCulled = elephant_simulation.controlPopulation( parameters, 
    population )

    # run the simulation for N years, storing the results
    results = []
    for i in range(parameters[elephant_simulation.IDXNumofYrs]):
        population = elephant_simulation.simulateYear( parameters, population )
        population,numCulled = elephant_simulation.controlPopulation( parameters, 
         population )
        results.append( elephant_simulation.calcResults( parameters, population, 
        numCulled ) )
        if results[i][0] > 2 * popsize or results[i][0] == 0 : 
            # cancel early, out of control
            print( 'Terminating early' )
            break
    return results


population= []
count_of_years_List = []
simulation_results = runSimulation(parameters)


#EXTENSION 1: save computed values to csv file
fp = open ("demographics by year.csv", "w")
fp.write(str('years') + ',' + str('population')  + ',' + str('number of calves') +',' + str('number of juveniles')+
         ',' + str('number of Adult_males') +',' + str('number of Adult_females')+',' + str('number of Seniors') + '\n')

for i in range(len(simulation_results)):
    fp.write(str(i) + ',' + str(simulation_results[i][0]) + ',' + str(simulation_results[i][1]) + ',' + str(simulation_results[i][2]) + ',' + str(simulation_results[i][3]) +
             ',' + str(simulation_results[i][4]) + ',' + str(simulation_results[i][5]) + ',' + str(simulation_results[i][6]) + '\n')

fp.close()
   
   
# Extension 2 Extract years and population for graphing   
def getYears_Population(simulation_results) :
    count_of_years=0
    for result in simulation_results:
            population.append(result[0])

            count_of_years_List.append(count_of_years)
            count_of_years+=1
    return count_of_years_List, population        

count_of_years_List_graph, population_graph = getYears_Population(simulation_results)         
        
            


##Add title/axes labels etc to the plot
plt.title( 'Plot of population of elephants for '+ str(NumofYrs) + ' years' )
plt.xlabel( 'Year' )
plt.ylabel( 'Population' )
plt.plot( count_of_years_List_graph , population_graph , color='b' , marker='' )  
  
##Save, then show the plot
plt.show()  





