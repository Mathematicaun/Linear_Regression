# Data Visualization and Linear Regression

This script performs data visualization and linear regression analysis. Below are the mathematical frameworks used in the linear regression calculation:

## Mathematical Frameworks

### Summation Operations

- **Sum of Products**: Calculates the sum of the products of corresponding elements from two arrays.
  
- **Product of Sums**: Calculates the product of the sums of the elements from two arrays.

### Linear Regression

- **Slope ($m$)**:
  
  $m = \frac{N \sum (x_i y_i) - \sum x_i \sum y_i}{N \sum x_i^2 - (\sum x_i)^2}$
  
  Where:
  - \(N\) is the number of data points.
  - \(\sum (x_i y_i)\) is the sum of the product of corresponding $x_{i}$ and $y_{i}$ values.
  - \(\sum x_i\) is the sum of $x_{i}$ values.
  - \(\sum y_i\) is the sum of $y_{i}$ values.
  - \(\sum x_i^2\) is the sum of $x_{i}^2$ values.

- **Intercept ($c$)**:
  
  $c = \frac{\sum y_i - m \sum x_i}{N}$
  
  Where:
  - \(m\) is the slope.
  - \(\sum y_i\) is the sum of $y_{i}$ values.
  - \(\sum x_i\) is the sum of $x_{i}$ values.
  - \(N\) is the number of data points.

These formulas are used to compute the parameters of the best-fit line in linear regression.

## Author
AYOUB ZAHRAN
