# Maximizing Business Efficiency through Constrained Optimization
<img src="http://ForTheBadge.com/images/badges/made-with-python.svg"/>

# Introduction
We are developed an application that will assist companies in determining the amount of products to make in order to maximize profit based on expenditures. This open source program utilizes constrained optimization libraries in which its output is displayed through a Graphical User Interface. We formulated equations for cost and revenue with the goal of determining the combination of products that maximizes profit. To test our results, we created understandable and applicable toy problems. This application is vital for any business that wants to minimize costs, improve their profits, and make more informed business decisions.

# Table of Contents
- [Introduction](#introduction)
- [Executable](#executable)
- [Visuals](#visuals)
   + [Error Codes](#error-codes)
- [GUI Buttons](#gui-options)
- [Data Entry](#data-entry)
    + [Objective Function](#objective-function)
    + [Variables](#variables)
    + [Constraints](#constraints)
    + [Constants](#constants)
- [Dependencies](#dependencies)
- [Project Status](#project-status)
- [License](#license)
- [Authors](#authors)


# Visuals
#### Main GUI
**The user will enter their data here**
![image](https://user-images.githubusercontent.com/60274768/162229671-9dc9af38-2d3f-44d0-8cc0-108b84166b6d.png)
#### Result GUI
**The result of the program is printed here**
![image](https://user-images.githubusercontent.com/60274768/164487998-33c7e0c6-5c8c-4878-b1c5-ab5300c7fa16.png)

### Error Codes
An integer representing the status of the algorithm.

0 : Optimization proceeding nominally.<br>
1 : Iteration limit reached.<br>
2 : Problem appears to be infeasible.<br>
3 : Problem appears to be unbounded.<br>
4 : Numerical difficulties encountered.

# GUI Options

Explain what every button does

Explain how the the list boxes work, poping off when deleted, etc..

| GUI Option        |  Type    | Function  |
| ------------- |:-------------:| -----|
| Help Me      | Button | Opens this file|
| Add Variable | Button | Adds the variable in the variable list box |
| Objective Function | Text Box | This is where the objective function is typed in |
| Maximize/Minimize| Drop Down |  Choose to maximize or minimize  |
| Linear/Non-Linear| Drop Down |  Choose to do linear or non-linear  |
| Add Constraints | Button | Adds the constraint in the variable list box  |
| Clear | Button | Clears the data from the GUI |
| Optimize | Button | Calculates the result based on the inputs |


# Data Entry
This is a guide to entering the correct data into the GUI!

**When using multiplication, you must notate with a \*.**

**Division is notated by a \\**



### Objective Function
When entering an objective function make sure every variable has been defined in the variable box.
### Variables
For the variables you must enter a single character.
Examples are: x, y, z.

If you have variables such as Chocolate, Gummies, Seltzer, etc.
you should use variables such as c, g, s.

Entering a variable that is more than 1 character will cause an error.
<br />
You must not enter two of the same variables.

### Constraints
Constraints must be at least 3 characters long. Anything less will cause an error.
Examples are: x<9, y=15, z+y=500

You must not put a constraint on a variable that is not already a defined variable.

### Constants
If you have a constant in the objective function:
1. Create a variable for it in the variable box
2. Use that variable in the objective function
3. Set the variable to its value in the constraints box
  - e.g.: x=200


# Dependencies
**pip install numpy**

**pip install scipy**

**pip install tkinter**

# Python to Executable
**pip install pyinstaller**

**pip install auto-py-to-exe**

*Run: auto-py-to-exe*


# Project Status
Currently the program can allow for maximizing and minimizing of linear functions. Future work on this program will maximizing and minimizing non linear functions.

# License
GNU General Public License v3.0
<br />
[Click here to learn more](https://github.com/nburnet1/Brandstract/blob/main/LICENSE)

# Authors
Noah Burnette<br>
Paul Ikenberry<br>
Liam O'Dowd<br>
R.J. Stubbs
