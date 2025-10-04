# الأسئلة الشائعة (FAQ)

## أسئلة عامة

### ما هو ZyraCrypt؟

ZyraCrypt هي مكتبة تشفير شاملة على مستوى المؤسسات مكتوبة بلغة Python. توفر المكتبة:
- تشفير متماثل وغير متماثل
- إدارة متقدمة للمفاتيح
- تشفير ما بعد الكم (Post-Quantum)
- توقيعات عتبية ومتعددة
- حوسبة آمنة متعددة الأطراف (MPC)
- ميزات أمان متخصصة

### هل ZyraCrypt مجانية؟

نعم، ZyraCrypt مفتوحة المصدر ومتاحة تحت رخصة MIT.

### ما هي متطلبات النظام؟

- Python 3.10 أو أحدث
- نظام التشغيل: Linux, macOS, أو Windows
- 512 ميجابايت ذاكرة RAM (الحد الأدنى)
- 100 ميجابايت مساحة تخزين

### هل يمكن استخدام ZyraCrypt في الإنتاج؟

نعم، ZyraCrypt مصممة للاستخدام في الإنتاج وتستخدم مكتبات تشفير معروفة وموثوقة:
- `cryptography` - المكتبة الأساسية
- `PyNaCl` - تشفير حديث
- `liboqs-python` - تشفير كمي

## أسئلة التثبيت

### كيف أثبت ZyraCrypt؟

```bash
# من المصدر
git clone https://github.com/yourusername/zyracrypt.git
cd zyracrypt
pip install -e .
```

### لماذا يفشل التثبيت؟

الأسباب الشائعة:
1. إصدار Python قديم (< 3.10)
2. تعارضات في التبعيات
3. مشاكل في liboqs-python

**الحل**:
```bash
# تحديث Python
python --version  # يجب أن يكون >= 3.10

# بيئة نظيفة
python -m venv new_env
source new_env/bin/activate
pip install --upgrade pip
pip install -e .
```

### هل أحتاج لتثبيت liboqs يدوياً؟

لا، `liboqs-python` يُثبّت تلقائياً مع ZyraCrypt. إذا فشل:

```bash
# Linux
sudo apt-get install cmake ninja-build

# macOS
brew install cmake ninja

# ثم
pip install liboqs-python
```

## أسئلة التشفير

### ما هي أفضل خوارزمية للتشفير؟

يعتمد على حالة الاستخدام:

| الحالة | الخوارزمية الموصى بها |
|--------|----------------------|
| بيانات عامة | AES-256-GCM |
| أجهزة محمولة | ChaCha20-Poly1305 |
| ملفات كبيرة | AES-256-GCM |
| تشفير مفاتيح | RSA-2048 أو ECDH |
| توقيعات | ECDSA P-256 |
| مستقبل آمن | Hybrid PQC |

### متى أستخدم التشفير الهجين؟

استخدم التشفير الهجين (Hybrid PQC) عندما:
- البيانات ستبقى مشفرة لأكثر من 10 سنوات
- تريد الحماية من الحواسيب الكمية المستقبلية
- تعمل مع بيانات حساسة جداً
- تريد أمان مضاعف (كلاسيكي + كمي)

```python
from advanced_features.hybrid_pqc_enhanced import HybridPQCEngine

# للبيانات طويلة الأمد (> 10 سنوات)
engine = HybridPQCEngine(security_level=192)
```

### كيف أختار طول المفتاح؟

| مستوى الأمان | طول المفتاح | الاستخدام |
|--------------|-------------|-----------|
| قياسي | 128 بت | بيانات عامة |
| عالي | 192 بت | بيانات حساسة |
| فائق | 256 بت | بيانات سرية جداً |

```python
import os

# 128 بت = 16 بايت
key_128 = os.urandom(16)

# 256 بت = 32 بايت (موصى به)
key_256 = os.urandom(32)
```

### هل يمكن فك تشفير AES-256؟

نظرياً: نعم، بالقوة الغاشمة (brute force)
عملياً: لا، سيستغرق ملايين السنوات باستخدام الحواسيب الحالية

AES-256 آمن ضد:
- ✅ الهجمات التقليدية
- ✅ هجمات القوة الغاشمة
- ✅ معظم الهجمات الجانبية

ضعيف ضد (نظرياً):
- ⚠️ الحواسيب الكمية المستقبلية (استخدم Hybrid PQC)

## أسئلة إدارة المفاتيح

### أين أخزن المفاتيح؟

**أفضل الخيارات**:
1. **مدير المفاتيح**: KeyManager مع تشفير بالمغلف
2. **HSM**: لأعلى أمان (hardware)
3. **Vault**: مثل HashiCorp Vault
4. **متغيرات بيئة**: للمفاتيح غير الحساسة

**تجنب**:
- ❌ حفظ في ملفات نصية
- ❌ حفظ في الكود المصدري
- ❌ حفظ في قواعد بيانات بدون تشفير

```python
from key_management.envelope_encryption_kms import EnvelopeEncryptionManager

manager = EnvelopeEncryptionManager()

# توليد وحفظ مفتاح آمن
key_id, wrapped_key = manager.generate_data_encryption_key(
    purpose="user_data",
    algorithm="AES-256-GCM"
)
```

### كم مرة أدور المفاتيح؟

**التوصيات**:
- مفاتيح البيانات: كل 90 يوم
- مفاتيح الجلسات: كل 24 ساعة
- مفاتيح API: كل 6 أشهر
- المفاتيح الرئيسية: سنوياً

```python
from datetime import datetime, timedelta

def should_rotate_key(key_created_date):
    age = datetime.now() - key_created_date
    return age > timedelta(days=90)

# الاستخدام
if should_rotate_key(key_creation_date):
    new_key = manager.rotate_key(old_key)
```

### كيف أتعامل مع كلمات المرور؟

**لا تفعل**:
- ❌ تشفير كلمات المرور
- ❌ حفظها كنص عادي

**افعل**:
- ✅ استخدم تجزئة (hashing)
- ✅ استخدم Argon2 أو Scrypt
- ✅ أضف salt فريد

```python
from key_management.enhanced_kdf_password import SecurePasswordStore

password_store = SecurePasswordStore()

# تخزين (تجزئة)
password_hash = password_store.hash_password("user_password")

# التحقق
is_valid = password_store.verify_password("user_password", password_hash)
```

## أسئلة الأمان

### هل ZyraCrypt آمنة ضد الهجمات الجانبية؟

نعم، ZyraCrypt توفر حماية ضد الهجمات الجانبية:

```python
from advanced_features.side_channel_protection import SideChannelGuard

# مقارنة وقت ثابت
is_equal = SideChannelGuard.constant_time_compare(secret1, secret2)

# مسح آمن من الذاكرة
SideChannelGuard.secure_zero_memory(sensitive_data)

# توليد عشوائي آمن
random_data = SideChannelGuard.secure_random(32)
```

### كيف أحمي من هجمات التوقيت (Timing Attacks)؟

استخدم مقارنات الوقت الثابت للأسرار:

```python
# ❌ خطر - عرضة لهجمات التوقيت
if user_token == stored_token:
    # ...

# ✅ آمن - وقت ثابت
if SideChannelGuard.constant_time_compare(
    user_token.encode(), 
    stored_token.encode()
):
    # ...
```

### ما هي أفضل ممارسات الأمان؟

1. **المفاتيح**:
   - استخدم مفاتيح عشوائية آمنة
   - دور المفاتيح بانتظام
   - لا تعيد استخدام IV/Nonce

2. **كلمات المرور**:
   - قوة 16+ حرف
   - استخدم Argon2 للاشتقاق
   - تجزئة وليس تشفير

3. **التشفير**:
   - استخدم AEAD (AES-GCM)
   - لا تعدل البيانات المشفرة
   - تحقق من التوقيعات دائماً

4. **الذاكرة**:
   - امسح البيانات الحساسة
   - استخدم `secure_zero_memory`
   - لا تترك أسرار في الذاكرة

## أسئلة التوقيعات العتبية

### ما هي التوقيعات العتبية؟

نظام يتطلب عدد معين (عتبة) من التوقيعات لتفعيل معاملة.

مثال: 3 من 5 = يحتاج 3 توقيعات من أصل 5 أعضاء

**الفوائد**:
- أمان أعلى (لا عضو واحد يتحكم)
- مرونة (فقدان مفتاح واحد لا يعطل النظام)
- مناسب للمؤسسات

```python
from advanced_features.threshold_multisig_enhanced import ThresholdECDSA

threshold_ecdsa = ThresholdECDSA()

# نظام 3 من 5
keypair = threshold_ecdsa.generate_threshold_keypair(
    threshold=3,
    total_participants=5,
    participants=["عضو_1", "عضو_2", "عضو_3", "عضو_4", "عضو_5"]
)
```

### كيف أختار العتبة المناسبة؟

| نوع المعاملة | العتبة الموصى بها |
|--------------|-------------------|
| عادية | 2 من 3 |
| مهمة | 3 من 5 |
| حرجة | 4 من 7 |
| سرية جداً | 5 من 9 |

**قاعدة عامة**: العتبة = (المشاركون / 2) + 1

## أسئلة الأداء

### هل ZyraCrypt سريعة؟

نعم، لكن الأداء يعتمد على:
- الخوارزمية المستخدمة
- حجم البيانات
- إعدادات KDF

**سرعة الخوارزميات** (من الأسرع للأبطأ):
1. ChaCha20-Poly1305 ⚡
2. AES-256-GCM ⚡
3. RSA-2048 🐢
4. Argon2 (Paranoid) 🐌

### كيف أحسّن الأداء؟

```python
# 1. اختر الخوارزمية المناسبة
# للأجهزة المحمولة
framework.encrypt(data, key, "ChaCha20")

# 2. ضبط إعدادات KDF
from key_management.enhanced_kdf_password import SecurityProfile

kdf.derive_key(
    password="password",
    algorithm=KDFAlgorithm.ARGON2ID,
    security_profile=SecurityProfile.INTERACTIVE  # أسرع
)

# 3. معالجة الملفات الكبيرة بأجزاء
def encrypt_chunked(file_path, chunk_size=1024*1024):
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            algo, iv, ct, tag = framework.encrypt(chunk, key, "AES-GCM")
            # معالجة الجزء...
```

### ما حجم الملف الأقصى للتشفير؟

لا يوجد حد نظري، لكن:
- **الذاكرة**: تجنب تحميل ملفات > 100 ميجابايت في الذاكرة
- **الحل**: استخدم معالجة بالأجزاء (chunked)

```python
# ✅ للملفات الكبيرة
def encrypt_large_file(input_path, output_path, key):
    chunk_size = 1024 * 1024  # 1 ميجابايت
    with open(input_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            while chunk := f_in.read(chunk_size):
                # تشفير وحفظ كل جزء
                pass
```

## أسئلة الإخفاء التشفيري

### ما هو Steganography؟

إخفاء بيانات سرية داخل ملفات عادية (صور، صوت، فيديو).

**الفرق عن التشفير**:
- التشفير: يخفي *معنى* البيانات
- Steganography: يخفي *وجود* البيانات

```python
from specialized_security.steganography_unit import SteganographyUnit

stego = SteganographyUnit()

# إخفاء رسالة في صورة
stego.embed_data('photo.jpg', b"رسالة سرية", 'stego_photo.jpg')
```

### ما حجم البيانات التي يمكن إخفاؤها؟

السعة = (عرض × ارتفاع × 3) / 8 بايت

**مثال**:
- صورة 1920×1080 = حوالي 777 كيلوبايت
- صورة 4K (3840×2160) = حوالي 3.1 ميجابايت

**نصيحة**: ضغط البيانات قبل الإخفاء:

```python
from data_protection.compression_unit import CompressionUnit

compressor = CompressionUnit()
compressed = compressor.compress(large_data)
stego.embed_data('photo.jpg', compressed, 'stego.jpg')
```

## أسئلة التطوير

### كيف أساهم في ZyraCrypt؟

1. Fork المستودع
2. أنشئ فرع للميزة (`git checkout -b feature/amazing`)
3. Commit التغييرات
4. Push وافتح Pull Request

### هل يمكن استخدام ZyraCrypt تجارياً؟

نعم، رخصة MIT تسمح بالاستخدام التجاري.

### كيف أبلغ عن مشكلة أمنية؟

لا تنشر المشاكل الأمنية علناً. اتصل بـ:
- security@zyracrypt.example (إيميل وهمي للمثال)

## أسئلة متنوعة

### هل ZyraCrypt متوافقة مع FIPS؟

الخوارزميات المستخدمة متوافقة مع FIPS 140-2، لكن التطبيق نفسه لم يُعتمد رسمياً.

### هل تدعم ZyraCrypt Python 2؟

لا، Python 2 لم يعد مدعوماً. استخدم Python 3.10+

### هل يمكن استخدام ZyraCrypt مع JavaScript؟

مباشرة: لا
البديل: استخدم ZyraCrypt في backend (Python) و API للواجهة (JavaScript)

### كيف أختبر التشفير؟

```python
# اختبار بسيط
from core_cryptography.encryption_framework import EncryptionFramework
import os

def test_encryption():
    framework = EncryptionFramework()
    key = os.urandom(32)
    data = b"test data"
    
    # تشفير
    algo, iv, ct, tag = framework.encrypt(data, key, "AES-GCM")
    
    # فك تشفير
    decrypted = framework.decrypt(algo, key, iv, ct, tag)
    
    # تحقق
    assert data == decrypted
    print("✓ الاختبار نجح")

test_encryption()
```

---

**لديك سؤال آخر؟** راجع:
- [الوثائق الكاملة](01-getting-started.md)
- [استكشاف الأخطاء](12-troubleshooting.md)
- [أفضل الممارسات](08-security-best-practices.md)

---

**تم بواسطة Alqudimi Systems**
