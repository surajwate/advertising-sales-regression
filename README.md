# Advertising Sales Regression

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-brightgreen)](https://advertising-sales-regression.streamlit.app/)

This repository contains the source code for a Streamlit app that demonstrates Simple and Multiple Linear Regression models applied to advertising sales data. The models were created and explained in detail in the following blog posts:

- [Simple Linear Regression](https://surajwate.com/blog/SimpleLinearRegression/)
- [Multiple Linear Regression](https://surajwate.com/blog/MultipleLinearRegression/)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [App Demo](#app-demo)
- [Data](#data)
- [Modeling](#modeling)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project showcases the application of Simple and Multiple Linear Regression models to predict sales based on advertising data. The models were built using Python and deployed using Streamlit, a popular framework for creating interactive web applications. The app allows users to explore the data, visualize relationships, and make predictions based on the regression models.

## Features

- **Data Visualization**: Interactive plots to explore the relationship between advertising channels (TV, Radio, Newspaper) and sales.
- **Model Building**: Simple and Multiple Linear Regression models are built and explained.
- **Prediction Interface**: Users can input their own values for advertising spend to see the predicted sales.
- **Explanation**: The app includes brief explanations of how the models work and what the results mean.

## Installation

To run this application locally, you need to have Python installed. Then, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/surajwate/advertising-sales-regression.git
    cd advertising-sales-regression
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Usage

Once the app is running, you'll be able to interact with the regression models through the web interface:

- **Input Data**: Adjust the sliders to input different values for TV, Radio, and Newspaper advertising budgets.
- **View Results**: The app will display the predicted sales based on the regression models.
- **Visualize**: Explore the interactive plots to understand the relationship between the different variables.

## App Demo

You can try out the live version of the app here: [Advertising Sales Regression App](https://advertising-sales-regression.streamlit.app/)

## Data

The dataset used in this project is the **Advertising Dataset**, which includes data on TV, Radio, and Newspaper advertising budgets and their corresponding sales. This dataset is a classic example used to explain linear regression.

- **Features**: 
  - `TV`: Advertising budget spent on TV (in thousands of dollars).
  - `Radio`: Advertising budget spent on Radio (in thousands of dollars).
  - `Newspaper`: Advertising budget spent on Newspapers (in thousands of dollars).
- **Target**: 
  - `Sales`: Sales generated (in thousands of units).

## Modeling

### Simple Linear Regression

- **Model**: Predicts sales based on a single independent variable (e.g., TV advertising).
- **Interpretation**: The slope of the regression line indicates how much sales are expected to increase for each additional dollar spent on TV advertising.

### Multiple Linear Regression

- **Model**: Predicts sales based on multiple independent variables (TV, Radio, and Newspaper advertising).
- **Interpretation**: Shows how sales are influenced by each advertising channel, accounting for the effects of the others.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
