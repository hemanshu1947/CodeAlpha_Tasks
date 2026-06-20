# Stock Portfolio Tracker

A simple Python console application that calculates total investment value based on predefined stock prices and user-entered quantities. It can also save the portfolio summary as a TXT or CSV report.

## Features

- Predefined stock price dictionary
- User input for stock symbols and quantities
- Portfolio summary with per-stock investment value
- Total investment calculation
- Optional report export as `.txt` or `.csv`

## Tech Stack

- Python 3
- Standard Python libraries only

## Project Structure

```text
stock-portfolio-tracker/
├── stock_portfolio_tracker.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── assets/
    └── output-screenshot.png
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/stock-portfolio-tracker.git
cd stock-portfolio-tracker
```

2. Run the Python file:

```bash
python stock_portfolio_tracker.py
```

## Sample Output

```text
Enter number of stocks you want to add: 2
Enter stock name: AAPL
Enter quantity: 3
Enter stock name: TSLA
Enter quantity: 2

----- Portfolio Summary -----
AAPL -> Quantity: 3, Investment: $540
TSLA -> Quantity: 2, Investment: $500

Total Investment Value: $1040
```

## Screenshot

Add your output screenshot inside the `assets` folder and name it:

```text
output-screenshot.png
```

Then it will appear here:

![Output Screenshot](assets/output-screenshot.png)

## What I Learned

- Taking user input in Python
- Using conditional statements and loops
- Working with dictionaries/lists
- Displaying formatted console output

## Author

Created as a Python beginner project.
