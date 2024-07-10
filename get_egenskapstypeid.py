# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:04:49 2024

@author: andryg
"""

import requests

def get_egenskapstypeid(egenskapstypeid):
    egenskapstype = requests.get(f"https://nvdbapiles-v3.atlas.vegvesen.no/vegobjekttyper/egenskapstyper/{egenskapstypeid}", headers={'X-client':'Datakatalog kvalitetskontroll'})
    if egenskapstype.status_code == 200:
        egenskapstype = egenskapstype.json()
    else:
        print("Error: "+str(egenskapstype.content))
        return {}
    
    return egenskapstype
    
def main():
    egenskapstypeid = 4705
    get_egenskapstypeid(egenskapstypeid)
    
if __name__ == "__main__":
    main()