%------------------------------------------------------------
% Hopfield Network Example
% Demonstration of pattern storage 
% CS308 Introduction to Artificial Intelligence
% Author: Pratik Shah
% Date: 3 April, 2019
% Place: IIITV, Gandhinagar
% Ref: Information, Inference and Learning Algorithms, D McKay
%------------------------------------------------------------

clear all;
close all;

%--------------------------------------------
% Patterns to store
% D, J, C, M
%--------------------------------------------
X = [1 1 1 1 -1 -1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 1 -1;
1 1 1 1 1 -1 -1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 1 -1 -1;
-1 1 1 1 1 1 -1 -1 -1 -1 1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 1 1 1;
1 -1 -1 -1 1 1 1 -1 1 1 1 -1 1 -1 1 1 -1 -1 -1 1 1 -1 -1 -1 1]';

%figure;
%imshow(reshape(-X(:,1),5,5)');

%--------------------------------------------
% Learn the weights according to Hebb's rule 
%--------------------------------------------
[m,n] = size(X);
W = zeros(m,m);
for i = 1:n
	W = W + X(:,i)*X(:,i)';
end
W(logical(eye(size(W)))) = 0;
W = W/n;

%-------------------------------------------
% Dynamical (Linear) System and fixed points
%-------------------------------------------
%for k = 1:100
x = X(:,1);
index=randperm(25,7);
for j = 1:length(index)
    x(index(j))=-1*x(index(j));    
end


figure(1);
subplot(1,2,1);
imshow(reshape(-X(:,1),5,5)');
subplot(1,2,2);
imshow(reshape(-x,5,5)');

y = x;
erry = 10;
while erry > 1
	yp = sign(W*y);	
	erry = norm(yp-y);
	y = yp;
	figure(2);
	imshow(reshape(-y, 5, 5)');
	pause();
end
%end
%--------------------------------------------
% Damaging 50 neurons!
%--------------------------------------------









