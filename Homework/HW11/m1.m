close all;
clear;

[t xy]=ode15s(@m1func,[0:0.01:1000],[-1,1]);

x=xy(:,1);
y=xy(:,2);
figure(1); 
plot(x,y);
xlabel("x");
ylabel("y");

