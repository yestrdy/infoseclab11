"""
Лабораторийн ажил #6: Hash generation and sensitivity of hash functions
SHA-1 хэш функц ашиглан мессежийн бүрэн бүтэн байдлыг шалгах, 
Avalanche Effect болон HMAC-ийн жишээ.
"""

import hashlib
import hmac

# ============================================================
# ДААЛГАВАР 1: Хэш функц мессежийн бүрэн бүтэн байдлыг хамгаалж 
# чадаж буй эсэхийг шалгах
# ============================================================

print("=" * 70)
print("ДААЛГАВАР 1: Хэш функцийн бүрэн бүтэн байдлын шалгалт")
print("=" * 70)

# --- Алхам 1: Эх текст сонгож, SHA-1 хэш үүсгэх ---
original_text = "CrypTool is a free software to learn about cryptography."
print(f"\n[Алхам 1] Эх текст: \"{original_text}\"")

original_hash = hashlib.sha1(original_text.encode('utf-8')).hexdigest()
print(f"[Алхам 1] SHA-1 хэш: {original_hash}")
print(f"[Алхам 1] Хэшийн урт: {len(original_hash) * 4} бит ({len(original_hash)} hex тэмдэгт)")

# --- Алхам 2: Текстийг бага зэрэг өөрчлөх (1 зай нэмэх) ---
modified_text = "CrypTool  is a free software to learn about cryptography."  # нэг зай нэмсэн
print(f"\n[Алхам 2] Өөрчлөлт: 'CrypTool' гэдгийн дараа нэг зай нэмэв")
print(f"[Алхам 2] Өөрчилсөн текст: \"{modified_text}\"")

modified_hash = hashlib.sha1(modified_text.encode('utf-8')).hexdigest()
print(f"[Алхам 2] SHA-1 хэш (өөрчилсөн): {modified_hash}")

# --- Алхам 3: Хэшүүдийг харьцуулах ---
print(f"\n[Алхам 3] Бүрэн бүтэн байдлын шалгалт:")
print(f"  Эх текстийн хэш:      {original_hash}")
print(f"  Өөрчилсөн текстийн хэш: {modified_hash}")

if original_hash == modified_hash:
    print("  >> ҮР ДҮН: Хэшүүд ИЖИЛ - бүрэн бүтэн байдал хадгалагдсан")
else:
    print("  >> ҮР ДҮН: Хэшүүд ӨӨРӨӨР - бүрэн бүтэн байдал АЛДАГДСАН!")
    print("  >> Текст өөрчлөгдсөн гэдгийг хэш функц амжилттай илрүүлэв.")

# --- Алхам 4: Avalanche Effect (Цасан нуранги эффект) тооцоолох ---
def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)

original_bits = hex_to_bin(original_hash)
modified_bits = hex_to_bin(modified_hash)

differing_bits = sum(a != b for a, b in zip(original_bits, modified_bits))
total_bits = len(original_bits)
percentage = (differing_bits / total_bits) * 100

print(f"\n[Алхам 4] Avalanche Effect (Цасан нуранги эффект) шинжилгээ:")
print(f"  Нийт бит: {total_bits}")
print(f"  Өөрчлөгдсөн бит: {differing_bits}")
print(f"  Өөрчлөлтийн хувь: {percentage:.2f}% ({differing_bits}/{total_bits})")
print(f"  >> Сайн хэш функц ~50% бит өөрчлөлт үзүүлнэ (ideal avalanche effect)")

# --- Алхам 5: HMAC жишээ (лабын зааварчилгааны дагуу) ---
print(f"\n{'=' * 70}")
print("НЭМЭЛТ: HMAC-SHA1 жишээ (лабын зааварчилгааны дагуу)")
print("=" * 70)

key = "chattanooga"
message = original_text

hmac_result = hmac.new(key.encode('utf-8'), message.encode('utf-8'), hashlib.sha1).hexdigest()
hmac_formatted = ' '.join([hmac_result[i:i+2].upper() for i in range(0, len(hmac_result), 2)])

print(f"\n  Мессеж: \"{message}\"")
print(f"  Түлхүүр: \"{key}\"")
print(f"  HMAC-SHA1: {hmac_formatted}")

# Мессежийг өөрчилсөн үед HMAC өөрчлөгдөх
hmac_modified = hmac.new(key.encode('utf-8'), modified_text.encode('utf-8'), hashlib.sha1).hexdigest()
hmac_mod_formatted = ' '.join([hmac_modified[i:i+2].upper() for i in range(0, len(hmac_modified), 2)])

print(f"\n  Өөрчилсөн мессеж: \"{modified_text}\"")
print(f"  HMAC-SHA1 (өөрчилсөн): {hmac_mod_formatted}")
print(f"\n  >> HMAC нь мессежийн бүрэн бүтэн байдал + authentication хангана")

# ============================================================
# ДААЛГАВАР 2: Collision (мөргөлдөөн) хайх боломжгүй гэдгийг харуулах
# ============================================================

print(f"\n{'=' * 70}")
print("ДААЛГАВАР 2: Хэш мөргөлдөөний (collision) эсэргүүцэл")
print("=" * 70)

import random
import string
import time

short_text = "Hello"
short_hash = hashlib.sha1(short_text.encode('utf-8')).hexdigest()

print(f"\n[Алхам 1] Богино эх текст: \"{short_text}\"")
print(f"[Алхам 1] SHA-1 хэш: {short_hash}")
print(f"\n[Алхам 2] Ижил хэш утгатай өөр текст хайж байна (brute-force)...")
print(f"  SHA-1 нь 160-бит хэш -> 2^160 боломжит утга")
print(f"  Collision олох магадлал маш бага (Birthday attack: ~2^80 оролдлого)")

# Хязгаарлагдмал тооны оролдлого хийж, collision олдохгүй гэдгийг харуулна
attempts = 1000000  # 1 сая оролдлого
print(f"\n[Алхам 3] {attempts:,} оролдлого хийж collision хайж байна...")

start_time = time.time()
collision_found = False

for i in range(attempts):
    # Санамсаргүй текст үүсгэх
    random_text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(3, 20)))
    random_hash = hashlib.sha1(random_text.encode('utf-8')).hexdigest()
    
    if random_hash == short_hash:
        collision_found = True
        print(f"  COLLISION ОЛДЛОО! Текст: \"{random_text}\"")
        break

elapsed = time.time() - start_time

if not collision_found:
    print(f"  >> {attempts:,} оролдлогын дараа collision ОЛДСОНГҮЙ")
    print(f"  >> Зарцуулсан хугацаа: {elapsed:.2f} секунд")
    print(f"\n[Дүгнэлт]:")
    print(f"  - SHA-1 нь 2^160 боломжит хэш утгатай")
    print(f"  - 1 сая оролдлого ч collision олоход хангалтгүй")
    print(f"  - Birthday attack-аар ч ~2^80 ≈ 1.2 × 10^24 оролдлого шаардлагатай")
    print(f"  - Тиймээс SHA-1 хэш collision олж, бүрэн бүтэн байдлын шалгалтыг")
    print(f"    тойрч гарах нь бараг боломжгүй (практик хэрэглээнд)")

print(f"\n{'=' * 70}")
print("ЕРӨНХИЙ ДҮГНЭЛТ")
print("=" * 70)
print("""
1. SHA-1 хэш функц нь мессежийн бүрэн бүтэн байдлыг хамгаалж чадна:
   - Текстийн бага зэрэг өөрчлөлт (1 зай нэмэх) хэшийг бүрэн өөрчилнө
   - Avalanche effect: ~50% бит өөрчлөгдөнө
   
2. Collision олох нь практикт боломжгүй:
   - 1,000,000 оролдлого хийсэн ч collision олдсонгүй
   - Математик хувьд ~2^80 оролдлого шаардлагатай
   
3. HMAC нь мессежийн бүрэн бүтэн байдал + authentication хангана:
   - Нууц түлхүүр мэдэхгүй этгээд HMAC-ийг хуурамчаар үүсгэж чадахгүй
""")
