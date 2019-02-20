clear all;
close all;

% reward Matrix
% row represents states, col represents actions
%
%   Start (1) |(2) | (3)end(+1)
%   ---------------------------
%   (4)       |(5) | (6)end(-1)
%   --------------------------- 
%   (7)       |(8) | (9)
%   ---------------------------
%   (10)      |(11)| (12)
%
% States: 1,2,3,4,5,6,7,8,9,10,11,12
% Actions: Down-1, Up-2, right-3, Left-4
% reward Matrix
r = -0.04;
re = [r -inf r -inf;
      r -inf 1 r;
      -1 -inf -inf r;
      r r r -inf;
      r r -1 r;
      r 1 -inf r;
      r r r -inf;
      r r r r;
      r -1 -inf r;
      -inf r r -inf;
      -inf r r r;
      -inf r -inf r];


% Q matrix
q = zeros(12,4);
% State Transition matrix
T = [4 1 2 1;
     5 2 3 1;
     6 3 3 2;
     7 1 5 4;
     8 2 6 4;
     9 3 6 5;
     10 4 8 7;
     11 5 9 7;
     12 6 9 8;
     10 7 11 10;
     11 8 12 10;
     12 9 11 12];
 
% Valid actions   down1 up2 right3 left4

A = [1,3,1,3;  %to correct the dimension of valid action matrix and considering the corner states case valid action is repeated.
1,3,4,1;
1,4,1,4;
1,2,3,1;
1,2,3,4;
1,2,4,4;
1,2,3,2;
1,2,3,4;
1,2,4,4;
2,3,2,3;
2,3,4,2;
2,4,2,4;];
 
% Q-Learn
gam = .8;

for episodes=1:1000
    s = 1;
    while s~=3 && s~=6
        a = A(s,randi(4));
      % Q= reward(s,a) + discount-factor*max(0.8*q(action) + 0.1*q(perpendicular direction) + 0.1*q(perpendicular direction))
        if a == 1
            q(s,a) = re(s,a)+gam*max(0.8*q(T(s,a),:)+0.1*q(T(s,3),:)+0.1*q(T(s,4),:));
        end
        if a == 2
            q(s,a) = re(s,a)+gam*max(0.8*q(T(s,a),:)+0.1*q(T(s,3),:)+0.1*q(T(s,4),:));
        end
        if a == 3
            q(s,a) = re(s,a)+gam*max(0.8*q(T(s,a),:)+0.1*q(T(s,1),:)+0.1*q(T(s,2),:));
        end
        if a == 4
            q(s,a) = re(s,a)+gam*max(0.8*q(T(s,a),:)+0.1*q(T(s,1),:)+0.1*q(T(s,2),:));
        end 
        s = T(s,a);
    end
end

