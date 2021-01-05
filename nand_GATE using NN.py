import random

class MPNeuron:

    def __init__(self,n=3,inputs=[1,1,1],weights=[1,1,1],threshold=2.5):
          self.n=n
          self.inputs=inputs
          self.weights=weights
          self.threshold=threshold

    def MP_Neuron_Input(self,n,threshold):
          self.n=n
          a=[]
          w=[]
          for j in range(n):
                a.append(float(input("enter the input")))
                w.append(float(random.uniform(-1,+1)))
          self.inputs= a      
          self.weights= w
          self.threshold=threshold

          print(self.inputs,self.weights)     

    def MP_Neuron_Evaluate(self):
         
         pass
obj=MPNeuron()
obj.MP_Neuron_Input(3,2)