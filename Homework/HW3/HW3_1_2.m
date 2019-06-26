%≤¥À…∑÷≤º
set(gcf,'Units','centimeters','Position',[6 6 12 30]);
num = [100,1000,5000];
lam=70;
for i = 1:3
sample=poissrnd(lam,num(i),1);% Simulated data
x=min(sample):1:max(sample);
subplot(3,1,i)
histogram(sample,x);
title(sprintf('Random Numbers of Poisson distribution (n=%d)', num(i)));
fprintf("i=%d",i);
[Lambdahat, Lambdaci]=poissfit (sample, 0.05);
end