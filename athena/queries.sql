CREATE DATABASE IF NOT EXISTS sebasti_n_var_n;

CREATE EXTERNAL TABLE IF NOT EXISTS sebasti_n_var_n.datos_usuarios (
  user_id STRING,
  name STRING,
  country STRING,
  city STRING,
  role STRING,
  department STRING,
  education STRING,
  age STRING,
  gender STRING,
  marital_status STRING,
  experience_years STRING,
  skills STRING,
  languages STRING,
  hobbies STRING,
  salary STRING,
  email STRING,
  phone STRING
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://bld-tseed-workshop-output-semillero-2026-q2-z/Sebastián_Varón/';

SELECT * FROM sebasti_n_var_n.datos_usuarios;
