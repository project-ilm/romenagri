# Konkani Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Konkani
- **ISO 639 code**: kok
- **Script**: Devanagari
- **Native speakers**: 2.5M
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Konkani-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Konkani keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | प्रदिश | `pradisha` | ml |
| `KW_MATRIX` | matrix | आव्यूह | `aavyuuha` | ml |
| `KW_VECTOR` | vector | सदिश | `sadisha` | ml |
| `KW_GRAD` | gradient | प्रवणता | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | प्रतिप्रसार | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | अग्रप्रसार | `agraprasaara` | ml |
| `KW_LAYER` | layer | स्तर | `stara` | ml |
| `KW_MODEL` | model | प्रतिमान | `pratimaana` | ml |
| `KW_TRAIN` | train | प्रशिक्षण | `prashik_sa_na` | ml |
| `KW_INFER` | infer | अनुमान | `anumaana` | ml |
| `KW_LOSS` | loss | हानि | `haani` | ml |
| `KW_OPTIMIZE` | optimize | अनुकूलन | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | सक्रियण | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | भार | `bhaara` | ml |
| `KW_BIAS` | bias | पक्षपात | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | कल्प | `kalpa` | ml |
| `KW_BATCH` | batch | पुञ्ज | `pu_nja` | ml |
| `KW_DATASET` | dataset | दत्तसमूह | `dattasamuuha` | ml |
| `KW_EMBED` | embed | निवेशन | `niveeshana` | ml |
| `KW_ATTENTION` | attention | अवधान | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | आनयन | `aanayana` | namespace |
| `KW_EXPORT` | export | निर्यापण | `niryaapa_na` | namespace |
| `KW_PACKAGE` | package | पुटक | `putaka` | namespace |
| `KW_NAMESPACE` | namespace | नामाकाश | `naamaakaasha` | namespace |
| `KW_USE` | use | उपयोग | `upayauga` | namespace |
| `KW_INCLUDE` | include | अन्तर्भाव | `antarbhaava` | preprocessor |
| `KW_FROM` | from | तः | `ta_h` | namespace |
| `KW_AS` | as | इव | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | तन्तु | `tantu` | concurrency |
| `KW_SPAWN` | spawn | उत्पाद | `utpaada` | concurrency |
| `KW_LOCK` | lock | तालक | `taalaka` | concurrency |
| `KW_SYNC` | synchronized | समकाल | `samakaala` | concurrency |
| `KW_CHANNEL` | channel | मार्ग | `maarga` | concurrency |
| `KW_SELECT` | select | वृणु | `vr_nu` | concurrency |

### Paradigm: dataflow

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | धारा | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | प्रणाल | `pra_naala` | reactive |
| `KW_MAP` | map | प्रतिचित्र | `praticitra` | reactive |
| `KW_FILTER` | filter | छाल | `chaala` | reactive |
| `KW_REDUCE` | reduce | न्यूनीकृ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | संवेष्ट | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | निरीक्ष | `niriik_sa` | reactive |
| `KW_EMIT` | emit | उत्सृज | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | अभिनिवेश | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | स्पन्दशोधन | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | ग्रन्थि | `granthi` | cluster |
| `KW_REPLICA` | replica | प्रतिकृति | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | सर्वसम्मति | `sarvasammati` | cluster |
| `KW_SHARD` | shard | खण्ड | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | जनवाद | `janavaada` | cluster |
| `KW_LEADER` | leader | नायक | `naayaka` | cluster |
| `KW_RPC` | rpc | दूरप्रक्रिया | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | कर्तृ | `kartr_` | cluster |
| `KW_MESSAGE` | message | सन्देश | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | अनामन् | `anaaman` | function |
| `KW_MATCH` | match | मेल | `meela` | pattern |
| `KW_WHEN` | when | यदा | `yadaa` | pattern |
| `KW_FUN` | fun | फल | `phala` | function |
| `KW_REC` | rec | पुनरावृत्त | `punaraavr_tta` | recursion |
| `KW_IN` | in | अन्तः | `anta_h` | binding |
| `KW_WHERE` | where | यत्र | `yatra` | binding |
| `KW_DATA` | data | दत्त | `datta` | type_def |
| `KW_TYPE` | type | प्रकार | `prakaara` | type_def |
| `KW_MODULE` | module | खण्ड | `kha_nda` | namespace |

### Paradigm: gpu

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | बीज | `biija` | compute |
| `KW_DEVICE` | device | यन्त्र | `yantra` | compute |
| `KW_HOST` | host | आतिथेय | `aatitheeya` | compute |
| `KW_GLOBAL` | global | वैश्विक | `vaishvika` | compute |
| `KW_SHARED` | shared | सहभाजित | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | तन्त्वङ्क | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | खण्डाङ्क | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | जाल | `jaala` | compute |
| `KW_BARRIER` | barrier | अवरोध | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | आणविक | `aa_navika` | compute |
| `KW_WARP` | warp | तन्तुसमूह | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | सत्ता | `sattaa` | hardware |
| `KW_ARCH` | architecture | स्थापत्य | `sthaapatya` | hardware |
| `KW_SIGNAL` | signal | सङ्केत | `sa_nkeeta` | hardware |
| `KW_PORT` | port | द्वार | `dvaara` | hardware |
| `KW_WIRE` | wire | तन्तु | `tantu` | hardware |
| `KW_REG` | reg | पञ्जी | `pa_njii` | hardware |
| `KW_MODULE_HW` | module | अंश | `a_nsha` | hardware |
| `KW_ALWAYS` | always | सदा | `sadaa` | hardware |
| `KW_ASSIGN` | assign | नियुक्त | `niyukta` | hardware |
| `KW_BEGIN` | begin | आरम्भ | `aarambha` | block |
| `KW_END` | end | अन्त | `anta` | block |

### Paradigm: imperative

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | यदि | `yadi` | control_flow |
| `KW_ELSE` | else | अन्यथा | `anyathaa` | control_flow |
| `KW_ELIF` | elif | नोचेद्यदि | `naucheedyadi` | control_flow |
| `KW_WHILE` | while | यावत् | `yaavat` | control_flow |
| `KW_DO` | do | कुरु | `kuru` | control_flow |
| `KW_FOR` | for | प्रति | `prati` | control_flow |
| `KW_BREAK` | break | भङ्ग | `bha_nga` | control_flow |
| `KW_CONTINUE` | continue | अनुवर्त | `anuvarta` | control_flow |
| `KW_SWITCH` | switch | विकल्प | `vikalpa` | control_flow |
| `KW_CASE` | case | पक्ष | `pak_sa` | control_flow |
| `KW_DEFAULT` | default | स्वभाव | `svabhaava` | control_flow |
| `KW_RETURN` | return | प्रत्यागम | `pratyaagama` | control_flow |
| `KW_GOTO` | goto | गच्छ | `gaccha` | control_flow |
| `KW_VAR` | var | चर | `cara` | declaration |
| `KW_CONST` | const | ध्रुव | `dhruva` | declaration |
| `KW_LET` | let | अस्तु | `astu` | declaration |
| `KW_INT` | int | पूर्णाङ्क | `puur_naa_nka` | type |
| `KW_FLOAT` | float | भिन्न | `bhinna` | type |
| `KW_DOUBLE` | double | द्विगुण | `dviguu_na` | type |
| `KW_CHAR` | char | वर्ण | `var_na` | type |
| `KW_BOOL` | bool | तार्किक | `taarkika` | type |
| `KW_STRING` | string | पदावली | `padaavalii` | type |
| `KW_VOID` | void | शून्य | `shuunya` | type |
| `KW_TRUE` | true | सत्य | `satya` | literal |
| `KW_FALSE` | false | असत्य | `asatya` | literal |
| `KW_NULL` | null | रिक्त | `rikta` | literal |
| `KW_TRY` | try | यत्न | `yatna` | exception |
| `KW_CATCH` | catch | गृहाण | `gr_haa_na` | exception |
| `KW_FINALLY` | finally | अन्ततः | `antata_h` | exception |
| `KW_THROW` | throw | क्षिप | `k_sipa` | exception |
| `KW_RAISE` | raise | उत्थापय | `utthaapaya` | exception |
| `KW_EXCEPT` | except | अपवाद | `apavaada` | exception |

### Paradigm: iot

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | कीलक | `kiilaka` | io |
| `KW_READ` | read | पठ | `patha` | io |
| `KW_WRITE` | write | लिख | `likha` | io |
| `KW_ANALOG` | analog | सदृश | `sadr_sha` | io |
| `KW_DIGITAL` | digital | अङ्कीय | `a_nkiiya` | io |
| `KW_PWM` | pwm | स्पन्दविस्तार | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | विघ्न | `vighna` | io |
| `KW_TIMER` | timer | कालयन्त्र | `kaalayantra` | io |
| `KW_SENSOR` | sensor | संवेदक | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | प्रवर्तक | `pravartaka` | io |
| `KW_BUS` | bus | मार्ग | `maarga` | io |
| `KW_PROTOCOL` | protocol | नियमावली | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | सुषुप्ति | `su_supti` | power |
| `KW_WAKE` | wake | जागृ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | सूत्र | `suutra` | clause |
| `KW_FACT` | fact | तथ्य | `tathya` | clause |
| `KW_QUERY` | query | प्रश्न | `prashna` | clause |
| `KW_NOT` | not | न | `na` | operator |
| `KW_AND` | and | च | `ca` | operator |
| `KW_OR` | or | वा | `vaa` | operator |

### Paradigm: memory

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | स्वामित्व | `svaamitva` | ownership |
| `KW_BORROW` | borrow | ऋण | `r_na` | ownership |
| `KW_MOVE` | move | स्थानान्तर | `sthaanaantara` | ownership |
| `KW_MUT` | mut | परिवर्त्य | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | आयुष्काल | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | क्षेत्र | `k_seetra` | allocation |
| `KW_GC` | gc | मलसंग्रह | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | स्मृतिकीलक | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | वर्ग | `varga` | type_def |
| `KW_OBJECT` | object | वस्तु | `vastu` | type_def |
| `KW_INTERFACE` | interface | सन्धि | `sandhi` | type_def |
| `KW_EXTENDS` | extends | विस्तृत | `vistr_ta` | inheritance |
| `KW_IMPLEMENTS` | implements | निष्पादित | `ni_spaadita` | inheritance |
| `KW_NEW` | new | नूतन | `nuutana` | instantiation |
| `KW_THIS` | this | एतत् | `eetat` | reference |
| `KW_SUPER` | super | पर | `para` | reference |
| `KW_PUBLIC` | public | सार्वजनिक | `saarvajanika` | access |
| `KW_PRIVATE` | private | गुप्त | `gupta` | access |
| `KW_PROTECTED` | protected | रक्षित | `rak_sita` | access |
| `KW_STATIC` | static | स्थिर | `sthira` | storage |
| `KW_ABSTRACT` | abstract | अमूर्त | `amuurta` | modifier |
| `KW_VIRTUAL` | virtual | आभास | `aabhaasa` | modifier |
| `KW_OVERRIDE` | override | अधिरोह | `adhirauha` | modifier |

### Paradigm: procedural

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | क्रिया | `kriyaa` | subroutine |
| `KW_PROC` | procedure | विधि | `vidhi` | subroutine |
| `KW_CALL` | call | आह्वान | `aahvaana` | subroutine |
| `KW_PARAM` | param | प्राचल | `praacala` | subroutine |
| `KW_YIELD` | yield | दा | `daa` | coroutine |
| `KW_AWAIT` | await | प्रतीक्ष | `pratiik_sa` | async |
| `KW_ASYNC` | async | असमकाल | `asamakaala` | async |

### Paradigm: robotics

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | चालक | `caalaka` | control |
| `KW_SERVO` | servo | अनुचालक | `anucaalaka` | control |
| `KW_JOINT` | joint | सन्धि | `sandhi` | control |
| `KW_POSE` | pose | मुद्रा | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | प्रक्षेपपथ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | प्रतिपुष्टि | `pratipu_sti` | control |
| `KW_PID` | pid | नियन्त्रक | `niyantraka` | control |
| `KW_DEADLINE` | deadline | कालसीमा | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | आवर्तिक | `aavartika` | realtime |
| `KW_PRIORITY` | priority | प्राथम्य | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | प्रवर्तय | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | प्रत्यक्ष | `pratyak_sa` | control |
| `KW_PLAN` | plan | योजना | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | निर्देशक | `nirdeeshaka` | memory |
| `KW_REF` | ref | सन्दर्भ | `sandarbha` | memory |
| `KW_ALLOC` | alloc | आवण्टन | `aava_ntana` | memory |
| `KW_FREE` | free | मुक्त | `mukta` | memory |
| `KW_SIZEOF` | sizeof | परिमाण | `parimaa_na` | memory |
| `KW_STRUCT` | struct | संरचना | `sa_nracanaa` | type_def |
| `KW_UNION` | union | सङ्घ | `sa_ngha` | type_def |
| `KW_ENUM` | enum | गणना | `ga_nanaa` | type_def |
| `KW_TYPEDEF` | typedef | प्रकारनिर्देश | `prakaaranirdeesha` | type_def |
| `KW_VOLATILE` | volatile | चञ्चल | `ca_ncala` | modifier |
| `KW_REGISTER` | register | पञ्जिका | `pa_njikaa` | storage |
| `KW_EXTERN` | extern | बाह्य | `baahya` | linkage |
| `KW_INLINE` | inline | अन्तःस्थ | `anta_hstha` | modifier |

### Paradigm: verification

| Construct | English | Konkani | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | अपेक्षते | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | सुनिश्चयति | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | अपरिवर्त्य | `aparivartya` | contract |
| `KW_ASSERT` | assert | प्रतिज्ञा | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | अध्यवस्यति | `adhyavasyati` | contract |
| `KW_PROVE` | prove | साधयति | `saadhayati` | contract |
| `KW_REFINES` | refines | परिष्करोति | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | प्रतिमानपरीक्षा | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Konkani native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Konkani a first-class systems-programming language, not a localized skin.

## Example

```
यदि (x > 0)        // romenagri: yadi
    ...
अन्यथा              // romenagri: anyathaa
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Konkani keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*