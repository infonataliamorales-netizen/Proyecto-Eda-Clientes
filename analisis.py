import pandas as pd

# Cargar datos
clientes = pd.read_excel("data/raw/clientes.xlsx")
ventas = pd.read_csv("data/raw/ventas.csv")

# Limpieza
clientes = clientes.drop_duplicates()
ventas = ventas.drop_duplicates()

clientes = clientes.dropna()
ventas = ventas.dropna()

# Convertir fecha
ventas["fecha"] = pd.to_datetime(ventas["fecha"])

# Unir datasets
df = pd.merge(
    clientes,
    ventas,
    left_on="Identificador Usuario",
    right_on="id_cliente",
    how="inner"
)

# Crear nuevas columnas
df["mes"] = df["fecha"].dt.month
df["año"] = df["fecha"].dt.year

# Guardar resultado final
df.to_csv("data/processed/datos_finales.csv", index=False)

print("Dataset final creado correctamente")