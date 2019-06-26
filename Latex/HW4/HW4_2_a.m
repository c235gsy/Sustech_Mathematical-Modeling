%
x = [7,14,21,28,35,42];
y = [8,41,133,250,280,297];

p = polyfit(x,y,1);
poly2sym(p)

x1 = linspace(0,49);
y1 = polyval(p,x1);
figure
plot(x,y,'o')
hold on
plot(x1,y1)
hold off

%plot(x,y);
%hold on
%plot(x,sqrty);
%hold on
%plot(x,logy);
%hold on
%plot(x,log2y);
%hold on
%plot(x,log10y);