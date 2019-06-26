x = [17, 19, 20, 22, 23, 25, 31, 36, 37, 39, 41]; 
y = [19, 25, 32, 51, 57, 71, 141, 192, 205, 248, 294];

[p,S] = polyfit(x,y,7); 

[y_fit,delta] = polyval(p,x,S);

plot(x,y,'bo')
hold on
plot(x,y_fit,'r-')
plot(x,y_fit+2*delta,'m--',x,y_fit-2*delta,'m--')
title('Linear Fit of Data with 95% Prediction Interval')
legend('Data','Linear Fit','95% Prediction Interval')