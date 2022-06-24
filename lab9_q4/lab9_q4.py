# February Temperatures for each region, based on their index in .csv file
FEB_NE_TEMP = 3
FEB_MW_TEMP = 4
FEB_PA_TEMP = 5

# March Temps for each region, based on their index in .csv file
MAR_NE_TEMP = -3
MAR_MW_TEMP = -2
MAR_PA_TEMP = -1

LOCATION = ['Northeast', 'Midwest', 'Pennsylvania'] # these locations are referenced in the print statements

def extract_feb_averages(year_data):
    """
    Returns a February averages for a year by region
    :param year_data: list of the years data
    :return: (Northeast Feb, Midwest Feb, PA Feb)
    """

    return year_data[FEB_NE_TEMP], year_data[FEB_MW_TEMP], year_data[FEB_PA_TEMP]

def extract_march_averages(year_data):
    """
    Returns a March averages for a year by region
    :param year_data: list of the years data
    :return: (Northeast March, Midwest March, PA March)
    """

    return year_data[MAR_NE_TEMP], year_data[MAR_MW_TEMP], year_data[MAR_PA_TEMP]

def update_totals(month_totals, curr_month_avgs):
    """
    Returns an updated total of average temperatures based on region
    :param month_totals: running total or months sum average temperatures
    :param curr_month_avgs: new month averages being added to month_totals
    :return: [Northeast Avg Total, Midwest March Avg Total, PA March Avg
    Total]
    """
    if curr_month_avgs[0] == "":
        return month_totals # if there are no new month averages
    
    running_totals = [] # initialize as empty list
    
    for index in range(len(curr_month_avgs)):
        running_total = month_totals[index] + float(curr_month_avgs[index]) # add nth element of months sum average temp with new month average
        running_totals.append(running_total) # append the result to list of running totals
    
    return running_totals

def analyze_data(filename):
    """
    Analyzes data in .csv file, calculates total temperature averages for each region based on month and full/no groundhog shadow.
    Afterwards, the function prints out these averages.
    :return: None
    """
    file_obj = open(filename, 'r')
    
    # initialize as lists with three empty number elements
    full_shadow_feb_totals = [0,0,0] 
    no_shadow_feb_totals = [0,0,0]
    
    full_shadow_mar_totals = [0,0,0]
    no_shadow_mar_totals = [0,0,0]

    # initialize counters
    full_shadow_ct = 0
    no_shadow_ct = 0
    
    file_obj.readline() # disregard first line

    for line in file_obj:
        line = line.strip().split(',') # for each line, remove whitespace and split line into a list, based on commas
        
        if line[1] == 'Full Shadow':
            feb_avgs = extract_feb_averages(line) # extract_feb_averages for the line, saved as variable
            march_avgs = extract_march_averages(line)
            
            if feb_avgs[0] != '':
                full_shadow_ct += 1 # increment if there was no shadow data for particular year
            
            # update totals
            full_shadow_feb_totals = update_totals(full_shadow_feb_totals, feb_avgs)
            full_shadow_mar_totals = update_totals(full_shadow_mar_totals, march_avgs)

        elif line[1] == 'No Shadow':
            feb_avgs = extract_feb_averages(line)
            march_avgs = extract_march_averages(line)
            if feb_avgs[0] != "":
                no_shadow_ct += 1
            no_shadow_feb_totals = update_totals(no_shadow_feb_totals, feb_avgs)
            no_shadow_mar_totals = update_totals(no_shadow_mar_totals, march_avgs)
        
    for i in range(len(LOCATION)):

        # calculate averages
        feb_full_avg = full_shadow_feb_totals[i] / full_shadow_ct
        feb_no_avg = no_shadow_feb_totals[i] / no_shadow_ct
        mar_full_avg = full_shadow_mar_totals[i] / full_shadow_ct
        mar_no_avg = no_shadow_mar_totals[i] / no_shadow_ct
        
        print("{} when Phil sees his shadow the avg temp in FEB is {} when he doesn't see his shadow the average is {}".format(LOCATION[i],round(feb_full_avg, 2), round(feb_no_avg, 2)))
        print("{} when Phil sees his shadow the avg temp in MAR is {} when he doesn't see his shadow the average is {}".format(LOCATION[i],round(mar_full_avg, 2), round(mar_no_avg, 2)))

    file_obj.close()

analyze_data('groundhog_data.csv') # .csv file contains data on temperatures, for certain regions, for certain years of Groundhog Day.