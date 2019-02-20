Q= zeros(1,10); % change 10 to n if there are n actions (eg. in case of binary bandit n=2) 
N= zeros(1,10); % change 10 to n if there are n actions (eg. in case of binary bandit n=2)
Rn= zeros(1,1000);
itr =zeros(1,1000);
epsilon=0.1;
sum=0;

for iter = 1:1000
    itr(iter)=iter;
    if rand > epsilon
        [m,id]= max(Q);
        A= id;
    else
        temp= randperm(10);  % change 10 to n if there are n actions (eg. in case of binary bandit n=2)
        A= temp(1);
    end
    R= bandit_nonstat(A);
    N(A)= N(A)+1;
    Q(A)= Q(A)+ alpha*(R-Q(A));
    sum = sum + R;
    Rn(iter)= sum/iter;
end

plot(itr,Rn);