clear
clc
V(1)=0.08333;
V(2)=-32.08333;
V(3)=1279;
V(4)=-15623.666;
V(5)=84244.1666;
V(6)=-236957.5;
V(7)=375911.666;
V(8)=-340071.666;
V(9)=164062.5;
V(10)=-32812.5;


passo_tempo=0.001;
numero_passos=1000;
n=10;

a=1;


for j=1:1:numero_passos;
    tempo(j)=j*passo_tempo;
    
    soma=0.0;

    for i=1:1:n
       s=(log(2)/tempo(j))*i; 
//       disp("tempo",tempo(j))

       F_Laplace=(a)/(s^2+a^2);
        
       soma=soma+(V(i)*F_Laplace); 
    end

    
    F(j)=(log(2)/tempo(j))*soma;

end


y=besseli(0,1);



plot(tempo,F);
