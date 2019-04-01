clear all;
close all;
data=fopen("browncorpus_cleaned.txt","r");
A = rand(2,2);
B = rand(2,27);
a =0;
b =0;
for i = 1:2
    a = a+A(1,i);
end
for i = 1:2
    A(1,i) = A(1,i)./a;
end
for i = 1:27
    b = b+B(1,i);
end
for i = 1:27
    B(1,i) = B(1,i)./b;
end
a =0;
b =0;
for i = 1:2
    a = a+A(2,i);
end
for i = 1:2
    A(2,i) = A(2,i)./a;
end
for i = 1:27
    b = b+B(2,i);
end
for i = 1:27
    B(2,i) = B(2,i)./b;
end
check = 0;
check1 = 0;
for i = 1:27
    check = B(2,i)+check;
    check1 = B(1,i) + check1;
end
finaldata = textscan(data,'%c');
fclose(data);
ce = cell2mat(finaldata);

ce = ce';
% ESTTR and ESTEMIT are the estimated Transition and Emission matrix respectively.
[ESTTR,ESTEMIT] = hmmtrain(ce(1:100000),A,B);