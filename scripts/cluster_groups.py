import pprint
import pandas as pd

from sklearn import cluster
from sklearn.feature_extraction.text import TfidfVectorizer

path = pd.read_csv('../data/web.csv', index_col=False, header=0)
path['experience'] = path['experience'].map(lambda x: x if type(x) != str else x.lower().strip())
path['motivation'] = path['motivation'].map(lambda x: x if type(x) != str else x.lower().strip())
path['Area'] = path['Area'].map(lambda x: x if type(x) != str else x.lower().strip())

# choose which features to use for clustering
path_simplified = path[['Area']]
# choose output shape
path_simplified_output = path[['Area', 'devoted_time', 'python', 'git', 'Email']]

# Vectorize the data
path_to_list = path_simplified.values.tolist()
v = TfidfVectorizer(tokenizer=lambda i: i, lowercase=False)
x = v.fit_transform(path_to_list)

# cluster the data (number of groups(clusters) = number of students / 5)
k_means = cluster.KMeans(n_clusters=path.shape[0]/5)
k_means.fit(x)
labels = k_means.labels_
# print(labels)

groups = {}
for i in range(len(labels)):
    if labels[i] in groups:
        groups[labels[i]].append(i)
    else:
        groups[labels[i]] = [i]

# pprint.pprint(groups)

pso = path_simplified_output.values.tolist()
groups_out = []
for k,v in groups.iteritems():
    lista = list(pso[i] for i in v)
    groups_out.append(list(pso[i] for i in v))

output_file = open('../data/groups.txt', 'w')
for groups in groups_out:
    for group in groups:
        for student in group:
            output_file.write("%s " % student)
        output_file.write("\n\n")
    output_file.write("===============================\n")