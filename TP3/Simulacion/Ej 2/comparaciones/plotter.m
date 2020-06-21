function [ output_args ] = plotter( f1,f2,f3,v1,v2,v3,db )

if (db == 1)
    v1a=10.^(v1./20);
    v2a=10.^(v2./20);
    v3a=10.^(v3./20);
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
else
    v1a=v1;
    v2a=v2;
    v3a=v3;
end

plot(f1,v1a,f2,v2a,f3,v3a);
grid on
title('Comparacion de espectros')
xlabel('Frecuencia (hz)')
ylabel('Amplitud')

end
