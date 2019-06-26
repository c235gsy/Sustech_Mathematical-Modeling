x1 = linspace(-10,10);
l1 = 2-2/3*x1; 
l2 = 3*x1-15;
l3 = 4+x1;
l4 = 5.2-0.4*x1;
l5 = -5/7*x1+2;
l6 = 0*x1;
y1 = linspace(-10,10);

plot(x1,l1);
hold on
plot(x1,l2,'b');
plot(x1,l3);
plot(x1,l4);
plot(x1,l5,"--");
plot(x1,l6);
plot(0*x1,y1);
axis([-3 7 -3 6])
x = [0,0,  6/7,     202/34,5,3];
y = [2,4,4+6/7,202/34*3-15,0,0];
fill(x,y,'b');
legend('2x1+3x2=6','3x1-x2=15','x1-x2=-4','2x1+5x2=27','5x1+7x2=12',...
'x1=0','x2=0','target area')
hold off
