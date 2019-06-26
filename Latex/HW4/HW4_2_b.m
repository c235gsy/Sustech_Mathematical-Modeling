x = [7 14 21 28 35 42];
y = [8 41 133 250 280 297];
x1 = linspace(0,49);
y1 = la(x,y,x1);
plot(x,y,'o')
hold on
plot(x1,y1)
hold off

