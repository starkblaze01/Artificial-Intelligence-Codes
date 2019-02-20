function [reward] = bandit_nonstat(action)
m = [.1 .1 .1 .1 .1 .1 .1 .1 .1 .1]; % Mean rewards
reward = m(action)+ 0.01.*randn();  % random values of mean 0 and standard deviation 0.01
end