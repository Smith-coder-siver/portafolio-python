def calcular_metricas_transporte():
    print("--- CALCULADOR DE MÉTRICAS Y COSTOS DE TRANSPORTE ---")
    
    # Datos de ejemplo de una jornada o servicio
    distancia_km = 45.5
    consumo_por_100km = 8.5  # Litros promedio
    precio_combustible_galon = 15.0  # Costo por galón (ejemplo GLP/Combustible)
    otros_gastos = 10.0  # Mantenimiento, cochera, etc.
    
    # Conversión estimada (1 galón = 3.785 litros)
    litros_consumidos = (distancia_km * consumo_por_100km) / 100
    galones_consumidos = litros_consumidos / 3.785
    
    costo_combustible = galones_consumidos * precio_combustible_galon
    costo_total_operacion = costo_combustible + otros_gastos
    
    print(f"\nDistancia recorrida      : {distancia_km} km")
    print(f"Combustible estimado     : {galones_consumidos:.2f} galones")
    print(f"Costo de combustible     : S/. {costo_combustible:.2f}")
    print(f"Gastos operativos extras : S/. {otros_gastos:.2f}")
    print("------------------------------------------")
    print(f"COSTO TOTAL DE OPERACIÓN : S/. {costo_total_operacion:.2f}")
    print("==========================================")
    print("Estado del cálculo       : COMPLETADO")
    print("==========================================")

if __name__ == "__main__":
    calcular_metricas_transporte()