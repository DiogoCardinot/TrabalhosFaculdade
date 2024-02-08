from turtle import color
import numpy as np
import matplotlib.pyplot as plt


alfa=1
beta=1
gamma=1
deltaT = 0.5
t_inicial = 0
t_final=5
t=np.arange(t_inicial, t_final, deltaT)


deltaT_inicial=0.1
deltaT_final = 0.5
DeltaT= np.arange(deltaT_inicial, deltaT_final, 0.1)


ca=[len(t)]
cb=[len(t)]
cc=[len(t)]

#condições iniciais
ca[0]= 1
cb[0]= 0
cc[0]= 1

def dcadt(t,ca,cb,cc):
    return (-alfa*ca*cc+cb)

def dcbdt(t,ca,cb,cc):
    return (beta*ca*cc-cb)

def dccdt(t,ca,cb,cc):
    return (-gamma*ca*cc+cb-2*cc)

for i in range(t_inicial, len(t)-1): 
    #k1
    k1_ca= dcadt(t[i], ca[i], cb[i], cc[i])
    k1_cb= dcbdt(t[i], ca[i], cb[i], cc[i])
    k1_cc= dccdt(t[i], ca[i], cb[i], cc[i])
    print("k1Ca", k1_ca,"\n","k1Cb", k1_cb,"\n","k1Cc", k1_cc,"\n")
    #k2
    k2_ca= dcadt(t[i]+ deltaT/2, ca[i] + k1_ca*deltaT/2, cb[i] + k1_cb*deltaT/2, cc[i] + k1_cc*deltaT/2 )
    k2_cb= dcbdt(t[i]+ deltaT/2, ca[i] + k1_ca*deltaT/2, cb[i] + k1_cb*deltaT/2, cc[i] + k1_cc*deltaT/2)
    k2_cc= dccdt(t[i]+ deltaT/2, ca[i] + k1_ca*deltaT/2, cb[i] + k1_cb*deltaT/2, cc[i] + k1_cc*deltaT/2 )
    print("k2Ca", k2_ca,"\n","k2Cb", k2_cb,"\n","k2Cc", k2_cc,"\n")

    #k3
    k3_ca= dcadt(t[i]+ deltaT, ca[i]-k1_ca*deltaT + 2*k2_ca*deltaT, cb[i]-k1_cb*deltaT + 2*k2_cb*deltaT, cc[i]-k1_cc*deltaT + 2*k2_cc*deltaT)
    k3_cb= dcbdt(t[i]+ deltaT, ca[i]-k1_ca*deltaT + 2*k2_ca*deltaT, cb[i]-k1_cb*deltaT + 2*k2_cb*deltaT, cc[i]-k1_cc*deltaT + 2*k2_cc*deltaT)
    k3_cc= dccdt(t[i]+ deltaT, ca[i]-k1_ca*deltaT + 2*k2_ca*deltaT, cb[i]-k1_cb*deltaT + 2*k2_cb*deltaT, cc[i]-k1_cc*deltaT + 2*k2_cc*deltaT)
    print("k3Ca", k3_ca,"\n","k3Cb", k3_cb,"\n","k3Cc", k3_cc,"\n", "ca",ca,"\n", "cb",cb,"\n","cc", cc,"\n")


    ca.append(ca[i] + (1/6)*(k1_ca+4*k2_ca+k3_ca)*deltaT)
    cb.append(cb[i] + (1/6)*(k1_cb+4*k2_cb+k3_cb)*deltaT)
    cc.append(cc[i] + (1/6)*(k1_cc+4*k2_cc+k3_cc)*deltaT)

    
for i in range(deltaT_inicial, len(DeltaT)-1):
    print
     #k1
    k1_ca= dcadt(t[i], ca[i], cb[i], cc[i])
    k1_cb= dcbdt(t[i], ca[i], cb[i], cc[i])
    k1_cc= dccdt(t[i], ca[i], cb[i], cc[i])

    #k2
    k2_ca= dcadt(t[i]+ DeltaT[i]/2, ca[i] + k1_ca*DeltaT[i]/2, cb[i] + k1_cb*DeltaT[i]/2, cc[i] + k1_cc*DeltaT[i]/2 )
    k2_cb= dcbdt(t[i]+ DeltaT[i]/2, ca[i] + k1_ca*DeltaT[i]/2, cb[i] + k1_cb*DeltaT[i]/2, cc[i] + k1_cc*DeltaT[i]/2)
    k2_cc= dccdt(t[i]+ DeltaT[i]/2, ca[i] + k1_ca*DeltaT[i]/2, cb[i] + k1_cb*DeltaT[i]/2, cc[i] + k1_cc*DeltaT[i]/2 )


    #k3
    k3_ca= dcadt(t[i]+ DeltaT[i], ca[i]-k1_ca*DeltaT[i] + 2*k2_ca*DeltaT[i], cb[i]-k1_cb*DeltaT[i] + 2*k2_cb*DeltaT[i], cc[i]-k1_cc*DeltaT[i] + 2*k2_cc*DeltaT[i])
    k3_cb= dcbdt(t[i]+ DeltaT[i], ca[i]-k1_ca*DeltaT[i] + 2*k2_ca*DeltaT[i], cb[i]-k1_cb*DeltaT[i] + 2*k2_cb*DeltaT[i], cc[i]-k1_cc*DeltaT[i] + 2*k2_cc*DeltaT[i])
    k3_cc= dccdt(t[i]+ DeltaT[i], ca[i]-k1_ca*DeltaT[i] + 2*k2_ca*DeltaT[i], cb[i]-k1_cb*DeltaT[i] + 2*k2_cb*DeltaT[i], cc[i]-k1_cc*DeltaT[i] + 2*k2_cc*DeltaT[i])


    ca.append(ca[i] + (1/6)*(k1_ca+4*k2_ca+k3_ca)*DeltaT[i])
    cb.append(cb[i] + (1/6)*(k1_cb+4*k2_cb+k3_cb)*DeltaT[i])
    cc.append(cc[i] + (1/6)*(k1_cc+4*k2_cc+k3_cc)*DeltaT[i])




    
    


# plt.plot(t,f)
# plt.xlabel("Tempo(s)")
# plt.ylabel("F(n)")
# plt.plot(f,f, color='black')
# plt.show()

