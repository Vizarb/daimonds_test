import pandas as pd
import os
from enum import Enum

# Enum class to define menu options with corresponding values
class MenuOption(Enum):
    SHOW_ALL = 1
    AVERAGE_PRICE = 2
    MOST_EXPENSIVE = 3
    IDEAL_NUMBER = 4
    COLORS = 5
    CARATS = 6
    AVERAGE_PRICE_CARAT = 7
    AVERAGE_PRICE_BY_COLOR = 8
    CLEAR_TERMINAL = 888
    EXIT = 999

# Function to read and display the CSV file content
def read_csv(filename):
    try:
        df = pd.read_csv(filename)
        print(df)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Function to find and print the most expensive diamond's price from the CSV
def most_expensive(filename):
    try:
        df = pd.read_csv(filename)
        if 'price' not in df.columns:
            print("The CSV file does not contain a 'price' column.")
            return

        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df = df.dropna(subset=['price'])

        if df['price'].empty:
            print("No valid price data available.")
        else:
            max_price = df['price'].max()
            print(f"The highest price is: {max_price:.2f}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Function to count and print the number of diamonds with an 'Ideal' cut
def ideal_diamonds_amount(filename):
    try:
        df = pd.read_csv(filename)
        if 'cut' not in df.columns:
            print("The CSV file does not contain a 'cut' column.")
            return

        amount_of_ideal = df['cut'].str.count('Ideal').sum()
        print(f"The Ideal amount is: {amount_of_ideal}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Function to display the count of each diamond color in the CSV
def colors_of_diamonds(filename):
    try:
        df = pd.read_csv(filename)
        if 'color' not in df.columns:
            print("The CSV file does not contain a 'color' column.")
            return

        color_counts = df['color'].value_counts()

        print("Color counts:")
        for color, count in color_counts.items():
            print(f"{color}: {count}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Function to calculate and print the median carat weight of diamonds
def cart_of_daimonds(filename):
    try:
        df = pd.read_csv(filename)
        if 'carat' not in df.columns:
            print("The CSV file does not contain a 'carat' column.")
            return

        carat_median = df['carat'].median()
        print(f"Median carat: {carat_median}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Function to calculate and display the average carat weight by diamond cut
def avg_cart_of_diamonds(filename):
    try:
        df = pd.read_csv(filename)
        if 'cut' not in df.columns or 'carat' not in df.columns:
            print("The CSV file does not contain the required 'cut' or 'carat' columns.")
            return

        avg_carat_by_cut = df.groupby('cut')['carat'].mean()

        print("Average carat for each type of cut:")
        for cut, avg_carat in avg_carat_by_cut.items():
            print(f"{cut}: {avg_carat:.2f}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Function to calculate and display the average price of diamonds by color
def avg_price_of_diamonds_by_color(filename):
    try:
        df = pd.read_csv(filename)
        if 'price' not in df.columns or 'color' not in df.columns:
            print("The CSV file does not contain the required 'price' or 'color' columns.")
            return

        avg_price_by_color = df.groupby('color')['price'].mean()

        print("Average price for each color:")
        for color, avg_price in avg_price_by_color.items():
            print(f"{color}: {avg_price:.2f}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Function to calculate and print the average price of all diamonds
def average_price(filename):
    try:
        df = pd.read_csv(filename)
        if 'price' not in df.columns:
            print("The CSV file does not contain a 'price' column.")
            return

        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df = df.dropna(subset=['price'])

        if df['price'].empty:
            print("No valid price data available.")
        else:
            average = df['price'].mean()
            print(f"The average price is: {average:.2f}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Function to clear the terminal screen
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the menu options to the user
def display_menu():
    for option in MenuOption:
        print(f"{option.value}. {option.name}")

# Main menu function to handle user input and execute corresponding actions
def menu():
    filename = input("Enter your full file name with the ending: ").strip()
    while True:
        display_menu()
        try:
            user_input = int(input('Please select your choice: '))
            selected_option = MenuOption(user_input)

            if selected_option == MenuOption.SHOW_ALL:
                read_csv(filename)
            elif selected_option == MenuOption.IDEAL_NUMBER:
                ideal_diamonds_amount(filename)
            elif selected_option == MenuOption.AVERAGE_PRICE:
                average_price(filename)
            elif selected_option == MenuOption.MOST_EXPENSIVE:
                most_expensive(filename)
            elif selected_option == MenuOption.COLORS:
                colors_of_diamonds(filename)
            elif selected_option == MenuOption.CARATS:
                cart_of_daimonds(filename)
            elif selected_option == MenuOption.AVERAGE_PRICE_CARAT:
                avg_cart_of_diamonds(filename)
            elif selected_option == MenuOption.AVERAGE_PRICE_BY_COLOR:
                avg_price_of_diamonds_by_color(filename)
            elif selected_option == MenuOption.CLEAR_TERMINAL:
                clear_terminal()
            elif selected_option == MenuOption.EXIT:
                print("Goodbye!")
                exit()
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    menu()
