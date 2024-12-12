import pickle
import pandas as pd
import kagglehub

#download latest version of the file
path = kagglehub.dataset_download("vingkan/strategeion-resume-skills")

#open the resumes_development.csv
dev_data = pd.read_csv(path + '/resumes_development.csv')

# open a file, where you stored the pickled data
file = open('PARiS.pickle', 'rb')

# dump information to that file
weights = pickle.load(file)[0]

# close the file
file.close()

features = dev_data.columns[2:]

print("Feature\tWeights")
for i in range(len(weights)):
  print(f"{features[i]}:\t{weights[i]:.2f}")