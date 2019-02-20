function [V] = policy_evaluation_gbike(policy, Lamda, lamda, r, t, gam)

[m,n] = size(policy);

nn = 0:n-1;
P1 = exp(-Lamda(1))*(Lamda(1).^nn)./factorial(nn); %P1 = P1/sum(P1);
P2 = exp(-Lamda(2))*(Lamda(2).^nn)./factorial(nn); %P2 = P2/sum(P2);
P3 = exp(-lamda(1))*(lamda(1).^nn)./factorial(nn); %P3 = P3/sum(P3);
P4 = exp(-lamda(2))*(lamda(2).^nn)./factorial(nn); %P4 = P4/sum(P4);

V=zeros(m,n);
delta=10;
theta=0.1;
while delta > theta
%for count=1:2
	v=V;
	for i=1:m
		for j=1:n
			s1=i-1; s2=j-1; % state (0-20,0-20)
			Vs_=0; a = policy(i,j);
                        if s1>10 || s2>10
                            R = -abs(a)*t-4; % checking if the number of bikes at both location is greater than 10 then give penalty of Rs.4
                        else
                            R = -abs(a)*t;
                        end
                        s1_ = s1-a; s2_=s2+a;
			for n1=0:12
				for n2=0:14
					s1__=s1_-min(n1,s1_); s2__=s2_-min(n2,s2_);
	                               for n3=0:12
					 for n4=0:9
					 s1___=s1__+min(n3,20-s1__); s2___=s2__+min(n4,20-s2__);
   			                 R=R+(P1(n1+1)*P2(n2+1)*P3(n3+1)*P4(n4+1)*(min(n1,s1_+1)+min(n2,s2_+1)))*r;
					 Vs_=Vs_+P1(n1+1)*P2(n2+1)*P3(n3+1)*P4(n4+1)*V(s1___+1, s2___+1);	%Add movement of free shuttle				
					 end
				       end
				end
			end
			V(i,j) = R+(gam*Vs_);%2*R-70+gam*Vs_;
		end
	end
	delta = max(max(abs(v-V)));
%	pause()
end
end

