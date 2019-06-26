
close all;
clear;

[t xy]=ode15s(@m3func,[0:0.01:1000],[0,1]);

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
