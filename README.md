# Intérprete SQL ESPAÑOL

```
  ___      ___   __    _____  ___    _______  
 |"  \    /"  | |" \  (\"   \|"  \  /"     "| 
  \   \  //   | ||  | |.\\   \    |(: ______) 
  /\\  \/.    | |:  | |: \.   \\  | \/    |          へ♡ ╱|-`♡´-   
 |: \.        | |.  | |.  \    \. | // ___)_    ૮  >  <) (˚ˎ 。7  ִ ࣪𖤐
 |.  \    /:  | /\  |\|    \    \ |(:      "|   /  ⁻  ៸|  |、˜〵   
 |___|\__/|___|(__\_|_)\___|\____\) \_______) 乀(ˍ, ل ل  じしˍ,)ノ⁠♡
 
 MinervaSQL - Intérprete SQL en Español v1.0
```

## 🚀 Cómo Ejecutarlo
```sh
python main.py
```

## Secuencias Actuales
Éstas son las instrucciones reconocidas por el motor (ejemplos que pueden copiarse y probarse, no estrictamente la estructura lógica de las instrucciones, ésta se encuentra en HELP)

```sql
SELECCIONA HR, TEMP DESDE datos;
```
```sql
SELECCIONA * DESDE datos;
```
```sql
INSERTAR EN datos VALORES (130, 39);
```
```sql
INSERTAR EN datos (HR, TEMP) VALORES (100, 37.1);
```
```sql
ACTUALIZAR datos CON HR = 95 DONDE TEMP = 36.5;
```
```sql
BORRAR DE datos DONDE HR EQ 90;
```
```sql
DESHACER datos;
```
```sql
CONTAR DESDE datos;
```
```sql
CREAR TABLA pacientes (ID, NOMBRE, EDAD);
```
```sql
USAR BASE datos;
```
```sql
CREAR BASE laboratorio;
```
```sql
CREAR USUARIO fernando PARA 1234
```
```sql
LOGIN fernando PARA 1234
```
```sql
ELIMINAR USUARIO fernando
```
```sql
MOSTRAR BASES
```
```sql
MOSTRAR TABLAS
```
```sql
MOSTRAR USUARIOS
```
```sql
USUARIO_ACTUAL;
```
```sql
ELIMINAR BASE oficina;
```
```sql
BASE_ACTUAL;
```
```sql
HELP
```
```sql
SALIR
```
```sql
MODO DEPURACION
```
## Permisos
```sql
OTORGAR ver_bases A fernando;
```
```sql
OTORGAR otorgar A fernando;
```
```sql
OTORGAR ver_tablas A fernando;
```
```sql
OTORGAR insertar A fernando;
```
```sql
OTORGAR usar_base A fernando;
```
```sql
OTORGAR ver_usuarios A fernando;
```
```sql
OTORGAR crear_base A fernando;
```
```sql
OTORGAR actualizar A fernando;
```
```sql
OTORGAR contar A fernando;
```
```sql
OTORGAR eliminar A fernando;
```
```sql
OTORGAR crear_tabla A fernando;
```
```sql
OTORGAR eliminar_tabla A fernando;
```
## Explicación

La siguiente tabla da una breve decripción de los permisos que se pueden asignar a los usuarios.
| Permiso | Descripción |
|---------|-------------|
| ver_bases | Listar todas las bases de datos |
| otorgar | Asignar permisos a usuarios |
| ver_tablas | Mostrar tablas de una base |
| insertar | Añadir nuevos registros |
| usar_base | Seleccionar una base para trabajar |
| ver_usuarios | Listar usuarios existentes |
| crear_base | Crear nuevas bases de datos |
| actualizar | Modificar registros existentes |
| contar | Obtener cantidad de registros |
| eliminar | Borrar registros |
| crear_tabla | Crear nuevas tablas |
| eliminar_tabla | Eliminar tablas existentes |

## Léxico Actual
```python
TOKEN_PATTERNS = [
    (r'\bSELECCIONA\b', 'SELECCIONA'),
    (r'\bBORRAR\b', 'ELIMINAR'),
    (r'\bDESDE\b', 'DESDE'),
    (r'\bDONDE\b', 'DONDE'),
    (r'\bINSERTAR\b', 'INSERT'),
    (r'\bEN\b', 'INTO'),  
    (r'\bUSUARIO_ACTUAL\b', 'CURRENT_USER'),
    (r'\bBASE_ACTUAL\b', 'CURRENT_DATABASE'),
    (r'\bVALORES\b', 'VALUES'),  
    (r'\bUSAR\b', 'USE'),
    (r'\bBASE\b', 'DATABASE'),
    (r'\bBASES\b', 'DATABASES'),
    (r'\bMOSTRAR\b', 'SHOW'),
    (r'\bOTORGAR\b', 'GRANT'),
    (r'\bA\b', 'TO'),
    (r'\bMOSTRAR\b', 'MOSTRAR'),
    (r'\bTABLAS\b', 'TABLES'),
    (r'\bUSUARIO\b', 'USER'),
    (r'\bPARA\b', 'WITH'),
    (r'\bCREAR\b', 'CREATE'),
    (r'\bLOGIN\b', 'LOGIN'),
    (r'\bUSUARIO\b', 'USUARIO'),
    (r'\bUSUARIOS\b', 'USUARIOS'),
    (r'\bACTUALIZAR\b', 'ACTUALIZAR'),  
    (r'\bCREAR\b', 'CREATE'),
    (r'\bCON\b', 'SET'),
    (r'\bTABLA\b', 'TABLE'),
    (r'\bDESHACER\b', 'DESHACER'),
    (r'\bELIMINAR\b', 'DELETE'),
    (r'\bDE\b', 'FROM'),
    (r'\bCONTAR\b', 'COUNT'),
    (r'\bEQ\b', '='),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
    (r'\d+\.\d+', 'FLOAT'),
    (r'\d+', 'NUMBER'),  # Asegura que los valores flotantes también se manejen
    (r"\*", "ASTERISK"),
    (r'>', 'GT'),
    (r'<', 'LT'),
    (r'=', 'EQ'),
    (r',', 'COMMA'),
    (r';', 'SEMICOLON'),
    (r'\(', 'PARIZQ'),
    (r'\)', 'PARDER'),
    (r'(".*?"|\'.*?\')', 'STRING'),
    (r'\s+', None)  # Espacios en blanco que se ignoran
]

```
## A considerar
Interprete basado en SQL Español.
Algunas reglas y aspectos relevantes:

1. Consultas Avanzadas
 - Las operaciones como PROMEDIO, SUMA y otras funciones de agregación se gestionan a través de código externo al motor del gestor. Esto permite una mayor modularidad y flexibilidad en la implementación de funciones avanzadas.

2. Tipos de Datos Admitidos
 - Durante las operaciones de inserción, los tipos de datos reconocidos por el sistema son los siguientes:
FLOAT, INT, STRING

3. Gestión de Usuarios
 - La eliminación de usuarios no se realiza mediante comandos directos en el sistema. Esta debe efectuarse manualmente desde el archivo de control correspondiente.
 - El usuario root es generado automáticamente al realizar el primer inicio de sesión del sistema.
 - El usuario root no puede ser eliminado bajo ninguna circunstancia.
 - Este usuario posee privilegios administrativos y tiene asignados todos los permisos disponibles en el sistema.

4. Estructura de Archivos
 - Todos los archivos de base de datos se almacenan en el directorio denominado database.
 - Las bases de datos son generadas y gestionadas utilizando el formato de archivo con extensión .json.

5. Depuración del Sistema
 - El gestor incorpora un motor de depuración propio, accesible mediante la instrucción MODO DEPURACION.
 - Esta instrucción actúa como un interruptor, es decir, activa o desactiva el modo de depuración en función del estado actual del sistema.
 - El modo de depuración proporciona explicaciones detalladas en texto plano, facilitando el rastreo de errores y el análisis de comportamiento interno del gestor.

6. Reglas del Lenguaje
 - El sistema es sensible a mayúsculas y minúsculas (case-sensitive), tanto en nombres de entidades como en comandos.
 - Todas las palabras reservadas deben ser escritas exclusivamente en mayúsculas.
 - El uso del carácter ; al final de las instrucciones es opcional. Sin embargo, se recomienda su uso en aquellos comandos que estén destinados a mantener un estado persistente o que se ejecuten de forma secuencial.

7. Gestión de Permisos
 - No existe una instrucción específica para revocar permisos a un usuario.
 - La única manera de modificar los permisos asignados es directamente desde el archivo de configuración .json correspondiente al sistema.

## Respaldos cifrados SSH 
El proceso para crear respaldos de las bases de datos es el siguiente.

Para usar el respaldo por medio de ssh es necesario establecer una clave para ejecutar los scripts. Dicha clave se generara con el uso del siguiente comando.

```sh
ssh-keygen -t rsa -b 4096 -C "usuario@ip_usuario"
```
Tanto la ruta como la passphrase se recomienda dejar en default. Despues de creada la llave, se copia al servidor. Si se tiene un puerto diferente del 22, debe especificarse con -p y ser el mismo que el servidor escucha.
```sh
ssh-copy-id -p 5000 servidor@ip_servidor
```
Para comenzar con el uso de los comandos, deben darse permisos de ejecucion **como comando** a los scripts dentro de la carpeta ssh-backup.

```sh
chmod +x ssh-backups/descargar_respaldo.sh
```
```sh
chmod +x ssh-backups/enviar_bases.sh
```
```sh
chmod +x ssh-backups/restaurar_base.sh
```
### Comandos para el BACKUP
Para realizar una copia de seguridad de todas las bases de datos comprimida y encriptada en el servidor :
```sh
./ssh-backups/enviar_bases.sh servidor /home/servidor/backups
```

Para realizar una copia de seguridad de una base de datos especifica comprimida y encriptada en el servidor.
```sh
./ssh-backups/enviar_bases.sh servidor /home/servidor/backups "" "" "" nombre_base
```

En caso de querer descargar (no restaura inmediatamente, unicamente descarga) una base de datos desde el servidor a la carpeta backups:
```sh
./ssh-backups/descargar_respaldo.sh ferna /home/ferna/backups/laboratorio.tar.gz.gpg localhost ./backups/respaldo_recibido
```
Para restaurar una base de datos en el sistema desde la carpeta backups:
```sh
 ./ssh-backups/restaurar_base.sh ./backups/respaldo_recibido ./databases
```

## Ejemplo de los resultados esperados
NOTA: Por cuestiones de seguridad, se pedira clave en cada operacion. A continuacion se muestra la ejecucion esperada de los scripts.

```sh
usuario@CLIENTE:~$ cd biometric_interpreter
usuario@CLIENTE:~/biometric_interpreter$ ./ssh-backups/enviar_bases.sh servidor /home/servidor/backups
⏳ Empaquetando base de datos: default
🔐 Cifrando default.tar.gz
🚀 Enviando default.tar.gz.gpg a servidor@ip_servidor:/home/servidor/backups usando llave ~/.ssh/id_rsa
default.tar.gz.gpg                                                        100%  192   106.5KB/s   00:00
🧹 Limpiando archivos temporales
✅ Base default procesada.
⏳ Empaquetando base de datos: laboratorio
🔐 Cifrando laboratorio.tar.gz
🚀 Enviando laboratorio.tar.gz.gpg a servidor@ip_servidor:/home/servidor/backups usando llave ~/.ssh/id_rsa
laboratorio.tar.gz.gpg                                                    100%  386   480.7KB/s   00:00
🧹 Limpiando archivos temporales
✅ Base laboratorio procesada.
usuario@CLIENTE:~/biometric_interpreter$ ./ssh-backups/enviar_bases.sh servidor /home/servidor/backups "" "" "" laboratorio
⏳ Empaquetando base de datos: laboratorio
🔐 Cifrando laboratorio.tar.gz
🚀 Enviando laboratorio.tar.gz.gpg a servidor@ip_servidor:/home/servidor/backups usando llave ~/.ssh/id_rsa
laboratorio.tar.gz.gpg                                                    100%  386   224.9KB/s   00:00
🧹 Limpiando archivos temporales
✅ Base laboratorio procesada.
usuario@CLIENTE:~/biometric_interpreter$ ./ssh-backups/descargar_respaldo.sh servidor /home/servidor/backups/laboratorio.tar.gz.gpg host ./backups/respaldo_recibido
📥 Descargando /home/servidor/backups/laboratorio.tar.gz.gpg desde servidor@ip_servidor:5000 a ./backups/respaldo_recibido...
laboratorio.tar.gz.gpg                                                    100%  386   183.9KB/s   00:00
✅ Descarga completada.
usuario@CLIENTE:~/biometric_interpreter$  ./ssh-backups/restaurar_base.sh ./backups/respaldo_recibido ./databases
🔓 Descifrando ./backups/respaldo_recibido...
gpg: AES256.CFB encrypted data
gpg: encrypted with 1 passphrase
📦 Extrayendo ./backups/respaldo_recibido en ./databases...
🧹 Eliminando temporal: ./backups/respaldo_recibido
✅ Restauración completada en ./databases

```

## Árbol sintáctico

```mermaid
graph TD
    ROOT[RAÍZ] --> SELECT
    ROOT --> INSERT
    ROOT --> UPDATE
    ROOT --> DELETE
    ROOT --> UNDO
    ROOT --> COUNT
    ROOT --> CREATE_TABLE
    ROOT --> USE_DB
    ROOT --> CREATE_DB
    ROOT --> CREATE_USER
    ROOT --> LOGIN
    ROOT --> DROP_USER
    ROOT --> SHOW
    ROOT --> CURRENT
    ROOT --> DROP_DB
    ROOT --> HELP
    ROOT --> EXIT
    ROOT --> DEBUG
    ROOT --> GRANT

    %% SELECT
    SELECT --> SELECT_COLUMNS
    SELECT_COLUMNS -->|"SELECCIONA"| COL_LIST
    SELECT_COLUMNS -->|"DESDE"| TABLE_NAME
    SELECT --> SELECT_ALL
    SELECT_ALL -->|"SELECCIONA *"| ASTERISK
    SELECT_ALL -->|"DESDE"| TABLE_NAME_ALL

    %% INSERT
    INSERT --> INSERT_VALUES
    INSERT_VALUES -->|"INSERTAR EN"| TABLE_NAME_INSERT
    INSERT_VALUES -->|"VALORES"| VALUE_LIST
    INSERT --> INSERT_COLUMNS
    INSERT_COLUMNS -->|"INSERTAR EN"| TABLE_NAME_INSERT_COLS
    INSERT_COLUMNS -->|"("| COLUMN_LIST
    INSERT_COLUMNS -->|"VALORES"| VALUE_LIST_COLS

    %% UPDATE
    UPDATE -->|"ACTUALIZAR"| TABLE_UPDATE
    UPDATE -->|"CON"| SET_CLAUSE
    UPDATE -->|"DONDE"| WHERE_COND_UPDATE

    %% DELETE
    DELETE -->|"BORRAR DE"| TABLE_DELETE
    DELETE -->|"DONDE"| WHERE_COND_DELETE

    %% UNDO
    UNDO -->|"DESHACER"| UNDO_TABLE

    %% COUNT
    COUNT -->|"CONTAR"| COUNT_TARGET
    COUNT -->|"DESDE"| COUNT_SOURCE

    %% CREATE TABLE
    CREATE_TABLE -->|"CREAR TABLA"| TABLE_NAME_CREATE
    CREATE_TABLE -->|"("| TABLE_COLS

    %% USE DB
    USE_DB -->|"USAR BASE"| DB_NAME_USE

    %% CREATE DB
    CREATE_DB -->|"CREAR BASE"| DB_NAME_CREATE

    %% CREATE USER
    CREATE_USER -->|"CREAR USUARIO"| USER_NAME
    CREATE_USER -->|"PARA"| USER_PASS

    %% LOGIN
    LOGIN -->|"LOGIN"| LOGIN_USER
    LOGIN -->|"PARA"| LOGIN_PASS

    %% DROP USER
    DROP_USER -->|"ELIMINAR USUARIO"| DROP_USER_NAME

    %% SHOW
    SHOW --> SHOW_DBS
    SHOW_DBS -->|"MOSTRAR BASES"| CMD_SHOW_DB
    SHOW --> SHOW_TABLES
    SHOW_TABLES -->|"MOSTRAR TABLAS"| CMD_SHOW_TABLES
    SHOW --> SHOW_USERS
    SHOW_USERS -->|"MOSTRAR USUARIOS"| CMD_SHOW_USERS

    %% CURRENT
    CURRENT --> CURRENT_USER
    CURRENT_USER -->|"USUARIO_ACTUAL"| CMD_CURRENT_USER
    CURRENT --> CURRENT_DB
    CURRENT_DB -->|"BASE_ACTUAL"| CMD_CURRENT_DB

    %% DROP DB
    DROP_DB -->|"ELIMINAR BASE"| DROP_DB_NAME

    %% HELP
    HELP -->|"HELP"| HELP_CMD

    %% EXIT
    EXIT -->|"SALIR"| EXIT_CMD

    %% DEBUG
    DEBUG -->|"MODO DEPURACION"| DEBUG_CMD

    %% GRANT
    GRANT --> GRANT_INSTR
    GRANT_INSTR -->|"OTORGAR"| PERMISSION_NAME
    GRANT_INSTR -->|"A"| USER_GRANT

    %% PERMISSION_LIST
    PERMISSION_NAME --> ver_bases
    PERMISSION_NAME --> otorgar
    PERMISSION_NAME --> ver_tablas
    PERMISSION_NAME --> insertar
    PERMISSION_NAME --> usar_base
    PERMISSION_NAME --> ver_usuarios
    PERMISSION_NAME --> crear_base
    PERMISSION_NAME --> actualizar
    PERMISSION_NAME --> contar
    PERMISSION_NAME --> eliminar
    PERMISSION_NAME --> crear_tabla
    PERMISSION_NAME --> eliminar_tabla
```
    
