function dydt = m1func(t,Y)
    x=Y(1);
    y=Y(2);
    dydt = [-x+y;
            -x-y];
end
