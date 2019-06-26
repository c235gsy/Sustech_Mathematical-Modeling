function dydt = m3func(t,Y)
    % [S] = y(1), [ES] = y(2), [P] = y(3)
    a = 1;
    b = 1;
    c = 1;
    m = 1;
    n = 1;
    p = 1;
    x=Y(1);
    y=Y(2);
    dydt = [-a*x+b*y+c;
            m*x-n*y+p];
end
