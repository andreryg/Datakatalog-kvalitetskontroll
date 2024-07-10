# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 08:53:03 2024

@author: andryg
"""

import pandas as pd
import numpy as np
import nvdbapiv3


def main():
    egenskapstyper = [10148,8348,12251,1352,1363,1365,1368,1373,1375,4170,5648,9810,8786,1611]
    antall_desimaler = [1,1,1,1,1,1,1,1,1,1,1,2,1,1]
    vegobjekttyper = [871,785,969,3,49,59,72,145,167,519,623,859,49,3]
    
    egenskapstypeid = 1365
    vegobjekttypeid = 59
    
    egenskapstype_tabell = pd.read_excel('EGENSKAPSTYPE.xlsx')
    egenskapstype_tabell = egenskapstype_tabell[['ID_EGENSKAPSTYPE', 'ID_VEGOB_TYPE', 'TOTAL_FELTLENGDE', 'ANTALL_DESIMALER', 'Absolutt_min', 'RIMELIG_MINV', 'RIMELIG_MAXV', 'Absolutt_maks', 'MASKE', 'DEFAULTVERDI', 'Dato_fra_NVDB']]
    egenskapstype_tabell = egenskapstype_tabell[egenskapstype_tabell['Dato_fra_NVDB'].notna()]
    egenskapstype_tabell['fjern'] = egenskapstype_tabell.apply(lambda x: 0 if pd.isna([x.ANTALL_DESIMALER,x.Absolutt_min,x.RIMELIG_MINV,x.RIMELIG_MAXV,x.Absolutt_maks,x.MASKE,x.DEFAULTVERDI]).all() else 1, axis=1)
    egenskapstype_tabell = egenskapstype_tabell[egenskapstype_tabell['fjern'] == 1]
    
    antall_desimaler = pd.DataFrame(columns=['egenskapstypeid', 'vegobjekttypeid', 'datakatalogverdi', 'tot_antall', 'antall_oppfyller_krav', 'prosent_oppfyller_krav', '0_desimaler', '1_desimal', '2_desimaler', '3_desimaler', '>3_desimaler'])
    print(egenskapstype_tabell)
    
    
if __name__=="__main__":
    main()