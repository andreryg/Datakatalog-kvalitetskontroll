# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:33:12 2024

@author: andryg
"""

import nvdbapiv3

def get_egenskaper(vegobjekttypeid, egenskapstypeid):
    vegobjekt = nvdbapiv3.nvdbFagdata(vegobjekttypeid)
    ettVegobjekt = vegobjekt.nesteNvdbFagObjekt()
    egenskapsverdier = []
    i = 0
    while ettVegobjekt:
        egenskapsverdier.append(ettVegobjekt.egenskapverdi(egenskapstypeid))
        ettVegobjekt = vegobjekt.nesteNvdbFagObjekt()
        
    return egenskapsverdier
    
def main():
    get_egenskaper(59, 1365)
    
if __name__=="__main__":
    main()