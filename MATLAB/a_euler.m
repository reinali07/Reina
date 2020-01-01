%adaptive euler's method for ODEs

function [t,y] = a_euler(f,t0,tN,y0,h)
    t = [t0];
    y = [y0];
    y_temp = 0;
    Z = 0;
    D = 0;
    i = 1;
    tol = 1e-8;
    while t(end) < tN
        y_temp = y(i) + f(t(i),y(i))*h;
        Z = y(i) + f(t(i),y(i))*h/2;
        Z = Z + f(t(i)+h/2,Z)*h/2;
        D = Z-y_temp;
        if abs(D) < tol
            y = cat(2,y,[Z+D]);
            t = cat(2,t,t(i)+h);
            i = i+1;
        else
            h = 0.9*h*min(max(tol/abs(D),0.3),2);
        end
    end
end
