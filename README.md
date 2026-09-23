# Premier_League_Transfer_Value_Predictor-
Python project that predicts Premier League player market values using performance statistics.
# Premier League Transfer Value Predictor

A Python project that estimates a Premier League player's market value using their performance statistics.

## Features

- Retrieves Premier League player data using the football-data.org API
- Collects matches, goals and assists
- Uses player market-value data
- Uses Linear Regression to estimate market value
- Allows the user to enter player statistics
- Displays an estimated market value

## Limitations
- The current model is trained using a small sample of player data, so predictions may not always be realistic.
- Predictions become less reliable when statistics are far outside the range of the training data.
 

## Technologies Used

- Python
- Requests
- Pandas
- Scikit-learn
- CSV
- football-data.org API

## How It Works

The program collects player performance data and combines it with market-value data. A Linear Regression model is then trained using matches, goals and assists to estimate a player's market value.

## Example

Input:

- Matches: 5
- Goals: 4
- Assists: 3

Output:

- Estimated Market Value: approximately €99.6 million

## Project Purpose

This project was created to explore how Python, APIs, data processing and machine learning can be applied to football data.
