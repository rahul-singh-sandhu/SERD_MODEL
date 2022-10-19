import matplotlib.pyplot as plt
import numpy as np
import random

pd=float(1/3)
pr=float(1/3)
pt=pd+pr

propArray=[int(0),int(0)]
St=int(1)
Et=int(1)

StEv=[St]
EtEv=[Et]

StEvIt=[]
EtEvIt=[]

TS1=int(100)
TS2=int(200)
iterations=int(100000)

ObsStEvTot=[]
ObsEtEvTot=[]
ObsTauEvTot=[]
ObsSampleSize=[]

inputStart=bool(False)
allowAutoSplits=bool(False)
merged=bool(False)

for i1 in range(TS2+1):
  StEvIt.append(0)
  EtEvIt.append(0)

for i1 in range(TS2):
  ObsStEvTot.append(0)
  ObsEtEvTot.append(0)
  ObsTauEvTot.append(0)
  ObsSampleSize.append(0)

obsStLoc=100
obsStHalfRange=10

obsEtLoc=100
obsEtHalfRange=10

sampleSize=int(0)

for i1 in range(iterations):
  
  inputChosen=bool(False)
  
  merged=False

  propArray=[int(0),int(0)]
  St=int(1)
  Et=int(1)

  PIPprop=[St]
  updateTime=int(0)

  for t1 in range(TS1):
    shift=[int(0)]

    if merged==False:

      for x1 in range(St):
        rand=float(random.random())

        if rand < pd:
          propArray[x1+shift[x1]]+=1
          propArray.insert(x1+shift[x1]+1,0)
          shift.append(shift[x1]+1)

        elif rand < pt:
          propArray[x1+shift[x1]]=propArray[x1+shift[x1]]+propArray[x1+shift[x1]+1]-1
          propArray.pop(x1+shift[x1]+1)
          shift.append(shift[x1]-1)

        else:
          shift.append(shift[x1])

      St2=St+shift[St]
      Et2=Et+propArray[0]

      if St==0:
          St=1
          Et=1
          propArray=[int(0),int(0)]
          shift=[int(0)]
          PIPprop=[St]
      else:
        ind1=int(0)
        for x2 in range(St):
          while PIPprop[ind1]==x2:
            PIPprop[ind1]+=shift[x2]-1
            ind1+=1
            if ind1>St-1:
              break
          if ind1>St-1:
            break

        TSupdateTime=int(0)
        for t2 in range(t1-updateTime):
          if PIPprop[t2]<1:
            TSupdateTime+=1
          else:
            break

        for i2 in range(TSupdateTime):
          PIPprop.pop(0)

        updateTime+=TSupdateTime
        St=St2
        PIPprop.append(St)

        Et=Et2
        propArray.pop(0)
        propArray.append(0)

      
    if St>obsStLoc-obsStHalfRange:
      if St<=obsStLoc+obsStHalfRange:
        if Et>obsEtLoc-obsEtHalfRange:
          if Et<=obsEtLoc+obsEtHalfRange:
            inputChosen=bool(True)
            sampleSize+=1





  if inputChosen==True:
    for t1 in range(TS2):
      shift=[int(0)]

      if merged==False:

        for x1 in range(St):
          rand=float(random.random())

          if rand < pd:
            propArray[x1+shift[x1]]+=1
            propArray.insert(x1+shift[x1]+1,0)
            shift.append(shift[x1]+1)

          elif rand < pt:
            propArray[x1+shift[x1]]=propArray[x1+shift[x1]]+propArray[x1+shift[x1]+1]-1
            propArray.pop(x1+shift[x1]+1)
            shift.append(shift[x1]-1)

          else:
            shift.append(shift[x1])

        St2=St+shift[St]
        Et2=Et+propArray[0]

        if St==0:
          if allowAutoSplits==False:
            merged=True

          else:
            St=1
            Et=1
            propArray=[int(0),int(0)]
            shift=[int(0)]
            PIPprop=[St]
        else:
          ind1=int(0)
          for x2 in range(St):
            while PIPprop[ind1]==x2:
              PIPprop[ind1]+=shift[x2]-1
              ind1+=1
              if ind1>St-1:
                break
            if ind1>St-1:
              break

          TSupdateTime=int(0)
          for t2 in range(TS1+t1-updateTime):
            if PIPprop[t2]<1:
              TSupdateTime+=1
            else:
              break

          for i2 in range(TSupdateTime):
            PIPprop.pop(0)
            ObsStEvTot[t1]+=St2
            ObsEtEvTot[t1]+=Et
            ObsTauEvTot[t1]+=TS1+t1-updateTime-i2+1
            ObsSampleSize[t1]+=1

          updateTime+=TSupdateTime
          St=St2
          PIPprop.append(St)

          Et=Et2
          propArray.pop(0)
          propArray.append(0)


normValObsStEvTot=[]
normValObsEtEvTot=[]
normValObsTauEvTot=[]

for i1 in range(TS2):
  if ObsSampleSize[i1]>0:
    normValObsStEvTot.append(ObsStEvTot[i1]/ObsSampleSize[i1])
    normValObsEtEvTot.append(ObsEtEvTot[i1]/ObsSampleSize[i1])
    normValObsTauEvTot.append(ObsTauEvTot[i1]/ObsSampleSize[i1])
  else:
    normValObsStEvTot.append(0)
    normValObsEtEvTot.append(0)
    normValObsTauEvTot.append(0)




MatStrNormValObsStEvTot="{"
MatStrNormValObsEtEvTot="{"
MatStrNormValObsTauEvTot="{"

for i1 in range(TS2):
  if i1<TS2-1:
    MatStrNormValObsStEvTot=MatStrNormValObsStEvTot + str(normValObsStEvTot[i1]) + ","
    MatStrNormValObsEtEvTot=MatStrNormValObsEtEvTot + str(normValObsEtEvTot[i1]) + ","
    MatStrNormValObsTauEvTot=MatStrNormValObsTauEvTot + str(normValObsTauEvTot[i1]) + ","
  else:
    MatStrNormValObsStEvTot=MatStrNormValObsStEvTot + str(normValObsStEvTot[i1]) + "}"
    MatStrNormValObsEtEvTot=MatStrNormValObsEtEvTot + str(normValObsEtEvTot[i1]) + "}"
    MatStrNormValObsTauEvTot=MatStrNormValObsTauEvTot + str(normValObsTauEvTot[i1]) + "}"

print("{"+MatStrNormValObsStEvTot+",")
print(MatStrNormValObsEtEvTot+",")
print(MatStrNormValObsTauEvTot+"}")
print(sampleSize)

mathematicaFormForResults="{"+MatStrNormValObsStEvTot+","+MatStrNormValObsEtEvTot+","+MatStrNormValObsTauEvTot+"}"

f = open("SystemEvA1.txt", "w")
f.write(mathematicaFormForResults)
f.close()

y1 = np.array(normValObsStEvTot)
y2 = np.array(normValObsEtEvTot)
y3 = np.array(normValObsTauEvTot)

plt.plot(y1)
plt.plot(y2)
plt.plot(y3)

plt.show()