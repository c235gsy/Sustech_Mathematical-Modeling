p = [0.25,0.25,0.50;
     0.10,0.30,0.60;
     0.05,0.15,0.80];

totnum = 10000;
t = 0;

for i=1:totnum 
%s = [0.25,0.25,0.5];
s = rand(1,3);
s = s/sum(s);

m = s;
fl = 0;

while  m ~= m*p
m = m*p;
fl = fl+1;
end

if sum(m == [0.0741,0.1852,0.7407])==0
t = t+1;
end

end
fprintf('the percentage of different start state to the same stable state: \n%d %% \n',t/100);
