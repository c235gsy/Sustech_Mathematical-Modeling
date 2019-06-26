x = [7 14 21 28 35 42];
y = [8 41 133 250 280 297];

p2 = polyfit(x,y,2);
p3 = polyfit(x,y,3);

poly2sym(p2)
poly2sym(p3)

x1 = linspace(0,49);
y2 = polyval(p2,x1);
y3 = polyval(p3,x1);

figure
plot(x,y,'o')
hold on
plot(x1,y2,'-')
plot(x1,y3,'--')
legend('data points','second order polynomials','third order polynomials')
hold off