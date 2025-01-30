from pandas import pandas

f = pandas.read_csv("https://docs.google.com/spreadsheets/d/1n8n1yBekzmYfzdffakw3G_NYtv4IaJaBewXG2KnnPjo/edit?gid=578062115#gid=578062115")
data = f.head();
print(data)