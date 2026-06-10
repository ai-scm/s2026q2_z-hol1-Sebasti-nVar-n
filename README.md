🚀 Hands-On Lab 1: Data Engineering Pipeline
📝 Descripción del Proyecto
Este proyecto implementa un flujo de trabajo Serverless en AWS para el procesamiento de datos. El objetivo es automatizar la ingesta de archivos CSV y su transformación a formato JSON mediante AWS Lambda, almacenándolos en S3 y habilitando su consulta analítica a través de Amazon Athena.

🏗️ Arquitectura
sample_users.csv ➔ S3 (Input) ➔ AWS Lambda ➔ S3 (Output) ➔ Amazon Athena ➔ SQL Queries

⚙️ Configuración Técnica
Servicios: AWS Lambda, S3, Athena, IAM.

Bucket de Entrada: bld-tseed-workshop-input-semillero-2026-q2-z

Bucket de Salida: bld-tseed-workshop-output-semillero-2026-q2-z

Carpeta de Salida: Sebastián_Varón/

Estructura del Repositorio:

s2026q2_z-hol1-Sebasti-nVar-n/
│
├── 🐍 lambda/
│   └── lambda_function.py
│
├── 📊 athena/
│   └── queries.sql
│
├── 📸 screenshots/
│
└── 📝 README.md

Funcionamiento de Lambda:

La función realiza el proceso de ETL (Extract, Transform, Load):

Lectura: Captura el archivo desde el bucket de origen.

Transformación: Convierte cada fila del CSV en un objeto JSON estructurado.

Carga: Almacena el resultado final en el bucket de destino siguiendo la partición definida.
