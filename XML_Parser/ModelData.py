import xml.dom.minidom


class ModelData:
    def __init__(self, filename: str):
        data = xml.dom.minidom.parse("../model_data/model_parameters/" + filename + ".xml")
        self.U_nom = float(data.getElementsByTagName("U_nom")[0].firstChild.nodeValue)
        self.f = float(data.getElementsByTagName("f")[0].firstChild.nodeValue)
        self.X = float(data.getElementsByTagName("X")[0].firstChild.nodeValue)
        self.R = float(data.getElementsByTagName("R")[0].firstChild.nodeValue)
        self.B_s = float(data.getElementsByTagName("B_s")[0].firstChild.nodeValue)
        self.B_r = float(data.getElementsByTagName("B_r")[0].firstChild.nodeValue)



