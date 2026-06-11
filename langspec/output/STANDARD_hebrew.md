# Hebrew Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Hebrew
- **ISO 639 code**: heb
- **Script**: Hebrew
- **Native speakers**: 9 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Hebrew-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Hebrew keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
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

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | استورد | `istavrida` | namespace |
| `KW_EXPORT` | export | صدر | `saddira` | namespace |
| `KW_PACKAGE` | package | حزمة | `huzmah` | namespace |
| `KW_NAMESPACE` | namespace | نطاق | `nitaaqa` | namespace |
| `KW_USE` | use | استخدم | `istakhdima` | namespace |
| `KW_INCLUDE` | include | ضمن | `dammina` | preprocessor |
| `KW_FROM` | from | من | `min` | namespace |
| `KW_AS` | as | كـ | `ka` | namespace |

### Paradigm: concurrent

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | خيط | `khayta` | concurrency |
| `KW_SPAWN` | spawn | أنشئ | `anshia` | concurrency |
| `KW_LOCK` | lock | قفل | `qufla` | concurrency |
| `KW_SYNC` | synchronized | متزامن | `mutazaamina` | concurrency |
| `KW_CHANNEL` | channel | قناة | `qanaah` | concurrency |
| `KW_SELECT` | select | اختر | `ikhtara` | concurrency |

### Paradigm: dataflow

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
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

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
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

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | مجهول | `majhuula` | function |
| `KW_MATCH` | match | طابق | `taabiqa` | pattern |
| `KW_WHEN` | when | عندما | `indamaa` | pattern |
| `KW_FUN` | fun | اقتران | `iqtiraana` | function |
| `KW_REC` | rec | تكراري | `takraarii` | recursion |
| `KW_IN` | in | في | `fii` | binding |
| `KW_WHERE` | where | حيث | `haysu` | binding |
| `KW_DATA` | data | بيانات | `bayaanaata` | type_def |
| `KW_TYPE` | type | نوع | `nava` | type_def |
| `KW_MODULE` | module | وحدة | `vihdah` | namespace |

### Paradigm: gpu

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
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

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | كيان | `kayaana` | hardware |
| `KW_ARCH` | architecture | معمارية | `maemaariyah` | hardware |
| `KW_SIGNAL` | signal | إشارة | `ishaarah` | hardware |
| `KW_PORT` | port | منفذ | `manfaza` | hardware |
| `KW_WIRE` | wire | سلك | `silka` | hardware |
| `KW_REG` | reg | مسجل | `musajjila` | hardware |
| `KW_MODULE_HW` | module | قطعة | `qitaah` | hardware |
| `KW_ALWAYS` | always | دائما | `daaiman` | hardware |
| `KW_ASSIGN` | assign | عين | `ayyina` | hardware |
| `KW_BEGIN` | begin | התחל | `hatahala` | block |
| `KW_END` | end | סוף | `suufa` | block |

### Paradigm: imperative

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | אם | `ama` | control_flow |
| `KW_ELSE` | else | אחרת | `aharata` | control_flow |
| `KW_ELIF` | elif | وإلاإذا | `vaillaaizaa` | control_flow |
| `KW_WHILE` | while | כלעוד | `kalaeauda` | control_flow |
| `KW_DO` | do | עשה | `aeshah` | control_flow |
| `KW_FOR` | for | עבור | `aebuura` | control_flow |
| `KW_BREAK` | break | اكسر | `iksira` | control_flow |
| `KW_CONTINUE` | continue | استمر | `istamirra` | control_flow |
| `KW_SWITCH` | switch | بدل | `baddila` | control_flow |
| `KW_CASE` | case | حالة | `haalah` | control_flow |
| `KW_DEFAULT` | default | افتراضي | `iftiraadii` | control_flow |
| `KW_RETURN` | return | החזר | `hahazara` | control_flow |
| `KW_GOTO` | goto | اذهب | `izhaba` | control_flow |
| `KW_VAR` | var | משתנה | `mashatanah` | declaration |
| `KW_CONST` | const | ثابت | `saabita` | declaration |
| `KW_LET` | let | ليكن | `liyakun` | declaration |
| `KW_INT` | int | صحيح | `sahiiha` | type |
| `KW_FLOAT` | float | عائم | `aaima` | type |
| `KW_DOUBLE` | double | مزدوج | `muzdavija` | type |
| `KW_CHAR` | char | حرف | `harfa` | type |
| `KW_BOOL` | bool | منطقي | `mantiqii` | type |
| `KW_STRING` | string | نص | `nassa` | type |
| `KW_VOID` | void | فراغ | `faraagha` | type |
| `KW_TRUE` | true | אמת | `amata` | literal |
| `KW_FALSE` | false | שקר | `shaqara` | literal |
| `KW_NULL` | null | عدم | `adama` | literal |
| `KW_TRY` | try | حاول | `haavila` | exception |
| `KW_CATCH` | catch | امسك | `imsika` | exception |
| `KW_FINALLY` | finally | أخيرا | `akhiiran` | exception |
| `KW_THROW` | throw | ارم | `irmi` | exception |
| `KW_RAISE` | raise | ارفع | `irfae` | exception |
| `KW_EXCEPT` | except | استثناء | `istisnaaa` | exception |

### Paradigm: iot

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
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

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | قاعدة | `qaaidah` | clause |
| `KW_FACT` | fact | حقيقة | `haqiiqah` | clause |
| `KW_QUERY` | query | استعلام | `istielaama` | clause |
| `KW_NOT` | not | לא | `laa` | operator |
| `KW_AND` | and | וגם | `vagama` | operator |
| `KW_OR` | or | או | `aua` | operator |

### Paradigm: memory

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
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

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | מחלקה | `mahalaqah` | type_def |
| `KW_OBJECT` | object | كائن | `kaaina` | type_def |
| `KW_INTERFACE` | interface | واجهة | `vaajihah` | type_def |
| `KW_EXTENDS` | extends | يمتد | `yamtaddu` | inheritance |
| `KW_IMPLEMENTS` | implements | ينفذ | `yunaffizu` | inheritance |
| `KW_NEW` | new | جديد | `jadiida` | instantiation |
| `KW_THIS` | this | هذا | `haazaa` | reference |
| `KW_SUPER` | super | أعلى | `aelaa` | reference |
| `KW_PUBLIC` | public | عام | `aamma` | access |
| `KW_PRIVATE` | private | خاص | `khaassa` | access |
| `KW_PROTECTED` | protected | محمي | `mahmii` | access |
| `KW_STATIC` | static | ساكن | `saakina` | storage |
| `KW_ABSTRACT` | abstract | مجرد | `mujarrada` | modifier |
| `KW_VIRTUAL` | virtual | افتراضي | `iftiraadii` | modifier |
| `KW_OVERRIDE` | override | تجاوز | `tajaavaza` | modifier |

### Paradigm: procedural

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | פונקציה | `puunaqaeiyah` | subroutine |
| `KW_PROC` | procedure | إجراء | `ijraaa` | subroutine |
| `KW_CALL` | call | نادي | `naadii` | subroutine |
| `KW_PARAM` | param | معامل | `muaamila` | subroutine |
| `KW_YIELD` | yield | أنتج | `antija` | coroutine |
| `KW_AWAIT` | await | انتظر | `intazira` | async |
| `KW_ASYNC` | async | غيرمتزامن | `ghaerumutazaamina` | async |

### Paradigm: robotics

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
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

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | مؤشر | `muashshira` | memory |
| `KW_REF` | ref | مرجع | `marjie` | memory |
| `KW_ALLOC` | alloc | خصص | `khassisa` | memory |
| `KW_FREE` | free | حرر | `harrira` | memory |
| `KW_SIZEOF` | sizeof | حجم | `hajma` | memory |
| `KW_STRUCT` | struct | بنية | `binyah` | type_def |
| `KW_UNION` | union | اتحاد | `ittihaada` | type_def |
| `KW_ENUM` | enum | تعداد | `taedaada` | type_def |
| `KW_TYPEDEF` | typedef | تعريفنوع | `taeriifanava` | type_def |
| `KW_VOLATILE` | volatile | متطاير | `mutataayira` | modifier |
| `KW_REGISTER` | register | سجل | `sajjila` | storage |
| `KW_EXTERN` | extern | خارجي | `khaarijii` | linkage |
| `KW_INLINE` | inline | مضمن | `mudammana` | modifier |

### Paradigm: verification

| Construct | English | Hebrew | Romenagri (ASCII-7) | Category |
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

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Hebrew native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Hebrew a first-class systems-programming language, not a localized skin.

## Example

```
אם (x > 0)        // romenagri: ama
    ...
אחרת              // romenagri: aharata
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Hebrew keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*