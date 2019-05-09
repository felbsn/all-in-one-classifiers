


Yapay Zeka 2. Ödev
A. Bilal Güvenç 16011069 Fatih Elbasan 16011075

Veri Seti:
Dataset 3 adet sınıf içermekte  portakal , domates ,elma resimler telefon kamerası ile çektim tekli çoklu farklı poziyonlarda ve farklı arkaplanlarda örnekler aldım. Veriseti üzerinde herhagi bir boyutlandırma işlemi yapmadım , boyutlandırmayı program içerisinde yapıyorum.

Program:
Sınıflandırma için python sklearn kütüphanesini kullandım. Kendi sitesinde verilmiş olan sınıflandırma kodlarına sınıflandırmayı resim yapabilecek hale getirdim , hali hazırda 9 tane algoritmaya sahipti bu kod , 9 tanesini de örneğin içerisine koydum.
Program dataseti mevcut konumundaki ‘data’ klasörü içerisindeki klasörlere bakarak okuyor.
data/elma/ .. elma resimleri
data/portakal/ .. portakal resimleri
Gerekli Kütüphaneler
    • numpy
    • sklearn
    • skimage
    • matploplib
not: uygulamayı linux üzerinde python 3.7 ile çalıştırıyorum 

Dahil Edilen Algoritmalar<br>
 Nearest Neighbors <br>
 Linear SVM <br>
 RBF SVM <br>
 Gaussian Process <br>
 Decision Tree <br>
 Random Forest <br>
 Neural Net <br>
 AdaBoost <br>
 Naive Bayes <br>
 
Sonuçlar:<br>
Sonuçları eğitim işlemi bittikten sonra test verisinin %30 u  ile kontrol edip başarı oranlarını yazdırdım




















512x512 

Algoritma   Nearest Neighbors <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 0 0 2 2 0 2 2 1 1 2 0 0 0 0 2 0 1 0 2 0 0 1 2 2] <br>
 başarı oranı  0.6071428571428571

Algoritma   Linear SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 0 2 0 0 0 0 1 2 0 2 2 1 1 1 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   RBF SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] <br>
 başarı oranı  0.2857142857142857

Algoritma   Gaussian Process <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 2 2 1 2 2 0 0 0 0 1 2 0 2 2 0 1 0 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   Decision Tree <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 2 0 1 2 0 2 2 2 2 1 1 1 0 0 1 2 0 2 2 1 2 0 2 2] <br>
 başarı oranı  0.7142857142857143

Algoritma   Random Forest <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 1 1 0 1 2 1 2 2 1 1 2 0 0 1 1 1 2 1 1 2 1 0 1 2 2] <br>
 başarı oranı  0.5714285714285714

Algoritma   Neural Net <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
 başarı oranı  1.0

Algoritma   AdaBoost <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 1 0 1 1 1 0 1 1 1 1 1 0 1 0 0 1 1 2 1 1 1 1 2 1 1] <br>
 başarı oranı  0.5

Algoritma   Naive Bayes <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 1 1 1 2 1 2 2 1 1 1 0 0 0 0 1 2 1 1 2 1 1 1 1 2] <br>
 başarı oranı  0.6071428571428571


256x256 

Algoritma   Nearest Neighbors <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 0 0 2 2 0 2 2 1 1 2 0 0 0 0 2 0 1 0 2 0 0 1 2 2] <br>
 başarı oranı  0.6071428571428571

Algoritma   Linear SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 0 2 0 0 0 0 1 2 0 2 2 1 1 1 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   RBF SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] <br>
 başarı oranı  0.2857142857142857

Algoritma   Gaussian Process <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 2 2 1 2 2 0 0 0 0 1 2 0 2 2 0 1 0 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   Decision Tree <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 0 2 1 2 0 2 2 2 2 1 0 1 0 0 1 0 0 2 2 1 2 0 2 2] <br>
 başarı oranı  0.7142857142857143

Algoritma   Random Forest <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 1 0 1 1 0 2 1 1 1 2 0 2 0 0 1 0 1 1 2 1 1 0 1 2] <br>
 başarı oranı  0.6071428571428571

Algoritma   Neural Net <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
 başarı oranı  1.0

Algoritma   AdaBoost <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 1 2 1 1 1 0 1 1 1 1 1 0 1 0 0 1 1 2 1 1 1 1 2 1 1] <br>
 başarı oranı  0.4642857142857143

Algoritma   Naive Bayes <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 1 1 1 2 1 2 2 1 1 1 0 0 0 0 1 2 1 1 2 1 1 1 1 2] <br>
 başarı oranı  0.6071428571428571



128x128

Algoritma   Nearest Neighbors <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 0 0 2 2 0 2 2 1 1 2 0 0 0 0 2 0 1 0 2 0 0 1 2 2] <br>
 başarı oranı  0.6071428571428571

Algoritma   Linear SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 0 2 0 0 0 0 1 2 0 2 2 1 1 1 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   RBF SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] <br>
 başarı oranı  0.2857142857142857

Algoritma   Gaussian Process <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 2 2 1 2 2 0 0 0 0 1 2 0 2 2 0 1 0 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   Decision Tree <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 1 2 2 0 2 1 2 0 2 2 2 2 1 0 1 0 0 1 1 0 2 2 1 2 0 2 2] <br>
 başarı oranı  0.6785714285714286

Algoritma   Random Forest <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [2 0 2 2 2 1 1 2 2 2 1 2 1 2 0 1 0 0 0 1 1 1 2 1 2 2 2 2] <br>
 başarı oranı  0.42857142857142855

Algoritma   Neural Net <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
 başarı oranı  1.0

Algoritma   AdaBoost <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 1 0 1 1 1 0 1 1 1 1 1 1 1 0 0 1 1 2 1 1 1 1 0 1 1] <br>
 başarı oranı  0.5

Algoritma   Naive Bayes <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 1 1 1 2 1 2 2 1 1 1 0 0 0 0 1 2 1 1 2 1 1 1 1 2] <br>
 başarı oranı  0.6071428571428571



64 x 64
Algoritma   Nearest Neighbors <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 0 0 2 2 0 2 2 1 1 2 0 0 0 0 2 0 1 0 2 0 0 1 2 2] <br>
 başarı oranı  0.6071428571428571

Algoritma   Linear SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 0 2 0 0 0 0 1 2 0 2 2 1 1 1 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   RBF SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] <br>
 başarı oranı  0.2857142857142857

Algoritma   Gaussian Process <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 2 2 1 2 2 0 0 0 0 1 2 0 2 2 0 1 0 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   Decision Tree <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 1 2 2 2 2 1 2 0 2 1 2 2 1 0 1 0 0 1 2 0 2 2 1 2 0 2 1] <br>
 başarı oranı  0.6071428571428571

Algoritma   Random Forest <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 1 2 2 1 1 1 2 1 2 2 2 2 2 2 1 1 0 2 2 0 1 2 1 1 1 2 2] <br>
 başarı oranı  0.5357142857142857

Algoritma   Neural Net <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
 başarı oranı  1.0 <br>

Algoritma   AdaBoost <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 1 0 1 1 1 0 1 1 1 1 1 1 1 0 0 1 1 2 1 1 1 1 0 1 1] <br>
 başarı oranı  0.5 <br>

Algoritma   Naive Bayes <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 1 1 1 2 1 2 2 1 1 1 0 0 0 0 1 2 1 1 2 1 1 1 1 2] <br>
 başarı oranı  0.6071428571428571 <br>





32 x 32 <br>

Algoritma   Nearest Neighbors <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 0 0 2 2 0 2 2 1 1 2 0 0 0 0 2 0 1 0 2 0 0 1 2 2] <br>
 başarı oranı  0.6071428571428571

Algoritma   Linear SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 0 2 0 0 0 0 1 2 0 2 2 1 1 1 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   RBF SVM <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1] <br>
 başarı oranı  0.2857142857142857

Algoritma   Gaussian Process <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 2 2 1 2 2 0 0 0 0 1 2 0 2 2 0 1 0 2 2] <br>
 başarı oranı  0.9285714285714286

Algoritma   Decision Tree <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 1 2 2 0 2 1 2 0 2 0 2 2 1 1 1 0 0 1 2 2 2 2 1 2 0 2 2] <br>
 başarı oranı  0.6071428571428571

Algoritma   Random Forest <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 0 2 0 0 1 2 1 2 1 0 1 1 0 0 0 0 0 2 1 1 0 0 1 1 2 2] <br>
 başarı oranı  0.5357142857142857

Algoritma   Neural Net <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
 başarı oranı  1.0av

Algoritma   AdaBoost <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 1 1 2 1 1 1 0 1 1 1 1 1 0 1 0 0 1 1 2 1 1 1 1 2 1 1] <br>
 başarı oranı  0.4642857142857143

Algoritma   Naive Bayes <br>
gercek [1 0 1 2 0 0 1 2 0 1 2 1 2 2 0 0 0 0 1 2 0 2 2 1 1 0 2 2] <br>
tahmin [1 0 2 2 1 1 1 2 1 2 2 1 1 1 0 0 0 0 1 2 1 1 2 1 1 1 1 2] <br>
 başarı oranı  0.6071428571428571









Yorum:

Çözünürlük değişimi nearest neighboors ve naive bayes algoritmasında etkili olmuyor , aynı şekilde support vector machine algoritmaları da çok etkilenmiyorlar.

Seçim ağacı yüksek çözünürlükte  başarısı 0.71 iken çözünürlük düştükçe 0.60 a kadar geriliyor.

Yapay sinir ağları bir şekilde tam olarak fit oluyor tüm çözünürlüklerde , sanırım basit bir data olduğu için  sklearn optimizasyonları ile kısa sürede 1.0 a ulaşıyor.

Kütüphane İçerisinde değiştirebildiğim parameterelerde 

256x256 boyutta

Nearest Neighbors(3)		             Nearest Neighbors(10)
0.7857142857142857 	             0.6071428571428571

Algoritma   Decision Tree(depth 5)    Decision Tree(depth 10)
0.7142857142857143                         0.7142857142857143

