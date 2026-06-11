# Urdu Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Urdu
- **ISO 639 code**: urd
- **Script**: Perso-Arabic (Nastaliq)
- **Native speakers**: 230 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Urdu-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Urdu keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | موتر | `mautira` | ml |
| `KW_MATRIX` | matrix | مصفوفة | `masfuufah` | ml |
| `KW_VECTOR` | vector | متجه | `muttajiha` | ml |
| `KW_GRAD` | gradient | تدرج | `tadarruja` | ml |
| `KW_BACKPROP` | backprop | انتشارخلفي | `intishaarakhalfii` | ml |
| `KW_FORWARD` | forward | أمامي | `amaamii` | ml |
| `KW_LAYER` | layer | طبقة | `tabaqah` | ml |
| `KW_MODEL` | model | نموذج | `namuuzaja` | ml |
| `KW_TRAIN` | train | تدريب | `tadriiba` | ml |
| `KW_INFER` | infer | استدلال | `istidlaala` | ml |
| `KW_LOSS` | loss | خسارة | `khasaarah` | ml |
| `KW_OPTIMIZE` | optimize | تحسين | `tahsiina` | ml |
| `KW_ACTIVATION` | activation | تنشيط | `tanshiita` | ml |
| `KW_WEIGHT` | weight | وزن | `vazna` | ml |
| `KW_BIAS` | bias | انحياز | `inhiyaaza` | ml |
| `KW_EPOCH` | epoch | حقبة | `huqbah` | ml |
| `KW_BATCH` | batch | دفعة | `dufaah` | ml |
| `KW_DATASET` | dataset | مجموعةبيانات | `majmuuabayaanaata` | ml |
| `KW_EMBED` | embed | تضمين | `tadmiina` | ml |
| `KW_ATTENTION` | attention | انتباه | `intibaaha` | ml |

### Paradigm: common

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | درآمد | `daraamada` | namespace |
| `KW_EXPORT` | export | برآمد | `baraamada` | namespace |
| `KW_PACKAGE` | package | بستہ | `bastah` | namespace |
| `KW_NAMESPACE` | namespace | نامخلا | `naamakhalaa` | namespace |
| `KW_USE` | use | استعمال | `istaemaala` | namespace |
| `KW_INCLUDE` | include | شامل | `shaamila` | preprocessor |
| `KW_FROM` | from | سے | `see` | namespace |
| `KW_AS` | as | بطور | `bataura` | namespace |

### Paradigm: concurrent

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | دھاگہ | `dhaagah` | concurrency |
| `KW_SPAWN` | spawn | پیدا | `paedaa` | concurrency |
| `KW_LOCK` | lock | تالا | `taalaa` | concurrency |
| `KW_SYNC` | synchronized | ہمآہنگ | `hamaahanga` | concurrency |
| `KW_CHANNEL` | channel | ذریعہ | `zariiah` | concurrency |
| `KW_SELECT` | select | چنو | `cunau` | concurrency |

### Paradigm: dataflow

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | تدفق | `tadaffuqa` | reactive |
| `KW_PIPE` | pipe | أنبوب | `anbuuba` | reactive |
| `KW_MAP` | map | خريطة | `khariitah` | reactive |
| `KW_FILTER` | filter | رشح | `rashshiha` | reactive |
| `KW_REDUCE` | reduce | اختزل | `ikhtazila` | reactive |
| `KW_FOLD` | fold | طي | `tayya` | reactive |
| `KW_OBSERVE` | observe | راقب | `raaqiba` | reactive |
| `KW_EMIT` | emit | أصدر | `asdira` | reactive |
| `KW_SUBSCRIBE` | subscribe | اشترك | `ishtaraka` | reactive |
| `KW_DEBOUNCE` | debounce | إزالةارتداد | `izaalahirtidaada` | reactive |

### Paradigm: distributed

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | عقدة | `uqdah` | cluster |
| `KW_REPLICA` | replica | نسخة | `nuskhah` | cluster |
| `KW_CONSENSUS` | consensus | إجماع | `ijmaae` | cluster |
| `KW_SHARD` | shard | شظية | `shaziyah` | cluster |
| `KW_GOSSIP` | gossip | إشاعة | `ishaaah` | cluster |
| `KW_LEADER` | leader | قائد | `qaaida` | cluster |
| `KW_RPC` | rpc | استدعاءبعيد | `istidaaabaiida` | cluster |
| `KW_ACTOR` | actor | فاعل | `faaila` | cluster |
| `KW_MESSAGE` | message | رسالة | `risaalah` | cluster |

### Paradigm: functional

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | بےنام | `benaama` | function |
| `KW_MATCH` | match | میل | `meela` | pattern |
| `KW_WHEN` | when | جب | `jaba` | pattern |
| `KW_FUN` | fun | فعل | `fela` | function |
| `KW_REC` | rec | تکراری | `takaraarii` | recursion |
| `KW_IN` | in | میں | `mei_n` | binding |
| `KW_WHERE` | where | جہاں | `jahaa_n` | binding |
| `KW_DATA` | data | مواد | `mavaada` | type_def |
| `KW_TYPE` | type | قسم | `qisma` | type_def |
| `KW_MODULE` | module | حصہ | `hissah` | namespace |

### Paradigm: gpu

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | نواة | `navaah` | compute |
| `KW_DEVICE` | device | جهاز | `jahaaza` | compute |
| `KW_HOST` | host | مضيف | `mudiifa` | compute |
| `KW_GLOBAL` | global | عام | `aamma` | compute |
| `KW_SHARED` | shared | مشترك | `mushtaraka` | compute |
| `KW_THREADIDX` | threadidx | معرفخيط | `muarrifkhayta` | compute |
| `KW_BLOCKIDX` | blockidx | معرفكتلة | `muarrifkutlah` | compute |
| `KW_GRID` | grid | شبكة | `shabakah` | compute |
| `KW_BARRIER` | barrier | حاجز | `haajiza` | compute |
| `KW_ATOMIC` | atomic | ذري | `zarrii` | compute |
| `KW_WARP` | warp | التواء | `iltivaaa` | compute |

### Paradigm: hdl

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | وجود | `vajuuda` | hardware |
| `KW_ARCH` | architecture | تعمیر | `taemiira` | hardware |
| `KW_SIGNAL` | signal | اشارہ | `ishaarah` | hardware |
| `KW_PORT` | port | بندرگاہ | `bandaragaah` | hardware |
| `KW_WIRE` | wire | تار | `taara` | hardware |
| `KW_REG` | reg | رجسٹر | `rajistara` | hardware |
| `KW_MODULE_HW` | module | پرزہ | `parzah` | hardware |
| `KW_ALWAYS` | always | ہمیشہ | `hameeshah` | hardware |
| `KW_ASSIGN` | assign | تفویض | `tafaviiza` | hardware |
| `KW_BEGIN` | begin | آغاز | `aaghaaza` | block |
| `KW_END` | end | اختتام | `ikhatitaama` | block |

### Paradigm: imperative

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | اگر | `agara` | control_flow |
| `KW_ELSE` | else | ورنہ | `varnah` | control_flow |
| `KW_ELIF` | elif | وگرنہ_اگر | `vagarnah_agara` | control_flow |
| `KW_WHILE` | while | جبتک | `jabataka` | control_flow |
| `KW_DO` | do | کرو | `karau` | control_flow |
| `KW_FOR` | for | برائے | `baraae` | control_flow |
| `KW_BREAK` | break | توڑو | `taudau` | control_flow |
| `KW_CONTINUE` | continue | جاری | `jaarii` | control_flow |
| `KW_SWITCH` | switch | انتخاب | `inatikhaaba` | control_flow |
| `KW_CASE` | case | حالت | `haalata` | control_flow |
| `KW_DEFAULT` | default | طےشدہ | `taeshudah` | control_flow |
| `KW_RETURN` | return | واپس | `vaapasa` | control_flow |
| `KW_GOTO` | goto | جاؤ | `jaao` | control_flow |
| `KW_VAR` | var | متغیر | `mutaghayyira` | declaration |
| `KW_CONST` | const | ثابت | `saabita` | declaration |
| `KW_LET` | let | مانو | `maanau` | declaration |
| `KW_INT` | int | صحیح | `sahiiha` | type |
| `KW_FLOAT` | float | اعشاری | `aeshaarii` | type |
| `KW_DOUBLE` | double | دوہرا | `dauharaa` | type |
| `KW_CHAR` | char | حرف | `harfa` | type |
| `KW_BOOL` | bool | منطقی | `mantiqii` | type |
| `KW_STRING` | string | جملہ | `jumlah` | type |
| `KW_VOID` | void | خالی | `khaalii` | type |
| `KW_TRUE` | true | سچ | `sacha` | literal |
| `KW_FALSE` | false | جھوٹ | `jhauta` | literal |
| `KW_NULL` | null | تہی | `tahii` | literal |
| `KW_TRY` | try | کوشش | `kaushisha` | exception |
| `KW_CATCH` | catch | پکڑو | `pakadau` | exception |
| `KW_FINALLY` | finally | آخرکار | `aakhirakaara` | exception |
| `KW_THROW` | throw | پھینکو | `phei_nkau` | exception |
| `KW_RAISE` | raise | اٹھاؤ | `uthaao` | exception |
| `KW_EXCEPT` | except | استثنا | `istisnaa` | exception |

### Paradigm: iot

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | دبوس | `dabuusa` | io |
| `KW_READ` | read | اقرأ | `iqraa` | io |
| `KW_WRITE` | write | اكتب | `uktuba` | io |
| `KW_ANALOG` | analog | تماثلي | `tamaasulii` | io |
| `KW_DIGITAL` | digital | رقمي | `raqamii` | io |
| `KW_PWM` | pwm | تعديلعرض | `taediilaarda` | io |
| `KW_INTERRUPT` | interrupt | مقاطعة | `muqaataah` | io |
| `KW_TIMER` | timer | مؤقت | `muaqqita` | io |
| `KW_SENSOR` | sensor | مستشعر | `mustashaira` | io |
| `KW_ACTUATOR` | actuator | مشغل | `mushaghghila` | io |
| `KW_BUS` | bus | ناقل | `naaqila` | io |
| `KW_PROTOCOL` | protocol | بروتوكول | `bruutuukuula` | io |
| `KW_SLEEP` | sleep | نوم | `nauma` | power |
| `KW_WAKE` | wake | استيقظ | `istayqiza` | power |

### Paradigm: logic

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | قاعدہ | `qaaedah` | clause |
| `KW_FACT` | fact | حقیقت | `haqiiqata` | clause |
| `KW_QUERY` | query | سوال | `savaala` | clause |
| `KW_NOT` | not | نہیں | `nahii_n` | operator |
| `KW_AND` | and | اور | `aura` | operator |
| `KW_OR` | or | یا | `yaa` | operator |

### Paradigm: memory

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | امتلك | `imtalika` | ownership |
| `KW_BORROW` | borrow | استعر | `istaaira` | ownership |
| `KW_MOVE` | move | انقل | `inqula` | ownership |
| `KW_MUT` | mut | متغير | `mutaghayyira` | ownership |
| `KW_LIFETIME` | lifetime | عمر | `umra` | ownership |
| `KW_ARENA` | arena | ساحة | `saahah` | allocation |
| `KW_GC` | gc | جمعالمهملات | `jamealmuhmalaata` | allocation |
| `KW_PIN_MEM` | pin | تثبيتذاكرة | `tasbiitzaakirah` | allocation |

### Paradigm: oop

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | جماعت | `jamaaata` | type_def |
| `KW_OBJECT` | object | شے | `shae` | type_def |
| `KW_INTERFACE` | interface | سطحرابطہ | `satharaabitah` | type_def |
| `KW_EXTENDS` | extends | توسیع | `tausiia` | inheritance |
| `KW_IMPLEMENTS` | implements | نافذ | `naafiza` | inheritance |
| `KW_NEW` | new | نیا | `nayaa` | instantiation |
| `KW_THIS` | this | یہ | `yah` | reference |
| `KW_SUPER` | super | اعلیٰ | `aelaa` | reference |
| `KW_PUBLIC` | public | عوامی | `avaamii` | access |
| `KW_PRIVATE` | private | نجی | `nijii` | access |
| `KW_PROTECTED` | protected | محفوظ | `mahafuuza` | access |
| `KW_STATIC` | static | ساکن | `saakina` | storage |
| `KW_ABSTRACT` | abstract | تجریدی | `tajriidii` | modifier |
| `KW_VIRTUAL` | virtual | مجازی | `majaazii` | modifier |
| `KW_OVERRIDE` | override | بالادست | `baalaadasta` | modifier |

### Paradigm: procedural

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | تابع | `taabe` | subroutine |
| `KW_PROC` | procedure | طریقہ | `tariiqah` | subroutine |
| `KW_CALL` | call | بلاؤ | `bulaao` | subroutine |
| `KW_PARAM` | param | سہولت | `sahuulata` | subroutine |
| `KW_YIELD` | yield | دو | `dau` | coroutine |
| `KW_AWAIT` | await | انتظار | `intizaara` | async |
| `KW_ASYNC` | async | غیرہمزمان | `ghaerahamazamaana` | async |

### Paradigm: robotics

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | محرك | `muharrika` | control |
| `KW_SERVO` | servo | محركخادم | `muharrikakhaadima` | control |
| `KW_JOINT` | joint | مفصل | `mafsila` | control |
| `KW_POSE` | pose | وضعية | `vadaiyah` | control |
| `KW_TRAJECTORY` | trajectory | مسار | `masaara` | control |
| `KW_FEEDBACK` | feedback | تغذيةراجعة | `taghziyahraajiah` | control |
| `KW_PID` | pid | متحكم | `mutahakkima` | control |
| `KW_DEADLINE` | deadline | موعدنهائي | `mauidnihaaii` | realtime |
| `KW_PERIODIC` | periodic | دوري | `dauriiy` | realtime |
| `KW_PRIORITY` | priority | أولوية | `avlaviyah` | realtime |
| `KW_ACTUATE` | actuate | شغل | `shaghghila` | control |
| `KW_PERCEIVE` | perceive | أدرك | `adrika` | control |
| `KW_PLAN` | plan | خطط | `khattata` | control |

### Paradigm: systems

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | اشارہ | `ishaarah` | memory |
| `KW_REF` | ref | حوالہ | `havaalah` | memory |
| `KW_ALLOC` | alloc | تخصیص | `takhsiisa` | memory |
| `KW_FREE` | free | آزاد | `aazaada` | memory |
| `KW_SIZEOF` | sizeof | حجم | `hajma` | memory |
| `KW_STRUCT` | struct | ساخت | `saakhta` | type_def |
| `KW_UNION` | union | اتحاد | `itihaada` | type_def |
| `KW_ENUM` | enum | شمار | `shumaara` | type_def |
| `KW_TYPEDEF` | typedef | قسمتعریف | `qismataeriifa` | type_def |
| `KW_VOLATILE` | volatile | متلون | `mutalavvina` | modifier |
| `KW_REGISTER` | register | اندراج | `inadraaja` | storage |
| `KW_EXTERN` | extern | خارجی | `khaarijii` | linkage |
| `KW_INLINE` | inline | اندرونی | `anadaruunii` | modifier |

### Paradigm: verification

| Construct | English | Urdu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | يتطلب | `yatatallaba` | contract |
| `KW_ENSURES` | ensures | يضمن | `yadmana` | contract |
| `KW_INVARIANT` | invariant | ثابت | `saabita` | contract |
| `KW_ASSERT` | assert | أكد | `akkida` | contract |
| `KW_ASSUME` | assume | افترض | `iftarida` | contract |
| `KW_PROVE` | prove | أثبت | `asbita` | contract |
| `KW_REFINES` | refines | يحسن | `yuhassina` | contract |
| `KW_MODEL_CHECK` | modelcheck | فحصالنموذج | `fahsalnamuuzaja` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Urdu native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Urdu a first-class systems-programming language, not a localized skin.

## Example

```
اگر (x > 0)        // romenagri: agara
    ...
ورنہ              // romenagri: varnah
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Urdu keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*