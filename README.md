# Problem Var
Bu Python programı, kullanıcıların bilgisayar başında olmadıkları zamanlarda, bilgisayarlarına başkalarının müdahale edip etmediğini öğrenmelerini sağlar. Program, belirli aralıklarla hem görüntü hem de ses kaydı alır. Bu sayede, bilgisayarınızda kimlerin müdahale ettiğini tespit edebilir ve kaydedilen ses ve görüntü dosyalarını inceleyerek başkalarının bilgisayarınıza izinsiz erişip erişmediğini öğrenebilirsiniz.

Özellikler
- **Görüntü Kaydı**: Program, belirli aralıklarla kameradan görüntü alır ve kaydeder.
- **Ses Kaydı**: Program, belirli bir süre boyunca ses kaydı yapar ve kaydeder.
- **Ayrı Thread'lerde Çalışma**: Görüntü ve ses kaydı işlemleri aynı anda çalışır.
- **Esnek Konfigürasyon**: Ses kaydı ve görüntü kaydına dair parametreleri ihtiyacınıza göre değiştirebilirsiniz.

## Kurulum
Bu projeyi kullanabilmek için bazı Python kütüphanelerini kurmanız gerekmektedir. Gereksinimleri kurmak için aşağıdaki adımları takip edebilirsiniz.
### **1.** Gereksinimler
- Python 3.x
- `pyaudio` (ses kaydı için)
- `opencv-python` (görüntü kaydı için)

### **2.** Kütüphanelerin Kurulumu
Gereksinimlerinizi aşağıdaki komutları kullanarak kurabilirsiniz:

   ```bash
pip install pyaudio opencv-python
   ``` 
Eğer `pyaudio` kurulumu sırasında sorun yaşarsanız, platformunuza uygun bir şekilde yükleyebilirsiniz. Örneğin, Windows kullanıyorsanız, şu komutu kullanabilirsiniz:
   
```bash
 pip install pipwin
 pipwin install pyaudio
 ```
## Konfigürasyon

Programda, ses ve görüntü kaydını özelleştirebileceğiniz bazı önemli parametreler bulunmaktadır. Aşağıda, her parametreyi açıklıyoruz:

 ### Ses Kaydı Parametreleri
- **CHANNELS**: Ses kaydında kaç kanal kullanılacağını belirtir. `1` mono, `2` stereo ses kaydı sağlar. Varsayılan değer: `2`.
- **SAMPLE_RATE**: Ses kaydının örnekleme hızı. `48000` örnekleme hızı genellikle kaliteli ses kaydı için uygun bir değerdir. Varsayılan değer: `48000`.
- **FORMAT**: Ses kaydının formatı. `pyaudio.paInt16` genellikle yaygın olarak kullanılan ve ses kaydına uygun bir formattır.
- **CHUNK_SIZE**: Ses kaydının parça boyutu, her bir okunan ses verisi bloğunun boyutudur. Varsayılan değer: `1024`.
- **input_device_index**: Mikrofon cihazının ID'si. Eğer sisteminizde birden fazla mikrofon bağlıysa, doğru mikrofonu seçmek için bu parametreyi ayarlamanız gerekebilir. Bunun için, aşağıdaki Python kodunu kullanarak cihazları listeleyebilirsiniz:

  ```bash
    import pyaudio
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

Çıktıdaki cihaz listesinde, hangi mikrofonun hangi ID'ye sahip olduğunu öğrenebilirsiniz.

### Görüntü Kaydı Parametreleri
- **CAMERAID**: Kullanılacak kamera cihazının ID'sini belirtir. Çoğu bilgisayarda entegre kamera `0` olarak tanımlıdır. Eğer birden fazla kamera bağlıysa, doğru kamerayı seçmek için bu parametreyi değiştirmeniz gerekebilir.
- **PATH**: Kaydedilecek görüntülerin dosya yolu. Görüntüler `problem` adındaki bir klasöre kaydedilecektir. Eğer farklı bir dizin istiyorsanız, burayı değiştirebilirsiniz.
- **NAMING**: Görüntü ve ses dosyalarının adlandırılmasında kullanılacak tarih formatı. Varsayılan olarak, tarih ve saat bilgisi kullanılır (`%Y-%m-%d--%H-%M-%S`).

## Program Kullanımı
**1.** Scripti çalıştırın:

```bash
python ProblemVar.py
```
**2.** Program, ses ve görüntü kaydını başlatacaktır. Ses kaydı, belirtilen ayarlara göre yapılacak ve görüntü kaydı belirli aralıklarla alınacaktır.

**3.** Verilerin kaydedilmesi:
- Ses dosyaları `.wav` formatında, belirttiğiniz ses kaydı dizininde kaydedilecektir.
- Görüntü dosyaları `.jpg` formatında, belirttiğiniz görüntü kaydı dizininde kaydedilecektir.

<hr>

# Önemli Notlar !!!
- **Mikrofon ve Kamera Seçimi**: Eğer sisteminizde birden fazla mikrofon veya kamera varsa, doğru cihazı seçmek için `input_device_index` (mikrofon) ve `CAMERAID` (kamera) parametrelerini kontrol edin ve gerektiğinde ayarlayın.
- **Hedef Dizin**: Program, ses ve görüntü dosyalarını kaydetmek için belirli dizinlere ihtiyaç duyar. Bu dizinler, belirtilen klasörler yoksa otomatik olarak oluşturulacaktır. Ancak, kaydedilen dosyalar yerel diskinizde yer kaplayabileceği için dizin yapısını ihtiyacınıza göre ayarlayabilirsiniz.
- **Performans**: Ses ve görüntü kaydı sürekli olarak çalışırken sisteminizin performansını etkileyebilir. Eğer çok yüksek çözünürlükte görüntü kaydı yapıyorsanız veya ses kaydını uzun süre yapıyorsanız, performans düşüşleri gözlemlenebilir.

Kullanıcı, her iki kaydı durdurmak için `Ctrl+C` tuşlarına bir kere basarak programı sonlandırabilir.

