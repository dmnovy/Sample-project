#Military Spending

#Create a menu that allows the users to select how many countries to analyze and

def country_compare(num_countries, years_countries):

    #Create a cop of the data set to conduct the analysis
    Mil_Country_Compare = Military_Data


    #create string variables based on the starting year and ending year, which will be used for column identification
    start_year = 2016 - years_countries + 1
    end_year = 2016
    
    start_spend = str(start_year) + '_spend'
    end_spend = str(end_year) + '_spend'

    start_gdp = str(start_year) + '_%gdp'
    end_gdp = str(end_year) + '_%gdp'

    start_percap = str(start_year) + '_MilPerCap'
    end_percap = str(end_year) + '_MilPerCap'






    #Section 1: Top military spending countries by the average military expenditures over the specified time period 
    print()
    print('Section 1: Top ' + str(num_countries) +' countries by average military spending from ' + str(start_year) + ' to ' + str(end_year) + '.')
    print()

    #Create 2 new columns for the average military spending and total military spending over the specified time range
    Mil_Country_Compare['Total Spending Over Time (US $M)'] =  Mil_Country_Compare[start_spend]

    #loop through the military spending columns to create a summed total
    i = start_year + 1
    while i <= end_year:
        col_indexer = str(i) + '_spend'
        Mil_Country_Compare['Total Spending Over Time (US $M)'] = Mil_Country_Compare['Total Spending Over Time (US $M)'] + Mil_Country_Compare[col_indexer]
        i = i + 1

    Mil_Country_Compare['Average Spending (US $M)'] = Mil_Country_Compare['Total Spending Over Time (US $M)'] / years_countries


    #create a list of years from the start year to the end year (used to plot years on the x-axis without the suffixes)
    year_list = list(range(start_year, end_year +1))



    #Show the countries with the largest average military spending over specified time range for the specified number of countries
    Greatest_Average = Mil_Country_Compare.sort_values(by ='Average Spending (US $M)', ascending = False).head(num_countries)
    ax = Greatest_Average['Average Spending (US $M)'].plot(kind = 'bar', title= 'Greatest Average in Military Spending (in 2015 USD, Millions)', figsize = (15,7))
    plt.legend(loc='best')
    ax.set_xlabel('Country')
    ax.set_ylabel('Average Military Spending (in Millions 2015 USD)')
    fmt = '$%1.0fM' 
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    plt.show()


    #For the same countries with the largest average military spending, create a new column that calculates the percent
    Greatest_Average_Sum = Greatest_Average['Average Spending (US $M)'].sum()
    Greatest_Average['Percent of Top Averages'] = (Greatest_Average['Average Spending (US $M)'] / Greatest_Average_Sum) * 100



    #Create a pie graph to compare the top countries with the average military spending to each other in terms of percent
    plt.figure(figsize=(10,10))
    sizes = Greatest_Average['Average Spending (US $M)'] 
    labels = Greatest_Average.index
    plt.pie(sizes, shadow = True, startangle =140, autopct='%1.1f%%')
    plt.legend(labels)
    plt.title('Top Miliary Spending Countries by Percent')
    plt.show()



    #Plot the yearly trends for the countries with the highest average yearly military spending over the specified time period
    Military_Trend = Greatest_Average.loc[:, start_spend:end_spend]

    #Change the column names to remove the '_spend' prefix and just reflect the years:
    Military_Trend.columns = year_list

    #Transpose the data set to graph years on the x axis and each line will represent a country
    Military_Trend_Transposed = Military_Trend.transpose()
    Military_Trend_Plot= Military_Trend_Transposed.plot.line(figsize = (15,10), title = 'Military Spending by Year for Countries with the Highest Average Military Spending')

    #Reform y-axis ticks to be dollar million
    fmt = '$%1.0fM' 
    yticks = mtick.FormatStrFormatter(fmt)
    Military_Trend_Plot.yaxis.set_major_formatter(yticks)
    Military_Trend_Plot.set_xlabel('Year')
    Military_Trend_Plot.set_ylabel('Military Spending USD M')
    plt.show()



    #Create the same graph as above, but exclude the US and China given the size
    if 'China, P.R.' in Greatest_Average.index and 'USA' in Greatest_Average.index and num_countries > 2:
        Military_Trend_USexcl = Greatest_Average.loc[:, start_spend:end_spend]
        Military_Trend_USexcl.columns = year_list
        Military_Trend_USexcl = Military_Trend_USexcl.drop('USA')
        Military_Trend_USexcl = Military_Trend_USexcl.drop('China, P.R.')
        Military_Trend_USexcl_Transposed = Military_Trend_USexcl.transpose()
        Military_Trend_Plot_USexcl= Military_Trend_USexcl_Transposed.plot.line(figsize = (15,10), title = 'Military Spending by Year for Countries with the Highest Average Military Spending (excl. US and China)')
        fmt = '$%1.0fM' 
        yticks = mtick.FormatStrFormatter(fmt)
        Military_Trend_Plot_USexcl.yaxis.set_major_formatter(yticks)
        Military_Trend_Plot_USexcl.set_xlabel('Year')
        Military_Trend_Plot_USexcl.set_ylabel('Military Spending USD M')
        Military_Trend_Plot_USexcl.legend(loc='lower left')
        plt.show()

    print()



    #__________________________________________________________________________________________



    #Section 2- GDP Data: For the top military spending countries, compare the percent of the GPD
    print('Section 2: compare the GDP and per capita data for the same top ' + str(num_countries) + ' military spending countries')


    #Create new columns for calculating the average %GDP over the time period
    Greatest_Average['Sum %GDP'] =  Greatest_Average[start_gdp]

    #Loop through the GDP columns to create a summed GDP amount (will then be used to calculate the average)
    j = start_year + 1
    while j <= end_year:
        col_indexer2 = str(j) + '_%gdp'
        Greatest_Average['Sum %GDP'] = Greatest_Average['Sum %GDP'] + Greatest_Average[col_indexer2]
        j = j + 1

    Greatest_Average['Average % GDP'] = Greatest_Average['Sum %GDP'] / years_countries


    #Plot the average Military spending % GDP for these countries
    ax = Greatest_Average['Average % GDP'].plot(kind = 'bar', title= 'Average Military Spending in % of GDP', figsize = (7,7))
    plt.legend(loc='best')
    ax.set_xlabel('Country')
    ax.set_ylabel('Average Military Spending in % of GDP')
    fmt = '%.0f%%' 
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    plt.show()  


    #Plot the GDP Trends
    GDP_Trends = Greatest_Average.loc[:, start_gdp:end_gdp]

    #Change the column names to remove the '_gdp' prefix and just reflect the years:
    GDP_Trends.columns = year_list

    #Transpose the data to plot years on the x-axis
    GDP_Trends_Transposed = GDP_Trends.transpose()
    GDP_Trends_Plot= GDP_Trends_Transposed.plot.line(figsize = (15,10), title = 'Military Spending as % of GDP')

    #Reform y-axis ticks to be a percent
    fmt = '%.0f%%' 
    yticks = mtick.FormatStrFormatter(fmt)
    GDP_Trends_Plot.yaxis.set_major_formatter(yticks)
    GDP_Trends_Plot.set_xlabel('Year')
    GDP_Trends_Plot.set_ylabel('Military Spending as % of GDP')
    plt.show()



    #Calculate the Average per Captia GDP by deriving from existing columns

    #Calculate the average GDP, by using the average military spneding (convert from $M to $) and the Military spending % GDP fields
    Greatest_Average['Average GDP'] = Greatest_Average['Average Spending (US $M)'] * 1000000 * 100 / Greatest_Average['Average % GDP']

    #Create a new column to calculate the average Military Capita 
    Greatest_Average['Sum MilperCapita'] =  Greatest_Average[start_percap]

    #Loop through the military per capita spending to create a summed total used to calculate the average
    k = start_year + 1
    while k <= end_year:
        col_indexer3 = str(k) + '_MilPerCap'
        Greatest_Average['Sum MilperCapita'] = Greatest_Average['Sum MilperCapita'] + Greatest_Average[col_indexer3]
        k = k + 1

    Greatest_Average['Average Military Spending Per Capita'] = Greatest_Average['Sum MilperCapita'] / years_countries   

    #Calculate the average population using the average military per capita and the average military spending
    Greatest_Average['Average Pop'] = (Greatest_Average['Average Spending (US $M)'] * 1000000) / Greatest_Average['Average Military Spending Per Capita']

    #Caclulate the average Per Capita GDP
    Greatest_Average['Average GDP Per Capita'] = Greatest_Average['Average GDP'] / Greatest_Average['Average Pop']

    #Graph the Average Military Spending Per Capita
    ax = Greatest_Average['Average Military Spending Per Capita'].plot(kind = 'bar', title= 'Average Military Spending per Capita', figsize = (7,7))
    plt.legend(loc='best')
    ax.set_xlabel('Country')
    ax.set_ylabel('Average Military Spending per Capita')
    fmt = '$%1.0f' 
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    plt.show()  

    #Graph the GDP Per Capita
    ax = Greatest_Average['Average GDP Per Capita'].plot(kind = 'bar', title= 'Average GDP per Capita', figsize = (7,7))
    plt.legend(loc='best')
    ax.set_xlabel('Country')
    ax.set_ylabel('Average GDP per Capita')
    fmt = '$%1.0f' 
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    plt.show()  

    #Create clustered bar chart for comparison
    GDPPerCap = list(Greatest_Average['Average GDP Per Capita'])
    MilPerCap = list(Greatest_Average['Average Military Spending Per Capita'])
    countryList = list(Greatest_Average.index.values)

    # create plot
    fig, ax = plt.subplots(figsize=(20,10))
    index = np.arange(num_countries)
    bar_width = 0.35
    opacity = 0.8

    Percap1 = plt.bar(index, GDPPerCap, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Avg. GDP Per Capita')

    Percap2 = plt.bar(index + bar_width, MilPerCap, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Avg. Mil Spending per Capita')

    plt.xlabel('Country')
    plt.ylabel('Mil Spending / GDP per Capita ($)')
    plt.title('Comparison of Military Spending vs. GDP Per Capita')
    plt.xticks(index + bar_width, countryList, rotation = 'vertical')
    plt.legend()
    plt.show()

    print()
    print()


    #________________________________________________________________________________________

    #Section 3: find the countries with the largest increase in military spending ($ and %)
    print('Section 3: Find the countries with the largest increase in military spending in $ and %.')
    print()


    #Create a new column for the change in spending over time is USD
    Mil_Country_Compare['Military Spending Increase (US $M)'] = Mil_Country_Compare[end_spend] - Mil_Country_Compare[start_spend]
    Mil_Country_Compare['Military Spending Increase (%)'] = (Mil_Country_Compare['Military Spending Increase (US $M)'] / Mil_Country_Compare[start_spend]) * 100


    #Show the countries with the largest increase in spending over specified time range for the specified number of countries
    Greatest_Increase = Mil_Country_Compare.sort_values(by = 'Military Spending Increase (US $M)', ascending = False).head(num_countries)
    ax = Greatest_Increase['Military Spending Increase (US $M)'].plot(kind = 'bar', title= 'Greatest Increase in Military Spending (in 2015 USD, Millions)', figsize = (7,7))
    plt.legend(loc='best')
    ax.set_xlabel('Country')
    ax.set_ylabel('Total Military Spending Increase (in Millions 2015 USD)')
    fmt = '$%1.0fM' 
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    plt.show()

    #Plot the 10 year spending trends for these countries with the greatest dollar increase
    Greatest_Increase_Trend = Greatest_Increase.loc[:, start_spend:end_spend]
    Greatest_Increase_Trend.columns = year_list
    Greatest_Increase_Trend_Transposed = Greatest_Increase_Trend.transpose()
    Greatest_Increase_Trend_Plot= Greatest_Increase_Trend_Transposed.plot.line(figsize = (7,7), title = 'Military Spending by Year')
    fmt = '$%1.0fM' 
    yticks = mtick.FormatStrFormatter(fmt)
    Greatest_Increase_Trend_Plot.yaxis.set_major_formatter(yticks)
    Greatest_Increase_Trend_Plot.set_xlabel('Year')
    Greatest_Increase_Trend_Plot.set_ylabel('Military Spending USD M')
    plt.show()    

    #Same plot as above, excluding the US and China
    if 'China, P.R.' in Greatest_Increase.index and 'USA' in Greatest_Increase.index and num_countries > 2:
        Greatest_Increase_Trend_exclUS = Greatest_Increase.loc[:, start_spend:end_spend]
        Greatest_Increase_Trend_exclUS.columns = year_list
        Greatest_Increase_Trend_exclUS = Greatest_Increase_Trend_exclUS.drop('USA')
        Greatest_Increase_Trend_exclUS = Greatest_Increase_Trend_exclUS.drop('China, P.R.')
        Greatest_Increase_Trend_exclUS_Transposed = Greatest_Increase_Trend_exclUS.transpose()
        Greatest_Increase_Trend_exclUS_Plot= Greatest_Increase_Trend_exclUS_Transposed.plot.line(figsize = (7,7), title = 'Military Spending by Year, excl. US & China')
        fmt = '$%1.0fM' 
        yticks = mtick.FormatStrFormatter(fmt)
        Greatest_Increase_Trend_exclUS_Plot.yaxis.set_major_formatter(yticks)
        Greatest_Increase_Trend_exclUS_Plot.set_xlabel('Year')
        Greatest_Increase_Trend_exclUS_Plot.set_ylabel('Military Spending USD M')
        plt.show()  



    #Show the countries with the largest Percent increase in spending over the specified time range for the specified number of countries
    Greatest_Increase_Per = Mil_Country_Compare.sort_values(by = 'Military Spending Increase (%)', ascending = False).head(num_countries)
    ax = Greatest_Increase_Per['Military Spending Increase (%)'].plot(kind = 'bar', title= 'Greatest Percent Increase in Military Spending ', figsize = (7,7))
    plt.legend(loc='best')
    ax.set_xlabel('Country')
    ax.set_ylabel('Total Military Spending Increase (% increase)')
    fmt = '%.0f%%' 
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    plt.show() 

    #Plot the 10 year spending trends for these countries with the greatest percent increase
    Greatest_Increase_Per_Trend = Greatest_Increase_Per.loc[:, start_spend:end_spend]
    Greatest_Increase_Per_Trend.columns = year_list
    Greatest_Increase_Per_Trend_Transposed = Greatest_Increase_Per_Trend.transpose()
    Greatest_Increase_Per_Trend_Plot= Greatest_Increase_Per_Trend_Transposed.plot.line(figsize = (7,7), title = 'Military Spending by Year')
    fmt = '$%1.0fM' 
    yticks = mtick.FormatStrFormatter(fmt)
    Greatest_Increase_Per_Trend_Plot.yaxis.set_major_formatter(yticks)
    Greatest_Increase_Per_Trend_Plot.set_xlabel('Year')
    Greatest_Increase_Per_Trend_Plot.set_ylabel('Military Spending USD M')
    plt.show()   

    #Same plot above, excluding China (if in data set)
    if 'China, P.R.' in Greatest_Increase_Per.index:
        Greatest_Increase_Per_Trend_exclChina = Greatest_Increase_Per.loc[:, start_spend:end_spend]
        Greatest_Increase_Per_Trend_exclChina.columns = year_list
        Greatest_Increase_Per_Trend_exclChina = Greatest_Increase_Per_Trend_exclChina.drop('China, P.R.')
        Greatest_Increase_Per_Trend_exclChina_Transposed = Greatest_Increase_Per_Trend_exclChina.transpose()
        Greatest_Increase_Per_Trend_exclChina_Plot= Greatest_Increase_Per_Trend_exclChina_Transposed.plot.line(figsize = (7,7), title = 'Military Spending by Year (excl. China)')
        fmt = '$%1.0fM' 
        yticks = mtick.FormatStrFormatter(fmt)
        Greatest_Increase_Per_Trend_exclChina_Plot.yaxis.set_major_formatter(yticks)
        Greatest_Increase_Per_Trend_exclChina_Plot.set_xlabel('Year')
        Greatest_Increase_Per_Trend_exclChina_Plot.set_ylabel('Military Spending USD M')
        plt.show()   


    #Plot only the country with the largest percent increase
    Greatest_Increase_Per_TrendII = Greatest_Increase_Per.loc[:, start_spend:end_spend]
    Greatest_Increase_Per_TrendII.columns = year_list
    Greatest_Increase_Per_TrendII = Greatest_Increase_Per_TrendII.iloc[0]
    Greatest_Increase_Per_TrendII_Transposed = Greatest_Increase_Per_TrendII.transpose()
    Greatest_Increase_Per_Trend_PlotII= Greatest_Increase_Per_TrendII_Transposed.plot.line(figsize = (7,7), title = 'Military Spending by Year')
    fmt = '$%1.0fM' 
    yticks = mtick.FormatStrFormatter(fmt)
    Greatest_Increase_Per_Trend_PlotII.yaxis.set_major_formatter(yticks)
    Greatest_Increase_Per_Trend_PlotII.set_xlabel('Year')
    Greatest_Increase_Per_Trend_PlotII.set_ylabel('Military Spending USD M')

    #calcualte the starting, ending and average growth per year for this one country
    start_mil = Greatest_Increase_Per_TrendII.iloc[0][start_spend].round(0)
    end_mil = Greatest_Increase_Per_TrendII.iloc[0][end_spend].round(0)
    avg_inc = ((start_mil - end_mil) / years_countries).round(0)
    print('Starting military expenditure: ' + str(start_mil))
    print('Ending military expenditure: ' + str(end_mil))
    print('Average growth: ' + avg_inc + ' / year')
    plt.show()  
    
    
    
    #Create a function to allow the user to enter the number of countries and number of years to analyze

def country_compare_menu():
    #limit the number of years to 10 and countries to 25 def country_compare_menu(): print('Compare the top military spending data among a selected number of countries') print('Select the number of countries to compare (between 2 and 25) :') num_countries = input() num_countries = int(num_countries) print('Select the number of year(s) to compare trends (between 2 and 10) :') years_countries = input() years_countries = int(years_countries)
    print('Compare the top military spending data among a selected number of countries')
    print('Select the number of countries to compare (between 2 and 25): ')
    num_countries = input()
    num_countries = int(num_countries)
    print('Select the number of year(s) to compare trends (between 2 and 10) :')
    years_countries = input()
    years_countries = int(years_countries)
    if num_countries >= 2 and num_countries <= 25 and years_countries >= 2 and years_countries <= 10:
        country_compare(num_countries, years_countries)
    else:
        print('Invalid number of countries / years')
        return()
    
    
    
    #Create a main function with a menu to run the analysis or quit def main(): print() print('Analysis of Military Spending') print()
def main(): 
    selection = ''
    while selection != 'q':
        print()
        print('1. Run Military Spending Analysis')
        print('q. Quit')
        print()
        selection=input('Please select 1 or q: ')
        print()
        if selection == '1':
            country_compare_menu()
        elif selection.lower() == 'q':
            selection == 'q'
            break
        else:
            print('Invalid selection. Please try again.')
            print()
main()

