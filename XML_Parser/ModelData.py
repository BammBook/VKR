import xml.dom.minidom


class ModelData:
    def __init__(self, filename):
        data = xml.dom.minidom.parse("../model_data/model_parameters/" + filename + ".xml")
        self.U_nom = data.getElementsByTagName("U_nom")[0].firstChild.nodeValue
        self.X = data.getElementsByTagName("X")[0].firstChild.nodeValue
        self.R = data.getElementsByTagName("R")[0].firstChild.nodeValue



