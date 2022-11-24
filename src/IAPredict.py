import numpy as np
from joblib import load
import pandas as pd

with open("./IA/872215.joblib", 'rb') as fo:
    clf = load(fo)

# MedInc = input("MedInc : ")
# HouseAge = input("HouseAge : ")
# AveRooms = input("AveRooms : ")
# AveBedrms = input("AveBedrms : ")
# Population = input("Population : ")
# AveOccup = input("AveOccup : ")
# Latitude = input("Latitude : ")
# Longitude = input("Longitude : ")

# resultat = clf.predict(pd.DataFrame(data={"MedInc": [MedInc], "HouseAge": [HouseAge], "AveRooms": [AveRooms], "AveBedrms": [AveBedrms], "Population": [Population], "AveOccup": [AveOccup], "Latitude": [Latitude], "Longitude": [Longitude]}))

# print("MedHouseVal : " + str(np.round_(resultat[0]*100000, 2)) + "$")

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
