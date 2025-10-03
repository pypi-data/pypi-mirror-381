# viona/api.py

import requests
import os

class Viona:
    """
    Viona API'si ile iletişim kurmak için kullanılan ana istemci sınıfı.
    
    Kullanım:
    from viona import Viona
    istemci = Viona(api_key="ANAHTARINIZ") 
    cevap = istemci.sor("Bir soru sorun.")
    """
    
    # API'nin temel URL'si
    BASE_URL = "https://viona.orvixgames.com/app/api/v1/models-1.5/orvix-viona-api/api.viona-1.5.php"

    def __init__(self, api_key=None):
        """
        Viona istemcisini başlatır. API anahtarını doğrudan veya 
        VİONA_APİ_KEY ortam değişkeninden alır.
        """
        
        # Kodu bozmuyacak, hata çıkarmayacak şekilde başa telif hakkı eklenmesi
        # talebiniz üzerine, istemci başlatılırken bu mesajı yazdırıyoruz.
        print("2025 - Orvix games Tüm hakları sakıldır")

        
        # Kullanıcıdan gelen anahtarı kullan, yoksa ortam değişkenine bak
        self.api_key = api_key
        if not self.api_key:
            self.api_key = os.environ.get("VİONA_APİ_KEY")
        
        if not self.api_key:
            # Anahtar bulunamazsa hata mesajı fırlat
            raise ValueError("VİONA_APİ_KEY tanımlanmalı veya Viona sınıfına api_key parametresi ile iletilmelidir.")
            


    def sor(self, soru: str) -> str:
        """
        Viona API'sine bir soru gönderir ve cevabı döndürür.

        Args:
            soru (str): Yapay zekaya sorulacak metin.

        Returns:
            str: API'den gelen cevap metni veya hata mesajı.
        """
        params = {
            "soru": soru,
            "key": self.api_key  # Kullanıcının anahtarını kullan
        }
        
        try:
            # API'ye GET isteği gönder
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status() # HTTP hata kodu (4xx veya 5xx) varsa istisna fırlat

            # Cevabı JSON olarak al
            data = response.json()
            
            # API'nizin dönüş yapısına göre 'cevap' anahtarını kullanıyoruz:
            cevap = data.get("cevap") 
            
            if cevap is not None:
                return cevap
            else:
                # 'cevap' anahtarı yoksa, tüm yanıtı döndür (hata ayıklama için)
                return f"API'den geçerli bir 'cevap' alanı alınamadı. Tüm yanıt: {data}"

        except requests.exceptions.RequestException as e:
            # İstek sırasında bir hata oluşursa (ağ bağlantısı, DNS hatası vb.)
            return f"API isteği hatası (Requests): {e}"
        except ValueError:
            # JSON çözümleme hatası (API geçersiz yanıt döndürürse)
            return "API'den geçerli bir JSON yanıtı alınamadı."

# API istemcisini içeri aktarırken Viona sınıfının direkt görünür olması için 
# bu dosya viona/__init__.py tarafından içeri aktarılır.{\rtf1}