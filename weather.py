import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """

    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    human_date = date.strftime("%A %d %B %Y")
    return human_date


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    converted_to_celcius = round(((float(temp_in_farenheit) - 32) * (5/9)),1)
    return converted_to_celcius


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0
    for number in weather_data:
        sum = sum + float(number)
    mean =  sum / len(weather_data)
    return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list_of_lines = []
    with open(csv_file) as my_file: 
        read_file =csv.reader(my_file)
        next(read_file, None)
        for line in read_file:
            if line:
                integers = [int(value) if len(value) < 4 else value for value in line]
                list_of_lines.append(integers)
    return list_of_lines


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and its position in the list.
    """

    if len(weather_data) == 0:
        return ()
    
    min_value = float(weather_data[0])
    min_index = 0

    for index, temp in enumerate(weather_data):
        if float(temp) <= min_value:
            min_value = float(temp)
            min_index = index

            #workaround pre-enumerate --> min_index = len(weather_data) -1 - weather_data[::-1].index(temp)

    return (min_value, min_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) == 0:
        return ()

    max_value = float(weather_data[0])
    max_index = 0

    for index, temp in enumerate(weather_data):
        if float(temp) >= max_value:
            max_value = float(temp)
            max_index = index
            #workaround pre-enumerate --> max_index = len(weather_data) -1 - weather_data[::-1].index(temp)

    return (max_value, max_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    iso_date = []
    min_temps = []
    max_temps = []

    for line in weather_data:
        iso_date.append(line[0])
        min_temps.append(line[1])
        max_temps.append(line[2])

    min_temp, min_index = find_min(min_temps)
    max_temp, max_index = find_max(max_temps)

    min_average = calculate_mean(min_temps)
    max_average = calculate_mean(max_temps)

    summary = (f"{len(weather_data)} Day Overview\n  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {convert_date(iso_date[min_index])}.\n  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {convert_date(iso_date[max_index])}.\n  The average low this week is {format_temperature(convert_f_to_c(min_average))}.\n  The average high this week is {format_temperature(convert_f_to_c(max_average))}.\n")
    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    daily_summary = ""
    for line in weather_data:
        daily_summary = daily_summary +(f"---- {convert_date(line[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(line[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(line[2]))}\n\n")
    return daily_summary
