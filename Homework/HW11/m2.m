% filename: mm.m
close all;
clear;

[t xy]=ode15s(@m2func,[0:10000],[1,1]);

x=xy(:,1);
y=xy(:,2);
figure(1); 
plot(x,y);
xlabel("x");
ylabel("y");
% plot(log10(t),v_real,'.-r',log10(t),v_predicted,'.-b');
% legend('Calculatd turnover rate v','Predicted turnover rate v0',0);
% xlabel('log(Time) (s)');
% ylabel('Turn-over rate (M/s)');
