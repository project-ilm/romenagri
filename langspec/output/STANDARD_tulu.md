# Tulu Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Tulu
- **ISO 639 code**: tcy
- **Script**: Kannada
- **Native speakers**: 2M
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Tulu-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Tulu keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
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

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | ಆನಯನ | `aanayana` | namespace |
| `KW_EXPORT` | export | ನಿರ್ಯಾಪಣ | `niryaapa_na` | namespace |
| `KW_PACKAGE` | package | ಪುಟಕ | `putaka` | namespace |
| `KW_NAMESPACE` | namespace | ನಾಮಾಕಾಶ | `naamaakaasha` | namespace |
| `KW_USE` | use | ಉಪಯೋಗ | `upayauga` | namespace |
| `KW_INCLUDE` | include | ಅನ್ತರ್ಭಾವ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | ತಃ | `ta_h` | namespace |
| `KW_AS` | as | ಇವ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | ತನ್ತು | `tantu` | concurrency |
| `KW_SPAWN` | spawn | ಉತ್ಪಾದ | `utpaada` | concurrency |
| `KW_LOCK` | lock | ತಾಲಕ | `taalaka` | concurrency |
| `KW_SYNC` | synchronized | ಸಮಕಾಲ | `samakaala` | concurrency |
| `KW_CHANNEL` | channel | ಮಾರ್ಗ | `maarga` | concurrency |
| `KW_SELECT` | select | ವೃಣು | `vr_nu` | concurrency |

### Paradigm: dataflow

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
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

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
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

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | ಅನಾಮನ್ | `anaaman` | function |
| `KW_MATCH` | match | ಮೇಲ | `meela` | pattern |
| `KW_WHEN` | when | ಯದಾ | `yadaa` | pattern |
| `KW_FUN` | fun | ಫಲ | `phala` | function |
| `KW_REC` | rec | ಪುನರಾವೃತ್ತ | `punaraavr_tta` | recursion |
| `KW_IN` | in | ಅನ್ತಃ | `anta_h` | binding |
| `KW_WHERE` | where | ಯತ್ರ | `yatra` | binding |
| `KW_DATA` | data | ದತ್ತ | `datta` | type_def |
| `KW_TYPE` | type | ಪ್ರಕಾರ | `prakaara` | type_def |
| `KW_MODULE` | module | ಖಣ್ಡ | `kha_nda` | namespace |

### Paradigm: gpu

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
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

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | ಸತ್ತಾ | `sattaa` | hardware |
| `KW_ARCH` | architecture | ಸ್ಥಾಪತ್ಯ | `sthaapatya` | hardware |
| `KW_SIGNAL` | signal | ಸಙ್ಕೇತ | `sa_nkeeta` | hardware |
| `KW_PORT` | port | ದ್ವಾರ | `dvaara` | hardware |
| `KW_WIRE` | wire | ತನ್ತು | `tantu` | hardware |
| `KW_REG` | reg | ಪಞ್ಜೀ | `pa_njii` | hardware |
| `KW_MODULE_HW` | module | ಅಂಶ | `a_nsha` | hardware |
| `KW_ALWAYS` | always | ಸದಾ | `sadaa` | hardware |
| `KW_ASSIGN` | assign | ನಿಯುಕ್ತ | `niyukta` | hardware |
| `KW_BEGIN` | begin | ಆರಮ್ಭ | `aarambha` | block |
| `KW_END` | end | ಅನ್ತ | `anta` | block |

### Paradigm: imperative

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | ಯದಿ | `yadi` | control_flow |
| `KW_ELSE` | else | ಅನ್ಯಥಾ | `anyathaa` | control_flow |
| `KW_ELIF` | elif | ನೋಚೇದ್ಯದಿ | `naucheedyadi` | control_flow |
| `KW_WHILE` | while | ಯಾವತ್ | `yaavat` | control_flow |
| `KW_DO` | do | ಕುರು | `kuru` | control_flow |
| `KW_FOR` | for | ಪ್ರತಿ | `prati` | control_flow |
| `KW_BREAK` | break | ಭಙ್ಗ | `bha_nga` | control_flow |
| `KW_CONTINUE` | continue | ಅನುವರ್ತ | `anuvarta` | control_flow |
| `KW_SWITCH` | switch | ವಿಕಲ್ಪ | `vikalpa` | control_flow |
| `KW_CASE` | case | ಪಕ್ಷ | `pak_sa` | control_flow |
| `KW_DEFAULT` | default | ಸ್ವಭಾವ | `svabhaava` | control_flow |
| `KW_RETURN` | return | ಪ್ರತ್ಯಾಗಮ | `pratyaagama` | control_flow |
| `KW_GOTO` | goto | ಗಚ್ಛ | `gaccha` | control_flow |
| `KW_VAR` | var | ಚರ | `cara` | declaration |
| `KW_CONST` | const | ಧ್ರುವ | `dhruva` | declaration |
| `KW_LET` | let | ಅಸ್ತು | `astu` | declaration |
| `KW_INT` | int | ಪೂರ್ಣಾಙ್ಕ | `puur_naa_nka` | type |
| `KW_FLOAT` | float | ಭಿನ್ನ | `bhinna` | type |
| `KW_DOUBLE` | double | ದ್ವಿಗುಣ | `dviguu_na` | type |
| `KW_CHAR` | char | ವರ್ಣ | `var_na` | type |
| `KW_BOOL` | bool | ತಾರ್ಕಿಕ | `taarkika` | type |
| `KW_STRING` | string | ಪದಾವಲೀ | `padaavalii` | type |
| `KW_VOID` | void | ಶೂನ್ಯ | `shuunya` | type |
| `KW_TRUE` | true | ಸತ್ಯ | `satya` | literal |
| `KW_FALSE` | false | ಅಸತ್ಯ | `asatya` | literal |
| `KW_NULL` | null | ರಿಕ್ತ | `rikta` | literal |
| `KW_TRY` | try | ಯತ್ನ | `yatna` | exception |
| `KW_CATCH` | catch | ಗೃಹಾಣ | `gr_haa_na` | exception |
| `KW_FINALLY` | finally | ಅನ್ತತಃ | `antata_h` | exception |
| `KW_THROW` | throw | ಕ್ಷಿಪ | `k_sipa` | exception |
| `KW_RAISE` | raise | ಉತ್ಥಾಪಯ | `utthaapaya` | exception |
| `KW_EXCEPT` | except | ಅಪವಾದ | `apavaada` | exception |

### Paradigm: iot

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
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

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | ಸೂತ್ರ | `suutra` | clause |
| `KW_FACT` | fact | ತಥ್ಯ | `tathya` | clause |
| `KW_QUERY` | query | ಪ್ರಶ್ನ | `prashna` | clause |
| `KW_NOT` | not | ನ | `na` | operator |
| `KW_AND` | and | ಚ | `ca` | operator |
| `KW_OR` | or | ವಾ | `vaa` | operator |

### Paradigm: memory

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
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

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | ವರ್ಗ | `varga` | type_def |
| `KW_OBJECT` | object | ವಸ್ತು | `vastu` | type_def |
| `KW_INTERFACE` | interface | ಸನ್ಧಿ | `sandhi` | type_def |
| `KW_EXTENDS` | extends | ವಿಸ್ತೃತ | `vistr_ta` | inheritance |
| `KW_IMPLEMENTS` | implements | ನಿಷ್ಪಾದಿತ | `ni_spaadita` | inheritance |
| `KW_NEW` | new | ನೂತನ | `nuutana` | instantiation |
| `KW_THIS` | this | ಏತತ್ | `eetat` | reference |
| `KW_SUPER` | super | ಪರ | `para` | reference |
| `KW_PUBLIC` | public | ಸಾರ್ವಜನಿಕ | `saarvajanika` | access |
| `KW_PRIVATE` | private | ಗುಪ್ತ | `gupta` | access |
| `KW_PROTECTED` | protected | ರಕ್ಷಿತ | `rak_sita` | access |
| `KW_STATIC` | static | ಸ್ಥಿರ | `sthira` | storage |
| `KW_ABSTRACT` | abstract | ಅಮೂರ್ತ | `amuurta` | modifier |
| `KW_VIRTUAL` | virtual | ಆಭಾಸ | `aabhaasa` | modifier |
| `KW_OVERRIDE` | override | ಅಧಿರೋಹ | `adhirauha` | modifier |

### Paradigm: procedural

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | ಕ್ರಿಯಾ | `kriyaa` | subroutine |
| `KW_PROC` | procedure | ವಿಧಿ | `vidhi` | subroutine |
| `KW_CALL` | call | ಆಹ್ವಾನ | `aahvaana` | subroutine |
| `KW_PARAM` | param | ಪ್ರಾಚಲ | `praacala` | subroutine |
| `KW_YIELD` | yield | ದಾ | `daa` | coroutine |
| `KW_AWAIT` | await | ಪ್ರತೀಕ್ಷ | `pratiik_sa` | async |
| `KW_ASYNC` | async | ಅಸಮಕಾಲ | `asamakaala` | async |

### Paradigm: robotics

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
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

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | ನಿರ್ದೇಶಕ | `nirdeeshaka` | memory |
| `KW_REF` | ref | ಸನ್ದರ್ಭ | `sandarbha` | memory |
| `KW_ALLOC` | alloc | ಆವಣ್ಟನ | `aava_ntana` | memory |
| `KW_FREE` | free | ಮುಕ್ತ | `mukta` | memory |
| `KW_SIZEOF` | sizeof | ಪರಿಮಾಣ | `parimaa_na` | memory |
| `KW_STRUCT` | struct | ಸಂರಚನಾ | `sa_nracanaa` | type_def |
| `KW_UNION` | union | ಸಙ್ಘ | `sa_ngha` | type_def |
| `KW_ENUM` | enum | ಗಣನಾ | `ga_nanaa` | type_def |
| `KW_TYPEDEF` | typedef | ಪ್ರಕಾರನಿರ್ದೇಶ | `prakaaranirdeesha` | type_def |
| `KW_VOLATILE` | volatile | ಚಞ್ಚಲ | `ca_ncala` | modifier |
| `KW_REGISTER` | register | ಪಞ್ಜಿಕಾ | `pa_njikaa` | storage |
| `KW_EXTERN` | extern | ಬಾಹ್ಯ | `baahya` | linkage |
| `KW_INLINE` | inline | ಅನ್ತಃಸ್ಥ | `anta_hstha` | modifier |

### Paradigm: verification

| Construct | English | Tulu | Romenagri (ASCII-7) | Category |
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

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Tulu native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Tulu a first-class systems-programming language, not a localized skin.

## Example

```
ಯದಿ (x > 0)        // romenagri: yadi
    ...
ಅನ್ಯಥಾ              // romenagri: anyathaa
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Tulu keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*