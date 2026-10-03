def procesar_datos_financieros():
    print("--- INICIANDO SISTEMA DE AUTOMATIZACIÓN DE REPORTES ---")
    
    registros = [
        {"cliente": "Viaje Centro", "monto": 25.0, "estado": "Completado"},
        {"cliente": "Viaje Mall", "monto": 45.0, "estado": "Completado"},
        {"cliente": "Cancelado", "monto": 0.0, "estado": "Cancelado"},
        {"cliente": "Viaje Aeropuerto", "monto": 120.0, "estado": "Completado"},
        {"cliente": "Viaje Urbano", "monto": 15.0, "estado": "Completado"}
    ]
    
    total_ingresos = 0
    servicios_exitosos = 0
    
    print("\n[Procesando registros válidos...]")
    for item in registros:
        if item["estado"] == "Completado":
            total_ingresos += item["monto"]
            servicios_exitosos += 1
            print(f" -> Procesado: {item['cliente']} | S/. {item['monto']}")

    promedio = total_ingresos / servicios_exitosos if servicios_exitosos > 0 else 0

    print("\n==========================================")
    print("           REPORTE FINAL GENERADO         ")
    print("==========================================")
    print(f"Total de servicios completados : {servicios_exitosos}")
    print(f"Ingresos totales acumulados    : S/. {total_ingresos:.2f}")
    print(f"Promedio por servicio          : S/. {promedio:.2f}")
    print("Estado del proceso             : ÉXITO")
    print("==========================================")

if __name__ == "__main__":
    procesar_datos_financieros()