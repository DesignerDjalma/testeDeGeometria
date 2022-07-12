import arcpy

class TipoDeGeometria:
    ponto = "POINT"
    multiponto = "MULTIPOINT"
    poligono = "POLYGON"
    polilinha = "POLYLINE"

class ReferencialEspacial:
    sirgas2000 = 4674
    sirgas2000zona21s = 31981
    sirgas2000zona22s = 31982
    sirgas2000zona23s = 31983

class Geometria:

    referencia_espacial = None
    tipo_de_geometria = None
    diretorio_saida = None
    nome_saida = None

    def __init__(self):
        pass

    def setValoresGeometria(self, referencia_espacial:ReferencialEspacial, diretorio_saida: str, nome_saida: str, tipo_de_geometria: TipoDeGeometria):
        """São setados os valores que depois serão plotados.

        Args:
            referencia_espacial (ReferencialEspacial): _description_
            diretorio_saida (str): _description_
            nome_saida (str): _description_
            tipo_de_geometria (TipoDeGeometria): _description_
        """

        self.referencia_espacial = referencia_espacial
        self.diretorio_saida = diretorio_saida
        self.nome_saida = nome_saida
        self.tipo_de_geometria = tipo_de_geometria

    def criarGeometriaVazia(self):
        arcpy.CreateFeatureclass_management(
            spatial_reference=self.referencia_espacial,
            out_path=self.diretorio_saida,
            out_name=self.nome_saida,
            geometry_type=self.tipo_de_geometria,
            )

    def plotarCoordenadas(self, shape, latitude, longitude):
        # Fique "long" de "eX"
        valores = latitude, longitude

        for val in valores:
            assert (
                isinstance(val, float) or isinstance(val, int)
                ), ''.join(
                   ("Erro no valor. Valor númerico não fornecido. ",
                    "Valor Recebido: {0}. ",
                    "Tipo de Valor: {1}. ",)
                    ).format(
                        val, type(val)
                        )
    
        ponto = arcpy.Point(longitude, latitude)
        cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
        cursor.inserRow([ponto])