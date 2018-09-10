
# coding: utf-8

# # Desafio 1

# link a los datos: http://campus.digitalhouse.com/mod/url/view.php?id=32168
# Es necesario guardar el csv con el nombre properatti.csv en una carpeta DATA en el raiz del proyecto

# In[1]:


#Importar librerias
import numpy as np
import pandas as pd
import re
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Leemos el archivo y creamos el dataframe "data"
data = pd.read_csv("properatti.csv")


# In[3]:


# Regex para determinar ambientes


# In[4]:


patron = r'(\d*|mono|\w*)\s*?amb\w*'
regex = re.compile(patron, flags=re.IGNORECASE)
data["title_dato"] = data.title.str.extract(r'(\d*|mono|\w*)\s*?amb\w*', expand=False)


# In[5]:


patron = r'(\d*|MONO|\w*)\s*?AMB\w*'
regex = re.compile(patron, flags=re.IGNORECASE)
data["title_dato1"] = data.title.str.extract(r'(\d*|MONO|\w*)\s*?AMB\w*', expand=False)


# In[6]:


patron = r'(\d*|mono|\w*)\s*?amb\w*'
regex = re.compile(patron, flags=re.IGNORECASE)
data["description_dato"] = data.description.str.extract(r'(\d*|mono|\w*)\s*?amb\w*', expand=False)


# In[7]:


patron = r'(\d*|MONO|\w*)\s*?AMB\w*'
regex = re.compile(patron, flags=re.IGNORECASE)
data["description_dato1"] = data.description.str.extract(r'(\d*|MONO|\w*)\s*?AMB\w*', expand=False)


# In[8]:


# Reemplazar los valores NaN por 0


# In[9]:


data["title_dato"]= data["title_dato"].fillna(0)
data["title_dato1"]= data["title_dato1"].fillna(0)
data["description_dato"]= data["description_dato"].fillna(0)
data["description_dato1"]= data["description_dato1"].fillna(0)


# In[10]:


# Generar datos de ambientes con palabras clave


# In[11]:


data.replace({'title_dato': {'4º':0,'3º':0,'½':0,"Mono":1,"siete":7,"IMPORTANTE":1,"importante":1,"0002":2,"AMPLISIMO":1,"hermoso":1,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1,"0":0,"Comodo":1,"amplio":1,"Unico":1,"gran":1,"Único":1,"Amplio":1,"un":1,"MONOH":1,"MON":1,"AMPLIO":1,"BMONO":1,"M0NO":1,"UN":1,"MONO":1, "mono":1, "DOS":2, "dos":2, "TRES":3, "tres":3, "CUATRO":4, "cuatro":4,"CINCO":5, "cinco":5}},  inplace = True)
data.replace({'title_dato1': {'4º':0,'3º':0,'½':0,"Mono":1,"siete":7,"IMPORTANTE":1,"importante":1,"0002":2,"AMPLISIMO":1,"hermoso":1,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1,"0":0,"Comodo":1,"amplio":1,"Unico":1,"gran":1,"Único":1,"Amplio":1,"un":1,"MONOH":1,"MON":1,"AMPLIO":1,"BMONO":1,"M0NO":1,"UN":1,"MONO": 1, "mono": 1, "DOS" : 2, "dos": 2, "TRES": 3,"tres":3,"CUATRO":4,"cuatro":4,"CINCO":5, "cinco":5}},  inplace = True)
data.replace({'description_dato': {'4º':0,'3º':0,'½':0,"Mono":1,"siete":7,"IMPORTANTE":1,"importante":1,"0002":2,"AMPLISIMO":1,"hermoso":1,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1,"0":0,"Comodo":1,"amplio":1,"Unico":1,"gran":1,"Único":1,"Amplio":1,"un":1,"MONOH":1,"MON":1,"AMPLIO":1,"BMONO":1,"M0NO":1,"UN":1,"MONO": 1, "mono": 1, "DOS" : 2, "dos": 2, "TRES": 3,"tres":3,"CUATRO":4,"cuatro":4,"CINCO":5, "cinco":5}},  inplace = True)
data.replace({'description_dato1': {'4º':0,'3º':0,'½':0,"Mono":1,"siete":7,"IMPORTANTE":1,"importante":1,"0002":2,"AMPLISIMO":1,"hermoso":1,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1,"0":0,"Comodo":1,"amplio":1,"Unico":1,"gran":1,"Único":1,"Amplio":1,"un":1,"MONOH":1,"MON":1,"AMPLIO":1,"BMONO":1,"M0NO":1,"UN":1,"MONO": 1, "mono": 1, "DOS" : 2, "dos": 2, "TRES": 3,"tres":3,"CUATRO":4,"cuatro":4,"CINCO":5, "cinco":5}},  inplace = True)


# In[12]:


# Los valores texto indetrminados los convierto en 0


# In[13]:


data["title_dato"]=data["title_dato"].replace(r'[a-z]|[A-Z]', 0, regex=True)
data["title_dato1"]=data["title_dato1"].replace(r'[a-z]|[A-Z]', 0, regex=True)
data["description_dato"]=data["description_dato"].replace(r'[a-z]|[A-Z]', 0, regex=True)
data["description_dato1"]=data["description_dato1"].replace(r'[a-z]|[A-Z]', 0, regex=True)


# In[14]:


#convierto los datoa a numeric para poder calcular los ambientes


# In[15]:


data[['title_dato','title_dato1','description_dato','description_dato1']] = data[['title_dato','title_dato1','description_dato','description_dato1']].apply(pd.to_numeric)


# In[16]:


#Calculo los ambientes


# In[17]:


data['Ambientes']=data[['title_dato','title_dato1','description_dato','description_dato1']].apply(np.max,axis=1)


# In[18]:


#Convierto Ambientes a int 


# In[19]:


data['Ambientes']=data['Ambientes'].astype(int)


# In[21]:


data = data.drop('title_dato', 1)
data = data.drop('title_dato1', 1)
data = data.drop('description_dato', 1)
data = data.drop('description_dato1', 1)
data.head


# In[ ]:


#La columna Ambientes tiene el numero correspondite solo en los casos que me fue posible...

