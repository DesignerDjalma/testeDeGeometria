import arcpy

import os


def escolherNome(nome_arquivo):
    nome_arquivo = nome_arquivo[:-4] + '_1'
    contador = 2
    while True:
        if os.path.exists(nome_arquivo):
            nome_arquivo = nome_arquivo.split('_')[0] + "_" + str(contador)
            contador += 1
            continue
        else:
            nome_saida = nome_arquivo + '.shp'
            return nome_saida


class Projecao:
    """Retorna o EPSG da Projecao"""

    GCS_SIRGAS_2000 = 4674
    GCS_SIRGAS = 4170
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

    def criarGeometriaVazia(self):
        """Cria um Shape vazio para inserção de pontos."""

        arcpy.CreateFeatureclass_management(
            spatial_reference=self.referencia_espacial,
            out_path=self.diretorio_saida,
            out_name=self.nome_saida,
            geometry_type=self.tipo_de_geometria,
            )

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
                ),''.join(("Erro no valor. Valor númerico não fornecido. ",
                            "Valor Recebido: {0}. ",
                            "Tipo de Valor: {1}. ",)).format(val, type(val))

        # longitude = X , latitude = Y
        ponto = arcpy.Point(longitude, latitude)
        cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
        cursor.insertRow([ponto])


    def testeGeral(self):
                
        referencia_espacial = ReferenciaEspacial.get(Projecao.GCS_SIRGAS_2000)
        tipo_de_geometria = TipoDeGeometria.ponto 
        diretorio_saida = r'C:\Users\djalma.filho\repositorios\plotagem-de-pontos-ocorrencia\outputShapes'
        nome_saida = escolherNome('ocorrencia')

        self.setValoresGeometria(referencia_espacial, tipo_de_geometria, diretorio_saida, nome_saida)
        self.criarGeometriaVazia()
        self.plotarCoordenadas(r"C:\Users\djalma.filho\repositorios\plotagem-de-pontos-ocorrencia\outputShapes\novo_automatico.shp", -2.279, -48.288)







            