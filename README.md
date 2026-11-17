# Premier League Transfer Value Predictor

A Python project that estimates a Premier League player's market value from their performance statistics.

## Features

- Fetches up to 500 Premier League scorers from the football-data.org API
- Collects matches played, goals and assists
- Matches players to market values from a Transfermarkt dataset 
- Trains a Random Forest model to estimate market value
- Lets the user enter player statistics and shows the estimated value
- Caps inputs at the highest stats in the training data, so unrealistic inputs don't give unrealistic values

## Technologies Used

- Python
- Requests
- Pandas
- NumPy
- Scikit-learn
- football-data.org API

## How It Works

1. The program fetches player stats (matches, goals, assists) from the API.
2. It matches each player to a market value in `players.csv.gz`.
3. A Random Forest model is trained on the matched players, using the log of the market value so very high values don't dominate.
4. The user enters matches, goals and assists, and the program prints an estimated market value.

## Example

Input:

- Matches: 38
- Goals: 20
- Assists: 10

Output:

- Predicted Market Value: €43.7 million

## Limitations

- Trained on about 139 matched players, so predictions can be rough.
- The player list only includes players who have scored, so defenders and goalkeepers are underrepresented.
- Age, position and club are not used yet, and they strongly affect market value.
- Market values depend on how recent the dataset is.


## Project Purpose

This project was created to explore how Python, APIs, data processing and machine learning can be applied to football data.
