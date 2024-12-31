"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    #Abrir archivo
    archivo = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";",encoding='utf-8', index_col=0 )

    #Nulos
    archivo.isna().sum()
    df = archivo.dropna()

    #df["barrio"].info()
    df['barrio'] = df['barrio'].astype(str)
    df['barrio'] = df['barrio'].str.replace('_', ' ').str.replace('-', ' ')
    df['barrio'] = df['barrio'].str.lower()
    df['barrio'] = df['barrio'].str.replace(r'no\.\s*(\d+)', r'no\1', regex=True)
    
    #df["comuna_ciudadano].info()
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)

    #df["estrato"].info()
    df['estrato'] = df['estrato'].astype(int)

    #df["fecha_de_beneficio"].info()
    def formato(fecha):
        try:
            return pd.to_datetime(fecha, format='%Y/%m/%d')
        except ValueError:
            return pd.to_datetime(fecha, format='%d/%m/%Y')

    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(formato)

    #df["idea_negocio"].info()
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ').str.replace('-', ' ')
    df['idea_negocio'] = df['idea_negocio'].str.lower().str.strip()

    #df["línea_credito"].info()
    df['línea_credito'] = df['línea_credito'].str.replace('-', ' ').str.replace('_', ' ')
    df['línea_credito'] = df['línea_credito'].str.lower().str.strip()

    df['monto_del_credito'] = df['monto_del_credito'].replace({'\$': '', ',': '', ' ': ''}, regex=True)
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)

    df['sexo'] = df['sexo'].str.lower().str.strip()

    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().str.strip()

    #eliminar duplicados
    df = df.drop_duplicates()

    #Carpeta salida
    if not os.path.exists('files/output/'):
        os.makedirs('files/output/', exist_ok=True)

    #salvar
    df.to_csv('files/output/solicitudes_de_credito.csv', index=False, sep=';')

if __name__ == '__main__':
    print(pregunta_01())



    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
