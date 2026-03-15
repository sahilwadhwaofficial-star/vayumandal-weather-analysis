# =========================
# Vayumandal Setup Cell
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("🌦 Running Vayumandal Weather Analysis...")

class Independent_Analysis:
    def __init__(self,df,disp):
        if 'datetime' in df.columns:
            df['datetime'] = pd.to_datetime(df['datetime'])
            df.set_index('datetime', inplace=True)
        self.pdf = df
        self.disp = disp

    
    def get_key(self,d,v):
        i = 0
        for k,v1 in d.items():
            i +=1
            if v == v1:
                return(k,i)
        return (None, -1) 
                
    def Monthly_pressure_analysis(self,*data):
        try:
            pdf = self.pdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return

        #Month extraction from the datetime object
        pdf['month'] = pdf.index.to_period('M').astype(str)
        
        #grouping of month and avg pressure
        monthly_avg = pdf.groupby('month')[data[0]].mean().round(2)

        result = {}
        for k,v in monthly_avg.items():
            result[pd.to_datetime(str(k))] =  float(v)
            

        usr = data[1] 
        d1 = {}
        for k,v in result.items():
            if (k.year) == usr:
                d1[k.strftime("%B")] = v
        #PLOT
        dates = d1.keys()
        pressure = d1.values()
        plt.figure(figsize=(12,6))
        plt.plot(dates,pressure,marker= "o",linestyle = '-',color = 'royalblue')
        str1 = "Monthly "+ disp+ "in " + str(data[0]) + " in " + str(usr)
        plt.title(str1)
        plt.xlabel("Month")
        plt.ylabel(disp)
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()
        marr = np.array(list(d1.values()))
        mmax = marr.max()
        mmin = marr.min()
        mavg = marr.mean()
        print(f"Maximum {disp} is in ", self.get_key(d1,mmax)[0]," : ",mmax)
        print(f"Minimum {disp} is in ", self.get_key(d1,mmin)[0]," : ",mmin)
        print(f"Average {disp} is : ", mavg.round(2))

    
    def Yearly_pressure_analysis(self,state):
        try:
            pdf = self.pdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return

        #conversion of datetime to proper datetime object

        #Year extraction from the datetime object
        pdf['year'] = pdf.index.to_period('Y').astype(str)
            
        #grouping of year and avg pressure
        yearly_avg = pdf.groupby('year')[state].mean().round(2)

        result = {}
        for k,v in yearly_avg.items():
            result[int(k)] = v

        #Plotting
        years = result.keys()
        pressure = result.values()
        plt.figure(figsize=(12,6))
        plt.plot(years,pressure,marker= "o",linestyle = '-',color = 'royalblue')
        str1 = "Yearly "+disp+" analysis of " + state
        plt.title(str1)
        plt.xlabel("Year")
        plt.ylabel(disp)
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()
        marr = np.array(list(result.values()))
        mmax = marr.max()
        mmin = marr.min()
        mavg = marr.mean()
        print(f"Maximum {disp} is in ", self.get_key(result,mmax)[0]," : ",mmax)
        print(f"Maximum {disp} is in ", self.get_key(result,mmin)[0]," : ",mmin)
        print(f"Average {disp} is : ", mavg.round(2))
        print("\n\n\n")
    def Hourly_Analysis(self,state,disp):
        try:
            tdf = self.pdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return
        city = state     # Choosing a city to analyze hourly pattern
        tdf['hour'] = tdf.index.hour     # Extracting hour from datetime index

        hourly_avg = tdf.groupby('hour')[city].mean()     # Grouping by hour and average

        plt.figure(figsize=(10, 5))
        plt.plot(hourly_avg.index, hourly_avg.values, marker='o', color='purple')
        plt.title(f'Hourly Average {disp} in {city}')
        plt.xlabel('Hour of Day')
        plt.ylabel(disp)
        plt.xticks(range(0, 24))
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    def main(self):
        try:
            pdf = self.pdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return
        
        while True:
            print("States :")
            b = 0
            for i in range(1,len(pdf.columns)):
                print(b+1,")",pdf.columns[i])
                b+=1
            print(f"Select One Option :-\n1 - Monthly Air {disp} Analysis\n2 - Yearly Air {disp} Analysis \n3 - All\n4 - Exit\n5 - Hourly {disp}Analysis")
            pref= int(input("Enter your Preference No:- "))
            if pref == 4:
                print("Shutting Down.......")
                return
            elif pref == 1:
                state = input("Write your prefrence as it is:").strip()
                yr = int(input("Write Year between 2012-2017:"))
                self.Monthly_pressure_analysis(state,yr)
            elif pref == 2:
                state = input("Write your prefrence as it is:").strip()
                self.Yearly_pressure_analysis(state)
            elif pref == 3:
                print("Monthly Analysis:-")
                state = input("Write your prefrence as it is:").strip()
                yr = int(input("Write Year between 2012-2017:"))
                self.Monthly_pressure_analysis(state,yr)
                print("Yearly Analysis:-")
                print("##############")
                self.Yearly_pressure_analysis(state 
                print("Hourly Analysis:-")
                print("##############")
                self.Hourly_Analysis(state)
            elif pref == 5:
                state = input("Write your prefrence as it is:").strip()
                self.Hourly_Analysis(state)
            else:
                print("Invalid Option")
class Advanced_analysis:
    def __init__(self,df,disp):
        self.tdf = df
        self.disp = disp
    
    def daily_Average_trends(self,cities):
        try:
            tdf = self.tdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return
        
        selected_cities = cities # Selecting cities for visualization
        daily_avg = tdf[selected_cities].resample('D').mean()  # Resample to daily averages

        plt.figure(figsize=(14, 6))
        for city in selected_cities:
            plt.plot(daily_avg.index, daily_avg[city], label=city)
        opt = 'Daily Average'+ disp +'Trends'
        plt.title(opt)
        plt.xlabel('Date')
        plt.ylabel(disp)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    def max_min_calculation(self):
        try:
            tdf = self.tdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return
        # Find the hottest temperature and which city/time it occurred
        max_temp = tdf.max().max()
        max_city = tdf.max().idxmax()
        max_time = tdf[tdf[max_city] == max_temp].index[0]

        # Find coldest temperature and where it occurred
        min_temp = tdf.min().min()
        min_city = tdf.min().idxmin()
        min_time = tdf[tdf[min_city] == min_temp].index[0]

        print(f"Maximum {disp}: {max_temp:.2f} in {max_city} on {max_time}")
        print(f"Mininmum {disp}: {min_temp:.2f} in {min_city} on {min_time}")
        
    def Avg_per(self):
        try:
            tdf = self.tdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return
        avg_temps = tdf.mean().sort_values(ascending=False)   # Computing average temperature per city
        plt.figure(figsize=(10, 6))
        avg_temps.plot(kind='bar', color='red')
        plt.title('Average '+ disp +' per City')
        plt.ylabel(disp)
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
        # Top 5 hottest and coldest cities by average temp
        opt = "Top 5 Highest"+disp+" Cities (Average "+disp+"):"
        print(opt)
        print(avg_temps.head(5))
        opt2 = "\nTop 5 lowest "+disp+" Cities (Average "+disp+"):"
        print(opt2)
        print(avg_temps.tail(5))
        
    def hist(self):
        try:
            tdf = self.tdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return
        monthly_avg = tdf.resample('ME').mean().mean(axis=1)  #histogram of monthly avg. temperatures of all cities
        plt.figure(figsize=(10, 5))
        plt.hist(monthly_avg, bins=12, color='teal', edgecolor='black')
        opt = 'Histogram of Monthly Average '+disp+' (All Cities Combined)'
        plt.title(opt)
        opt2= 'Average '+disp
        plt.xlabel(opt2)
        plt.ylabel('Frequency (Number of Months)')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
    def monthly_yearly_analysis_template(self, year, cities):
        try:
            tdf = self.tdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return

        # Ensure datetime index
        tdf.index = pd.to_datetime(tdf.index)

        # Resampling by month and year
        monthly_avg = tdf.resample('ME').mean()
        monthly_max = tdf.resample('ME').max()
        monthly_min = tdf.resample('ME').min()

        yearly_avg = tdf.resample('YE').mean()
        yearly_max = tdf.resample('YE').max()
        yearly_min = tdf.resample('YE').min()

        # Monthly Line Plot
        print(f"\nMonthly {disp} Trends for Year {year}")
        monthly_avg_year = monthly_avg.loc[str(year)]
        monthly_max_year = monthly_max.loc[str(year)]
        monthly_min_year = monthly_min.loc[str(year)]

        for city in cities:
            plt.figure(figsize=(10, 5))
            plt.plot(monthly_avg_year.index.month_name(), monthly_avg_year[city], label='Average', color='blue')
            plt.plot(monthly_max_year.index.month_name(), monthly_max_year[city], label='Maximum', color='green')
            plt.plot(monthly_min_year.index.month_name(), monthly_min_year[city], label='Minimum', color='red')
            plt.title(f"Monthly {disp} - {city} ({year})")
            plt.xlabel("Month")
            plt.ylabel(disp)
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        # Yearly Line Plot 
        print(f"\nYearly {disp} Trends")
        for city in cities:
            plt.figure(figsize=(10, 5))
            plt.plot(yearly_avg.index.year, yearly_avg[city], label='Average', marker='o', color='blue')
            plt.plot(yearly_max.index.year, yearly_max[city], label='Maximum', marker='^', color='green')
            plt.plot(yearly_min.index.year, yearly_min[city], label='Minimum', marker='v', color='red')
            plt.title(f"Yearly {disp} - {city}")
            plt.xlabel("Year")
            plt.ylabel(disp)
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        # Monthly Bar Chart 
        print(f"\nMonthly {disp} (Bar Chart) - {year}")
        for city in cities:
            plt.figure(figsize=(12, 6))
            x = monthly_avg_year.index.month_name()
            plt.bar(x, monthly_avg_year[city], label='Average', color='blue', alpha=0.6)
            plt.bar(x, monthly_max_year[city], label='Maximum', color='green', alpha=0.4)
            plt.bar(x, monthly_min_year[city], label='Minimum', color='red', alpha=0.4)
            plt.title(f"Monthly {disp} (Bar Chart) - {city} ({year})")
            plt.xlabel("Month")
            plt.ylabel(disp)
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    def main(self):
        try:
            tdf = self.tdf
            disp = self.disp
        except:
            print("Dataframe Parsing Error")
            return
            
        # Define cities for analysis
        print("States :")
        b = 0
        for i in range(1,len(tdf.columns)):
            print(b+1,")",tdf.columns[i])
            b+=1
        inp = int(input("Enter no of Cities you wanna analyze :"))
        selected_cities = []
        for i in range(inp):
            city = input("Enter City :- ").strip()
            selected_cities.append(city)
        # Execute class methods
        year = int(input("Enter year for monthly_yearly_analysis :-"))
        self.monthly_yearly_analysis_template(year, selected_cities)
        self.daily_Average_trends(selected_cities)
        self.max_min_calculation()
        self.Avg_per()
        self.hist()
def main():
    print("Select the parameter to analyze:")
    print("1 - Temperature")
    print("2 - Humidity")
    print("3 - Wind Speed")
    print("4 - Air Pressure")
    ch = int(input("Enter your choice (1-4): "))
    if ch == 1:
        disp = "Temperature (°C)"
        path = "data/processed/cleaned_temp.csv"
    elif ch == 2:
        disp = "Humidity"
        path = "data/processed/cleaned_humidity2.csv"
    elif ch == 3:
        disp = "Wind Speed (km/h)"
        path = "data/processed/wind_speed_final.csv"
    elif ch == 4:
        disp = "Air Pressure (hPa)"
        path = "data/processed/FINAL_pressure.csv"
    else:
        print("Invalid Choice")
        return

    try:
        df = pd.read_csv(path)
        if 'datetime' in df.columns:
            df['datetime'] = pd.to_datetime(df['datetime'])
            df.set_index('datetime', inplace=True)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    ch1 = int(input("Choose analysis type:\n1 - Independent Analysis\n2 - Advanced Analysis\nEnter your choice: "))

    if ch1 == 1:
        obj = Independent_Analysis(df, disp)
        obj.main()
    elif ch1 == 2:
        obj = Advanced_analysis(df, disp)
        obj.main()
    else:
        print("Invalid Analysis Type")
if __name__ == "__main__":
    main()
    print("✅ Analysis Completed Successfully")
