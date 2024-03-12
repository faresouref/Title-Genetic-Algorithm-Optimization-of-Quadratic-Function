# Genetic Algorithm Optimization

This repository contains a Python implementation of a simple genetic algorithm for optimizing a quadratic function within a specified search space.

## Overview

Genetic algorithms are a class of optimization algorithms inspired by the process of natural selection. In this implementation, the genetic algorithm is used to find the maximum value of a quadratic function `f(x) = x^2 - 4x + 3` within a given search space.

The algorithm works by generating a population of candidate solutions (chromosomes), evaluating their fitness based on the objective function, selecting the fittest individuals to act as parents for the next generation, and applying genetic operators such as crossover and mutation to create offspring. This process iterates over multiple generations until a termination condition is met.

## Files

- `genetic_algorithm.py`: Python script containing the implementation of the genetic algorithm.
- `README.md`: This file, providing an overview of the project.

## Requirements

- Python 3.x
- No external libraries required

## Usage

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/your_username/genetic-algorithm-optimization.git
    ```

2. Navigate to the repository directory:

    ```
    cd genetic-algorithm-optimization
    ```

3. Run the `genetic_algorithm.py` script:

    ```
    python genetic_algorithm.py
    ```

4. View the results printed to the console.

## Customization

- Modify the objective function `func(x)` in the `genetic_algorithm.py` script to optimize a different function.
- Adjust the search space, population size, and number of generations in the script according to your requirements.
- Experiment with different selection, crossover, and mutation strategies to improve optimization performance.


