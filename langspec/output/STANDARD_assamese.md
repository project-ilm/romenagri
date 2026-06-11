# Assamese Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Assamese
- **ISO 639 code**: asm
- **Script**: Assamese (Bengali-Assamese)
- **Native speakers**: 23 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Assamese-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Assamese keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | প্রদিশ | `pradisha` | ml |
| `KW_MATRIX` | matrix | আ঵্যূহ | `aavyuuha` | ml |
| `KW_VECTOR` | vector | সদিশ | `sadisha` | ml |
| `KW_GRAD` | gradient | প্র঵ণতা | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | প্রতিপ্রসার | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | অগ্রপ্রসার | `agraprasaara` | ml |
| `KW_LAYER` | layer | স্তর | `stara` | ml |
| `KW_MODEL` | model | প্রতিমান | `pratimaana` | ml |
| `KW_TRAIN` | train | প্রশিক্ষণ | `prashik_sa_na` | ml |
| `KW_INFER` | infer | অনুমান | `anumaana` | ml |
| `KW_LOSS` | loss | হানি | `haani` | ml |
| `KW_OPTIMIZE` | optimize | অনুকূলন | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | সক্রিযণ | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | ভার | `bhaara` | ml |
| `KW_BIAS` | bias | পক্ষপাত | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | কল্প | `kalpa` | ml |
| `KW_BATCH` | batch | পুঞ্জ | `pu_nja` | ml |
| `KW_DATASET` | dataset | দত্তসমূহ | `dattasamuuha` | ml |
| `KW_EMBED` | embed | নি঵েশন | `niveeshana` | ml |
| `KW_ATTENTION` | attention | অ঵ধান | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | আনযন | `aanayana` | namespace |
| `KW_EXPORT` | export | নির্যাপণ | `niryaapa_na` | namespace |
| `KW_PACKAGE` | package | পুটক | `putaka` | namespace |
| `KW_NAMESPACE` | namespace | নামাকাশ | `naamaakaasha` | namespace |
| `KW_USE` | use | উপযোগ | `upayauga` | namespace |
| `KW_INCLUDE` | include | অন্তর্ভা঵ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | তঃ | `ta_h` | namespace |
| `KW_AS` | as | ই঵ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | তন্তু | `tantu` | concurrency |
| `KW_SPAWN` | spawn | উত্পাদ | `utpaada` | concurrency |
| `KW_LOCK` | lock | তালক | `taalaka` | concurrency |
| `KW_SYNC` | synchronized | সমকাল | `samakaala` | concurrency |
| `KW_CHANNEL` | channel | মার্গ | `maarga` | concurrency |
| `KW_SELECT` | select | ঵ৃণু | `vr_nu` | concurrency |

### Paradigm: dataflow

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | ধারা | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | প্রণাল | `pra_naala` | reactive |
| `KW_MAP` | map | প্রতিচিত্র | `praticitra` | reactive |
| `KW_FILTER` | filter | ছাল | `chaala` | reactive |
| `KW_REDUCE` | reduce | ন্যূনীকৃ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | সং঵েষ্ট | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | নিরীক্ষ | `niriik_sa` | reactive |
| `KW_EMIT` | emit | উত্সৃজ | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | অভিনি঵েশ | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | স্পন্দশোধন | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | গ্রন্থি | `granthi` | cluster |
| `KW_REPLICA` | replica | প্রতিকৃতি | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | সর্঵সম্মতি | `sarvasammati` | cluster |
| `KW_SHARD` | shard | খণ্ড | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | জন঵াদ | `janavaada` | cluster |
| `KW_LEADER` | leader | নাযক | `naayaka` | cluster |
| `KW_RPC` | rpc | দূরপ্রক্রিযা | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | কর্তৃ | `kartr_` | cluster |
| `KW_MESSAGE` | message | সন্দেশ | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | অনামন্ | `anaaman` | function |
| `KW_MATCH` | match | মেল | `meela` | pattern |
| `KW_WHEN` | when | যদা | `yadaa` | pattern |
| `KW_FUN` | fun | ফল | `phala` | function |
| `KW_REC` | rec | পুনরা঵ৃত্ত | `punaraavr_tta` | recursion |
| `KW_IN` | in | অন্তঃ | `anta_h` | binding |
| `KW_WHERE` | where | যত্র | `yatra` | binding |
| `KW_DATA` | data | দত্ত | `datta` | type_def |
| `KW_TYPE` | type | প্রকার | `prakaara` | type_def |
| `KW_MODULE` | module | খণ্ড | `kha_nda` | namespace |

### Paradigm: gpu

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | বীজ | `biija` | compute |
| `KW_DEVICE` | device | যন্ত্র | `yantra` | compute |
| `KW_HOST` | host | আতিথেয | `aatitheeya` | compute |
| `KW_GLOBAL` | global | ঵ৈশ্঵িক | `vaishvika` | compute |
| `KW_SHARED` | shared | সহভাজিত | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | তন্ত্঵ঙ্ক | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | খণ্ডাঙ্ক | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | জাল | `jaala` | compute |
| `KW_BARRIER` | barrier | অ঵রোধ | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | আণ঵িক | `aa_navika` | compute |
| `KW_WARP` | warp | তন্তুসমূহ | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | সত্তা | `sattaa` | hardware |
| `KW_ARCH` | architecture | স্থাপত্য | `sthaapatya` | hardware |
| `KW_SIGNAL` | signal | সঙ্কেত | `sa_nkeeta` | hardware |
| `KW_PORT` | port | দ্঵ার | `dvaara` | hardware |
| `KW_WIRE` | wire | তন্তু | `tantu` | hardware |
| `KW_REG` | reg | পঞ্জী | `pa_njii` | hardware |
| `KW_MODULE_HW` | module | অংশ | `a_nsha` | hardware |
| `KW_ALWAYS` | always | সদা | `sadaa` | hardware |
| `KW_ASSIGN` | assign | নিযুক্ত | `niyukta` | hardware |
| `KW_BEGIN` | begin | আৰম্ভ | `aarambha` | block |
| `KW_END` | end | শেষ | `sheesa` | block |

### Paradigm: imperative

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | যদি | `yadi` | control_flow |
| `KW_ELSE` | else | অন্যথা | `anyathaa` | control_flow |
| `KW_ELIF` | elif | নোচেদ্যদি | `naucheedyadi` | control_flow |
| `KW_WHILE` | while | যেতিয়ালৈ | `yeetiyaalai` | control_flow |
| `KW_DO` | do | কৰা | `karaa` | control_flow |
| `KW_FOR` | for | বাবে | `baabee` | control_flow |
| `KW_BREAK` | break | ভঙ্গ | `bha_nga` | control_flow |
| `KW_CONTINUE` | continue | অনু঵র্ত | `anuvarta` | control_flow |
| `KW_SWITCH` | switch | ঵িকল্প | `vikalpa` | control_flow |
| `KW_CASE` | case | পক্ষ | `pak_sa` | control_flow |
| `KW_DEFAULT` | default | স্঵ভা঵ | `svabhaava` | control_flow |
| `KW_RETURN` | return | ঘূৰাই | `ghuuraai` | control_flow |
| `KW_GOTO` | goto | গচ্ছ | `gaccha` | control_flow |
| `KW_VAR` | var | চর | `cara` | declaration |
| `KW_CONST` | const | ধ্রু঵ | `dhruva` | declaration |
| `KW_LET` | let | অস্তু | `astu` | declaration |
| `KW_INT` | int | পূর্ণাঙ্ক | `puur_naa_nka` | type |
| `KW_FLOAT` | float | ভিন্ন | `bhinna` | type |
| `KW_DOUBLE` | double | দ্঵িগুণ | `dviguu_na` | type |
| `KW_CHAR` | char | ঵র্ণ | `var_na` | type |
| `KW_BOOL` | bool | তার্কিক | `taarkika` | type |
| `KW_STRING` | string | পদা঵লী | `padaavalii` | type |
| `KW_VOID` | void | শূন্য | `shuunya` | type |
| `KW_TRUE` | true | সঁচা | `sa_ncaa` | literal |
| `KW_FALSE` | false | মিছা | `michaa` | literal |
| `KW_NULL` | null | রিক্ত | `rikta` | literal |
| `KW_TRY` | try | যত্ন | `yatna` | exception |
| `KW_CATCH` | catch | গৃহাণ | `gr_haa_na` | exception |
| `KW_FINALLY` | finally | অন্ততঃ | `antata_h` | exception |
| `KW_THROW` | throw | ক্ষিপ | `k_sipa` | exception |
| `KW_RAISE` | raise | উত্থাপয | `utthaapaya` | exception |
| `KW_EXCEPT` | except | অপ঵াদ | `apavaada` | exception |

### Paradigm: iot

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | কীলক | `kiilaka` | io |
| `KW_READ` | read | পঠ | `patha` | io |
| `KW_WRITE` | write | লিখ | `likha` | io |
| `KW_ANALOG` | analog | সদৃশ | `sadr_sha` | io |
| `KW_DIGITAL` | digital | অঙ্কীয | `a_nkiiya` | io |
| `KW_PWM` | pwm | স্পন্দ঵িস্তার | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | ঵িঘ্ন | `vighna` | io |
| `KW_TIMER` | timer | কালযন্ত্র | `kaalayantra` | io |
| `KW_SENSOR` | sensor | সং঵েদক | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | প্র঵র্তক | `pravartaka` | io |
| `KW_BUS` | bus | মার্গ | `maarga` | io |
| `KW_PROTOCOL` | protocol | নিযমা঵লী | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | সুষুপ্তি | `su_supti` | power |
| `KW_WAKE` | wake | জাগৃ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | সূত্র | `suutra` | clause |
| `KW_FACT` | fact | তথ্য | `tathya` | clause |
| `KW_QUERY` | query | প্রশ্ন | `prashna` | clause |
| `KW_NOT` | not | নহয় | `nahaya` | operator |
| `KW_AND` | and | আৰু | `aaru` | operator |
| `KW_OR` | or | বা | `baa` | operator |

### Paradigm: memory

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | স্঵ামিত্঵ | `svaamitva` | ownership |
| `KW_BORROW` | borrow | ঋণ | `r_na` | ownership |
| `KW_MOVE` | move | স্থানান্তর | `sthaanaantara` | ownership |
| `KW_MUT` | mut | পরি঵র্ত্য | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | আযুষ্কাল | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | ক্ষেত্র | `k_seetra` | allocation |
| `KW_GC` | gc | মলসংগ্রহ | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | স্মৃতিকীলক | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | শ্ৰেণী | `shree_nii` | type_def |
| `KW_OBJECT` | object | ঵স্তু | `vastu` | type_def |
| `KW_INTERFACE` | interface | সন্ধি | `sandhi` | type_def |
| `KW_EXTENDS` | extends | ঵িস্তৃত | `vistr_ta` | inheritance |
| `KW_IMPLEMENTS` | implements | নিষ্পাদিত | `ni_spaadita` | inheritance |
| `KW_NEW` | new | নূতন | `nuutana` | instantiation |
| `KW_THIS` | this | এতত্ | `eetat` | reference |
| `KW_SUPER` | super | পর | `para` | reference |
| `KW_PUBLIC` | public | সার্঵জনিক | `saarvajanika` | access |
| `KW_PRIVATE` | private | গুপ্ত | `gupta` | access |
| `KW_PROTECTED` | protected | রক্ষিত | `rak_sita` | access |
| `KW_STATIC` | static | স্থির | `sthira` | storage |
| `KW_ABSTRACT` | abstract | অমূর্ত | `amuurta` | modifier |
| `KW_VIRTUAL` | virtual | আভাস | `aabhaasa` | modifier |
| `KW_OVERRIDE` | override | অধিরোহ | `adhirauha` | modifier |

### Paradigm: procedural

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | কাৰ্য | `kaarya` | subroutine |
| `KW_PROC` | procedure | ঵িধি | `vidhi` | subroutine |
| `KW_CALL` | call | আহ্঵ান | `aahvaana` | subroutine |
| `KW_PARAM` | param | প্রাচল | `praacala` | subroutine |
| `KW_YIELD` | yield | দা | `daa` | coroutine |
| `KW_AWAIT` | await | প্রতীক্ষ | `pratiik_sa` | async |
| `KW_ASYNC` | async | অসমকাল | `asamakaala` | async |

### Paradigm: robotics

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | চালক | `caalaka` | control |
| `KW_SERVO` | servo | অনুচালক | `anucaalaka` | control |
| `KW_JOINT` | joint | সন্ধি | `sandhi` | control |
| `KW_POSE` | pose | মুদ্রা | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | প্রক্ষেপপথ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | প্রতিপুষ্টি | `pratipu_sti` | control |
| `KW_PID` | pid | নিযন্ত্রক | `niyantraka` | control |
| `KW_DEADLINE` | deadline | কালসীমা | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | আ঵র্তিক | `aavartika` | realtime |
| `KW_PRIORITY` | priority | প্রাথম্য | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | প্র঵র্তয | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | প্রত্যক্ষ | `pratyak_sa` | control |
| `KW_PLAN` | plan | যোজনা | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | নির্দেশক | `nirdeeshaka` | memory |
| `KW_REF` | ref | সন্দর্ভ | `sandarbha` | memory |
| `KW_ALLOC` | alloc | আ঵ণ্টন | `aava_ntana` | memory |
| `KW_FREE` | free | মুক্ত | `mukta` | memory |
| `KW_SIZEOF` | sizeof | পরিমাণ | `parimaa_na` | memory |
| `KW_STRUCT` | struct | সংরচনা | `sa_nracanaa` | type_def |
| `KW_UNION` | union | সঙ্ঘ | `sa_ngha` | type_def |
| `KW_ENUM` | enum | গণনা | `ga_nanaa` | type_def |
| `KW_TYPEDEF` | typedef | প্রকারনির্দেশ | `prakaaranirdeesha` | type_def |
| `KW_VOLATILE` | volatile | চঞ্চল | `ca_ncala` | modifier |
| `KW_REGISTER` | register | পঞ্জিকা | `pa_njikaa` | storage |
| `KW_EXTERN` | extern | বাহ্য | `baahya` | linkage |
| `KW_INLINE` | inline | অন্তঃস্থ | `anta_hstha` | modifier |

### Paradigm: verification

| Construct | English | Assamese | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | অপেক্ষতে | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | সুনিশ্চযতি | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | অপরি঵র্ত্য | `aparivartya` | contract |
| `KW_ASSERT` | assert | প্রতিজ্ঞা | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | অধ্য঵স্যতি | `adhyavasyati` | contract |
| `KW_PROVE` | prove | সাধযতি | `saadhayati` | contract |
| `KW_REFINES` | refines | পরিষ্করোতি | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | প্রতিমানপরীক্ষা | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Assamese native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Assamese a first-class systems-programming language, not a localized skin.

## Example

```
যদি (x > 0)        // romenagri: yadi
    ...
অন্যথা              // romenagri: anyathaa
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Assamese keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*