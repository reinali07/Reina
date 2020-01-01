%solve a 2-by-2 system of ODEs
function [t,x] = solvesystem_lireina(f1,f2,t0,tN,x0,h)
    t = t0:h:tN;
    N = length(t);
    x1 = zeros(0,N);
    x2 = zeros(0,N);
    x1(1) = x0(1);
    x2(1) = x0(2);
    for i = 1:N-1
        x1(i+1) = x1(i) + f1(t(i),x1(i),x2(i))*h;
        x2(i+1) = x2(i) + f2(t(i),x1(i),x2(i))*h;
        x1(i+1) = x1(i) + 0.5*(f1(t(i),x1(i),x2(i))+f1(t(i+1),x1(i+1),x2(i+1)))*h;
        x2(i+1) = x2(i) + 0.5*(f2(t(i),x1(i),x2(i))+f2(t(i+1),x1(i+1),x2(i+1)))*h;
    end
    x = [x1;x2];
end
