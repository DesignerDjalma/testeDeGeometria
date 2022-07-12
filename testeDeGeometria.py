
class Geometria:

    """Geometria(caminho_coordenadas, caminho_shape, tipo_geometria, epsg, plotar)
    
    Inseri um conjunto de Coordenadas apartir de um arquivo .txt
    em um Shape.
    """

    def __init__(self, caminho_coordenadas, caminho_shape, tipo_geometria, epsg, plotar=False):
        self.caminho_coordenadas = caminho_coordenadas
        self.caminho_shape = caminho_shape
        self.tipo_geometria = tipo_geometria
        self.epsg = epsg

        if plotar:
            self.plotar()

    @staticmethod
    def _lerArquivo(caminho_arquivo):
        """Le o arquivos com as coordenadas em formato x,y.

        Args:
            caminho_arquivo (str): caminho contendo o arquivo .txt.

        Returns:
            str: String contendo as coordenadas pseudo-formatadas
        """
        with open(caminho_arquivo, 'r') as f:
            coordenadas = f.read()
            return coordenadas

    @staticmethod
    def _criarGeometriaVazia(caminho_salvar, tipo_geometria, EPSG=4674):
        """Cria uma geometria do tipo POINT vazio.

        Args:
            caminho_salvar (str): caminho no qual o .shp sera salvo
            tipo_geometria (str): "POINT", "POLYLINE" ou "POLYGON".
            EPSG (int, optional): Projecao do Shape. Padrao 4674 SIRGAS 2000.

        Returns:
            str: caminho no qual o .shp foi salvo
        """
        arcpy.CreateFeatureclass_management(
            spatial_reference=arcpy.SpatialReference(EPSG),
            out_path=os.path.dirname(caminho_salvar),
            out_name=os.path.basename(caminho_salvar),
            geometry_type=tipo_geometria,
        )
        return caminho_salvar

    def _plotarCoordenadas(self, coordenadas, shape):
        """Formata as coordenadas e ensira pra cada ponto uma linha na TDA do .shp

        Args:
            coordenadas (str): coordenadas pseudo-formatadas
            shape (str): Caminho do .shp que sera inserida coordenadas
        """
        def _ponto():
            cc = coordenadas.split('\n')
            cc.pop()
            for i in cc:
                xey = i.split(',')
                x, y = float(xey[0]), float(xey[1])
                p = arcpy.Point(x,y)
                cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
                cursor.insertRow([p])

        def _poligono():
            cc = coordenadas.split('\n')
            cc.pop()
            lista = []
            for i in cc:
                xey = i.split(',')
                x, y = float(xey[0]), float(xey[1])
                p = arcpy.Point(x,y)
                lista.append(p)
            array = arcpy.Array(items=lista)
            poligono = arcpy.Polygon(array)
            cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
            cursor.insertRow([poligono])

        if self.tipo_geometria == "POINT":
            _ponto()
        if self.tipo_geometria == "POLYGON":
            _poligono()
            
    def plotar(self):
        """Faz os procedimentos necessarios."""
        
        coordenadas = self._lerArquivo(
            caminho_arquivo=self.caminho_coordenadas)

        shape = self._criarGeometriaVazia(
            caminho_salvar=self.caminho_shape,
            tipo_geometria=self.tipo_geometria,
            EPSG=self.epsg)
        
        
        self._plotarCoordenadas(
            coordenadas=coordenadas,
            shape=shape)

