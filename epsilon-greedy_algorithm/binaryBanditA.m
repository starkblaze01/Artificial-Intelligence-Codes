function [value] = binaryBanditA(action)
%----------------------------------------------
% Exercise: Evaluation vs. Instruction
% CS308 AI, IIITV
% Winter 2018-19
% Author : Pratik Shah
% Ref: Reinforcement Learning, Sutton and Barto
%----------------------------------------------
% Two actions 1 and 2
% Rewards are stochastic 1-Success/ 0-Failure
%
% For help on usage type >>help binaryBanditA
%
% >> binaryBanditA(action)
%----------------------------------------------

p = [.1 .2];
if rand < p(action)
	value = 1;
else
	value = 0;
end
end