# Persian Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Persian
- **ISO 639 code**: fas
- **Script**: Perso-Arabic
- **Native speakers**: 130 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Persian-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Persian keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
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

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | واردکن | `vaaridkun` | namespace |
| `KW_EXPORT` | export | صادرکن | `saadirkun` | namespace |
| `KW_PACKAGE` | package | بسته | `bastah` | namespace |
| `KW_NAMESPACE` | namespace | فضاینام | `fazaaynaama` | namespace |
| `KW_USE` | use | استفاده | `istifaadah` | namespace |
| `KW_INCLUDE` | include | شامل | `shaamila` | preprocessor |
| `KW_FROM` | from | از | `az` | namespace |
| `KW_AS` | as | بهعنوان | `bahunavaana` | namespace |

### Paradigm: concurrent

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | نخ | `nakha` | concurrency |
| `KW_SPAWN` | spawn | پدیدآور | `padiidaavar` | concurrency |
| `KW_LOCK` | lock | قفل | `qufla` | concurrency |
| `KW_SYNC` | synchronized | همگام | `hamgaama` | concurrency |
| `KW_CHANNEL` | channel | کانال | `kaanaala` | concurrency |
| `KW_SELECT` | select | انتخابکن | `intikhaabkun` | concurrency |

### Paradigm: dataflow

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
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

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
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

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | بینام | `biinaama` | function |
| `KW_MATCH` | match | تطبیق | `tatbiiqa` | pattern |
| `KW_WHEN` | when | هنگامیکه | `hanagaamiikah` | pattern |
| `KW_FUN` | fun | کنش | `kunisha` | function |
| `KW_REC` | rec | بازگشتی | `baazgashtii` | recursion |
| `KW_IN` | in | در | `dar` | binding |
| `KW_WHERE` | where | کجا | `kujaa` | binding |
| `KW_DATA` | data | داده | `daadah` | type_def |
| `KW_TYPE` | type | نوع | `nava` | type_def |
| `KW_MODULE` | module | پیمانه | `paymaanah` | namespace |

### Paradigm: gpu

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
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

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | موجودیت | `maujuudiyata` | hardware |
| `KW_ARCH` | architecture | معماری | `maemaarii` | hardware |
| `KW_SIGNAL` | signal | سیگنال | `siignaala` | hardware |
| `KW_PORT` | port | درگاه | `dargaaha` | hardware |
| `KW_WIRE` | wire | سیم | `siima` | hardware |
| `KW_REG` | reg | ثبات | `sabaata` | hardware |
| `KW_MODULE_HW` | module | قطعه | `qitaah` | hardware |
| `KW_ALWAYS` | always | همیشه | `hamiishah` | hardware |
| `KW_ASSIGN` | assign | تخصیصده | `takhsiisdah` | hardware |
| `KW_BEGIN` | begin | آغاز | `aaghaaza` | block |
| `KW_END` | end | پایان | `paayaana` | block |

### Paradigm: imperative

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | اگر | `agar` | control_flow |
| `KW_ELSE` | else | وگرنه | `vagarnah` | control_flow |
| `KW_ELIF` | elif | وگرنهاگر | `vagarnahagar` | control_flow |
| `KW_WHILE` | while | تازمانیکه | `taazamaaniikah` | control_flow |
| `KW_DO` | do | انجامبده | `anjaamabdah` | control_flow |
| `KW_FOR` | for | برای | `baraaya` | control_flow |
| `KW_BREAK` | break | بشکن | `bishkan` | control_flow |
| `KW_CONTINUE` | continue | ادامه | `adaamah` | control_flow |
| `KW_SWITCH` | switch | انتخاب | `intikhaaba` | control_flow |
| `KW_CASE` | case | حالت | `haalata` | control_flow |
| `KW_DEFAULT` | default | پیشفرض | `piishfarza` | control_flow |
| `KW_RETURN` | return | بازگرد | `baazgard` | control_flow |
| `KW_GOTO` | goto | برو | `birav` | control_flow |
| `KW_VAR` | var | متغیر | `mutaghayyira` | declaration |
| `KW_CONST` | const | ثابت | `saabita` | declaration |
| `KW_LET` | let | بگذار | `bigzaar` | declaration |
| `KW_INT` | int | صحیح | `sahiiha` | type |
| `KW_FLOAT` | float | اعشاری | `aeshaarii` | type |
| `KW_DOUBLE` | double | دوگانه | `daugaanah` | type |
| `KW_CHAR` | char | نویسه | `naviisah` | type |
| `KW_BOOL` | bool | منطقی | `mantiqii` | type |
| `KW_STRING` | string | رشته | `rishtah` | type |
| `KW_VOID` | void | تهی | `tahii` | type |
| `KW_TRUE` | true | درست | `durusta` | literal |
| `KW_FALSE` | false | نادرست | `naadurusta` | literal |
| `KW_NULL` | null | پوچ | `puuca` | literal |
| `KW_TRY` | try | تلاش | `talaasha` | exception |
| `KW_CATCH` | catch | بگیر | `bigiir` | exception |
| `KW_FINALLY` | finally | سرانجام | `saranjaama` | exception |
| `KW_THROW` | throw | پرتابکن | `partaabkun` | exception |
| `KW_RAISE` | raise | بالاببر | `baalaabbar` | exception |
| `KW_EXCEPT` | except | استثنا | `istisnaa` | exception |

### Paradigm: iot

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
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

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | قاعده | `qaaidah` | clause |
| `KW_FACT` | fact | واقعیت | `vaaqiiyata` | clause |
| `KW_QUERY` | query | پرسوجو | `parsavajuu` | clause |
| `KW_NOT` | not | نه | `nah` | operator |
| `KW_AND` | and | و | `va` | operator |
| `KW_OR` | or | یا | `yaa` | operator |

### Paradigm: memory

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
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

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | رده | `radah` | type_def |
| `KW_OBJECT` | object | شیء | `shaya` | type_def |
| `KW_INTERFACE` | interface | واسط | `vaasita` | type_def |
| `KW_EXTENDS` | extends | گسترش | `gustarisha` | inheritance |
| `KW_IMPLEMENTS` | implements | پیادهسازی | `piyaadahsaazii` | inheritance |
| `KW_NEW` | new | جدید | `jadiida` | instantiation |
| `KW_THIS` | this | این | `iin` | reference |
| `KW_SUPER` | super | ابر | `abara` | reference |
| `KW_PUBLIC` | public | عمومی | `umuumii` | access |
| `KW_PRIVATE` | private | خصوصی | `khusuusii` | access |
| `KW_PROTECTED` | protected | محافظتشده | `muhaafazatshudah` | access |
| `KW_STATIC` | static | ایستا | `iistaa` | storage |
| `KW_ABSTRACT` | abstract | انتزاعی | `intizaaii` | modifier |
| `KW_VIRTUAL` | virtual | مجازی | `majaazii` | modifier |
| `KW_OVERRIDE` | override | بازنویسی | `baaznaviisii` | modifier |

### Paradigm: procedural

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | تابع | `taabe` | subroutine |
| `KW_PROC` | procedure | رویه | `raviyah` | subroutine |
| `KW_CALL` | call | فراخوان | `faraakhvaan` | subroutine |
| `KW_PARAM` | param | پارامتر | `paaraamtara` | subroutine |
| `KW_YIELD` | yield | بده | `bidah` | coroutine |
| `KW_AWAIT` | await | منتظر | `muntazira` | async |
| `KW_ASYNC` | async | ناهمزمان | `naahamzamaana` | async |

### Paradigm: robotics

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
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

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | اشارهگر | `ishaarahgara` | memory |
| `KW_REF` | ref | ارجاع | `irjaae` | memory |
| `KW_ALLOC` | alloc | تخصیص | `takhsiisa` | memory |
| `KW_FREE` | free | آزاد | `aazaada` | memory |
| `KW_SIZEOF` | sizeof | اندازه | `andaazah` | memory |
| `KW_STRUCT` | struct | ساختار | `saakhtaara` | type_def |
| `KW_UNION` | union | اجتماع | `ijtimaae` | type_def |
| `KW_ENUM` | enum | شمارش | `shumaarisha` | type_def |
| `KW_TYPEDEF` | typedef | تعریفنوع | `taeriifnava` | type_def |
| `KW_VOLATILE` | volatile | فرار | `faraara` | modifier |
| `KW_REGISTER` | register | ثبات | `sabaata` | storage |
| `KW_EXTERN` | extern | بیرونی | `biiruunii` | linkage |
| `KW_INLINE` | inline | درونخطی | `daruunkhattii` | modifier |

### Paradigm: verification

| Construct | English | Persian | Romenagri (ASCII-7) | Category |
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

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Persian native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Persian a first-class systems-programming language, not a localized skin.

## Example

```
اگر (x > 0)        // romenagri: agar
    ...
وگرنه              // romenagri: vagarnah
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Persian keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*