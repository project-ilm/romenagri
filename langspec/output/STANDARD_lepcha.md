# Lepcha Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Lepcha
- **ISO 639 code**: lep
- **Script**: Lepcha
- **Native speakers**: 66K
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Lepcha-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Lepcha keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | pradisha | `pradisha` | ml |
| `KW_MATRIX` | matrix | aavyuuha | `aavyuuha` | ml |
| `KW_VECTOR` | vector | sadisha | `sadisha` | ml |
| `KW_GRAD` | gradient | prava_nataa | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | pratiprasaara | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | agraprasaara | `agraprasaara` | ml |
| `KW_LAYER` | layer | stara | `stara` | ml |
| `KW_MODEL` | model | pratimaana | `pratimaana` | ml |
| `KW_TRAIN` | train | prashik_sa_na | `prashik_sa_na` | ml |
| `KW_INFER` | infer | anumaana | `anumaana` | ml |
| `KW_LOSS` | loss | haani | `haani` | ml |
| `KW_OPTIMIZE` | optimize | anukuulana | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | sakriya_na | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | bhaara | `bhaara` | ml |
| `KW_BIAS` | bias | pak_sapaata | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | kalpa | `kalpa` | ml |
| `KW_BATCH` | batch | pu_nja | `pu_nja` | ml |
| `KW_DATASET` | dataset | dattasamuuha | `dattasamuuha` | ml |
| `KW_EMBED` | embed | niveeshana | `niveeshana` | ml |
| `KW_ATTENTION` | attention | avadhaana | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | aanayana | `aanayana` | namespace |
| `KW_EXPORT` | export | niryaapa_na | `niryaapa_na` | namespace |
| `KW_PACKAGE` | package | putaka | `putaka` | namespace |
| `KW_NAMESPACE` | namespace | naamaakaasha | `naamaakaasha` | namespace |
| `KW_USE` | use | upayauga | `upayauga` | namespace |
| `KW_INCLUDE` | include | antarbhaava | `antarbhaava` | preprocessor |
| `KW_FROM` | from | ta_h | `ta_h` | namespace |
| `KW_AS` | as | iva | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | tantu | `tantu` | concurrency |
| `KW_SPAWN` | spawn | utpaada | `utpaada` | concurrency |
| `KW_LOCK` | lock | taalaka | `taalaka` | concurrency |
| `KW_SYNC` | synchronized | samakaala | `samakaala` | concurrency |
| `KW_CHANNEL` | channel | maarga | `maarga` | concurrency |
| `KW_SELECT` | select | vr_nu | `vr_nu` | concurrency |

### Paradigm: dataflow

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | dhaaraa | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | pra_naala | `pra_naala` | reactive |
| `KW_MAP` | map | praticitra | `praticitra` | reactive |
| `KW_FILTER` | filter | chaala | `chaala` | reactive |
| `KW_REDUCE` | reduce | nyuuniikr_ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | sa_nvee_sta | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | niriik_sa | `niriik_sa` | reactive |
| `KW_EMIT` | emit | utsr_ja | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | abhiniveesha | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | spandashaudhana | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | granthi | `granthi` | cluster |
| `KW_REPLICA` | replica | pratikr_ti | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | sarvasammati | `sarvasammati` | cluster |
| `KW_SHARD` | shard | kha_nda | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | janavaada | `janavaada` | cluster |
| `KW_LEADER` | leader | naayaka | `naayaka` | cluster |
| `KW_RPC` | rpc | duuraprakriyaa | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | kartr_ | `kartr_` | cluster |
| `KW_MESSAGE` | message | sandeesha | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | anaaman | `anaaman` | function |
| `KW_MATCH` | match | meela | `meela` | pattern |
| `KW_WHEN` | when | yadaa | `yadaa` | pattern |
| `KW_FUN` | fun | phala | `phala` | function |
| `KW_REC` | rec | punaraavr_tta | `punaraavr_tta` | recursion |
| `KW_IN` | in | anta_h | `anta_h` | binding |
| `KW_WHERE` | where | yatra | `yatra` | binding |
| `KW_DATA` | data | datta | `datta` | type_def |
| `KW_TYPE` | type | prakaara | `prakaara` | type_def |
| `KW_MODULE` | module | kha_nda | `kha_nda` | namespace |

### Paradigm: gpu

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | biija | `biija` | compute |
| `KW_DEVICE` | device | yantra | `yantra` | compute |
| `KW_HOST` | host | aatitheeya | `aatitheeya` | compute |
| `KW_GLOBAL` | global | vaishvika | `vaishvika` | compute |
| `KW_SHARED` | shared | sahabhaajita | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | tantva_nka | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | kha_ndaa_nka | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | jaala | `jaala` | compute |
| `KW_BARRIER` | barrier | avaurudha | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | aa_navika | `aa_navika` | compute |
| `KW_WARP` | warp | tantusamuuha | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | sattaa | `sattaa` | hardware |
| `KW_ARCH` | architecture | sthaapatya | `sthaapatya` | hardware |
| `KW_SIGNAL` | signal | sa_nkeeta | `sa_nkeeta` | hardware |
| `KW_PORT` | port | dvaara | `dvaara` | hardware |
| `KW_WIRE` | wire | tantu | `tantu` | hardware |
| `KW_REG` | reg | pa_njii | `pa_njii` | hardware |
| `KW_MODULE_HW` | module | a_nsha | `a_nsha` | hardware |
| `KW_ALWAYS` | always | sadaa | `sadaa` | hardware |
| `KW_ASSIGN` | assign | niyukta | `niyukta` | hardware |
| `KW_BEGIN` | begin | aarambha | `aarambha` | block |
| `KW_END` | end | anta | `anta` | block |

### Paradigm: imperative

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | yadi | `yadi` | control_flow |
| `KW_ELSE` | else | anyathaa | `anyathaa` | control_flow |
| `KW_ELIF` | elif | naucheedyadi | `naucheedyadi` | control_flow |
| `KW_WHILE` | while | yaavat | `yaavat` | control_flow |
| `KW_DO` | do | kuru | `kuru` | control_flow |
| `KW_FOR` | for | prati | `prati` | control_flow |
| `KW_BREAK` | break | bha_nga | `bha_nga` | control_flow |
| `KW_CONTINUE` | continue | anuvarta | `anuvarta` | control_flow |
| `KW_SWITCH` | switch | vikalpa | `vikalpa` | control_flow |
| `KW_CASE` | case | pak_sa | `pak_sa` | control_flow |
| `KW_DEFAULT` | default | svabhaava | `svabhaava` | control_flow |
| `KW_RETURN` | return | pratyaagama | `pratyaagama` | control_flow |
| `KW_GOTO` | goto | gaccha | `gaccha` | control_flow |
| `KW_VAR` | var | cara | `cara` | declaration |
| `KW_CONST` | const | dhruva | `dhruva` | declaration |
| `KW_LET` | let | astu | `astu` | declaration |
| `KW_INT` | int | puur_naa_nka | `puur_naa_nka` | type |
| `KW_FLOAT` | float | bhinna | `bhinna` | type |
| `KW_DOUBLE` | double | dviguu_na | `dviguu_na` | type |
| `KW_CHAR` | char | var_na | `var_na` | type |
| `KW_BOOL` | bool | taarkika | `taarkika` | type |
| `KW_STRING` | string | padaavalii | `padaavalii` | type |
| `KW_VOID` | void | shuunya | `shuunya` | type |
| `KW_TRUE` | true | satya | `satya` | literal |
| `KW_FALSE` | false | asatya | `asatya` | literal |
| `KW_NULL` | null | rikta | `rikta` | literal |
| `KW_TRY` | try | yatna | `yatna` | exception |
| `KW_CATCH` | catch | gr_haa_na | `gr_haa_na` | exception |
| `KW_FINALLY` | finally | antata_h | `antata_h` | exception |
| `KW_THROW` | throw | k_sipa | `k_sipa` | exception |
| `KW_RAISE` | raise | utthaapaya | `utthaapaya` | exception |
| `KW_EXCEPT` | except | apavaada | `apavaada` | exception |

### Paradigm: iot

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | kiilaka | `kiilaka` | io |
| `KW_READ` | read | patha | `patha` | io |
| `KW_WRITE` | write | likha | `likha` | io |
| `KW_ANALOG` | analog | sadr_sha | `sadr_sha` | io |
| `KW_DIGITAL` | digital | a_nkiiya | `a_nkiiya` | io |
| `KW_PWM` | pwm | spandavistaara | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | vighna | `vighna` | io |
| `KW_TIMER` | timer | kaalayantra | `kaalayantra` | io |
| `KW_SENSOR` | sensor | sa_nveedaka | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | pravartaka | `pravartaka` | io |
| `KW_BUS` | bus | maarga | `maarga` | io |
| `KW_PROTOCOL` | protocol | niyamaavalii | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | su_supti | `su_supti` | power |
| `KW_WAKE` | wake | jaagr_ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | suutra | `suutra` | clause |
| `KW_FACT` | fact | tathya | `tathya` | clause |
| `KW_QUERY` | query | prashna | `prashna` | clause |
| `KW_NOT` | not | na | `na` | operator |
| `KW_AND` | and | ca | `ca` | operator |
| `KW_OR` | or | vaa | `vaa` | operator |

### Paradigm: memory

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | svaamitva | `svaamitva` | ownership |
| `KW_BORROW` | borrow | r_na | `r_na` | ownership |
| `KW_MOVE` | move | sthaanaantara | `sthaanaantara` | ownership |
| `KW_MUT` | mut | parivartya | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | aayu_skaala | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | k_seetra | `k_seetra` | allocation |
| `KW_GC` | gc | malasa_ngraha | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | smr_tikiilaka | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | varga | `varga` | type_def |
| `KW_OBJECT` | object | vastu | `vastu` | type_def |
| `KW_INTERFACE` | interface | sandhi | `sandhi` | type_def |
| `KW_EXTENDS` | extends | vistr_ta | `vistr_ta` | inheritance |
| `KW_IMPLEMENTS` | implements | ni_spaadita | `ni_spaadita` | inheritance |
| `KW_NEW` | new | nuutana | `nuutana` | instantiation |
| `KW_THIS` | this | eetat | `eetat` | reference |
| `KW_SUPER` | super | para | `para` | reference |
| `KW_PUBLIC` | public | saarvajanika | `saarvajanika` | access |
| `KW_PRIVATE` | private | gupta | `gupta` | access |
| `KW_PROTECTED` | protected | rak_sita | `rak_sita` | access |
| `KW_STATIC` | static | sthira | `sthira` | storage |
| `KW_ABSTRACT` | abstract | amuurta | `amuurta` | modifier |
| `KW_VIRTUAL` | virtual | aabhaasa | `aabhaasa` | modifier |
| `KW_OVERRIDE` | override | adhirauha | `adhirauha` | modifier |

### Paradigm: procedural

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | kriyaa | `kriyaa` | subroutine |
| `KW_PROC` | procedure | vidhi | `vidhi` | subroutine |
| `KW_CALL` | call | aahvaana | `aahvaana` | subroutine |
| `KW_PARAM` | param | praacala | `praacala` | subroutine |
| `KW_YIELD` | yield | daa | `daa` | coroutine |
| `KW_AWAIT` | await | pratiik_sa | `pratiik_sa` | async |
| `KW_ASYNC` | async | asamakaala | `asamakaala` | async |

### Paradigm: robotics

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | caalaka | `caalaka` | control |
| `KW_SERVO` | servo | anucaalaka | `anucaalaka` | control |
| `KW_JOINT` | joint | sandhi | `sandhi` | control |
| `KW_POSE` | pose | mudraa | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | prak_seepapatha | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | pratipu_sti | `pratipu_sti` | control |
| `KW_PID` | pid | niyantraka | `niyantraka` | control |
| `KW_DEADLINE` | deadline | kaalasiimaa | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | aavartika | `aavartika` | realtime |
| `KW_PRIORITY` | priority | praathamya | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | pravartaya | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | pratyak_sa | `pratyak_sa` | control |
| `KW_PLAN` | plan | yaujanaa | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | nirdeeshaka | `nirdeeshaka` | memory |
| `KW_REF` | ref | sandarbha | `sandarbha` | memory |
| `KW_ALLOC` | alloc | aava_ntana | `aava_ntana` | memory |
| `KW_FREE` | free | mukta | `mukta` | memory |
| `KW_SIZEOF` | sizeof | parimaa_na | `parimaa_na` | memory |
| `KW_STRUCT` | struct | sa_nracanaa | `sa_nracanaa` | type_def |
| `KW_UNION` | union | sa_ngha | `sa_ngha` | type_def |
| `KW_ENUM` | enum | ga_nanaa | `ga_nanaa` | type_def |
| `KW_TYPEDEF` | typedef | prakaaranirdeesha | `prakaaranirdeesha` | type_def |
| `KW_VOLATILE` | volatile | ca_ncala | `ca_ncala` | modifier |
| `KW_REGISTER` | register | pa_njikaa | `pa_njikaa` | storage |
| `KW_EXTERN` | extern | baahya | `baahya` | linkage |
| `KW_INLINE` | inline | anta_hstha | `anta_hstha` | modifier |

### Paradigm: verification

| Construct | English | Lepcha | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | apeek_satee | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | sunishcayati | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | aparivartya | `aparivartya` | contract |
| `KW_ASSERT` | assert | pratijnyaa | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | adhyavasyati | `adhyavasyati` | contract |
| `KW_PROVE` | prove | saadhayati | `saadhayati` | contract |
| `KW_REFINES` | refines | pari_skarauti | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | pratimaanapariik_saa | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Lepcha native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Lepcha a first-class systems-programming language, not a localized skin.

## Example

```
yadi (x > 0)        // romenagri: yadi
    ...
anyathaa              // romenagri: anyathaa
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Lepcha keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*