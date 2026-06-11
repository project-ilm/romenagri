# Hindi Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Hindi
- **ISO 639 code**: hin
- **Script**: Devanagari
- **Native speakers**: 600 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Hindi-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Hindi keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | प्रदिश | `pradisha` | ml |
| `KW_MATRIX` | matrix | आव्यूह | `aavyuuha` | ml |
| `KW_VECTOR` | vector | सदिश | `sadisha` | ml |
| `KW_GRAD` | gradient | प्रवणता | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | पश्चप्रसार | `pashcaprasaara` | ml |
| `KW_FORWARD` | forward | अग्रसार | `agrasaara` | ml |
| `KW_LAYER` | layer | परत | `parata` | ml |
| `KW_MODEL` | model | प्रतिमान | `pratimaana` | ml |
| `KW_TRAIN` | train | प्रशिक्षण | `prashik_sa_na` | ml |
| `KW_INFER` | infer | अनुमान | `anumaana` | ml |
| `KW_LOSS` | loss | हानि | `haani` | ml |
| `KW_OPTIMIZE` | optimize | इष्टतम | `i_statama` | ml |
| `KW_ACTIVATION` | activation | सक्रियण | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | भार | `bhaara` | ml |
| `KW_BIAS` | bias | अभिनति | `abhinati` | ml |
| `KW_EPOCH` | epoch | युग | `yuga` | ml |
| `KW_BATCH` | batch | बैच | `baica` | ml |
| `KW_DATASET` | dataset | दत्तसमुच्चय | `dattasamuccaya` | ml |
| `KW_EMBED` | embed | अंतःस्थापन | `anta_hsthaapana` | ml |
| `KW_ATTENTION` | attention | अवधान | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | आयात | `aayaata` | namespace |
| `KW_EXPORT` | export | निर्यात | `niryaata` | namespace |
| `KW_PACKAGE` | package | बस्ता | `bastaa` | namespace |
| `KW_NAMESPACE` | namespace | नामस्थान | `naamasthaana` | namespace |
| `KW_USE` | use | उपयोग | `upayauga` | namespace |
| `KW_INCLUDE` | include | सम्मिलित | `sammilita` | preprocessor |
| `KW_FROM` | from | से | `see` | namespace |
| `KW_AS` | as | रूप | `ruupa` | namespace |

### Paradigm: concurrent

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | सूत्र | `suutra` | concurrency |
| `KW_SPAWN` | spawn | उत्पन्न | `utpanna` | concurrency |
| `KW_LOCK` | lock | ताला | `taalaa` | concurrency |
| `KW_SYNC` | synchronized | समकालिक | `samakaalika` | concurrency |
| `KW_CHANNEL` | channel | माध्यम | `maadhyama` | concurrency |
| `KW_SELECT` | select | चुनो | `cunau` | concurrency |

### Paradigm: dataflow

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | धारा | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | नाली | `naalii` | reactive |
| `KW_MAP` | map | मानचित्र | `maanacitra` | reactive |
| `KW_FILTER` | filter | छानो | `chaanau` | reactive |
| `KW_REDUCE` | reduce | घटाओ | `ghataaau` | reactive |
| `KW_FOLD` | fold | मोड़ो | `mau_dau` | reactive |
| `KW_OBSERVE` | observe | निरीक्षण | `niriik_sa_na` | reactive |
| `KW_EMIT` | emit | उत्सर्जन | `utsarjana` | reactive |
| `KW_SUBSCRIBE` | subscribe | अभिदान | `abhidaana` | reactive |
| `KW_DEBOUNCE` | debounce | विस्पंदन | `vispa_ndana` | reactive |

### Paradigm: distributed

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | गाँठ | `gaa_ntha` | cluster |
| `KW_REPLICA` | replica | प्रतिकृति | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | सर्वसम्मति | `sarvasammati` | cluster |
| `KW_SHARD` | shard | खंड | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | जनश्रुति | `janashruti` | cluster |
| `KW_LEADER` | leader | नेता | `neetaa` | cluster |
| `KW_RPC` | rpc | दूरप्रक्रिया | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | कर्ता | `kartaa` | cluster |
| `KW_MESSAGE` | message | संदेश | `sa_ndeesha` | cluster |

### Paradigm: functional

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | अनाम | `anaama` | function |
| `KW_MATCH` | match | मिलान | `milaana` | pattern |
| `KW_WHEN` | when | जब | `jaba` | pattern |
| `KW_FUN` | fun | फलन | `phalana` | function |
| `KW_REC` | rec | पुनरावर्ती | `punaraavartii` | recursion |
| `KW_IN` | in | में | `me_n` | binding |
| `KW_WHERE` | where | जहाँ | `jahaa_n` | binding |
| `KW_DATA` | data | आँकड़ा | `aa_nka_daa` | type_def |
| `KW_TYPE` | type | प्रकार | `prakaara` | type_def |
| `KW_MODULE` | module | खंड | `kha_nda` | namespace |

### Paradigm: gpu

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | कर्नेल | `karneela` | compute |
| `KW_DEVICE` | device | यंत्र | `ya_ntra` | compute |
| `KW_HOST` | host | परिचारक | `paricaaraka` | compute |
| `KW_GLOBAL` | global | वैश्विक | `vaishvika` | compute |
| `KW_SHARED` | shared | साझा | `saajhaa` | compute |
| `KW_THREADIDX` | threadidx | सूत्रांक | `suutraa_nka` | compute |
| `KW_BLOCKIDX` | blockidx | खंडांक | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | जाल | `jaala` | compute |
| `KW_BARRIER` | barrier | अवरोध | `avaraudha` | compute |
| `KW_ATOMIC` | atomic | अणुक | `a_nuka` | compute |
| `KW_WARP` | warp | ताना | `taanaa` | compute |

### Paradigm: hdl

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | इकाई | `ikaaii` | hardware |
| `KW_ARCH` | architecture | स्थापत्य | `sthaapatya` | hardware |
| `KW_SIGNAL` | signal | संकेत | `sa_nkeeta` | hardware |
| `KW_PORT` | port | द्वार | `dvaara` | hardware |
| `KW_WIRE` | wire | तार | `taara` | hardware |
| `KW_REG` | reg | पंजिका | `pa_njikaa` | hardware |
| `KW_MODULE_HW` | module | पुरज़ा | `puraza` | hardware |
| `KW_ALWAYS` | always | सदैव | `sadaiva` | hardware |
| `KW_ASSIGN` | assign | निर्धारित | `nirdhaarita` | hardware |
| `KW_BEGIN` | begin | आरंभ | `aara_nbha` | block |
| `KW_END` | end | अंत | `a_nta` | block |

### Paradigm: imperative

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | यदि | `yadi` | control_flow |
| `KW_ELSE` | else | अन्यथा | `anyathaa` | control_flow |
| `KW_ELIF` | elif | अथवा_यदि | `athavaa_yadi` | control_flow |
| `KW_WHILE` | while | जबतक | `jabataka` | control_flow |
| `KW_DO` | do | करो | `karau` | control_flow |
| `KW_FOR` | for | हेतु | `heetu` | control_flow |
| `KW_BREAK` | break | विराम | `viraama` | control_flow |
| `KW_CONTINUE` | continue | जारी | `jaarii` | control_flow |
| `KW_SWITCH` | switch | चयन | `cayana` | control_flow |
| `KW_CASE` | case | स्थिति | `sthiti` | control_flow |
| `KW_DEFAULT` | default | मूल | `muula` | control_flow |
| `KW_RETURN` | return | लौटाओ | `lautaaau` | control_flow |
| `KW_GOTO` | goto | जाओ | `jaaau` | control_flow |
| `KW_VAR` | var | चर | `cara` | declaration |
| `KW_CONST` | const | अचर | `acara` | declaration |
| `KW_LET` | let | मानो | `maanau` | declaration |
| `KW_INT` | int | पूर्णांक | `puur_naa_nka` | type |
| `KW_FLOAT` | float | दशमलव | `dashamalava` | type |
| `KW_DOUBLE` | double | द्विगुण | `dviguu_na` | type |
| `KW_CHAR` | char | अक्षर | `ak_sara` | type |
| `KW_BOOL` | bool | तार्किक | `taarkika` | type |
| `KW_STRING` | string | वाक्य | `vaakya` | type |
| `KW_VOID` | void | शून्य | `shuunya` | type |
| `KW_TRUE` | true | सत्य | `satya` | literal |
| `KW_FALSE` | false | असत्य | `asatya` | literal |
| `KW_NULL` | null | रिक्त | `rikta` | literal |
| `KW_TRY` | try | प्रयास | `prayaasa` | exception |
| `KW_CATCH` | catch | पकड़ो | `paka_dau` | exception |
| `KW_FINALLY` | finally | अंततः | `a_ntata_h` | exception |
| `KW_THROW` | throw | फेंको | `phee_nkau` | exception |
| `KW_RAISE` | raise | उठाओ | `uthaaau` | exception |
| `KW_EXCEPT` | except | अपवाद | `apavaada` | exception |

### Paradigm: iot

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | पिन | `pina` | io |
| `KW_READ` | read | पढ़ो | `pa_dau` | io |
| `KW_WRITE` | write | लिखो | `likhau` | io |
| `KW_ANALOG` | analog | अनुरूप | `anuruupa` | io |
| `KW_DIGITAL` | digital | अंकीय | `a_nkiiya` | io |
| `KW_PWM` | pwm | स्पंदचौड़ाई | `spa_ndacau_daaii` | io |
| `KW_INTERRUPT` | interrupt | व्यवधान | `vyavadhaana` | io |
| `KW_TIMER` | timer | समयक | `samayaka` | io |
| `KW_SENSOR` | sensor | संवेदक | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | प्रवर्तक | `pravartaka` | io |
| `KW_BUS` | bus | पथ | `patha` | io |
| `KW_PROTOCOL` | protocol | नियमावली | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | निद्रा | `nidraa` | power |
| `KW_WAKE` | wake | जागो | `jaagau` | power |

### Paradigm: logic

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | नियम | `niyama` | clause |
| `KW_FACT` | fact | तथ्य | `tathya` | clause |
| `KW_QUERY` | query | प्रश्न | `prashna` | clause |
| `KW_NOT` | not | नहीं | `nahii_n` | operator |
| `KW_AND` | and | और | `aura` | operator |
| `KW_OR` | or | या | `yaa` | operator |

### Paradigm: memory

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | स्वामित्व | `svaamitva` | ownership |
| `KW_BORROW` | borrow | उधार | `udhaara` | ownership |
| `KW_MOVE` | move | स्थानांतर | `sthaanaa_ntara` | ownership |
| `KW_MUT` | mut | परिवर्ती | `parivartii` | ownership |
| `KW_LIFETIME` | lifetime | जीवनकाल | `jiivanakaala` | ownership |
| `KW_ARENA` | arena | क्षेत्र | `k_seetra` | allocation |
| `KW_GC` | gc | कचरासंग्रह | `kacaraasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | स्मृतिपिन | `smr_tipina` | allocation |

### Paradigm: oop

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | वर्ग | `varga` | type_def |
| `KW_OBJECT` | object | वस्तु | `vastu` | type_def |
| `KW_INTERFACE` | interface | अन्तरफलक | `antaraphalaka` | type_def |
| `KW_EXTENDS` | extends | विस्तारित | `vistaarita` | inheritance |
| `KW_IMPLEMENTS` | implements | कार्यान्वित | `kaaryaanvita` | inheritance |
| `KW_NEW` | new | नवीन | `naviina` | instantiation |
| `KW_THIS` | this | यह | `yaha` | reference |
| `KW_SUPER` | super | परम | `parama` | reference |
| `KW_PUBLIC` | public | सार्वजनिक | `saarvajanika` | access |
| `KW_PRIVATE` | private | निजी | `nijii` | access |
| `KW_PROTECTED` | protected | संरक्षित | `sa_nrak_sita` | access |
| `KW_STATIC` | static | स्थिर | `sthira` | storage |
| `KW_ABSTRACT` | abstract | अमूर्त | `amuurta` | modifier |
| `KW_VIRTUAL` | virtual | आभासी | `aabhaasii` | modifier |
| `KW_OVERRIDE` | override | अधिरोहण | `adhirauha_na` | modifier |

### Paradigm: procedural

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | कृत्य | `kr_tya` | subroutine |
| `KW_PROC` | procedure | प्रक्रिया | `prakriyaa` | subroutine |
| `KW_CALL` | call | बुलाओ | `bulaaau` | subroutine |
| `KW_PARAM` | param | प्राचल | `praacala` | subroutine |
| `KW_YIELD` | yield | प्रदान | `pradaana` | coroutine |
| `KW_AWAIT` | await | प्रतीक्षा | `pratiik_saa` | async |
| `KW_ASYNC` | async | अतुल्यकाल | `atulyakaala` | async |

### Paradigm: robotics

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | मोटर | `maotara` | control |
| `KW_SERVO` | servo | सर्वो | `sarvau` | control |
| `KW_JOINT` | joint | संधि | `sa_ndhi` | control |
| `KW_POSE` | pose | मुद्रा | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | प्रक्षेपपथ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | प्रतिपुष्टि | `pratipu_sti` | control |
| `KW_PID` | pid | पीआईडी | `piiaaiidii` | control |
| `KW_DEADLINE` | deadline | समयसीमा | `samayasiimaa` | realtime |
| `KW_PERIODIC` | periodic | आवर्ती | `aavartii` | realtime |
| `KW_PRIORITY` | priority | प्राथमिकता | `praathamikataa` | realtime |
| `KW_ACTUATE` | actuate | प्रवर्तन | `pravartana` | control |
| `KW_PERCEIVE` | perceive | प्रत्यक्षण | `pratyak_sa_na` | control |
| `KW_PLAN` | plan | योजना | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | संकेतक | `sa_nkeetaka` | memory |
| `KW_REF` | ref | संदर्भ | `sa_ndarbha` | memory |
| `KW_ALLOC` | alloc | आवंटन | `aava_ntana` | memory |
| `KW_FREE` | free | मुक्त | `mukta` | memory |
| `KW_SIZEOF` | sizeof | आकार | `aakaara` | memory |
| `KW_STRUCT` | struct | संरचना | `sa_nracanaa` | type_def |
| `KW_UNION` | union | संघ | `sa_ngha` | type_def |
| `KW_ENUM` | enum | गणना | `ga_nanaa` | type_def |
| `KW_TYPEDEF` | typedef | प्रकारलेख | `prakaaraleekha` | type_def |
| `KW_VOLATILE` | volatile | अस्थिर | `asthira` | modifier |
| `KW_REGISTER` | register | पंजी | `pa_njii` | storage |
| `KW_EXTERN` | extern | बाह्य | `baahya` | linkage |
| `KW_INLINE` | inline | अंतःपंक्ति | `anta_hpa_nkti` | modifier |

### Paradigm: verification

| Construct | English | Hindi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | अपेक्षित | `apeek_sita` | contract |
| `KW_ENSURES` | ensures | सुनिश्चित | `sunishcita` | contract |
| `KW_INVARIANT` | invariant | अचर | `acara` | contract |
| `KW_ASSERT` | assert | दृढ़कथन | `dr_dakathana` | contract |
| `KW_ASSUME` | assume | मानना | `maananaa` | contract |
| `KW_PROVE` | prove | सिद्ध | `siddha` | contract |
| `KW_REFINES` | refines | परिष्कृत | `pari_skr_ta` | contract |
| `KW_MODEL_CHECK` | modelcheck | प्रतिमानजाँच | `pratimaanajaa_nca` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Hindi native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Hindi a first-class systems-programming language, not a localized skin.

## Example

```
यदि (x > 0)        // romenagri: yadi
    ...
अन्यथा              // romenagri: anyathaa
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Hindi keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*