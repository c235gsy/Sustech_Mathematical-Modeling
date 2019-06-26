format long
x = [0, 1, 2, 3, 4, 5, 6, 7]; 
y = [1, 4.5, 20, 90, 403, 1808, 8103, 36316];
%plot(x,y);
divided_difference_table(x,y)

[p,S] = polyfit(x,y,7);

poly2sym(p)

x1 = linspace(min(x),max(x));
y1 = polyval(p,x1);

[y0,delta] = polyval(p,x,S);
 
disp(delta);

plot(x,y,'o');
hold on
errorbar(x,y0,2*delta,"*"); 
plot(x1,y1,'-');
legend('data points','polynomial appropriate point with 95% Prediction Interval','polynomial appropriate curve');
hold off