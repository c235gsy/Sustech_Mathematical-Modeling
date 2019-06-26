%指数分布
set(gcf,'Units','centimeters','Position',[0 0 30 30]);
num = [100,1000,5000];
mu = 3;
for i = 1:3
sample = exprnd(mu,num(i),1);% Simulated data
x=min(sample):1:max(sample);
subplot(3,3,3*i-2)
histogram(sample,x);
title(sprintf('Exponential distribution (n=%d)', num(i)));
fprintf("i=%d",i);
[muhat,muci] = expfit(sample, 0.05)
end

%泊松分布
num = [100,1000,5000];
lam=70;
for i = 1:3
sample=poissrnd(lam,num(i),1);% Simulated data
x=min(sample):1:max(sample);
subplot(3,3,3*i-1)
histogram(sample,x);
title(sprintf('Poisson distribution (n=%d)', num(i)));
fprintf("i=%d",i);
[Lambdahat, Lambdaci]=poissfit (sample, 0.05)
end

%正态分布
num = [100,1000,5000]*2;
for i = 1:3
sample = normrnd(0,1,num(i),1);
x=min(sample):0.1:max(sample);
subplot(3,3,3*i)
histogram(sample,x);
title(sprintf('Normal distribution (n=%d)', num(i)));
fprintf("i=%d",i);
[muhat,sigmahat,muci,sigmaci]=normfit(sample, 0.05)
end