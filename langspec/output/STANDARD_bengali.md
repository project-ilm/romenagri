# Bengali Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Bengali
- **ISO 639 code**: ben
- **Script**: Bengali
- **Native speakers**: 270 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Bengali-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Bengali keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
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

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | আমদানি | `aamadaani` | namespace |
| `KW_EXPORT` | export | রপ্তানি | `raptaani` | namespace |
| `KW_PACKAGE` | package | মোড়ক | `mau_daka` | namespace |
| `KW_NAMESPACE` | namespace | নামাকাশ | `naamaakaasha` | namespace |
| `KW_USE` | use | উপযোগ | `upayauga` | namespace |
| `KW_INCLUDE` | include | অন্তর্ভা঵ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | তঃ | `ta_h` | namespace |
| `KW_AS` | as | ই঵ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | সুতা | `sutaa` | concurrency |
| `KW_SPAWN` | spawn | উৎপন্ন | `uutpanna` | concurrency |
| `KW_LOCK` | lock | তালা | `taalaa` | concurrency |
| `KW_SYNC` | synchronized | সমলয় | `samalaya` | concurrency |
| `KW_CHANNEL` | channel | মাধ্যম | `maadhyama` | concurrency |
| `KW_SELECT` | select | বাছো | `baachau` | concurrency |

### Paradigm: dataflow

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
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

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
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

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | অনামা | `anaamaa` | function |
| `KW_MATCH` | match | মিল | `mila` | pattern |
| `KW_WHEN` | when | যখন | `yakhana` | pattern |
| `KW_FUN` | fun | ফলন | `phalana` | function |
| `KW_REC` | rec | পুনরাবৃত্ত | `punaraabr_tta` | recursion |
| `KW_IN` | in | মধ্যে | `madhyee` | binding |
| `KW_WHERE` | where | যেখানে | `yeekhaanee` | binding |
| `KW_DATA` | data | উপাত্ত | `upaatta` | type_def |
| `KW_TYPE` | type | প্রকার | `prakaara` | type_def |
| `KW_MODULE` | module | অংশ | `a_nsha` | namespace |

### Paradigm: gpu

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
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

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | সত্তা | `sattaa` | hardware |
| `KW_ARCH` | architecture | স্থাপত্য | `sthaapatya` | hardware |
| `KW_SIGNAL` | signal | সংকেত | `sa_nkeeta` | hardware |
| `KW_PORT` | port | দ্বার | `dbaara` | hardware |
| `KW_WIRE` | wire | তার | `taara` | hardware |
| `KW_REG` | reg | নিবন্ধক | `nibandhaka` | hardware |
| `KW_MODULE_HW` | module | যন্ত্রাংশ | `yantraa_nsha` | hardware |
| `KW_ALWAYS` | always | সর্বদা | `sarbadaa` | hardware |
| `KW_ASSIGN` | assign | নির্ধারণ | `nirdhaara_na` | hardware |
| `KW_BEGIN` | begin | শুরু | `shuru` | block |
| `KW_END` | end | শেষ | `sheesa` | block |

### Paradigm: imperative

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | যদি | `yadi` | control_flow |
| `KW_ELSE` | else | অন্যথা | `anyathaa` | control_flow |
| `KW_ELIF` | elif | নতুবা_যদি | `natubaa_yadi` | control_flow |
| `KW_WHILE` | while | যতক্ষণ | `yatak_sa_na` | control_flow |
| `KW_DO` | do | করো | `karau` | control_flow |
| `KW_FOR` | for | জন্য | `janya` | control_flow |
| `KW_BREAK` | break | বিরতি | `birati` | control_flow |
| `KW_CONTINUE` | continue | চালু | `caalu` | control_flow |
| `KW_SWITCH` | switch | নির্বাচন | `nirbaacana` | control_flow |
| `KW_CASE` | case | ক্ষেত্র | `k_seetra` | control_flow |
| `KW_DEFAULT` | default | পূর্বনির্ধারিত | `puurbanirdhaarita` | control_flow |
| `KW_RETURN` | return | ফেরত | `pheerata` | control_flow |
| `KW_GOTO` | goto | যাও | `yaaau` | control_flow |
| `KW_VAR` | var | চল | `cala` | declaration |
| `KW_CONST` | const | ধ্রুবক | `dhrubaka` | declaration |
| `KW_LET` | let | ধরি | `dhari` | declaration |
| `KW_INT` | int | পূর্ণসংখ্যা | `puur_nasa_nkhyaa` | type |
| `KW_FLOAT` | float | দশমিক | `dashamika` | type |
| `KW_DOUBLE` | double | দ্বিগুণ | `dbigu_na` | type |
| `KW_CHAR` | char | অক্ষর | `ak_sara` | type |
| `KW_BOOL` | bool | যৌক্তিক | `yauktika` | type |
| `KW_STRING` | string | বাক্য | `baakya` | type |
| `KW_VOID` | void | শূন্য | `shuunya` | type |
| `KW_TRUE` | true | সত্য | `satya` | literal |
| `KW_FALSE` | false | মিথ্যা | `mithyaa` | literal |
| `KW_NULL` | null | ফাঁকা | `phaa_nkaa` | literal |
| `KW_TRY` | try | চেষ্টা | `cee_staa` | exception |
| `KW_CATCH` | catch | ধরো | `dharau` | exception |
| `KW_FINALLY` | finally | অবশেষে | `abasheesee` | exception |
| `KW_THROW` | throw | ছোড়ো | `chau_dau` | exception |
| `KW_RAISE` | raise | তোলো | `taulau` | exception |
| `KW_EXCEPT` | except | ব্যতিক্রম | `byatikrama` | exception |

### Paradigm: iot

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
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

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | নিয়ম | `niyama` | clause |
| `KW_FACT` | fact | তথ্য | `tathya` | clause |
| `KW_QUERY` | query | প্রশ্ন | `prashna` | clause |
| `KW_NOT` | not | নয় | `naya` | operator |
| `KW_AND` | and | এবং | `eeba_n` | operator |
| `KW_OR` | or | অথবা | `athabaa` | operator |

### Paradigm: memory

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
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

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | শ্রেণী | `shree_nii` | type_def |
| `KW_OBJECT` | object | বস্তু | `bastu` | type_def |
| `KW_INTERFACE` | interface | সংযোগস্থল | `sa_nyaugasthala` | type_def |
| `KW_EXTENDS` | extends | সম্প্রসারিত | `samprasaarita` | inheritance |
| `KW_IMPLEMENTS` | implements | বাস্তবায়িত | `baastabaayita` | inheritance |
| `KW_NEW` | new | নতুন | `natuna` | instantiation |
| `KW_THIS` | this | এই | `eei` | reference |
| `KW_SUPER` | super | পরম | `parama` | reference |
| `KW_PUBLIC` | public | সর্বজনীন | `sarbajaniina` | access |
| `KW_PRIVATE` | private | ব্যক্তিগত | `byaktigata` | access |
| `KW_PROTECTED` | protected | সুরক্ষিত | `surak_sita` | access |
| `KW_STATIC` | static | স্থির | `sthira` | storage |
| `KW_ABSTRACT` | abstract | বিমূর্ত | `bimuurta` | modifier |
| `KW_VIRTUAL` | virtual | আভাসী | `aabhaasii` | modifier |
| `KW_OVERRIDE` | override | অধিরোহণ | `adhirauha_na` | modifier |

### Paradigm: procedural

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | কাজ | `kaaja` | subroutine |
| `KW_PROC` | procedure | প্রক্রিয়া | `prakriyaa` | subroutine |
| `KW_CALL` | call | ডাকো | `daakau` | subroutine |
| `KW_PARAM` | param | প্রাচল | `praacala` | subroutine |
| `KW_YIELD` | yield | দাও | `daaau` | coroutine |
| `KW_AWAIT` | await | অপেক্ষা | `apeek_saa` | async |
| `KW_ASYNC` | async | অসমলয় | `asamalaya` | async |

### Paradigm: robotics

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
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

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | নির্দেশক | `nirdeeshaka` | memory |
| `KW_REF` | ref | উল্লেখ | `ulleekha` | memory |
| `KW_ALLOC` | alloc | বরাদ্দ | `baraadda` | memory |
| `KW_FREE` | free | মুক্ত | `mukta` | memory |
| `KW_SIZEOF` | sizeof | আকার | `aakaara` | memory |
| `KW_STRUCT` | struct | কাঠামো | `kaathaamau` | type_def |
| `KW_UNION` | union | সংঘ | `sa_ngha` | type_def |
| `KW_ENUM` | enum | গণনা | `ga_nanaa` | type_def |
| `KW_TYPEDEF` | typedef | প্রকারলেখ | `prakaaraleekha` | type_def |
| `KW_VOLATILE` | volatile | অস্থির | `asthira` | modifier |
| `KW_REGISTER` | register | নিবন্ধ | `nibandha` | storage |
| `KW_EXTERN` | extern | বাহ্যিক | `baahyika` | linkage |
| `KW_INLINE` | inline | অন্তঃরেখ | `anta_hreekha` | modifier |

### Paradigm: verification

| Construct | English | Bengali | Romenagri (ASCII-7) | Category |
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

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Bengali native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Bengali a first-class systems-programming language, not a localized skin.

## Example

```
যদি (x > 0)        // romenagri: yadi
    ...
অন্যথা              // romenagri: anyathaa
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Bengali keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*