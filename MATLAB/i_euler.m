%improve euler's method for ODEs

function [t,y] = i_euler(f,t0,tN,y0,h)
    t = t0:h:tN;
    N = length(t);
    y = zeros(0,N);
    y(1) = y0;
    for i = 1:N-1
        y(i+1) = y(i) + f(t(i),y(i))*h;
        y(i+1) = y(i) + 0.5*(f(t(i),y(i))+f(t(i+1),y(i+1)))*h;
    end
end
