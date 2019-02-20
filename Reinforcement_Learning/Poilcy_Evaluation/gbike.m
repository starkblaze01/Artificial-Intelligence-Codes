%----------------------------------------------
% Gbike bicycles on rental 
% Value iteration method
% Ref: Reinforcement Learning, Sutton and Barto
% Course: CS308 Artificial Intelligence
% Author: Pratik Shah
% Date: 15 Jan, 2019
% Winter 2019, IIITV
% Gandhinagar
% 
%----------------------------------------------
clear all;
close all;

Lamda = [3 4]; % Rental request arrival
lamda = [3 2]; % Retrun 

r = 10; % 10 rupee rental reward
t = 2; % 2 rupee transfer fees 

policy = zeros(21,21); % Initial policy of no trasfer, transfer policy(i,j) from location 1 to location 2 
gam = 0.9;

policystable = false;
count = 0;
while ~policystable
        V = policy_evaluation_gbike(policy, Lamda, lamda, r, t, gam);
	[policy, policystable] = policy_improvement_gbike(V, policy, Lamda, lamda, r, t, gam);
        count = count+1;
%        figure(1); 
%        subplot(2,1,1);contour(policy,[-5:5]);
%        subplot(2,1,2);surf(V);
%        pause();
end
figure(1); 
subplot(2,1,1);contour(policy,[-5:5]);
subplot(2,1,2);surf(V);
