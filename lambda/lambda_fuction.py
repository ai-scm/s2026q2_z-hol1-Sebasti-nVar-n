import boto3
import json
import csv

BUCKET_INPUT = 'bld-tseed-workshop-input-semillero-2026-q2-z'
BUCKET_OUTPUT = 'bld-tseed-workshop-output-semillero-2026-q2-z'
PREFIXES_A_PROBAR = ['Sebastiàn_Varòn/', 'Sebastián_Varón/', 'Sebastian_Varon/']

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        file_key = None
        carpeta_activa = 'Sebastiàn_Varòn/'
        
        for prefix in PREFIXES_A_PROBAR:
            response_objects = s3_client.list_objects_v2(Bucket=BUCKET_INPUT, Prefix=prefix)
            if 'Contents' in response_objects:
                for obj in response_objects['Contents']:
                    key = obj['Key']
                    if key.lower().endswith('.csv'):
                        file_key = key
                        carpeta_activa = prefix
                        break
            if file_key:
                break

        if not file_key:
            return {
                'statusCode': 404, 
                'body': json.dumps({'error': "No se encontro ningun archivo CSV"})
            }
            
        print(f"Procesando archivo origen: {file_key}")
        
        response = s3_client.get_object(Bucket=BUCKET_INPUT, Key=file_key)
        csv_content = response['Body'].read().decode('utf-8', errors='ignore').splitlines()
        
        csv_reader = csv.DictReader(csv_content)
        contador = 1
        
        for fila in csv_reader:
            if not fila or all(value == '' for value in fila.values()):
                continue
                
            fila_limpia = {str(k).strip(): str(v).strip() for k, v in fila.items() if k is not None}
            json_key = f"{carpeta_activa}{contador}.json"
            json_data = json.dumps(fila_limpia, ensure_ascii=False)
            
            s3_client.put_object(
                Bucket=BUCKET_OUTPUT,
                Key=json_key,
                Body=json_data,
                ContentType='application/json'
            )
            contador += 1
            
        print(f"Proceso terminado. Se crearon {contador - 1} archivos JSON.")
        return {
            'statusCode': 200,
            'body': json.dumps({
                'resultado': 'Exito', 
                'archivos_creados': contador - 1,
                'carpeta_destino': carpeta_activa
            })
        }

    except Exception as e:
        print(f"Error detectado en la ejecucion: {str(e)}")
        return {
            'statusCode': 500, 
            'body': json.dumps({'error_detectado': str(e)})
        }