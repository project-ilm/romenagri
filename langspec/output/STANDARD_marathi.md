# Marathi Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Marathi
- **ISO 639 code**: mar
- **Script**: Devanagari
- **Native speakers**: 83 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Marathi-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Marathi keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
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

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | आयात | `aayaata` | namespace |
| `KW_EXPORT` | export | निर्यात | `niryaata` | namespace |
| `KW_PACKAGE` | package | पॅकेज | `paikeeja` | namespace |
| `KW_NAMESPACE` | namespace | नामाकाश | `naamaakaasha` | namespace |
| `KW_USE` | use | उपयोग | `upayauga` | namespace |
| `KW_INCLUDE` | include | अन्तर्भाव | `antarbhaava` | preprocessor |
| `KW_FROM` | from | तः | `ta_h` | namespace |
| `KW_AS` | as | इव | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | धागा | `dhaagaa` | concurrency |
| `KW_SPAWN` | spawn | निर्माण | `nirmaa_na` | concurrency |
| `KW_LOCK` | lock | कुलूप | `kuluupa` | concurrency |
| `KW_SYNC` | synchronized | समकालिक | `samakaalika` | concurrency |
| `KW_CHANNEL` | channel | माध्यम | `maadhyama` | concurrency |
| `KW_SELECT` | select | निवडा | `nivadaa` | concurrency |

### Paradigm: dataflow

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
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

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
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

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | निनावी | `ninaavii` | function |
| `KW_MATCH` | match | जुळवा | `julavaa` | pattern |
| `KW_WHEN` | when | जेव्हा | `jeevhaa` | pattern |
| `KW_FUN` | fun | फलन | `phalana` | function |
| `KW_REC` | rec | पुनरावर्ती | `punaraavartii` | recursion |
| `KW_IN` | in | मध्ये | `madhyee` | binding |
| `KW_WHERE` | where | जिथे | `jithee` | binding |
| `KW_DATA` | data | विदा | `vidaa` | type_def |
| `KW_TYPE` | type | प्रकार | `prakaara` | type_def |
| `KW_MODULE` | module | घटक | `ghataka` | namespace |

### Paradigm: gpu

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
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

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | घटक | `ghataka` | hardware |
| `KW_ARCH` | architecture | स्थापत्य | `sthaapatya` | hardware |
| `KW_SIGNAL` | signal | संकेत | `sa_nkeeta` | hardware |
| `KW_PORT` | port | बंदर | `ba_ndara` | hardware |
| `KW_WIRE` | wire | तार | `taara` | hardware |
| `KW_REG` | reg | नोंद | `nau_nda` | hardware |
| `KW_MODULE_HW` | module | भाग | `bhaaga` | hardware |
| `KW_ALWAYS` | always | नेहमी | `neehamii` | hardware |
| `KW_ASSIGN` | assign | नेमणूक | `neema_nuuka` | hardware |
| `KW_BEGIN` | begin | प्रारंभ | `praara_nbha` | block |
| `KW_END` | end | शेवट | `sheevata` | block |

### Paradigm: imperative

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | जर | `jara` | control_flow |
| `KW_ELSE` | else | अन्यथा | `anyathaa` | control_flow |
| `KW_ELIF` | elif | किंवाजर | `ki_nvaajara` | control_flow |
| `KW_WHILE` | while | पर्यंत | `parya_nta` | control_flow |
| `KW_DO` | do | करा | `karaa` | control_flow |
| `KW_FOR` | for | साठी | `saathii` | control_flow |
| `KW_BREAK` | break | थांबा | `thaa_mbaa` | control_flow |
| `KW_CONTINUE` | continue | सुरूठेवा | `suruutheevaa` | control_flow |
| `KW_SWITCH` | switch | निवड | `nivada` | control_flow |
| `KW_CASE` | case | स्थिती | `sthitii` | control_flow |
| `KW_DEFAULT` | default | पूर्वनिर्धारित | `puurvanirdhaarita` | control_flow |
| `KW_RETURN` | return | परत | `parata` | control_flow |
| `KW_GOTO` | goto | जा | `jaa` | control_flow |
| `KW_VAR` | var | चल | `cala` | declaration |
| `KW_CONST` | const | स्थिरांक | `sthiraa_nka` | declaration |
| `KW_LET` | let | समजा | `samajaa` | declaration |
| `KW_INT` | int | पूर्णांक | `puur_naa_nka` | type |
| `KW_FLOAT` | float | दशांश | `dashaa_nsha` | type |
| `KW_DOUBLE` | double | द्विगुण | `dvigu_na` | type |
| `KW_CHAR` | char | अक्षर | `ak_sara` | type |
| `KW_BOOL` | bool | तार्किक | `taarkika` | type |
| `KW_STRING` | string | अक्षरमाला | `ak_saramaalaa` | type |
| `KW_VOID` | void | शून्य | `shuunya` | type |
| `KW_TRUE` | true | सत्य | `satya` | literal |
| `KW_FALSE` | false | असत्य | `asatya` | literal |
| `KW_NULL` | null | रिक्त | `rikta` | literal |
| `KW_TRY` | try | प्रयत्न | `prayatna` | exception |
| `KW_CATCH` | catch | पकडा | `pakadaa` | exception |
| `KW_FINALLY` | finally | अखेरीस | `akheeriisa` | exception |
| `KW_THROW` | throw | फेका | `pheekaa` | exception |
| `KW_RAISE` | raise | उठवा | `uthavaa` | exception |
| `KW_EXCEPT` | except | अपवाद | `apavaada` | exception |

### Paradigm: iot

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
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

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | नियम | `niyama` | clause |
| `KW_FACT` | fact | तथ्य | `tathya` | clause |
| `KW_QUERY` | query | प्रश्न | `prashna` | clause |
| `KW_NOT` | not | नाही | `naahii` | operator |
| `KW_AND` | and | आणि | `aa_ni` | operator |
| `KW_OR` | or | किंवा | `ki_nvaa` | operator |

### Paradigm: memory

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
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

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | वर्ग | `varga` | type_def |
| `KW_OBJECT` | object | वस्तू | `vastuu` | type_def |
| `KW_INTERFACE` | interface | अंतरफलक | `a_ntaraphalaka` | type_def |
| `KW_EXTENDS` | extends | विस्तारित | `vistaarita` | inheritance |
| `KW_IMPLEMENTS` | implements | अंमलात | `a_nmalaata` | inheritance |
| `KW_NEW` | new | नवीन | `naviina` | instantiation |
| `KW_THIS` | this | हे | `hee` | reference |
| `KW_SUPER` | super | परम | `parama` | reference |
| `KW_PUBLIC` | public | सार्वजनिक | `saarvajanika` | access |
| `KW_PRIVATE` | private | खाजगी | `khaajagii` | access |
| `KW_PROTECTED` | protected | संरक्षित | `sa_nrak_sita` | access |
| `KW_STATIC` | static | स्थिर | `sthira` | storage |
| `KW_ABSTRACT` | abstract | अमूर्त | `amuurta` | modifier |
| `KW_VIRTUAL` | virtual | आभासी | `aabhaasii` | modifier |
| `KW_OVERRIDE` | override | अधिक्रमण | `adhikrama_na` | modifier |

### Paradigm: procedural

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | कार्य | `kaarya` | subroutine |
| `KW_PROC` | procedure | प्रक्रिया | `prakriyaa` | subroutine |
| `KW_CALL` | call | बोलवा | `baolavaa` | subroutine |
| `KW_PARAM` | param | प्राचल | `praacala` | subroutine |
| `KW_YIELD` | yield | द्या | `dyaa` | coroutine |
| `KW_AWAIT` | await | प्रतीक्षा | `pratiik_saa` | async |
| `KW_ASYNC` | async | असमकालिक | `asamakaalika` | async |

### Paradigm: robotics

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
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

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | निर्देशक | `nirdeeshaka` | memory |
| `KW_REF` | ref | संदर्भ | `sa_ndarbha` | memory |
| `KW_ALLOC` | alloc | वाटप | `vaatapa` | memory |
| `KW_FREE` | free | मुक्त | `mukta` | memory |
| `KW_SIZEOF` | sizeof | आकार | `aakaara` | memory |
| `KW_STRUCT` | struct | संरचना | `sa_nracanaa` | type_def |
| `KW_UNION` | union | संघ | `sa_ngha` | type_def |
| `KW_ENUM` | enum | गणना | `ga_nanaa` | type_def |
| `KW_TYPEDEF` | typedef | प्रकारव्याख्या | `prakaaravyaakhyaa` | type_def |
| `KW_VOLATILE` | volatile | अस्थिर | `asthira` | modifier |
| `KW_REGISTER` | register | नोंदणी | `nau_nda_nii` | storage |
| `KW_EXTERN` | extern | बाह्य | `baahya` | linkage |
| `KW_INLINE` | inline | ओळीत | `auliita` | modifier |

### Paradigm: verification

| Construct | English | Marathi | Romenagri (ASCII-7) | Category |
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

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Marathi native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Marathi a first-class systems-programming language, not a localized skin.

## Example

```
जर (x > 0)        // romenagri: jara
    ...
अन्यथा              // romenagri: anyathaa
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Marathi keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*