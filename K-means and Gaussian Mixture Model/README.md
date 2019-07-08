# Objective:
To understand the k-means clustering algorithm and its connection with the Bayesian framework.

# Problem:
- Generate 100 data points coming from the mixture of four Gaussians in R2 with weightages =[0.4 0.3 0.2 0.1], </br>
means =[(0,0) (4,4) (0,3) (4,0)].
The covariance matrices corresponding to the Gaussians are as follows: </br>
C1=[1 0.7; 0.7 1], C2=[1 0.25; 0.25 0.5], C3 =[0.5 0.1; 0.1 1], and C4=[0.25 0;0 0.35].
- Make a version of the K-means algorithm that models the data as a mixture of K arbitrary Gaussians, i.e., Gaussians that are not constrained to be axis-aligned.  Use the developed algorithm to cluster the data points generated in part 1 with K=1,2,3,4,5,6.
