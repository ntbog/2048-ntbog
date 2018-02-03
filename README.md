Current situation - program freezes but still runs infinitely somehow

It keeps staying within the while loop at line 235

Returning 1 at line 237 after "print('layer3')" stops the program but with a deepcopy error

It needs to run for a while until we start seeing the prints, varies with computer strength

Initially it'll freeze and if you wait long enough it'll print the statement inside the grow function, a lot

eventually does make its way to the minimax print statements, which it prints a lot

And finally reaches the while loop at 235 and prints "layer3", a lot


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

Extra credits (4 points)
------
While depth-3 search gives ok performance, it can apparently be improved by searching more depth. As the tree gets bigger, you may need to pay attention to the efficiency of the code -- a naive implementation of depth-5 search may make each decision quite slow. 

You get up to 4 extra points if you can engineer the AI to reach 2048 very often, while each step is reasonably smooth when running on a laptop. If that is not challenging enough, check the code to see how you can make the board larger, and you can write your extra-credit report based on this project (message me to discuss the details). 

Note that engineering the evaluation function, for instance by giving some heuristic score for different tile configurations, may help. 

Note
------
Make sure to start immediately. You can see that significantly more code is required compared to Assignment 1. At the deadline, Github will automatically save the last commit as your submission. 
