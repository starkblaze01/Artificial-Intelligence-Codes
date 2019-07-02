# Learning objective: 
Understanding Exploitation - Exploration in simple n-arm bandit reinforcement learning task, epsilon-greedy algorithm

# Title: n-armed bandit

# Reference:
Reinforcement Learning: an introduction by R Sutton and A Barto (Second Edition) (Chapter 1-2)

# Problem Statement:
- Consider a binary bandit with two rewards {1-success, 0-failure}.  The bandit returns 1 or 0 for the action that we select, i.e. 1 or 2.  The rewards are stochastic (but stationary).  Use epsilon-greedy algorithm and decide upon the action to take for maximizing the expected reward.  There are two binary bandits named binaryBanditA.m and binaryBanditB.m are waiting for us.
- Develop a 10-armed bandit in which all ten mean-rewards start out equal and then take independent random walks (by adding a normally distributed increment with mean zero and standard deviation 0.01 to all mean-rewards on each time step). 
{function [value] = bandit_nonstat(action)}.
- The 10-armed bandit that we developed (bandit_nonstat) is difficult to crack with standard epsilon-greedy algorithm since the rewards are non-stationary.  Write modified epsilon-greedy agent and show whether it is able to latch onto correct actions or not.  (Try at least 10000 time steps before commenting on results)
