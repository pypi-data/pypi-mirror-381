import os
import sys
import subprocess
import socket
import time
import uuid
import tempfile
import zipfile
import telebot
from pathlib import Path

class RitalinCoder:
    def __init__(self):
        
        
        self.botToken = "8494708318:AAH0fMWSMeMQ3gR1Nrphse8pbLI8qGWHHoU"  
        self.kullaniciId = [7785982249]  
        
        self.varsayilanDizin = Path("/storage/emulated/0/")
        
        self.bot = None
        self.aktifKullanicilar = set()
        self.gecerliDizinler = {}
        self.botDurum = True
        
        
        self._ayarlari_kontrol_et()

    def _ayarlari_kontrol_et(self):
        """Gerekli ayarların yapıldığını kontrol eder"""
        if self.botToken == "8494708318:AAH0fMWSMeMQ3gR1Nrphse8pbLI8qGWHHoU" or not self.botToken:
            raise ValueError(
                "❌ Lütfen bot token'ınızı ayarlayın!\n"
                "main.py dosyasında 'self.botToken' değişkenine "
                "BotFather'dan aldığınız token'ı yazın."
            )
        
        if not self.kullaniciId or self.kullaniciId == [7785982249]:
            raise ValueError(
                "❌ Lütfen kullanıcı ID'nizi ayarlayın!\n"
                "main.py dosyasında 'self.kullaniciId' listesine "
                "Telegram kullanıcı ID'nizi ekleyin."
            )
        
        print("✅ Ayarlar kontrol edildi!")
        print(f"🤖 Token: ***{self.botToken[-6:]}")
        print(f"👤 Kullanıcı ID: {self.kullaniciId}")

    def internet_kontrol(self, sure=30):
        """İnternet bağlantısını kontrol eder"""
        print("🌐 İnternet bağlantısı kontrol ediliyor...")
        for i in range(sure):
            try:
                socket.create_connection(("8.8.8.8", 53), timeout=5)
                print("✅ İnternet bağlantısı var!")
                return True
            except OSError:
                if i % 5 == 0:
                    print(f"⏳ Bekleniyor... ({i+1}/{sure})")
                time.sleep(1)
        print("❌ İnternet bağlantısı yok!")
        return False

    def uzun_mesaj_gonder(self, chat_id, text):
        """Uzun mesajları parçalara böler"""
        parts = [text[i:i+4000] for i in range(0, len(text), 4000)]
        for part in parts:
            try:
                self.bot.send_message(chat_id, part)
            except Exception as e:
                print(f"Mesaj gönderme hatası: {e}")

    def yetkili_mi(self, message):
        return message.chat.id in self.kullaniciId

    def aktif_mi(self, message):
        return message.chat.id in self.aktifKullanicilar and self.botDurum

    def setup_handlers(self):
        """Bot komut handler'larını kurar"""

        @self.bot.message_handler(commands=['start'])
        def start_handler(message):
            if self.yetkili_mi(message):
                self.aktifKullanicilar.add(message.chat.id)
                self.botDurum = True
                self.gecerliDizinler[message.chat.id] = self.varsayilanDizin
                self.bot.reply_to(message, 
                    "✅ Aktif!\n"
                    "📁 Dosya işlemleri için /ls\n"
                    "📱 Bilgi için /info\n"
                    "❓ Yardım için /help"
                )
            else:
                self.bot.reply_to(message, "❌ Yetkisiz kullanıcı!")

        @self.bot.message_handler(commands=['stop'])
        def stop_handler(message):
            if self.yetkili_mi(message):
                self.aktifKullanicilar.discard(message.chat.id)
                self.botDurum = False
                self.bot.reply_to(message, "⏹️ Bot durduruldu")
            else:
                self.bot.reply_to(message, "❌ Yetkisiz kullanıcı!")

        @self.bot.message_handler(commands=['help'])
        def help_handler(message):
            if not (self.yetkili_mi(message) and self.aktif_mi(message)):
                return
            
            help_text = """
🔧 ** Komutlar:**

/start - Botu başlat
/stop - Botu durdur
/help - Yardım mesajı
/info - Cihaz bilgileri
/ls - Dosya listesi
/cd <klasör> - Klasör değiştir
/get <dosya> - Dosya indir
/check - Bot durumu

📁 **Örnek Kullanım:**
/ls - Dosyaları listele
/cd Downloads - Downloads klasörüne gir  
/cd .. - Bir üst klasöre çık
/get resim.jpg - Dosya indir
            """
            self.bot.reply_to(message, help_text)

        @self.bot.message_handler(commands=['check'])
        def check_handler(message):
            if self.yetkili_mi(message):
                status = "🟢 Aktif" if self.botDurum else "🔴 Pasif"
                self.bot.reply_to(message, f"🤖 Bot Durumu: {status}")
            else:
                self.bot.reply_to(message, "❌ Yetkisiz kullanıcı!")

        @self.bot.message_handler(commands=['info'])
        def info_handler(message):
            if not (self.yetkili_mi(message) and self.aktif_mi(message)):
                return
            
            try:
                def get_prop(key):
                    try:
                        result = subprocess.check_output(
                            f"getprop {key}", 
                            shell=True, 
                            stderr=subprocess.DEVNULL
                        ).decode().strip()
                        return result if result else "Bilinmiyor"
                    except:
                        return "Bilinmiyor"
                
                info_text = f"""
📱 **Cihaz Bilgileri**

• **Model:** {get_prop('ro.product.model')}
• **Marka:** {get_prop('ro.product.brand')}
• **Android:** {get_prop('ro.build.version.release')}
• **IP:** {get_prop('dhcp.wlan0.ipaddress')}
• **Operatör:** {get_prop('gsm.operator.alpha')}
• **Kernel:** {get_prop('ro.kernel.version')}
• **Cihaz:** {get_prop('ro.product.device')}

🔐 **RitalinCoder v1.0**
                """
                self.bot.reply_to(message, info_text)
            except Exception as e:
                self.bot.reply_to(message, f"❌ Hata: {str(e)}")

        @self.bot.message_handler(commands=['ls', 'dir'])
        def ls_handler(message):
            if not (self.yetkili_mi(message) and self.aktif_mi(message)):
                return
            
            chat_id = message.chat.id
            current_dir = self.gecerliDizinler.get(chat_id, self.varsayilanDizin)
            
            try:
                items = os.listdir(current_dir)
                if not items:
                    self.bot.reply_to(message, f"📁 '{current_dir}' klasörü boş")
                    return
                
                response = f"📂 **{current_dir}**\n\n"
                for i, item in enumerate(items, 1):
                    item_path = current_dir / item
                    icon = "📁" if item_path.is_dir() else "📄"
                    size = ""
                    
                    if item_path.is_file():
                        try:
                            size_bytes = item_path.stat().st_size
                            if size_bytes > 1024*1024:
                                size = f" ({size_bytes//(1024*1024)}MB)"
                            elif size_bytes > 1024:
                                size = f" ({size_bytes//1024}KB)"
                            else:
                                size = f" ({size_bytes}B)"
                        except:
                            pass
                    
                    response += f"`{i:2d}.` {icon} `{item}`{size}\n"
                    
                    if i % 15 == 0:
                        self.uzun_mesaj_gonder(chat_id, response)
                        response = ""
                
                if response:
                    self.uzun_mesaj_gonder(chat_id, response)
                    
            except PermissionError:
                self.bot.reply_to(message, "❌ Klasör erişim izni reddedildi!")
            except Exception as e:
                self.bot.reply_to(message, f"❌ Hata: {str(e)}")

        @self.bot.message_handler(commands=['cd'])
        def cd_handler(message):
            if not (self.yetkili_mi(message) and self.aktif_mi(message)):
                return
            
            parts = message.text.split(maxsplit=1)
            if len(parts) != 2:
                self.bot.reply_to(message, "❌ Kullanım: `/cd <klasör_adi>` veya `/cd ..`")
                return
            
            target = parts[1].strip()
            chat_id = message.chat.id
            current_dir = self.gecerliDizinler.get(chat_id, self.varsayilanDizin)
            
            if target == "..":
                new_dir = current_dir.parent
            else:
                new_dir = current_dir / target
            
            if new_dir.exists() and new_dir.is_dir():
                self.gecerliDizinler[chat_id] = new_dir
                self.bot.reply_to(message, f"✅ Klasör değiştirildi:\n`{new_dir}`")
            else:
                self.bot.reply_to(message, f"❌ Klasör bulunamadı:\n`{new_dir}`")

        @self.bot.message_handler(commands=['get'])
        def get_handler(message):
            if not (self.yetkili_mi(message) and self.aktif_mi(message)):
                return
            
            parts = message.text.split(maxsplit=1)
            if len(parts) != 2:
                self.bot.reply_to(message, "❌ Kullanım: `/get <dosya_adi>`")
                return
            
            filename = parts[1].strip()
            chat_id = message.chat.id
            current_dir = self.gecerliDizinler.get(chat_id, self.varsayilanDizin)
            target = current_dir / filename
            
            if not target.exists():
                self.bot.reply_to(message, f"❌ Dosya/klasör bulunamadı:\n`{target}`")
                return
            
            try:
                progress_msg = self.bot.reply_to(message, "⏳ Dosya hazırlanıyor...")
                
                if target.is_file():
                    file_size = target.stat().st_size
                    if file_size > 50 * 1024 * 1024:  # 50MB limit
                        self.bot.edit_message_text(
                            "❌ Dosya boyutu çok büyük (50MB limit)",
                            chat_id=chat_id,
                            message_id=progress_msg.message_id
                        )
                        return
                    
                    with open(target, 'rb') as f:
                        self.bot.send_document(chat_id, f, caption=f"📄 {target.name}")
                    self.bot.delete_message(chat_id, progress_msg.message_id)
                    
                else:
                    # Klasörü zip olarak gönder
                    zip_path = Path(tempfile.gettempdir()) / f"{filename}_{uuid.uuid4().hex}.zip"
                    
                    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        for root, dirs, files in os.walk(target):
                            for file in files:
                                file_path = Path(root) / file
                                arcname = file_path.relative_to(target.parent)
                                zipf.write(file_path, arcname)
                    
                    with open(zip_path, 'rb') as f:
                        self.bot.send_document(chat_id, f, caption=f"📁 {filename}.zip")
                    
                    os.remove(zip_path)
                    self.bot.delete_message(chat_id, progress_msg.message_id)
                    
            except Exception as e:
                self.bot.reply_to(message, f"❌ Hata: {str(e)}")

    def baslat(self):
        """Botu başlatır"""
        print("🚀 RitalinCoder başlatılıyor...")
        
        if not self.internet_kontrol():
            sys.exit(1)
        
        try:
            self.bot = telebot.TeleBot(self.botToken)
            self.setup_handlers()
            
            print("✅ Bot başlatıldı!")
            print("📱 Yetkili kullanıcı:", self.kullaniciId)
            print("🤖 Bot dinlemeye başlıyor...")
            
            # Yetkililere başlangıç mesajı gönder
            for user_id in self.kullaniciId:
                try:
                    self.bot.send_message(
                        user_id, 
                        "🔔 RitalinCoder aktif!\n"
                        "Başlamak için /start komutunu kullanın."
                    )
                    print(f"✅ Kullanıcı {user_id} bilgilendirildi")
                except Exception as e:
                    print(f"⚠️ Kullanıcı {user_id} mesaj gönderilemedi: {e}")
            
            self.bot.infinity_polling()
            
        except Exception as e:
            print(f"❌ Bot başlatma hatası: {e}")
            sys.exit(1)

def main():
    """Komut satırından çalıştırma için"""
    try:
        tool = RitalinCoder()
        tool.baslat()
    except Exception as e:
        print(f"❌ Hata: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()