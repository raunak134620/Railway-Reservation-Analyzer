<<<<<<< HEAD
Railway Reservation Analyzer

PS No.: 69

University: Rungta International Skills University
Department: School of Computer Science and Engineering
Course: Bachelor of Technology – Computer Science and Engineering
Semester: First Semester

1. Project Overview

Railway Reservation Analyzer is a Python-based project that reads railway booking information from a CSV file and analyzes the reservation data.

It uses Pandas for data analysis and Matplotlib for graphical representation.

2. Objectives

- Read railway booking data from a CSV file.
- Count bookings for each train.
- Calculate revenue per train.
- Calculate revenue using Confirmed tickets only.
- Count Confirmed, Waiting and Cancelled tickets.
- Handle missing files and invalid fare values.
- Display bar charts using Matplotlib.

3. Technologies Used

Technology| Purpose
Python 3| Programming language
Pandas| Data analysis
CSV| Data storage
Matplotlib| Bar charts
Git| Version control
GitHub| Project hosting

4. Project Structure

Railway-Reservation-Analyzer/
│
├── main.py
├── bookings.csv
├── requirements.txt
└── README.md

5. Installation

First, install Python 3.

Install the required libraries:

python -m pip install pandas matplotlib

Alternatively:

pip install -r requirements.txt

6. How to Run

Open the project folder in VS Code.

Open the terminal and execute:

python main.py

Enter the CSV filename:

bookings.csv

Select an option from the menu.

7. Features

1. Bookings per train.
2. Revenue per train (Confirmed tickets only).
3. Count bookings by status.
4. Invalid fare handling.
5. Missing CSV file handling.
6. Bar chart generation.

8. Sample Dataset

The project contains 10 sample railway booking records.

The CSV columns are:

- PNR
- Train
- Class
- Fare
- Status

9. Expected Output

Bookings per train

Train| Bookings
Gondwana| 4
Rajdhani| 3
Shatabdi| 3
Total| 10

Confirmed Revenue per Train

Train| Revenue
Gondwana| Rs. 2540
Rajdhani| Rs. 4100
Shatabdi| Rs. 1900
Total| Rs. 8540

Booking Status

Status| Count
Confirmed| 7
Waiting| 2
Cancelled| 1

10. Error Handling

The project handles:

- Missing CSV files.
- Invalid fare values.
- Negative fare values.
- Missing required columns.
- Empty CSV files.
- Invalid booking statuses.

Invalid records are skipped with a warning instead of crashing the program.

11. Conclusion

The Railway Reservation Analyzer project demonstrates the use of Python, Pandas, CSV and Matplotlib for railway reservation data analysis.

It helps analyze train bookings, calculate confirmed ticket revenue and display results through graphical charts.

12. Author

Project: Railway Reservation Analyzer
PS Number: 69
Language: Python 3
=======
# Railway-Reservation-Analyzer
| Description | Railway Reservation Analyzer using Python, Pandas and Matplotlib | | Visibility | Public | | Initialize README | Leave unchecked |
>>>>>>> 884ddf1ed03ee8da236be19462da35ff0168550e
