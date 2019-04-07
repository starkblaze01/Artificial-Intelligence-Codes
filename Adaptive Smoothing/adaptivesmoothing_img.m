I = imread("test_noisy.jpg");

y =I;
alpha = 0.1;
gamma = 4;
[m,n] = size(y);
S = zeros(m,n);
SF = zeros(m,n);
beta = zeros(m,n);
for count = 1:5
    for i = 1:m
        for j=1:n
            for k = i-1:i+1 % window size 3x3
                for l = j-1:j+1
                    if k>0 && l>0 && k<=m && l<=n
                        S(i,j)= S(i,j)+ 1/(1 + ( sqrt(double((k-i)^2 + (l-j)^2 + (y(i,j)-y(k,l))^2 )))^gamma);
                    end                        
                end
            end
            
            beta(i, j) = alpha/(S(i,j)-1);
            for k = i-1:i+1
                for l = j-1:j+1
                    if k>0 && l>0 && k<=m && l<=n
                        SF(i,j)= SF(i,j)+ (y(k,l)/(1 + ( sqrt(double((k-i)^2 + (l-j)^2 + (y(i,j)-y(k,l))^2 )))^gamma));
                    end                        
                end
            end
            SF(i,j) = SF(i,j)-y(i,j);
            y(i,j) = (1-alpha)*y(i,j) + beta(i,j)*SF(i,j);
        end
    end    
end
figure(1);
imshow(I);
figure(2);
imshow(y);
%Comparison with other filters
%figure(3);
%imshow(wiener2(I));