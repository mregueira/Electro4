clear all;
close all;

%variables del convertidor
C = sym ('C');
L = sym ('L');
d = sym ('d');
R = sym ('R');
Vd = sym ('Vd');

s = sym ('s');

%variables del amp de error
R2 = sym('R2');
R6 = sym('R6');
C2 = sym('C2');


Aon=[0, 0 ; 0, (-1/(R*C))];
Bon=[1/L ; 0];
Con=[0, 1];
Aoff=[0, -1/L ; 1/C, (-1/(R*C))];
Boff=Bon;
Coff=Con;

Abarra=Aon*d+Aoff*(1-d);
Bbarra=Bon;
Cbarra=Con;


X=[Vd/(R*(1-d)^2) ; Vd/(1-d)];
I=eye(2);

T_conv=Cbarra* inv(((s*I)-Abarra))*(((Aon-Aoff)*X)+((Bon-Boff)*Vd)) + (Con - Coff)*X;
pretty(simplify(T_conv))

T_realim= (R6/R2)*((s+(1/(C2*R6)))/(s)) *(1/19);
pretty(T_realim)


C=47e-6;
L=220e-6;
R=10;
d=0.6;
Vd=10;

R6=1e3;
R2=90e3;
C2=100e-9;


T_conv_n=simplify(subs(T_conv));
[n_Tc,d_Tc] = numden(T_conv_n);
syms s;
n=sym2poly(n_Tc); 
d=sym2poly(d_Tc);
n=n/d(3);
d=d/d(3);
T_conv_final=tf(n,d)

T_realim_n=simplify(subs(T_realim));
[n_Tr,d_Tr] = numden(T_realim_n);
syms s
n2=sym2poly(n_Tr)
d2=sym2poly(d_Tr)
n2=n2/n(2)
d2=d2/n(2)
T_realim_fin=tf(n2,d2)

R_1kOhm=T_conv_final/(1+T_conv_final*T_realim_fin)
bode(R_1kOhm )
%pzmap(R_1kOhm)
hold on;


%--------------------------------------
R6=10e3;

T_realim_n=simplify(subs(T_realim));
[n_Tr,d_Tr] = numden(T_realim_n);
syms s
n2=sym2poly(n_Tr)
d2=sym2poly(d_Tr)
n2=n2/n(2)
d2=d2/n(2)
T_realim_fin=tf(n2,d2)

R_10kOhm=T_conv_final/(1+T_conv_final*T_realim_fin)
bode(R_10kOhm )
%pzmap(R_10kOhm)
hold on;


%--------------------------------------
R6=22e3;

T_realim_n=simplify(subs(T_realim));
[n_Tr,d_Tr] = numden(T_realim_n);
syms s
n2=sym2poly(n_Tr)
d2=sym2poly(d_Tr)
n2=n2/n(2)
d2=d2/n(2)
T_realim_fin=tf(n2,d2)

R_22kOhm=T_conv_final/(1+T_conv_final*T_realim_fin)
bode(R_22kOhm )
%pzmap(R_22kOhm)
hold on;



