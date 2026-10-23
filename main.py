import pandas as pd


dane = pd.read_csv("./uczniowie.csv")
print(dane)
print("--------------------------------")

df = pd.DataFrame(dane)
print(df)
print("--------------------------------")
print(df.head())
print("--------------------------------")
print(df.shape)
print("--------------------------------")
print(df.columns)
print("--------------------------------")
print(df[["Imie","Ocena"]])
print("--------------------------------")
print(df["Ocena"].mean())
print("--------------------------------")
print(df["Ocena"].max())
print("------------------------------")
maximum = f"najwieksza ocena to {df["Ocena"].max()}"
with(open("max.txt","w")) as f:
    f.write(maximum)

print("***************************************************")

danejson = pd.read_json("./uczniowie.json")

dfjson = pd.DataFrame(danejson)
counter = 0
for data in dfjson["Wiek"]:
    if(data >= 18):
        counter += 1
print(counter)