# default url that will grab all 300 + pantires in georgia
food_bank_url = "https://services6.arcgis.com/ROofrLhCBDcunBIf/" \
                "arcgis/rest/services/Partner_Agencies_Feb_20_2020/" \
                "FeatureServer/0/query?f=json&where=AddStatus%20%3D%20%27" \
                "Share%27&returnGeometry=true&" \
                "spatialRel=esriSpatialRelIntersects&geometry=%7B%" \
                "22xmin%22%3A-9842297.023966135%2C%22ymin%22%3A3979255.766306073%2C%" \
                "22xmax%22%3A-7494151.515046145%2C%22ymax%22%3A4117453.9134456352%2C%" \
                "22spatialReference%22%3A%7B%22wkid%22%3A102100%7D%7D&geometryType=" \
                "esriGeometryEnvelope&inSR=102100&outFields=FID%2CAgyName%2CAdd_%" \
                "2CCounty%2CTel%2CCity%2CZip_1%2CMethod&orderByFields=FID%20ASC&outSR=102100"

"""
You can change these variables to specify what area you 
want to search for food pantries and stores

x_min = "9842297.023966135"
x_max = "-7494151.515046145"
y_max = "4117453.9134456352"
y_min = "3979255.766306073"

food_bank_url = "https://services6.arcgis.com/ROofrLhCBDcunBIf/arcgis/"\
                "rest/services/Partner_Agencies_Feb_20_2020/FeatureServer/"\
                "0/query?f=json&where=AddStatus%20%3D%20%27Share%27&returnGeometry"\
                "=true&spatialRel=esriSpatialRelIntersects&geometry=%7B%22"\
                "xmin%22%3A{}%2C%22ymin%22%3A{}%2C%22xmax%22%3A{}%2C%22ymax%22%3A{}%"\
                "2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%7D%7D&geometryType="\
                "esriGeometryEnvelope&inSR=102100&outFields=FID%2CAgyName%2CAdd_%"\
                "2CCounty%2CTel%2CCity%2CZip_1%2CMethod&orderByFields=FID%20ASC&outSR="\
                "102100".format(x_min, y_min, x_max, y_max)
"""

pantry_community_kitchens = "pantries_community_kitchens.json"
