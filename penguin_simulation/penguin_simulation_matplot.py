'''Papa Yaw Owusu Nti
    10/18/2023
    This program accepts user input to specify preferred years between El-Nino and numbers of years to simulate 
    and graphs the population growth every 5 years using the standard factors from the runSimulation function 
    in penguin.py
'''

import pylab as plt
import penguin_simulation



#accept user input for El_Nino Years and simulation years
Years_Between_ElNino= int(input('input your preferred years between EL-Nino:'))
N_yr= int(input('input your preferred number of Simulation years:'))

# Set standard parameters 
IniPopSize=500
ProbaFemales=0.5
ProbaElNino= 1.0/(Years_Between_ElNino)
GrowthStd =1.188
GrowthElNino=0.41
MaxCap=2000
MiniViaPop=10

# initialize plotting lists
years = []
population = [] 


# make sure 
for i in range(1, N_yr+1):
    if i%5 == 0:
        years.append(i)
        population_simulation= penguin.runSimulation(N_yr,IniPopSize,ProbaFemales, ProbaElNino, GrowthStd, GrowthElNino, MaxCap, MiniViaPop)
        population.append(population_simulation)


##Add title/axes labels etc to the plot
plt.title( 'Population growth of penguins' )
plt.xlabel( 'Year' )
plt.ylabel( 'Population' )
plt.plot( years , population , color='b' , marker='' )    
##Save, then show the plot
plt.savefig( 'populationbyyear.png' , bbox_inches='tight' )
plt.show()  