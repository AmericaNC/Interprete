#!/usr/bin/env python3 
import os
import getpass
import subprocess

def menu():
    print("📦 Herramienta de Backup SSH")
    print("1. Copia completa al servidor (cifrado simetrico)")
    print("2. Enviar respaldo específico (cifrado simetrico)")
    print("3. Descargar respaldo (simetrico o asimetrico)")
    print("4. Restaurar respaldo")
    print("5. Generar llave asimétrica")
    print("6. Ver llaves asimétricas")
    print("7. Exportar llaves asimétricas")
    print("8. Importar llaves asimétricas")
    print("9. Enviar respaldo específico Asimétrico")
    print("10. Restaurar respaldo Asimétrico")
    print("11. Firmar archivo")
    print("12. Verificar firma de archivo")
    print("0. Salir")
    return input("\nSeleccione una opción: ")

def ejecutar_comando(comando):
    print(f"\n🔧 Ejecutando: {comando}\n")
    resultado = subprocess.run(comando, shell=True)
    if resultado.returncode != 0:
        print("❌ Hubo un error al ejecutar el comando.")
    else:
        print("✅ Comando ejecutado correctamente.")

def restaurar_respaldo_asimetrico():
    nombre = input("Ruta del archivo cifrado (ej. ./backups/respaldo_algo.tar.gz.gpg): ")
    destino = input("Carpeta destino (por defecto ./databases): ").strip() or "./databases"
    passphrase = getpass.getpass("Frase secreta GPG: ")

    # Ejecutar el script de restauración asimétrica en bash
    comando = f'bash ./ssh-backups/restaurar_base_asimetrico.sh "{nombre}" "{destino}" "{passphrase}"'
    ejecutar_comando(comando)

def firmar_archivo():
    archivo = input("Ruta del archivo a firmar: ")
    
    if not os.path.exists(archivo):
        print(f"❌ Error: El archivo '{archivo}' no existe.")
        return
    
    # Mostrar las claves disponibles
    print("\nClaves disponibles para firmar:")
    ejecutar_comando("gpg --list-secret-keys")
    
    correo = input("\nIngrese el correo/ID de la clave a usar para firmar: ")
    tipo_firma = input("¿Crear firma separada (s) o archivo firmado (a)? [s/a]: ").lower()
    
    if tipo_firma == "s":
        # Crear firma separada (.sig)
        archivo_firma = f"{archivo}.sig"
        comando = f'gpg --output "{archivo_firma}" --detach-sign --local-user "{correo}" "{archivo}"'
        ejecutar_comando(comando)
        if os.path.exists(archivo_firma):
            print(f"✅ Firma creada en: {archivo_firma}")
    else:
        # Crear archivo firmado (.asc) con firma en armadura ASCII
        archivo_firmado = f"{archivo}.asc"
        comando = f'gpg --output "{archivo_firmado}" --sign --armor --local-user "{correo}" "{archivo}"'
        ejecutar_comando(comando)
        if os.path.exists(archivo_firmado):
            print(f"✅ Archivo firmado creado en: {archivo_firmado}")

def verificar_firma():
    archivo = input("Ruta del archivo a verificar: ")
    
    if not os.path.exists(archivo):
        print(f"❌ Error: El archivo '{archivo}' no existe.")
        return
    
    # Determinar el tipo de verificación
    if archivo.endswith(".sig"):
        # Es una firma separada, necesitamos el archivo original
        archivo_original = archivo[:-4]  # Quitar la extensión .sig
        if not os.path.exists(archivo_original):
            archivo_original = input(f"Archivo original no encontrado. Ingrese la ruta del archivo original: ")
            if not os.path.exists(archivo_original):
                print("❌ Error: No se encontró el archivo original.")
                return
        
        comando = f'gpg --verify "{archivo}" "{archivo_original}"'
    elif archivo.endswith(".asc"):
        # Es un archivo firmado
        comando = f'gpg --verify "{archivo}"'
    else:
        # Podría ser un archivo original, buscar la firma
        archivo_firma = f"{archivo}.sig"
        if os.path.exists(archivo_firma):
            comando = f'gpg --verify "{archivo_firma}" "{archivo}"'
        else:
            print("❌ No se encontró archivo de firma. Intentando verificar directamente...")
            comando = f'gpg --verify "{archivo}"'
    
    ejecutar_comando(comando)

def main():
    while True:
        opcion = menu()

        if opcion == "1":
            ejecutar_comando("bash ./ssh-backups/enviar_bases.sh ferna /home/ferna/backups 100.64.19.50 5000")
        elif opcion == "2":
            nombre = input("Nombre del respaldo (ej. laboratorio): ")
            ejecutar_comando(f"bash ./ssh-backups/enviar_bases.sh ferna /home/ferna/backups 100.64.19.50 5000 {nombre}")
        elif opcion == "3":
            nombre = input("Nombre del archivo a descargar (ej. laboratorio.tar.gz.gpg): ")
            ruta_local = f"./backups/{nombre}"

            if os.path.exists(ruta_local):
                respuesta = input(f"⚠️ El archivo '{ruta_local}' ya existe. ¿Deseas sobrescribirlo? (s/N): ").strip().lower()
                if respuesta != "s":
                    print("🚫 Descarga cancelada.")
                    continue

            ejecutar_comando(f"bash ./ssh-backups/descargar_respaldo.sh ferna /home/ferna/backups/{nombre} 100.64.19.50")
        elif opcion == "4":
            nombre = input("Ruta del archivo cifrado (ej. ./backups/respaldo_algo.tar.gz.gpg): ")
            destino = input("Carpeta destino (por defecto ./databases): ").strip() or "./databases"
            passphrase = getpass.getpass("Frase secreta GPG: ")
            ejecutar_comando(f'bash ./ssh-backups/restaurar_base.sh "{nombre}" "{destino}" "{passphrase}"')
        elif opcion == "5":
            ejecutar_comando("gpg --full-generate-key")
        elif opcion == "6":
            ejecutar_comando("gpg -k")
        elif opcion == "7":
            ejecutar_comando("gpg --output llaves-exportadas.pub --export")
            ejecutar_comando("pwd")
        elif opcion == "8":
            ejecutar_comando("gpg --import llaves-exportadas.pub")
        
        elif opcion == "9":
            nombre = input("Nombre del respaldo (ej. laboratorio): ")
            correo = input("Correo: ")
            archivo_comprimido = f"{nombre}.tar.gz"
            ejecutar_comando(f"tar -czf {archivo_comprimido} databases/{nombre}")
            archivo_cifrado = f"{archivo_comprimido}.asc"
            comando_cifrar = f"gpg -a -r \"{correo}\" --output backups/{archivo_cifrado} --encrypt {archivo_comprimido}"
            ejecutar_comando(comando_cifrar)
            if not os.path.exists(f"backups/{archivo_cifrado}"):
                print("❌ Error: el archivo cifrado no se creó. Abortando.")
                continue
            usuario_destino = "ferna"
            ruta_remota = "/home/ferna/backups"
            host = "100.64.19.50"
            puerto = 5000  
            comando_scp = f"scp -P {puerto} backups/{archivo_cifrado} {usuario_destino}@{host}:{ruta_remota}"
            ejecutar_comando(comando_scp)
            os.remove(archivo_comprimido)
            os.remove(f"backups/{archivo_cifrado}")
            print("✅ Respaldo enviado correctamente.")

        elif opcion == "10":
            restaurar_respaldo_asimetrico()
        elif opcion == "11":
            firmar_archivo()
        elif opcion == "12":
            verificar_firma()
        elif opcion == "0":
            print("👋 Saliendo...")
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
