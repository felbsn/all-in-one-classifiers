
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from sklearn  import metrics
from pathlib import Path
from skimage import io 
from skimage.transform import resize
from sklearn.utils import Bunch


# read dataset 
def load_image_files(container_path, dimension=(64, 64)):

    image_dir = Path(container_path)
    folders = [directory for directory in image_dir.iterdir() if directory.is_dir()]
    categories = [fo.name for fo in folders]
    descr = "dataset"
    images = []
    flat_data = []
    target = []

    print("Dataset okunuyor...")
    for i, direc in enumerate(folders):
        for file in direc.iterdir():
            img = io.imread(file)
            img_resized = resize(img, dimension, anti_aliasing=False, mode='reflect')
            flat_data.append(img_resized.flatten()) 
            images.append(img_resized)
            target.append(i)
            print(file)
    flat_data = np.array(flat_data)
    target = np.array(target)
    images = np.array(images)
 


    return Bunch(data=flat_data,
                 target=target,
                 target_names=categories,
                 images=images,
                 DESCR=descr)



names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(max_iter=100),
    AdaBoostClassifier(),
    GaussianNB(),
    ]

# kullanılacak classifiers
enables = [
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    ]

dimensions = (64 , 64) # default
print("#" , -1 , "=> " ,"Hepsi"    );
for i , name in enumerate(names):
    print("#" , i  , " => " ,name    );



enable = int(input("Seçimi yapın :") );



if enable == -1:
    for c in range(len(enables)):
        enables[c] = True
elif enable >= 0 and enable < len(enables):
    enables[enable] = True;
else:
    print("Seçim yapılmadı")
    exit(-1)


dims = input("Boyut girin w,h : " ).split(',');
dims = (int(dims[0]) ,int(dims[1])) 

print(" Aktif :"  ,names[enable]);
print(" Boyut :" , dims)



ds = load_image_files("data" , dimensions) 



X_train, X_test, y_train, y_test = train_test_split(ds.data, ds.target, test_size=0.3,random_state=42)    
i = 0
for clf in classifiers:
    if enables[i]:
        print("\nAlgoritma  " , names[i])
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        #print("gercek" , y_test)
        #print("tahmin" , y_pred)
        num = len(y_test)
        trueCount = 0;
        for c in range(len(y_test)):
            if y_test[c] ==  y_pred[c]:
                trueCount += 1;
        print(" başarı oranı " ,  trueCount / num);
        del clf;
    i +=1






 
