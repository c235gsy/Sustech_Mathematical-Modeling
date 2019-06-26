
a1 = 1;
a2 = 2;
b1 = 1;
b2 = 3;
c1 = 1;
c2 = 2;
P1 = 5;
P2 = 3;
F = 3;

f = @(x)(-1*(x(1)*(P1-a1*x(1)-b1*x(2)) + ...
          x(2)*(P2-a2*x(1)-b2*x(2)) ...
          - F - c1*x(1) - c2*x(2)));
opts = optimoptions(@fmincon,'Algorithm','interior-point');
% problem = createOptimProblem('fmincon', ...
%     'x0',[2;3],'objective',sixmin, ...
%     'Aineq',A,'bineq',b,'options',opts);

problem = createOptimProblem('fmincon','x0',[0;0],'objective',f,'options',opts);

[x,fval,eflag,output] = fmincon(problem)