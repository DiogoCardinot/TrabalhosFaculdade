import numpy as np
import matplotlib.pyplot as plt



def calculaX(s_inicial,s_final,swf,tempo,phi,q_t,A):
    x=[]
    SW =[]
    derivada = []
    s_w = np.arange(s_inicial, s_final, s_inicial/(s_final*100000))
    for i in range(len(s_w)):
        if s_w[i]>=swf:
            derivada.append((800*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(125*s_w[i]**4+700*s_w[i]**3-450*s_w[i]**2-420*s_w[i]+301)**2) 
            SW.append(s_w[i])
    ##insere no 0 prq o maior sw deve estar com o menor x
    SW.insert(0, s_inicial)
    SW.insert(0, s_inicial)
        
    for j in range(len(derivada)):
        x.append((q_t*tempo/ A*phi)*derivada[j])
    x.insert(0, x[0]) 
    x.insert(0,x[0]+ 0.5*x[0])
    return x, SW

def NewSincial(s_inicial,s_final,swf,tempo,phi,q_t,A):
    x=[]
    SW =[]
    derivada = []
    s_w = np.arange(s_inicial, s_final, s_inicial/(s_final*100000))
    for i in range(len(s_w)):
        if s_w[i]>=swf:
            derivada.append((800*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(125*s_w[i]**4+700*s_w[i]**3-450*s_w[i]**2-420*s_w[i]+301)**2) 
            SW.append(s_w[i])
    ##insere no 0 prq o maior sw deve estar com o menor x
    SW.insert(0, s_inicial)
    SW.insert(0, s_inicial)
        
    for j in range(len(derivada)):
        x.append((q_t*tempo/ A*phi)*derivada[j])
    x.insert(0, x[0]) 
    x.insert(0,x[0]+ 0.5*x[0])
    return x, SW


def plot(s_inicialIII,s_inicialIDI,s_final,swfIII,swfIDI,tempo,phi,q_t,A):
    plot = calculaX(s_inicialIII,s_final,swfIII,tempo,phi,q_t,A)
    plotNew = NewSincial(s_inicialIDI,s_final,swfIDI,tempo,phi,q_t,A)
    plt.plot(plot[0],plot[1], color='black', label=r'$S_{iw}=S_{ini}$')
    plt.plot(plotNew[0], plotNew[1], color='purple', label=r'$S_{iw} < S_{ini}$')
    plt.legend(title='Casos', loc=0)
    plt.xlabel(r'$X$')
    plt.ylabel(r'$S_w$')
    plt.title(r'$S_w \times X$')
    plt.show()
    

    
def SensibilidadeQ_t(s_inicial,s_final,swf,tempo,phi,q_ti,q_tf,A):
    QT = np.arange(q_ti,q_tf,0.001)

    for i in range(len(QT)):

        results = calculaX(s_inicial,s_final,swf,tempo,phi,QT[i],A)
        plt.plot(results[0],results[1],label=r'$Q_t$ = ' + str(QT[i]))
        plt.legend(title=r'$Q_t$', loc = 0)
        plt.xlabel(r'$X$')
        plt.ylabel(r'$S_w$')
        plt.title(r'Variação de $Q_t$')
    plt.show()

def SensibilidadeT(s_inicial,s_final,swf,tempo_i,tempo_f,phi,q_t,A):
    T = np.arange(tempo_i,tempo_f,20000000)

    for i in range(len(T)):
        results = calculaX(s_inicial,s_final,swf,T[i],phi,q_t,A)
        plt.plot(results[0],results[1],label=r'$Tempo$ = ' + str(T[i]))
        plt.legend(title=r'$Tempo$', loc = 0)
        plt.xlabel(r'$X$')
        plt.ylabel(r'$S_w$')
        plt.title(r'Variação de Tempo')
    plt.show()


def SensibilidadeA(s_inicial,s_final,swf,tempo,phi,q_t,A_i,A_f):
    A = np.arange(A_i,A_f,1)

    for i in range(len(A)):
        results = calculaX(s_inicial,s_final,swf,tempo,phi,q_t,A[i])
        plt.plot(results[0],results[1],label=r'$A$ = ' + str(A[i]))
        plt.legend(title=r'$A$', loc = 0)
        plt.xlabel(r'$X$')
        plt.ylabel(r'$S_w$')
        plt.title(r'Variação da Área')
    plt.show()


def SensibilidadePhi(s_inicial,s_final,swf,tempo,phi_i,phi_f,q_t,A):
    PHI = np.arange(phi_i,phi_f,0.1)

    for i in range(len(PHI)):
        results = calculaX(s_inicial,s_final,swf,tempo,PHI[i],q_t,A)
        plt.plot(results[0],results[1],label=r'$\phi$ = ' + str(PHI[i]))
        plt.legend(title=r'$\phi$', loc = 0)
        plt.xlabel(r'$X$')
        plt.ylabel(r'$S_w$')
        plt.title(r'Variação da Porosidade')
    plt.show()


def VarViscosidadeAgua(s_inicial,s_final,tempo,phi,q_t,A,ua_i,ua_f):
    mi=np.arange(ua_i,ua_f,0.0001)
    # print('Mi agua=',mi)
    for k in range(len(mi)):
        x=[]
        SW =[]
        derivada = []
        s_w = np.arange(s_inicial, s_final, s_inicial/(s_final*100000))

        for i in range(len(s_w)):
            if k==0:
                derivada_aux = (400*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(375*s_w[i]**4+100*s_w[i]**3-150*s_w[i]**2-220*s_w[i]+151)**2
                swf = 0.7380

            if k==1:
                derivada_aux =  (2000*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(625*s_w[i]**4+500*s_w[i]**3-450*s_w[i]**2-540*s_w[i]+377)**2
                swf = 0.7540

            if k==2:
                derivada_aux = (150*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(125*s_w[i]**4+200*s_w[i]**3-150*s_w[i]**2-160*s_w[i]+113)**2
                swf = 0.7663

            if k==3:
                derivada_aux =  (2800*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(375*s_w[i]**4+1100*s_w[i]**3-750*s_w[i]**2-740*s_w[i]+527)**2
                swf = 0.7763

            if k==4:
                derivada_aux = (800*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(125*s_w[i]**4+700*s_w[i]**3-450*s_w[i]**2-420*s_w[i]+301)**2
                swf = 0.7834


            if s_w[i]>=swf:
                derivada.append(derivada_aux) 
                SW.append(s_w[i])
        ##insere no 0 prq o maior sw deve estar com o menor x
        SW.insert(0, s_inicial)
        SW.insert(0, s_inicial)
            
        for j in range(len(derivada)):
            x.append((q_t*tempo/ A*phi)*derivada[j])
        x.insert(0, x[0]) 
        x.insert(0,x[0]+ 0.5*x[0])
         
        plt.plot(x,SW,label=r'$\mu_w$ = ' + str(mi[k]))
        plt.legend(title=r'$\mu_w$', loc= 0)
        plt.xlabel(r'$X$')
        plt.ylabel(r'$S_w$')
        plt.title(r'Variação da Viscosidade da Água')
    plt.show()

def VarViscosidadeOleo(s_inicial,s_final,tempo,phi,q_t,A,uo_i,uo_f):
    mi=np.arange(uo_i,uo_f,0.0001)
    print('Mi oleo=',mi)
    for k in range(len(mi)):
        x=[]
        SW =[]
        derivada = []
        s_w = np.arange(s_inicial, s_final, s_inicial/(s_final*100000))

        for i in range(len(s_w)):
            if k==0:
                derivada_aux = (56000*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(625*s_w[i]**4-8500*s_w[i]**3+4950*s_w[i]**2+4140*s_w[i]-3007)**2
                swf = 0.8058

            if k==1:
                derivada_aux = (125*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(8*(125*s_w[i]**3-75*s_w[i]**2-65*s_w[i]+47)**2)
                swf = 0.7998

            if k==2:
                derivada_aux = (72000*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(625*s_w[i]**4+7500*s_w[i]**3-4650*s_w[i]**2-4180*s_w[i]+3009)**2
                swf = 0.7929

            if k==3:
                derivada_aux = (800*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(125*s_w[i]**4+700*s_w[i]**3-450*s_w[i]**2-420*s_w[i]+301)**2
                swf = 0.7834

            if k==4:
                derivada_aux = (88000*(s_w[i]-1)*(5*s_w[i]-1)**3*(5*s_w[i]**2+2*s_w[i]-7))/(1875*s_w[i]**4+6500*s_w[i]**3-4350*s_w[i]**2-4220*s_w[i]+3011)**2
                swf = 0.7796


            if s_w[i]>=swf:
                derivada.append(derivada_aux) 
                SW.append(s_w[i])
        ##insere no 0 prq o maior sw deve estar com o menor x
        SW.insert(0, s_inicial)
        SW.insert(0, s_inicial)
            
        for j in range(len(derivada)):
            x.append((q_t*tempo/ A*phi)*derivada[j])
        x.insert(0, x[0]) 
        x.insert(0,x[0]+ 0.5*x[0])
         
        plt.plot(x,SW,label=r'$\mu_o$ = ' + str(mi[k]))
        plt.legend(title=r'$\mu_o$', loc= 0)
        plt.xlabel(r'$X$')
        plt.ylabel(r'$S_w$')
        plt.title(r'Variação da Viscosidade do Óleo')
    plt.show()

   



plot(s_inicialIII = 0.2,s_inicialIDI=0.2,s_final = 0.94,swfIII = 0.7834, swfIDI=0.7834,tempo= 100000000,phi =0.2,q_t = 5*10**(-3),A = 1)

SensibilidadeQ_t(s_inicial = 0.2,s_final = 0.94,swf = 0.7834,tempo= 100000000,phi =0.2,q_ti = 1*10**(-3),q_tf=6*10**(-3),A = 1)

SensibilidadeT(s_inicial = 0.2,s_final = 0.94,swf = 0.7834,tempo_i= 1000000,tempo_f=100000000,phi =0.2,q_t=5*10**(-3),A = 1)

SensibilidadeA(s_inicial = 0.2,s_final = 0.94,swf = 0.7834,tempo=100000000,phi =0.2,q_t=5*10**(-3),A_i= 1,A_f=25)

SensibilidadePhi(s_inicial = 0.2,s_final = 0.94,swf = 0.7834,tempo=100000000,phi_i =0.1,phi_f=0.6,q_t=5*10**(-3),A=1)

VarViscosidadeAgua(s_inicial = 0.2,s_final = 0.94,tempo=100000000,phi =0.2,q_t=5*10**(-3),A=1,ua_i=0.4*10**-3,ua_f=0.9*10**-3)

VarViscosidadeOleo(s_inicial = 0.2,s_final = 0.94,tempo=100000000,phi =0.2,q_t=5*10**(-3),A=1,uo_i=0.7*10**-3,uo_f=1.2*10**-3)


