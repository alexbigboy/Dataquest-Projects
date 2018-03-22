import read
from collections import Counter

df = read.load_data()

urls = df.url

domains = urls.value_counts()


for name, row in domains[:100].items():
    print("{0}: {1}".format(name, row))
    
print(urls)