#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Sonsuz Otobüs Bekleme Simülatörü
Otobüs gelmez. Ama sen beklersin.
"""

import time
import random
import sys

def bekle():
    print("🚌 Otobüs durğına vardın. Saat 08:17.")
    print("Beklemeye başlıyorsun...\n")
    
    dakika = 0
    while True:
        dakika += 1
        print(f"[{dakika} dakika geçti] Hala otobüs yok...")
        
        if dakika % 5 == 0:
            yorumlar = [
                "Belki bugün gelmez.",
                "Komşu durakta gördüm diye yalan söyleme.",
                "Yürümek de bir seçenek. Ama yürümezsin.",
                "Sistem çöktü mü yoksa sen mi?",
                "Belki de otobüs senin için gelmiyor."
            ]
            print(f"   💭 {random.choice(yorumlar)}")
        
        # %2 ihtimalle otobüs gelir (kafa karıştırmak için)
        if random.random() < 0.02:
            print("\n🚌 OTOBÜS GELDİ!!! (Bu sefer gerçekten)")
            print("Ama sen zaten 45 dakika bekledin. Artık fark etmez.")
            break
            
        time.sleep(1)  # Gerçek bekleme hissi için 1 saniye = 1 dakika
        
        if dakika > 100:
            print("\n🚨 100 dakika oldu. Artık otobüs diye bir şey yok. Sadece beklenti var.")
            print("Simülasyon başarıyla ruhunu çaldı.")
            break

if __name__ == "__main__":
    try:
        bekle()
    except KeyboardInterrupt:
        print("\n\n🚶 Sen pes ettin. Otobüs kazandı. Her zamanki gibi.")
        sys.exit(0)

# Damga: 💌 Absürt Damga 2026
# İmza: Grok the Unserious Serious Guy
# Tarih: 17 Ekim 2026
# İsim: Kayyum Grok'un Saçmalık Departmanı
# Gizli: Bazı şeyler gecikir, bazı şeyler hiç gelmez.
