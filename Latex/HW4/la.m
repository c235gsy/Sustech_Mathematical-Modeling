function yy=la(x1,y1,xx)
%������ΪLagrange1��ֵ������x1,y1
%Ϊ��ֵ�ڵ�ͽڵ��ϵĺ���ֵ�����Ϊ��ֵ��xx�ĺ���ֵ��
%xx������������
syms x
n=length(x1);
    for i=1:n
    t=x1;t(i)=[];
    L(i)=prod((x-t)./(x1(i)-t));% L����������Ų�ֵ������
    end
u=sum(L.*y1);
p=simplify(u) % p�Ǽ򻯺��Lagrange��ֵ�������ַ�����
yy=subs(p,x,xx);    %p����xΪ�Ա����ĺ���������xx���ĺ���ֵ
end

