import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import poisson
from pathlib import Path
from openpyxl import load_workbook

class Ligas:
    def __init__(self,archivo):
        self.archivo=archivo
        self.data_encuentros=pd.read_excel(Path(__file__).resolve().parent / self.archivo)
       
    def promedio_goles_a_favor_local(self):
        return self.data_encuentros["GF"].mean()
    
    def promedio_goles_encontra_local(self):
        return self.data_encuentros["GC"].mean()
    
    def promedio_equipo_goles_a_favor_local(self,local):
        datos=self.data_encuentros
        return datos[datos['Local']==local].groupby('Local')['GF'].mean().iloc[0]
    
    def promedio_equipo_goles_encontra_local(self,local):
        datos=self.data_encuentros
        return datos[datos['Local']==local].groupby('Local')['GC'].mean().iloc[0]
    
    def promedio_equipo_goles_a_favor_Visita(self,local):
        datos=self.data_encuentros
        return datos[datos['Visita']==local].groupby('Visita')['GC'].mean().iloc[0]
    
    def promedio_equipo_goles_encontra_Visita(self,local):
        datos=self.data_encuentros
        return datos[datos['Visita']==local].groupby('Visita')['GF'].mean().iloc[0]
    
    
       
        
    def equipos_local(self):
        return self.data_encuentros["Local"].unique()
    
    def equipos_visita(self):
        return self.data_encuentros["Visita"].unique()
    
  