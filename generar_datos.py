import pandas as pd
import numpy as np

# Cargar clientes
clientes = pd.read_excel("data/raw/clientes.xlsx")

# Crear ventas
np.random.seed(42)

ventas = pd.DataFrame({
    "id_cliente": np.random.choice(clientes["Identificador Usuario"], 5000),
    "fecha": pd.date_range(start="2023-01-01", periods=5000, freq="D"),
    "importe": np.random.randint(10, 500, 5000),
    "producto": np.random.choice(["Plan Básico", "Plan Premium", "Plan Estándar"], 5000)
})

ventas.to_csv("data/raw/ventas.csv", index=False)

print("Archivo ventas creado correctamente")