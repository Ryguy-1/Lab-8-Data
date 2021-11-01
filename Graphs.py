import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_lists_from_column(df, column_name):
    return df[column_name].tolist()

if __name__ == '__main__':
    # Read CSV file
    df = pd.read_csv('ExportedData.csv')
    print(df.head())

    # Get lists from columns
    # 9.9 degrees C
    nine_nine_time = get_lists_from_column(df, 'Time (s) 9.9')
    nine_nine_force = get_lists_from_column(df, 'Force (N) 9.9')

    # 11.4 degrees C
    eleven_four_time = get_lists_from_column(df, 'Time (s) 11.4')
    eleven_four_force = get_lists_from_column(df, 'Force (N) 11.4')

    # 13.6 degrees C
    thirteen_six_time = get_lists_from_column(df, 'Time (s) 13.6')
    thirteen_six_force = get_lists_from_column(df, 'Force (N) 13.6')

    # 15.2 degrees C
    fifteen_two_time = get_lists_from_column(df, 'Time (s) 15.2')
    fifteen_two_force = get_lists_from_column(df, 'Force (N) 15.2')

    # 16.7 degrees C
    sixteen_seven_time = get_lists_from_column(df, 'Time (s) 16.7')
    sixteen_seven_force = get_lists_from_column(df, 'Force (N) 16.7')

    # 17.7 degrees C
    seventeen_seven_time = get_lists_from_column(df, 'Time (s) 17.7')
    seventeen_seven_force = get_lists_from_column(df, 'Force (N) 17.7')

    # 19.0 degrees C
    nineteen_time = get_lists_from_column(df, 'Time (s) 19.0')
    nineteen_force = get_lists_from_column(df, 'Force (N) 19.0')

    # 20.1 degrees C
    twenty_one_time = get_lists_from_column(df, 'Time (s) 20.1')
    twenty_one_force = get_lists_from_column(df, 'Force (N) 20.1')

    # 21.4 degrees C
    twenty_one_four_time = get_lists_from_column(df, 'Time (s) 21.4')
    twenty_one_four_force = get_lists_from_column(df, 'Force (N) 21.4')

    # Remove nan values and values above -0.4 for force lists
    nine_nine_force = [x for x in nine_nine_force if not np.isnan(x) and x < -0.4]
    eleven_four_force = [x for x in eleven_four_force if not np.isnan(x) and x < -0.4]
    thirteen_six_force = [x for x in thirteen_six_force if not np.isnan(x) and x < -0.4]
    fifteen_two_force = [x for x in fifteen_two_force if not np.isnan(x) and x < -0.4]
    sixteen_seven_force = [x for x in sixteen_seven_force if not np.isnan(x) and x < -0.4]
    seventeen_seven_force = [x for x in seventeen_seven_force if not np.isnan(x) and x < -0.4]
    nineteen_force = [x for x in nineteen_force if not np.isnan(x) and x < -0.4]
    twenty_one_force = [x for x in twenty_one_force if not np.isnan(x) and x < -0.4]
    twenty_one_four_force = [x for x in twenty_one_four_force if not np.isnan(x) and x < -0.4]

    # Average Each List Force Values
    nine_nine_avg_force = np.mean(nine_nine_force)
    eleven_four_avg_force = np.mean(eleven_four_force)
    thirteen_six_avg_force = np.mean(thirteen_six_force)
    fifteen_two_avg_force = np.mean(fifteen_two_force)
    sixteen_seven_avg_force = np.mean(sixteen_seven_force)
    seventeen_seven_avg_force = np.mean(seventeen_seven_force)
    nineteen_avg_force = np.mean(nineteen_force)
    twenty_one_avg_force = np.mean(twenty_one_force)
    twenty_one_four_avg_force = np.mean(twenty_one_four_force)

    # Create list of average force values
    avg_force_list = [nine_nine_avg_force, eleven_four_avg_force, 
    thirteen_six_avg_force, fifteen_two_avg_force, sixteen_seven_avg_force, 
    seventeen_seven_avg_force, nineteen_avg_force, twenty_one_avg_force, twenty_one_four_avg_force]

    # Create list of force numbers
    temp_list = [9.9, 11.4, 13.6, 15.2, 16.7, 17.7, 19.0, 20.1, 21.4]

    # Plot avg_force_list versus force_list with a linear trendline and scatter plot
    plt.scatter(temp_list, avg_force_list)
    plt.xlabel('Temperature (C)')
    plt.ylabel('Average Force (N)')
    plt.title('Average Force vs. Temperature')
    # Get trendline using polyfit
    z = np.polyfit(temp_list, avg_force_list, 1)
    p = np.poly1d(z)
    plt.plot(temp_list, p(temp_list), "r--")
    # Label each point with its y value rounded to 3 decimal places
    for i, txt in enumerate(avg_force_list):
        plt.annotate(round(txt, 3), (temp_list[i], avg_force_list[i]))
    plt.show()


    # Calculate coeficient of friction for each average force value
    gravity = 9.81
    mass_bar = .490
    coef_friction_list = []
    for i in range(len(avg_force_list)):
        coef_friction = avg_force_list[i] / (mass_bar * gravity)
        coef_friction_list.append(coef_friction)

    print(coef_friction_list)

    # Plot coeficient of friction versus force_list with a linear trendline and scatter plot
    plt.scatter(temp_list, coef_friction_list)
    plt.xlabel('Temperature (C)')
    plt.ylabel('Coeficient of Friction')
    plt.title('Coeficient of Friction vs. Temperature')
    # Get trendline using polyfit
    z = np.polyfit(temp_list, coef_friction_list, 1)
    p = np.poly1d(z)
    plt.plot(temp_list, p(temp_list), "r--")
    # Label each point with its y value rounded to 5 decimal places
    for i in range(len(temp_list)):
        plt.annotate(str(round(coef_friction_list[i], 5)), xy=(temp_list[i], coef_friction_list[i]))
    plt.show()
