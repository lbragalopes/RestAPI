# - PYTHON INSTITUTE - 
### WORKIN WITH RESTFUL APIS

## - PROJECT: Vintage cars database -

Objectives
Learn how to:

- use the requests module facilities;
- build large software solutions using top-down tactics;
- cooperate with a remote database using REST.

Scenario
Your client has asked if you are able to write and deploy a software solution managing a small database that gathers data about vintage cars. Of course you are! It's a piece of cake for a programmer like you.

Don't forget to keep the server running when you start to run and debug your code!

Look carefully at the following terminal session — it will help you guess your client's needs. Of course, you can do it better and solve some issues in a smarter way than we have — feel free to experiment, but don’t lose sight of user satisfaction. This is the most valuable criteria of software usability.


+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 1
*** Database is empty ***
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 2
Car ID (empty string to exit): 1
Car brand (empty string to exit): Porsche
Car model (empty string to exit): 911
Car production year (empty string to exit): 1963
Is this car convertible? [y/n] (empty string to exit): n
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 2
Car ID (empty string to exit): 2
Car brand (empty string to exit): Ford
Car model (empty string to exit): Mustang
Car production year (empty string to exit): 1972
Is this car convertible? [y/n] (empty string to exit): y
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 1
id        | brand          | model     | production_year     | convertible    | 
1         | Porsche        | 911       | 1963                | False          | 
2         | Ford           | Mustang   | 1972                | True           | 

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4):  4
Car ID (empty string to exit): 2
Car brand (empty string to exit): Ford
Car model (empty string to exit): Mustang
Car production year (empty string to exit): 1973
Is this car convertible? [y/n] (empty string to exit): n
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 3
Car ID (empty string to exit): 1
Success!
Car ID (empty string to exit): 
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 0
Bye!