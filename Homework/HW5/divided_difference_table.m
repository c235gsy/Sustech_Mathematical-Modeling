function [] = divided_difference_table(x,y)

yy = 1:1:length(y)-1;
n = length(x)-length(y)+1;
for i = 1:length(y)-1
    yy(i) = ((y(i+1)-y(i))/(x(i+n)-x(i)));
end

if isempty(yy)
    
else
    disp(yy);
    divided_difference_table(x,yy);
end
end

