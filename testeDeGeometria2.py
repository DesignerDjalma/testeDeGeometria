

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


def verificaExistenciaDePasta(caminho_da_pasta):
    """Verifica se a pasta foi criada, se não ele cria."""
    if not os.path.exists(caminho_da_pasta):
        os.mkdir(caminho_da_pasta)
    else:
        pass




def verificaExistenciaArquivo(caminho_completo_shapefile):
    global contador_ocorrencias
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
    diretorio_saida = 'C:\\Users\\{}\\ocorrencias'.format(getpass.getuser())
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

        verificaExistenciaDePasta(diretorio_saida)
        real_nome_saida = verificaExistenciaArquivo(os.path.join(diretorio_saida, nome_saida))
        real_nome_saida_rec = real_nome_saida.split('\\')[-1]
        print("real_nome_saida", real_nome_saida)
        # self.setValoresGeometria(referencia_espacial, tipo_de_geometria, diretorio_saida, real_nome_saida)
        criarGeometriaVazia(referencia_espacial, tipo_de_geometria, diretorio_saida, real_nome_saida_rec)
        self.plotarCoordenadas(real_nome_saida, y, x)
    
    def plotarXY(self, longEX, latNY):
                
        x = longEX
        y = latNY

        referencia_espacial = ReferenciaEspacial.get(Projecao.GCS_SIRGAS_2000)
        tipo_de_geometria = TipoDeGeometria.ponto 
        diretorio_saida = Dados.diretorio_saida
        nome_saida = 'ocorrencia'

        verificaExistenciaDePasta(diretorio_saida)
        real_nome_saida = verificaExistenciaArquivo(os.path.join(diretorio_saida, nome_saida))
        real_nome_saida_rec = real_nome_saida.split('\\')[-1]
        print("real_nome_saida", real_nome_saida)
        # self.setValoresGeometria(referencia_espacial, tipo_de_geometria, diretorio_saida, real_nome_saida)
        criarGeometriaVazia(referencia_espacial, tipo_de_geometria, diretorio_saida, real_nome_saida_rec)
        self.plotarCoordenadas(real_nome_saida, y, x)
    
    def plotarYX(self, latNY, longEX, projecao):
                
        x = longEX
        y = latNY

        referencia_espacial = ReferenciaEspacial.get(projecao) 
        tipo_de_geometria = TipoDeGeometria.ponto  
        diretorio_saida = Dados.diretorio_saida
        nome_saida = 'ocorrencia'

        verificaExistenciaDePasta(diretorio_saida)
        real_nome_saida = verificaExistenciaArquivo(os.path.join(diretorio_saida, nome_saida))
        real_nome_saida_rec = real_nome_saida.split('\\')[-1]
        print("real_nome_saida", real_nome_saida)
        # self.setValoresGeometria(referencia_espacial, tipo_de_geometria, diretorio_saida, real_nome_saida)
        criarGeometriaVazia(referencia_espacial, tipo_de_geometria, diretorio_saida, real_nome_saida_rec)
        self.plotarCoordenadas(real_nome_saida, y, x)
    


def calcularCoordenadas(camada_a_se_calcular):
    arcpy.management.CalculateGeometryAttributes()


# copiar shapes
def copiar_shapes(camada_a_ser_copiada, camada_alvo):
    """Copia um shape e cola dentro do outro."""

    camada_a_ser_copiada = camada_por_nome(camada_a_ser_copiada)
    camada_alvo = camada_por_nome(camada_alvo)
    camada_alvo = arcpy.da.InsertCursor(camada_alvo, ["SHAPE@"])

    with arcpy.da.SearchCursor(camada_a_ser_copiada, ["SHAPE@"]) as cursor:
        for shape in cursor:
            camada_alvo.insertRow(shape)  

    arcpy.RefreshActiveView()



def camada_por_nome(nome_da_camada):
    mxd = arcpy.mapping.MapDocument("current")
    cmds = arcpy.mapping.ListLayers(mxd) # cmds = camadas

    # cmds_nome = {} # dicionario vazio, iniciando loop com for
    # for i in cmds:
    #     cmds_nome[i.name] = i
    #     # i.name retorna nome da camada (string)
    #     # i é a propria camada (objeto)

    cmds_nome = { i.name:i for i in cmds } # mesma coisa do que o de cima, mas em uma linha dict comprehension ;)
    return cmds_nome[nome_da_camada]

    


def adiciona_multipontos(lista_de_pontos_quadro, shape_a_adicionar):
    """Pega a lista que é gerada do quadro e tranforma em multipontos"""

    # A list of features and coordinate pairs
    # feature_info = [
    #     [ [1, 2], [2, 4], [3, 7] ],  # lista de pontos = 1 feature
    #     [ [6, 8], [5, 7], [7, 2], [9, 5] ], # lista de pontos = 1 feature
    #     ] # a lista maior # 

    # primeiro formata os pontos para o formato adequado
    ldc = lista_de_pontos_quadro
    l_ldc = ldc.split(';')
    l_l_ldc = [ i.split(' ')[1:] for i in l_ldc ]

    for j in range(2):
        for i in range(len(l_l_ldc)):
            l_l_ldc[i][j] = float(l_l_ldc[i][j])

    # A list that will hold each of the Multipoint objects
    features_multipontos = []

    # bug correction
    for feature in [l_l_ldc]:
        # Create a Multipoint object based on the array of points
        # Append to the list of Multipoint objects
        features_multipontos.append(
            arcpy.Multipoint(
                arcpy.Array(
                    [ arcpy.Point(*coords) for coords in feature ]
                )
            )
        )
    cursor = arcpy.da.InsertCursor(shape_a_adicionar, ["SHAPE@"])
    cursor.insertRow([features_multipontos])

    # cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
    # cursor.insertRow([ponto])
<<<<<<< HEAD

=======
>>>>>>> 5a3061040778303c0d095df40ef221d5bb134d75
    print("features_multipontos")
    print(features_multipontos)
    print("l_l_ldc")
    print(l_l_ldc)
    









   
string_com_comando = str("string aqui")
nova_string_com_comando = string_com_comando.replace('\\','/')
os.system(nova_string_com_comando)
 



# if __name__ == "__main__":
#     g = Geometria()
#     g.plotarYX(-4.123,-44.123, Projecao.GCS_SIRGAS_2000)