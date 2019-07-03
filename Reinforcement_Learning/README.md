# Learning Objective:
Understand the process of sequential decision making (stochastic environment) and the connection with reinforcement learning.

# Title: Markov Decision Process and Dynamic Programming

# References:
- Artificial Intelligence a Modern Approach, Russell and Norvig (third edition)
Chapter 16, 17, 21
- Reinforcement Learning, Sutton and Barto (second edition)
Chapter 3, 4

# Problem Statement:
- Suppose that an agent is situated in the 4x3 environment as shown in Figure .  Beginning in the start state, it must choose an action at each time step.  The interaction with the environment terminates when the agent reaches one of the goal states, marked +1 or -1.  We assume that the environment is fully observable, so that the agent always knows where it is.  We may decide to take following four actions in every state:  Up, Down, Left and Right.  However, the environment is stochastic, that means the action that we take may not lead us to desired state.  Each action achieves the intended effect with probability 0.8, but the rest of the time, the action moves the agent at right angles to the intended direction with equal probabilities.  Furthermore, if the agent bumps into a wall, it stays in the same square.  The immediate reward for moving to any state (s) except for the terminal states S+ is r(s)= -0.04.  And the reward for moving to terminal states is +1 and -1 respectively.  Find the value function corresponding to the optimal policy using value iteration. 
Find the value functions corresponding optimal policy for the following:
a) r(s)=-2
b) r(s)=0.1
c) r(s)=0.02
d) r(s)=1

- [Gbike bicycle rental] We are managing two locations for Gbike.  Each day, some number of customers arrive at each location to rent bicycles.  If we have a bike available, we rent it out and earn INR 10 from Gbike.  If we are out of bikes at that location, then the business is lost.  Bikes become available for renting the day after they are returned.  To help ensure that cars are available where they are needed, we can move them between the two locations overnight, at a cost of INR 2 per bike moved.  
Assumptions: Assume that the number of bikes requested and returned at each locations are Poisson random variables.  Expected numbers of rental requests are 3 and 4 and returns are 3 and 2 at the first and second locations respectively.  No more than 20 bikes can be parked at either of the locations.  We may move maximum 5 bikes from one location to the other in one night.  Consider the discount rate to be 0.9.
Formulate the continuing finite MDP, where time steps are days, the state is the number of cars at each location at the end of the day, and the actions are the net number of bikes moved between the two locations overnight.

- Write a program for policy iteration and re-solve gbike bicycle rental problem with the following changes.  One of our employee at the first location rides a bus home each night and lives near the second location.  She is happy to shuttle one bike to the second location for free.  Each additional bike still costs INR 2, as do all bikes moved in the other direction.  In addition, we have limited parking space at each location.  If more than 10 bikes are kept overnight at a location (after any moving of cars), then an additional cost of INR 4 must be incurred to use a second parking lot (independent of how many cars are kept there).
# Note: 
Policy Evaluation problems are directly taken from book by Sutton and Barto.
Changing the Jack’s car rental to Gbike bicycle rental is just to put things in context.  It has no intention of earning credit for posing the problem.  Credit goes to Sutton and Barto.
