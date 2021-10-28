# priority-queue
Sorun: Elimizde saniyede 1 fatura işleyebilen bir sunucu vardur. Burada sorun az fatura yollamış müşterilerin çok fatura yollayanları beklemesiyle ortalama bekleme süresinin artmasıdır. Yoğunluk azalsın diye her müşterinin önüne kendi faturası kadar arkasındakilerden fatura eklenebilir çözümü üretilmiştir. Örneğin:
Server<---Ali15 Ahmet1000
Server<---Ali15 Mert850 Ahmet1000 (Burada Hakan 250 fatura yolladığı zaman mert yoğunluğun azalması için ordan çıkarılıp arkaya koyulmalıdır.) 
Server<---Ali15 Hakan250 Ahmet1000 Mert850
Server<---Ali15 Fatma249 Hakan250 Ahmet1000 Mert850
Server<---Ali15 Fatma249 Hakan250 Ahmet1000 Mert850 Samet355 (Samet girebilecek bir yer bulamadığı için en arkaya atılmıştır.)
Server<---Ali15 Kamil248 Hakan250 Fatma249 Ahmet1000 Mert850 Samet355
Server<---Selim3 Ali15 Hakan250 Fatma249 Kamil248 Ahmet1000 Mert850 Samet355(En öne Selim geldiği zaman Hakan ve Fatma'nın önüne kendi faturalarından çok sonradan gelenlerin faturası gelmiş oluyor. Kamil zaten Fatma ve Hakan'dan sonra geldiği için arkalarına geçmelidir.)

