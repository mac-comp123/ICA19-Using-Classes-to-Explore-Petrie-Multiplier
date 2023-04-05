"""
File: petrieSim.py

Contains a simulation of the Petrie Multiplier that is based on classes.
"""

import random
import math


class Employee:
    """For this simulation, we only focus on the gender of an employee, and on whether or not this
    employee is likely to make negative statements towards the other gender."""

    def __init__(self, gender, willComment):
        """Takes in the employee's gender and whether they comment, and it saves those values to
        instance variables. It also initializes the variable that holds the comments received by this employee."""
        pass


    def __str__(self):
        """Produces a printable string format for this employee."""
        return self.gender + ": " + str(self.commentsReceived) + " sexist comments received"




def printEmployeeList(L):
    """given a list of employees, this method will print the details of each employee 
    by using the print() method"""
    pass
   

def createEmployees(totalNum):
    """Takes in the number of employees to make, builds and returns a list that contains
    that many employees. It ensures that ~80% are men and the rest women."""
    pass
    

def createCommenters(L):
    """Given a list of employees, make 20% of each gender be sexist employees. This
    method should not return anything."""
    pass

def generateComments(L):
    """Given a list of employees, have each sexist employee give one sexist comment to
    another employee of the opposite gender, chosen randomly. This method should
    not return anything """
    pass
            

def averageComments(L):
    """Returns a tuple that represents the average amount of comments received for men and women
    respectively. Return statement will be in the form (<avg_for_men>, <avg_for_women>) """
    pass

def main():
    """ this method will print out information about the average comments
    received by men and women after a simulation has been run """
    employeeList = createEmployees(100)
    createCommenters(employeeList)
    for rounds in range(50):
        generateComments(employeeList)

    (menAvg, womenAvg) = averageComments(employeeList)
    print("Men received on average  ", menAvg, "sexist comments")
    print("Women received on average", womenAvg, "sexist comments")


if __name__ == "__main__":

    # ------------------------------------------------
    # Test code for printEmployeeList
    L = [Employee('Man', True), Employee('Man', False), Employee('Woman', True), Employee('Woman', False)]
    printEmployeeList(L)

    # ------------------------------------------------
    # Test code for createEmployees
    employees = createEmployees(10)
    printEmployeeList(employees)

    # ------------------------------------------------
    # Test code for createCommenters
    createCommenters(employees)
    printEmployeeList(employees)

    # ------------------------------------------------
    # Test code for generateComments
    generateComments(employees)
    printEmployeeList(employees)

    # ------------------------------------------------
    # Test code for averageComments
    print(averageComments(employees))


    main() #<---DON'T DELETE THIS!!

