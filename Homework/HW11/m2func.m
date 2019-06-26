function dydt = m2func(t,Y)
    % [S] = y(1), [ES] = y(2), [P] = y(3)
    a=1;
    b=100;
    m=1;
    n=100;
    x=Y(1);
    y=Y(2);
    dydt = [a*x-b*x*y;
            m*y-n*x*y];
end
