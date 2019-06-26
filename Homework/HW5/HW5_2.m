x0 = [17, 19, 20, 22, 23, 25, 31, 32, 33, 36, 37, 38, 39, 41]; 
y0 = [19, 25, 32, 51, 57, 71, 141, 123, 187, 192, 205, 252, 248, 294];
%figure(1);
%plot(x0,y0);

x = [17, 19, 20, 22, 23, 25, 31, 36, 37, 39, 41]; 
y = [19, 25, 32, 51, 57, 71, 141, 192, 205, 248, 294];
%figure(2);
%plot(x,y);
for i = 6:9
divided_difference_table(x,y)
[p,S] = polyfit(x,y,i);
poly2sym(p);
x1 = linspace(min(x),max(x));
y1 = polyval(p,x1);
[y0,delta] = polyval(p,x,S);
disp(delta);
subplot(2,2,i-5)
plot(x,y,'o')
str_a=sprintf('%d-order polynomial fit',i);
title(str_a)
hold on
errorbar(x,y0,2*delta,"*"); 
plot(x1,y1,'-')
end

legend('data points','appropriate point with 95% Prediction Interval','polynomial appropriate curve');
hold off