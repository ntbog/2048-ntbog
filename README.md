Boolean Nguyen A12475550 

Depth 3

Score Highest tile

15516  1024

10908  1024

12200  1024

12268  1024

12684  1024

Assignment 2: 2048
=========

Your task is to implement a game AI for the 2048 game based on simple expectimax search. The game engine is a modification of the code [here](https://gist.github.com/lewisjdeane/752eeba4635b479f8bb2). 

Due date
-----
Feb-3 11:59pm Pacific Time. 

Grading
-----
1. Regular Commits (1 point)

You should push at least one nontrivial commit by Jan-27 11:59pm. 

2. Documentation (1 points)

Comment your code generously. 

3. Functionality (10 points)

The player should be modelled as a max player, and the computer modeled as a chance player (picking a random open spot and place a 2-tile). 

Each time, the evaluation function at leaf nodes should be a weighted sum of the following two factors: 

- The points that can be obtained at the end of simulation (either the total points or just the additional points from the current position). 
- The highest tile that can be achived at the end of the simulation. 

A simple sum may work already, but you can tune the weights and see if they change the performance. 

In README, write down the end score and highest tile that you get by running the following three types of AI (5 times each): 

- Random move. 
- Computing a depth-1 search tree (i.e., just one max-player move). 
- Computing a depth-3 search tree (i.e., a max-min-max sequence). 

Note that you can press "u" at the end of a game to undo the last move and see the last configuration. Check more keyboard options by reading the code. 

You should see depth-3 search reaching 512 tiles and a score over 5000 quite often, as shown in the movie file. 
