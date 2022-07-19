

import arcpy
import os
import getpass


contador_ocorrencias = 0

# Funciona Solo
def criarGeometriaVazia(_referencia_espacial,_tipo_de_geometria,_diretorio_saida,_nome_saida):
    """Cria um Shape vazio para inserção de pontos."""

    arcpy.CreateFeatureclass_management(
        spatial_reference=_referencia_espacial,
        geometry_type=_tipo_de_geometria,
        out_path=_diretorio_saida,
        out_name=_nome_saida,
        )

def verificaExistenciaArquivo(caminho_completo_shapefile):
    global contador_ocorrencias
    contador_ocorrencias += 1
    caminho_completo_shapefile = "{}__{}.shp".format(caminho_completo_shapefile, str(contador_ocorrencias))

    while True:
        if not os.path.exists(caminho_completo_shapefile):
            print("Caminho nao existe: {}".format(caminho_completo_shapefile))
            return caminho_completo_shapefile
        else:
            print("Caminho ja Existe: {}".format(caminho_completo_shapefile))
            contador_ocorrencias += 1
            caminho_completo_shapefile = caminho_completo_shapefile.split('__')[0]
            caminho_completo_shapefile = "{}__{}.shp".format(caminho_completo_shapefile, str(contador_ocorrencias))
            continue





class Dados:
    diretorio_saida = 'C:\\Users\\djalma.filho\\ocorrencias'
    msg_erro = ("Erro no valor. Valor númerico não fornecido. ",
                "Valor Recebido: {0}. ",    
                "Tipo de Valor: {1}. ",)


class Projecao:
    """Retorna o EPSG da Projeção"""

    GCS_SIRGAS = 4170
    GCS_SIRGAS_2000 = 4674
    GCS_WGS_1984 = 4326
    GCS_SAD_1969_96 = 5527
    SAD_1969_UTM_Zone_21S = 29191
    SAD_1969_UTM_Zone_22S = 29192
    SAD_1969_UTM_Zone_23S = 29193
    GCS_South_American_1969 = 4618
    SAD_1969_96_UTM_Zone_21S = 5531
    SAD_1969_96_UTM_Zone_22S = 5858
    SAD_1969_96_UTM_Zone_23S = 5533
    SIRGAS_2000_UTM_Zone_21S = 31981
    SIRGAS_2000_UTM_Zone_22S = 31982
    SIRGAS_2000_UTM_Zone_23S = 31983
    South_America_Lambert_Conformal_Conic = 102015



class ReferenciaEspacial:
    """use .get para pegar o objeto"""
    @staticmethod
    def get(projecao):
        return arcpy.SpatialReference(projecao)



class TipoDeGeometria:
    ponto = "POINT"
    polilinha = "POLYLINE"
    poligono = "POLYGON"
    multiponto = "MULTIPOINT"
    multilinhas = "MULTIPATCH"



class Geometria:
    referencia_espacial = None
    tipo_de_geometria = None
    diretorio_saida = None
    nome_saida = None

    def __init__(self):
        pass

    #def setValoresGeometria(self, referencia_espacial:ReferencialEspacial, tipo_de_geometria: TipoDeGeometria, diretorio_saida: str, nome_saida: str):
    def setValoresGeometria(self, referencia_espacial, tipo_de_geometria, diretorio_saida, nome_saida):
        """São setados os valores que depois serão plotados.

        Args:
            referencia_espacial (ReferenciaEspacial(Projecao)): _description_
            diretorio_saida (str): _description_
            nome_saida (str): _description_
            tipo_de_geometria (TipoDeGeometria): _description_
        """
        self.referencia_espacial = referencia_espacial
        self.tipo_de_geometria = tipo_de_geometria
        self.diretorio_saida = diretorio_saida
        self.nome_saida = nome_saida


    def plotarCoordenadas(self, shape, latitude, longitude):
        """Plota um ponto dentro do shape

        Args:
            shape (str): caminho do shape
            latitude (float, int): Y
            longitude (float, int): X
        """
        
        # Fique "long" de "eX"
        self.shape = shape
        valores = latitude, longitude

        for val in valores:
            assert ( isinstance(val, float) or isinstance(val, int)
                ),''.join(Dados.msg_erro_01).format(val, type(val))

        # longitude = X , latitude = Y
        ponto = arcpy.Point(longitude, latitude)
        cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
        cursor.insertRow([ponto])


    def plotar(self, longEX, latNY):
                
        x = longEX
        y = latNY

        referencia_espacial = ReferenciaEspacial.get(Projecao.GCS_SIRGAS_2000)
        tipo_de_geometria = TipoDeGeometria.ponto 
        diretorio_saida = Dados.diretorio_saida
        nome_saida = 'ocorrencia'

        real_nome_saida = verificaExistenciaArquivo(os.path.join(diretorio_saida, nome_saida))
        real_nome_saida_rec = real_nome_saida.split('\\')[-1]
        print("real_nome_saida", real_nome_saida)
        # self.setValoresGeometria(referencia_espacial, tipo_de_geometria, diretorio_saida, real_nome_saida)
        criarGeometriaVazia(referencia_espacial, tipo_de_geometria, diretorio_saida, real_nome_saida_rec)
        self.plotarCoordenadas(real_nome_saida, y, x)
    




    
   
string_com_comando = str("string aqui")
nova_string_com_comando = string_com_comando.replace('\\','/')
os.system(nova_string_com_comando)
 



