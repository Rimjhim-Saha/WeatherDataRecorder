# weather_recorder.py

import pandas as pd
from datetime import datetime

# Store weather data
weather_data = []
unique_dates = set()

# Function to add weather entry
def add_weather_entry(date_str, temperature, condition):
    if date_str in unique_dates:
        print("❌ Entry for this date already exists.")
        return
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        entry = {
            "Date": date_str,
            "Temperature": temperature,
            "Condition": condition
        }
        weather_data.append(entry)
        unique_dates.add(date_str)
        print("✅ Entry added successfully.")
    except ValueError:
        print("❌ Invalid date format! Use YYYY-MM-DD.")

# Function to view all entries
def view_data():
    if not weather_data:
        print("📭 No data yet.")
        return
    df = pd.DataFrame(weather_data)
    print("\n📋 All Weather Data:")
    print(df)

# Function to analyze and export summary
def export_summary():
    if not weather_data:
        print("⚠️ No data to analyze.")
        return
    df = pd.DataFrame(weather_data)
    avg_temp = df["Temperature"].mean()
    condition_counts = df["Condition"].value_counts()

    print("\n📊 Weather Summary:")
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print("\nWeather Condition Counts:")
    print(condition_counts)

    df.to_csv("weather_data.csv", index=False)
    print("💾 Data exported to weather_data.csv")

# Main menu
def main():
    while True:
        print("\n--- Weather Data Recorder ---")
        print("1. Add Weather Data")
        print("2. View All Entries")
        print("3. Export Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (°C): "))
                condition = input("Enter weather condition (e.g., Sunny, Rainy): ")
                add_weather_entry(date, temp, condition)
            except ValueError:
                print("❌ Please enter a valid temperature.")
        elif choice == '2':
            view_data()
        elif choice == '3':
            export_summary()
        elif choice == '4':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    main()
