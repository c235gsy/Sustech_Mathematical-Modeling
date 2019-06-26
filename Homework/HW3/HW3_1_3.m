%ÕýÌ¬·Ö²¼
num = [100,1000,5000]*2;
set(gcf,'Units','centimeters','Position',[6 6 12 30]);
for i = 1:3
sample = normrnd(0,1,num(i),1);
x=min(sample):0.1:max(sample);
subplot(3,1,i)
histogram(sample,x);
title(sprintf('Random Numbers of Normal distribution (n=%d)', num(i)));
fprintf("i=%d",i);
[muhat,sigmahat,muci,sigmaci]=normfit(sample, 0.05)
end