import csv

def leer_archivo_csv(archivo):
    """Función para leer el archivo CSV y devolver una lista de transacciones."""
    transacciones = []
    with open(archivo, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transacciones.append({
                'id': int(row['id']),
                'tipo': row['tipo'],
                'monto': float(row['monto'])
            })
    return transacciones

def generar_reporte(transacciones):
    """Genera el reporte final basado en las transacciones."""
    balance = 0
    credito_count = 0
    debito_count = 0
    max_transaccion = {'id': None, 'monto': 0}

    for transaccion in transacciones:
        # Actualiza el balance
        if transaccion['tipo'] == 'Crédito':
            balance += transaccion['monto']
            credito_count += 1
        elif transaccion['tipo'] == 'Débito':
            balance -= transaccion['monto']
            debito_count += 1
        
        # Verifica la transacción de mayor monto
        if transaccion['monto'] > max_transaccion['monto']:
            max_transaccion = transaccion

    # Muestra el reporte
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {max_transaccion['id']} - {max_transaccion['monto']:.2f}")
    print(f"Conteo de Transacciones: Crédito: {credito_count} Débito: {debito_count}")

def main():
    archivo_csv = 'transactions.csv'  # Ruta del archivo CSV
    transacciones = leer_archivo_csv(archivo_csv)
    generar_reporte(transacciones)

if __name__ == "__main__":
    main()
