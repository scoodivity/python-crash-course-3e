#! python3

import matplotlib.pyplot as plt

from random_walk import RandomWalk
from random_walk_refactored import RandomWalk as RaWaRefac

# 15-1. Cubes: A number raised to the third power is a cube. Plot 
# the first five cubic numbers, and then plot the first 5,000 cubic 
# numbers.
def ex15_1():
    """Create plot for cubes."""
    x_vals = range(5_000)
    y_vals = [x**3 for x in x_vals] 
    fig, ax = plt.subplots()
    ax.scatter(x_vals, y_vals)

    plt.show()


# 15-2. Colored Cubes: Apply a colormap to your cubes plot.
def ex15_2():
    """Applies cmap to cubes plot."""
    x_vals = range(5_000)
    y_vals = [x**3 for x in x_vals] 
    fig, ax = plt.subplots()
    ax.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.RdPu)

    plt.show()


# 15-3. Molecular Motion: Modify rw_visual.py by replacing ax.scatter() 
# with ax.plot(). To simulate the path of a pollen grain on the surface 
# of a drop of water, pass in the rw.x_values and rw.y_values, and 
# include a linewidth argument. Use 5,000 instead of 50,000 points to 
# keep the plot from being too busy.
def ex15_3():
    """Simulates pollen on water."""
    rw = RandomWalk(5_000)
    rw.fill_walk()
    point_numbers = range(rw.num_points)

    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=2)
    ax.set_aspect('equal')

    plt.show()


# 15-4. Modified Random Walks: In the RandomWalk class, x_step and 
# y_step are generated from the same set of conditions. The direction 
# is chosen randomly from the list [1, -1] and the distance from the 
# list [0, 1, 2, 3, 4]. Modify the values in these lists to see what 
# happens to the overall shape of your walks. Try a longer list of 
# choices for the distance, such as 0 through 8, or remove the −1 from 
# the x- or y-direction list.
def ex15_4():
    """Describes results of modifying distance and direction in 
    RandomWalk
    """
    ans = """Done.
    Modifying the x and y direction list will change whether the
    randomwalk can turn left/right or go up/down, respectively.
    Modifying the distance range will increase the max range
    traveled. Asymmetrics changes (e.g., max x_distance 10 vs max
    y_distance 5) will stretch the walk on that axis only.
    """
    print(ans)


# 15-5. Refactoring: The fill_walk() method is lengthy. Create a new 
# method called get_step() to determine the direction and distance for 
# each step, and then calculate the step. You should end up with two 
# calls to get_step() in fill_walk():
# x_step = self.get_step()
# y_step = self.get_step()
# This refactoring should reduce the size of fill_walk() and make the 
# method easier to read and understand.
def ex15_5():
    """Demonstrates use of refactored RandomWalk class."""
    rw = RaWaRefac(5_000)
    rw.fill_walk()
    point_numbers = range(rw.num_points)

    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=2)
    ax.set_aspect('equal')

    plt.show()

# 15-6. Two D8s: Create a simulation showing what happens when you roll 
# two eight-sided dice 1,000 times. Try to picture what you think the 
# visualization will look like before you run the simulation, then see 
# if your intuition was correct. Gradually increase the number of rolls 
# until you start to see the limits of your system’s capabilities.


# 15-7. Three Dice: When you roll three D6 dice, the smallest number 
# you can roll is 3 and the largest number is 18. Create a 
# visualization that shows what happens when you roll three D6 dice.


# 15-8. Multiplication: When you roll two dice, you usually add the two 
# numbers together to get the result. Create a visualization that shows 
# what happens if you multiply these numbers by each other instead.


# 15-9. Die Comprehensions: For clarity, the listings in this section 
# use the long form of for loops. If you’re comfortable using list 
# comprehensions, try writing a comprehension for one or both of the 
# loops in each of these programs.


# 15-10. Practicing with Both Libraries: Try using Matplotlib to make a 
# die-rolling visualization, and use Plotly to make the visualization 
# for a random walk. (You’ll need to consult the documentation for each 
# library to complete this exercise.)

while True:
    chapter = 15
    exercises = '1-15'
    print(f"Ch. {chapter} exercises {exercises}. Q to quit.")
    execute_func = input("Run exercise #: ")
    if execute_func.lower() == 'q':
        break
    try:
        exec(f"ex{chapter}_{execute_func}()")
    except NameError:
        print(f"\nInvalid input. Enter a valid exercise number or Q to quit.")
    else:
        print()