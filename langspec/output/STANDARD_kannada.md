# Kannada Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Kannada
- **ISO 639 code**: kan
- **Script**: Kannada
- **Native speakers**: 60 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Kannada-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Kannada keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | ಪ್ರದಿಶ | `pradisha` | ml |
| `KW_MATRIX` | matrix | ಆವ್ಯೂಹ | `aavyuuha` | ml |
| `KW_VECTOR` | vector | ಸದಿಶ | `sadisha` | ml |
| `KW_GRAD` | gradient | ಪ್ರವಣತಾ | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | ಪ್ರತಿಪ್ರಸಾರ | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | ಅಗ್ರಪ್ರಸಾರ | `agraprasaara` | ml |
| `KW_LAYER` | layer | ಸ್ತರ | `stara` | ml |
| `KW_MODEL` | model | ಪ್ರತಿಮಾನ | `pratimaana` | ml |
| `KW_TRAIN` | train | ಪ್ರಶಿಕ್ಷಣ | `prashik_sa_na` | ml |
| `KW_INFER` | infer | ಅನುಮಾನ | `anumaana` | ml |
| `KW_LOSS` | loss | ಹಾನಿ | `haani` | ml |
| `KW_OPTIMIZE` | optimize | ಅನುಕೂಲನ | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | ಸಕ್ರಿಯಣ | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | ಭಾರ | `bhaara` | ml |
| `KW_BIAS` | bias | ಪಕ್ಷಪಾತ | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | ಕಲ್ಪ | `kalpa` | ml |
| `KW_BATCH` | batch | ಪುಞ್ಜ | `pu_nja` | ml |
| `KW_DATASET` | dataset | ದತ್ತಸಮೂಹ | `dattasamuuha` | ml |
| `KW_EMBED` | embed | ನಿವೇಶನ | `niveeshana` | ml |
| `KW_ATTENTION` | attention | ಅವಧಾನ | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | ಆಮದು | `aamadu` | namespace |
| `KW_EXPORT` | export | ರಫ್ತು | `raphtu` | namespace |
| `KW_PACKAGE` | package | ಪೊಟ್ಟಣ | `pottana` | namespace |
| `KW_NAMESPACE` | namespace | ನಾಮಾಕಾಶ | `naamaakaasha` | namespace |
| `KW_USE` | use | ಉಪಯೋಗ | `upayauga` | namespace |
| `KW_INCLUDE` | include | ಅನ್ತರ್ಭಾವ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | ತಃ | `ta_h` | namespace |
| `KW_AS` | as | ಇವ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | ಎಳೆ | `ele` | concurrency |
| `KW_SPAWN` | spawn | ಸೃಷ್ಟಿಸು | `sr_stisu` | concurrency |
| `KW_LOCK` | lock | ಬೀಗ | `biiga` | concurrency |
| `KW_SYNC` | synchronized | ಸಮಕಾಲೀಕರಣ | `samakaaliikara_na` | concurrency |
| `KW_CHANNEL` | channel | ಮಾರ್ಗ | `maarga` | concurrency |
| `KW_SELECT` | select | ಆರಿಸು | `aarisu` | concurrency |

### Paradigm: dataflow

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | ಧಾರಾ | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | ಪ್ರಣಾಲ | `pra_naala` | reactive |
| `KW_MAP` | map | ಪ್ರತಿಚಿತ್ರ | `praticitra` | reactive |
| `KW_FILTER` | filter | ಛಾಲ | `chaala` | reactive |
| `KW_REDUCE` | reduce | ನ್ಯೂನೀಕೃ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | ಸಂವೇಷ್ಟ | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | ನಿರೀಕ್ಷ | `niriik_sa` | reactive |
| `KW_EMIT` | emit | ಉತ್ಸೃಜ | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | ಅಭಿನಿವೇಶ | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | ಸ್ಪನ್ದಶೋಧನ | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | ಗ್ರನ್ಥಿ | `granthi` | cluster |
| `KW_REPLICA` | replica | ಪ್ರತಿಕೃತಿ | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | ಸರ್ವಸಮ್ಮತಿ | `sarvasammati` | cluster |
| `KW_SHARD` | shard | ಖಣ್ಡ | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | ಜನವಾದ | `janavaada` | cluster |
| `KW_LEADER` | leader | ನಾಯಕ | `naayaka` | cluster |
| `KW_RPC` | rpc | ದೂರಪ್ರಕ್ರಿಯಾ | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | ಕರ್ತೃ | `kartr_` | cluster |
| `KW_MESSAGE` | message | ಸನ್ದೇಶ | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | ಅನಾಮಿಕ | `anaamika` | function |
| `KW_MATCH` | match | ಹೊಂದಿಸು | `ho_ndisu` | pattern |
| `KW_WHEN` | when | ಯಾವಾಗ | `yaavaaga` | pattern |
| `KW_FUN` | fun | ಫಲನ | `phalana` | function |
| `KW_REC` | rec | ಪುನರಾವರ್ತಿತ | `punaraavartita` | recursion |
| `KW_IN` | in | ಒಳಗೆ | `olage` | binding |
| `KW_WHERE` | where | ಎಲ್ಲಿ | `elli` | binding |
| `KW_DATA` | data | ದತ್ತಾಂಶ | `dattaa_nsha` | type_def |
| `KW_TYPE` | type | ಪ್ರಕಾರ | `prakaara` | type_def |
| `KW_MODULE` | module | ಘಟಕ | `ghataka` | namespace |

### Paradigm: gpu

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | ಬೀಜ | `biija` | compute |
| `KW_DEVICE` | device | ಯನ್ತ್ರ | `yantra` | compute |
| `KW_HOST` | host | ಆತಿಥೇಯ | `aatitheeya` | compute |
| `KW_GLOBAL` | global | ವೈಶ್ವಿಕ | `vaishvika` | compute |
| `KW_SHARED` | shared | ಸಹಭಾಜಿತ | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | ತನ್ತ್ವಙ್ಕ | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | ಖಣ್ಡಾಙ್ಕ | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | ಜಾಲ | `jaala` | compute |
| `KW_BARRIER` | barrier | ಅವರೋಧ | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | ಆಣವಿಕ | `aa_navika` | compute |
| `KW_WARP` | warp | ತನ್ತುಸಮೂಹ | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | ಅಸ್ತಿತ್ವ | `astitva` | hardware |
| `KW_ARCH` | architecture | ವಾಸ್ತುಶಿಲ್ಪ | `vaastushilpa` | hardware |
| `KW_SIGNAL` | signal | ಸಂಕೇತ | `sa_nkeeta` | hardware |
| `KW_PORT` | port | ಬಂದರು | `ba_ndaru` | hardware |
| `KW_WIRE` | wire | ತಂತಿ | `ta_nti` | hardware |
| `KW_REG` | reg | ನೋಂದಕ | `nau_ndaka` | hardware |
| `KW_MODULE_HW` | module | ಭಾಗ | `bhaaga` | hardware |
| `KW_ALWAYS` | always | ಯಾವಾಗಲೂ | `yaavaagaluu` | hardware |
| `KW_ASSIGN` | assign | ನಿಯೋಜಿಸು | `niyaujisu` | hardware |
| `KW_BEGIN` | begin | ಪ್ರಾರಂಭ | `praara_mbha` | block |
| `KW_END` | end | ಅಂತ್ಯ | `a_ntya` | block |

### Paradigm: imperative

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | ಆದರೆ | `aadaree` | control_flow |
| `KW_ELSE` | else | ಇಲ್ಲದಿದ್ದರೆ | `illadiddaree` | control_flow |
| `KW_ELIF` | elif | ಅಥವಾಆದರೆ | `athavaaaadaree` | control_flow |
| `KW_WHILE` | while | ತನಕ | `tanaka` | control_flow |
| `KW_DO` | do | ಮಾಡು | `maadu` | control_flow |
| `KW_FOR` | for | ಗಾಗಿ | `gaagi` | control_flow |
| `KW_BREAK` | break | ನಿಲ್ಲಿಸು | `nillisu` | control_flow |
| `KW_CONTINUE` | continue | ಮುಂದುವರಿ | `mu_nduvari` | control_flow |
| `KW_SWITCH` | switch | ಆಯ್ಕೆ | `aayke` | control_flow |
| `KW_CASE` | case | ಸ್ಥಿತಿ | `sthiti` | control_flow |
| `KW_DEFAULT` | default | ಪೂರ್ವನಿಯೋಜಿತ | `puurvaniyaujita` | control_flow |
| `KW_RETURN` | return | ಹಿಂತಿರುಗಿಸು | `hi_ntirugisu` | control_flow |
| `KW_GOTO` | goto | ಹೋಗು | `haugu` | control_flow |
| `KW_VAR` | var | ಚರ | `cara` | declaration |
| `KW_CONST` | const | ಸ್ಥಿರಾಂಕ | `sthiraa_nka` | declaration |
| `KW_LET` | let | ಇರಲಿ | `irali` | declaration |
| `KW_INT` | int | ಪೂರ್ಣಾಂಕ | `puur_naa_nka` | type |
| `KW_FLOAT` | float | ದಶಮಾಂಶ | `dashamaa_nsha` | type |
| `KW_DOUBLE` | double | ದ್ವಿಗುಣ | `dvigu_na` | type |
| `KW_CHAR` | char | ಅಕ್ಷರ | `ak_sara` | type |
| `KW_BOOL` | bool | ತಾರ್ಕಿಕ | `taarkika` | type |
| `KW_STRING` | string | ಪದಪುಂಜ | `padapu_nja` | type |
| `KW_VOID` | void | ಶೂನ್ಯ | `shuunya` | type |
| `KW_TRUE` | true | ನಿಜ | `nija` | literal |
| `KW_FALSE` | false | ಸುಳ್ಳು | `sullu` | literal |
| `KW_NULL` | null | ಖಾಲಿ | `khaali` | literal |
| `KW_TRY` | try | ಪ್ರಯತ್ನಿಸು | `prayatnisu` | exception |
| `KW_CATCH` | catch | ಹಿಡಿ | `hidi` | exception |
| `KW_FINALLY` | finally | ಕೊನೆಗೆ | `konege` | exception |
| `KW_THROW` | throw | ಎಸೆ | `ese` | exception |
| `KW_RAISE` | raise | ಎತ್ತು | `ettu` | exception |
| `KW_EXCEPT` | except | ಅಪವಾದ | `apavaada` | exception |

### Paradigm: iot

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | ಕೀಲಕ | `kiilaka` | io |
| `KW_READ` | read | ಪಠ | `patha` | io |
| `KW_WRITE` | write | ಲಿಖ | `likha` | io |
| `KW_ANALOG` | analog | ಸದೃಶ | `sadr_sha` | io |
| `KW_DIGITAL` | digital | ಅಙ್ಕೀಯ | `a_nkiiya` | io |
| `KW_PWM` | pwm | ಸ್ಪನ್ದವಿಸ್ತಾರ | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | ವಿಘ್ನ | `vighna` | io |
| `KW_TIMER` | timer | ಕಾಲಯನ್ತ್ರ | `kaalayantra` | io |
| `KW_SENSOR` | sensor | ಸಂವೇದಕ | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | ಪ್ರವರ್ತಕ | `pravartaka` | io |
| `KW_BUS` | bus | ಮಾರ್ಗ | `maarga` | io |
| `KW_PROTOCOL` | protocol | ನಿಯಮಾವಲೀ | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | ಸುಷುಪ್ತಿ | `su_supti` | power |
| `KW_WAKE` | wake | ಜಾಗೃ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | ನಿಯಮ | `niyama` | clause |
| `KW_FACT` | fact | ಸತ್ಯ | `satya` | clause |
| `KW_QUERY` | query | ಪ್ರಶ್ನೆ | `prashne` | clause |
| `KW_NOT` | not | ಅಲ್ಲ | `alla` | operator |
| `KW_AND` | and | ಮತ್ತು | `mattu` | operator |
| `KW_OR` | or | ಅಥವಾ | `athavaa` | operator |

### Paradigm: memory

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | ಸ್ವಾಮಿತ್ವ | `svaamitva` | ownership |
| `KW_BORROW` | borrow | ಋಣ | `r_na` | ownership |
| `KW_MOVE` | move | ಸ್ಥಾನಾನ್ತರ | `sthaanaantara` | ownership |
| `KW_MUT` | mut | ಪರಿವರ್ತ್ಯ | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | ಆಯುಷ್ಕಾಲ | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | ಕ್ಷೇತ್ರ | `k_seetra` | allocation |
| `KW_GC` | gc | ಮಲಸಂಗ್ರಹ | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | ಸ್ಮೃತಿಕೀಲಕ | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | ವರ್ಗ | `varga` | type_def |
| `KW_OBJECT` | object | ವಸ್ತು | `vastu` | type_def |
| `KW_INTERFACE` | interface | ಸಂಪರ್ಕಮುಖ | `sa_mparkamukha` | type_def |
| `KW_EXTENDS` | extends | ವಿಸ್ತರಿಸು | `vistarisu` | inheritance |
| `KW_IMPLEMENTS` | implements | ಅನುಷ್ಠಾನ | `anu_sthaana` | inheritance |
| `KW_NEW` | new | ಹೊಸ | `hosa` | instantiation |
| `KW_THIS` | this | ಇದು | `idu` | reference |
| `KW_SUPER` | super | ಪರ | `para` | reference |
| `KW_PUBLIC` | public | ಸಾರ್ವಜನಿಕ | `saarvajanika` | access |
| `KW_PRIVATE` | private | ಖಾಸಗಿ | `khaasagi` | access |
| `KW_PROTECTED` | protected | ಸಂರಕ್ಷಿತ | `sa_mrak_sita` | access |
| `KW_STATIC` | static | ಸ್ಥಿರ | `sthira` | storage |
| `KW_ABSTRACT` | abstract | ಅಮೂರ್ತ | `amuurta` | modifier |
| `KW_VIRTUAL` | virtual | ವಾಸ್ತವಿಕ | `vaastavika` | modifier |
| `KW_OVERRIDE` | override | ಅತಿಕ್ರಮಿಸು | `atikramisu` | modifier |

### Paradigm: procedural

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | ಕಾರ್ಯ | `kaarya` | subroutine |
| `KW_PROC` | procedure | ವಿಧಾನ | `vidhaana` | subroutine |
| `KW_CALL` | call | ಕರೆ | `karee` | subroutine |
| `KW_PARAM` | param | ನಿಯತಾಂಕ | `niyataa_nka` | subroutine |
| `KW_YIELD` | yield | ನೀಡು | `niidu` | coroutine |
| `KW_AWAIT` | await | ಕಾಯಿ | `kaayi` | async |
| `KW_ASYNC` | async | ಅಸಮಕಾಲಿಕ | `asamakaalika` | async |

### Paradigm: robotics

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | ಚಾಲಕ | `caalaka` | control |
| `KW_SERVO` | servo | ಅನುಚಾಲಕ | `anucaalaka` | control |
| `KW_JOINT` | joint | ಸನ್ಧಿ | `sandhi` | control |
| `KW_POSE` | pose | ಮುದ್ರಾ | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | ಪ್ರಕ್ಷೇಪಪಥ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | ಪ್ರತಿಪುಷ್ಟಿ | `pratipu_sti` | control |
| `KW_PID` | pid | ನಿಯನ್ತ್ರಕ | `niyantraka` | control |
| `KW_DEADLINE` | deadline | ಕಾಲಸೀಮಾ | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | ಆವರ್ತಿಕ | `aavartika` | realtime |
| `KW_PRIORITY` | priority | ಪ್ರಾಥಮ್ಯ | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | ಪ್ರವರ್ತಯ | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | ಪ್ರತ್ಯಕ್ಷ | `pratyak_sa` | control |
| `KW_PLAN` | plan | ಯೋಜನಾ | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | ಸೂಚಕ | `suucaka` | memory |
| `KW_REF` | ref | ಉಲ್ಲೇಖ | `ulleekha` | memory |
| `KW_ALLOC` | alloc | ಹಂಚಿಕೆ | `ha_ncike` | memory |
| `KW_FREE` | free | ಬಿಡುಗಡೆ | `bidugade` | memory |
| `KW_SIZEOF` | sizeof | ಗಾತ್ರ | `gaatra` | memory |
| `KW_STRUCT` | struct | ರಚನೆ | `racane` | type_def |
| `KW_UNION` | union | ಒಕ್ಕೂಟ | `okkuuta` | type_def |
| `KW_ENUM` | enum | ಎಣಿಕೆ | `e_nike` | type_def |
| `KW_TYPEDEF` | typedef | ಪ್ರಕಾರವ್ಯಾಖ್ಯೆ | `prakaaravyaakhye` | type_def |
| `KW_VOLATILE` | volatile | ಅಸ್ಥಿರ | `asthira` | modifier |
| `KW_REGISTER` | register | ನೋಂದಣಿ | `nau_nda_ni` | storage |
| `KW_EXTERN` | extern | ಬಾಹ್ಯ | `baahya` | linkage |
| `KW_INLINE` | inline | ಸಾಲೊಳಗೆ | `saalolage` | modifier |

### Paradigm: verification

| Construct | English | Kannada | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | ಅಪೇಕ್ಷತೇ | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | ಸುನಿಶ್ಚಯತಿ | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | ಅಪರಿವರ್ತ್ಯ | `aparivartya` | contract |
| `KW_ASSERT` | assert | ಪ್ರತಿಜ್ಞಾ | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | ಅಧ್ಯವಸ್ಯತಿ | `adhyavasyati` | contract |
| `KW_PROVE` | prove | ಸಾಧಯತಿ | `saadhayati` | contract |
| `KW_REFINES` | refines | ಪರಿಷ್ಕರೋತಿ | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | ಪ್ರತಿಮಾನಪರೀಕ್ಷಾ | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Kannada native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Kannada a first-class systems-programming language, not a localized skin.

## Example

```
ಆದರೆ (x > 0)        // romenagri: aadaree
    ...
ಇಲ್ಲದಿದ್ದರೆ              // romenagri: illadiddaree
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Kannada keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*