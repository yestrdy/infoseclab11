# МОНГОЛ УЛСЫН ИХ СУРГУУЛЬ
## МЭДЭЭЛЛИЙН ТЕХНОЛОГИ, ЭЛЕКТРОНИКИЙН СУРГУУЛЬ

**Д.Билгүүнтөгс**  
**24B1NUM0440**

# Лабораторын ажил №6
## Hash generation and sensitivity of hash functions to plaintext modifications

**2026 оны 5-р сарын 19**

---

## Мэдээллийн аюулгүй байдал ECEN324

---

## Ажлын зорилго

MD5 хэш функц ашиглан мессежийн бүрэн бүтэн байдлыг хамгаалах чадварыг шалгах, хэш функцийн plaintext-ийн өөрчлөлтөд хэрхэн мэдрэмтгий байдгийг (Avalanche Effect) судлах, мөн HMAC болон collision attack-ын тухай практик аргаар ойлголт авахад оршино.

---

## Үндсэн ойлголт

**Hash function** нь дурын урттай мессежийг тогтмол урттай хэш утга (digest) руу хувиргадаг нэг чиглэлт функц юм. Сайн хэш функц дараах шинж чанартай:

- **Collision resistance**: Ижил хэш утга үүсгэдэг хоёр өөр мессеж олоход маш хэцүү
- **Avalanche effect**: Оролтын бага зэрэг өөрчлөлт гаралтыг бүрэн өөрчилнө (~50% бит)
- **One-way**: Хэш утгаас эх мессежийг сэргээх боломжгүй

**HMAC (Keyed-Hash Message Authentication Code)** нь мессежийн бүрэн бүтэн байдал (integrity) болон authentication-ыг хангадаг. Илгээгч ба хүлээн авагч нийтлэг нууц түлхүүр ашиглана.

**SHA-1** нь 160 бит (20 байт) урттай хэш утга үүсгэдэг хэш функц юм.

**MD5** нь 128 бит (16 байт) урттай хэш утга үүсгэдэг хэш функц бөгөөд collision resistance сул тул аюулгүй биш гэж тооцогддог.

---

## Даалгавар ба Үр дүн

### Даалгавар 1: Хэш функц мессежийн бүрэн бүтэн байдлыг хамгаалж чадаж буйг шалгах

#### Алхам 1: Эх текст сонгож MD5 хэш үүсгэх

CrypTool 1.4.42 программ дээр дараах эх текстийг бичиж, **Indiv. Procedures → Hash → Generate Hash Value** цэсээр MD5 хэш утгыг үүсгэсэн.

**Эх текст:**
```
Mongolia is a beautiful country
```

**MD5 хэш утга:**
```
B2 93 89 21 40 C3 B2 E3 C3 D5 B3 9B 90 02 DD D0
```

Хэшийн урт: 128 бит (32 hex тэмдэгт)

#### Алхам 2: Текстийг бага зэрэг өөрчлөх

Эх текстийн "country" гэдэг үгийн эхний үсгийг том үсгээр сольсон (c → C):

**Өөрчилсөн текст:**
```
Mongolia is a beautiful Country
```
(country → Country)

#### Алхам 3: Өөрчилсөн текстийн хэш үүсгэж харьцуулах

Дахин **Indiv. Procedures → Hash → Generate Hash Value** цэсээр MD5 хэш үүсгэсэн.

**Өөрчилсөн текстийн MD5 хэш:**
```
76 1A 4D 15 C0 6B 89 15 4A 24 9D D7 09 DB C0 91
```

#### Алхам 4: Бүрэн бүтэн байдлын шалгалтын үр дүн

| | Эх текст | Өөрчилсөн текст |
|---|----------|-----------------|
| **Текст** | Mongolia is a beautiful country | Mongolia is a beautiful Country |
| **MD5 хэш** | B2 93 89 21 40 C3 B2 E3... | 76 1A 4D 15 C0 6B 89 15... |

**Үр дүн:** Хэшүүд бүрэн өөр → Текстэд нэг үсэг (c → C) өөрчлөхөд хэш функц өөрчлөлтийг амжилттай илрүүлсэн. Бүрэн бүтэн байдал алдагдсан гэж тодорхойлов.

#### Алхам 5: Avalanche Effect (Hash Demonstration)

**Indiv. Procedures → Hash → Hash Demonstration** цэсээр MD5 хэш функцийн avalanche effect-ийг шалгасан.

**Үр дүн:**
- Нийт бит: 128
- Өөрчлөгдсөн бит: 57
- **Өөрчлөлтийн хувь: 44.53% (57/128)**
- Хамгийн урт ижил бит дараалал: offset 33, урт 7

Сайн хэш функц нь оролтын нэг бит өөрчлөлтөд гаралтын ~50% битийг өөрчилдөг. MD5 функц 44.53% бит өөрчлөгдсөн нь Avalanche effect-ийг хангаж байгааг харуулж байна.

#### Нэмэлт: HMAC-MD5 жишээ

Лабын зааварчилгааны дагуу **Indiv. Procedures → Hash → Generation of HMACs** цэсээр HMAC үүсгэсэн:

- **Hash function:** MD5
- **HMAC variant:** Double hashing
- **Түлхүүр:** "chattanooga"

**HMAC-MD5 утга:**
```
A1 5D 4C 3B 8E 72 F6 90 1D 3A 48 B7 C2 E5 9F 04
```

HMAC нь мессежийн бүрэн бүтэн байдал + authentication-ыг хангана. Нууц түлхүүр мэдэхгүй этгээд HMAC-ийг хуурамчаар үүсгэж чадахгүй.

---

### Даалгавар 2: Collision (мөргөлдөөн) олж бүрэн бүтэн байдлын шалгалтыг тойрч гарах

#### Алхам 1: Attack тохиргоо

CrypTool дээр **Analysis → Symmetric Encryption (classic) → Hash → Attack on the Hash Value of the Digital Signature** цэсэээр Birthday Attack хийсэн.

**Тохиргоо (Options):**
- **Hash function:** MD5
- **Significant bit length:** 32 бит
- **Modification method:** Insert blanks (In front of end of line, Double blanks)

**Файлууд:**
- Harmless file: `C:\Program Files (x86)\CrypTool\examples\original.txt`
- Dangerous file: `C:\Program Files (x86)\CrypTool\examples\fake.txt`

#### Алхам 2: Attack үр дүн

**"Start search"** товч дарж collision хайлт эхлүүлсэн.

**Statistics of the Attack:**

| Үзүүлэлт | Утга |
|-----------|------|
| **Projected calculation time** | 1.06 секунд |
| **Projected steps required** | 163,840 |
| **Actual calculation time** | 0.12 секунд |
| **Actual steps required** | 171,290 |
| **Hash operations performed** | 472,552 |

**Steps required sorted by run:**

| Run | Steps until collision | Collision check | Total steps |
|-----|----------------------|-----------------|-------------|
| 01 | 53,091 | 1,570 | 54,661 |
| 02 | 76,881 | 39,748 | 116,629 |

**Text Modification:**
- 18 bytes were added to the harmless message
- 18 bytes were added to the dangerous message

#### Алхам 3: Дүгнэлт

Birthday Attack ашиглан MD5 хэш функцийн 32 битийн partial collision-ыг **0.12 секундэд** амжилттай олсон. Хоёр өөр агуулгатай мессеж (original.txt ба fake.txt) тус бүрд 18 байт (харагдахгүй зай тэмдэгтүүд) нэмэгдсэнээр **ижил хэш утгатай** болсон.

Энэ нь дараахийг баталж байна:
- Бүрэн бүтэн байдлын шалгалтыг тойрч гарах боломжтой (collision олдвол)
- MD5 хэш функц нь collision resistance сул тул аюулгүй биш
- Birthday paradox ашиглавал collision олох нь тооцооллоор боломжийн хугацаанд хийгдэнэ

---

## Дүгнэлт

Энэхүү лабораторийн ажлаар хэш функцийн мессежийн бүрэн бүтэн байдлыг хамгаалах чадварыг CrypTool 1.4.42 программ дээр практик аргаар судалсан.

**Гол үр дүнгүүд:**

1. **MD5 хэш функц** нь мессежийн бүрэн бүтэн байдлыг амжилттай хамгаалж чадна. Текстийн нэг үсэг өөрчлөхөд хэш утга бүрэн өөрчлөгдөж (44.53% бит), Avalanche effect хангагдсан.

2. **MD5 хэш функцийн collision** олдсон нь бүрэн бүтэн байдлын шалгалтыг тойрч гарах боломжтойг харуулсан. Birthday Attack-аар 0.12 секундэд 32 битийн partial collision олдсон.

3. **HMAC** нь нууц түлхүүр ашигладаг тул collision attack-аас хамгаалагдсан бөгөөд мессежийн integrity + authentication-ыг хангана.

Практик хэрэглээнд MD5-ыг ашиглахаас зайлсхийж, SHA-256 болон түүнээс хүчтэй хэш функцуудыг ашиглах нь зүйтэй.
