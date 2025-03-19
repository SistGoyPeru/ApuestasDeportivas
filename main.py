import streamlit as st
from clases import Ligas

liga=Ligas("liga_española.xlsm")

def main():
 

   st.sidebar.header("Encuentros")
   local=st.sidebar.selectbox("Equipo Local",liga.equipos_local())
   visita=st.sidebar.selectbox("Equipo Visita",liga.equipos_visita())
   st.markdown("## "+local+" - "+visita)
   total1,total2=st.columns(2,gap='large')
   with total1:
       st.metric(label="Promedio Goles a Favor Local",value="{:.2f}".format(liga.promedio_equipo_goles_a_favor_local(local)))
       st.metric(label="Promedio Goles encontra Local",value="{:.2f}".format(liga.promedio_equipo_goles_encontra_local(local)))
       st.metric(label="Fuerza Ofensiva Local",value="{:.2f}".format(liga.promedio_equipo_goles_a_favor_local(local)/liga.promedio_goles_a_favor_local()))
       st.metric(label="Fuerza Defensiva Local",value="{:.2f}".format(liga.promedio_equipo_goles_encontra_local(local)/liga.promedio_goles_encontra_local()))
       st.metric(label="Fuerza Promedio Local",value="{:.2f}".format(liga.promedio_equipo_goles_a_favor_local(local)/liga.promedio_goles_a_favor_local()*liga.promedio_equipo_goles_encontra_Visita(visita)/liga.promedio_goles_a_favor_local()))
   with total2:  
       st.metric(label="Promedio Goles a Favor Visita",value="{:.2f}".format(liga.promedio_equipo_goles_a_favor_Visita(visita)))
       st.metric(label="Promedio Goles encontra Visita",value="{:.2f}".format(liga.promedio_equipo_goles_encontra_Visita(visita)))
       st.metric(label="Fuerza Ofensiva Visita",value="{:.2f}".format(liga.promedio_equipo_goles_a_favor_Visita(visita)/liga.promedio_goles_encontra_local()))
       st.metric(label="Fuerza Defensiva Visita",value="{:.2f}".format(liga.promedio_equipo_goles_encontra_Visita(visita)/liga.promedio_goles_a_favor_local()))
       st.metric(label="Fuerza Promedio Visita",value="{:.2f}".format(liga.promedio_equipo_goles_a_favor_Visita(visita)/liga.promedio_goles_encontra_local()*liga.promedio_equipo_goles_encontra_local(local)/liga.promedio_goles_encontra_local()))

if __name__=='__main__':
    main()