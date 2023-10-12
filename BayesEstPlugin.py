#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pydot
#from IPython.display import SVG
from pycausal.pycausal import pycausal 



# #### Load the example dataset

# In[2]:

class BayesEstPlugin:
  def input(self, inputfile):
    data_dir = inputfile
    self.df = pd.read_table(data_dir, sep="\t")
  def run(self):
    pass
  def output(self, outputfile):
    # #### Start Java VM

    # In[3]:


    pc = pycausal()
    pc.start_vm()

    # #### Load causal algorithms from the py-causal library and Run BayesEst Discrete

    # In[4]:


    from pycausal import search as s

    bayesEst = s.bayesEst(self.df, depth = -1, alpha = 0.05, verbose = True)


    # #### BayesEst Discrete's Result's Nodes

    # In[5]:


    bayesEst.getNodes()


    # #### BayesEst Discrete's Result's Edges

    # In[6]:


    bayesEst.getEdges()


    # In[7]:

    #print(dir(bayesEst))

    #dot = bayesEst.getDot()
    #svg_str = dot.create_svg(prog='dot')
    #SVG(svg_str)


    # In[8]:


    bayesEst.getDag()


    # In[9]:


    bayesEst.getBayesPm()


    # In[10]:


    im = bayesEst.getBayesIm()
    im = im.toString()
    im


    # #### Stop Java VM

    # In[11]:

    try:
      pc.stop_vm()
    except:
      pass

    # In[ ]:




