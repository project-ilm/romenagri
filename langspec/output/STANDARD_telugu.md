# Telugu Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Telugu
- **ISO 639 code**: tel
- **Script**: Telugu
- **Native speakers**: 95 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Telugu-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Telugu keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | ప్రదిశ | `pradisha` | ml |
| `KW_MATRIX` | matrix | ఆవ్యూహ | `aavyuuha` | ml |
| `KW_VECTOR` | vector | సదిశ | `sadisha` | ml |
| `KW_GRAD` | gradient | ప్రవణతా | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | ప్రతిప్రసార | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | అగ్రప్రసార | `agraprasaara` | ml |
| `KW_LAYER` | layer | స్తర | `stara` | ml |
| `KW_MODEL` | model | ప్రతిమాన | `pratimaana` | ml |
| `KW_TRAIN` | train | ప్రశిక్షణ | `prashik_sa_na` | ml |
| `KW_INFER` | infer | అనుమాన | `anumaana` | ml |
| `KW_LOSS` | loss | హాని | `haani` | ml |
| `KW_OPTIMIZE` | optimize | అనుకూలన | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | సక్రియణ | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | భార | `bhaara` | ml |
| `KW_BIAS` | bias | పక్షపాత | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | కల్ప | `kalpa` | ml |
| `KW_BATCH` | batch | పుఞ్జ | `pu_nja` | ml |
| `KW_DATASET` | dataset | దత్తసమూహ | `dattasamuuha` | ml |
| `KW_EMBED` | embed | నివేశన | `niveeshana` | ml |
| `KW_ATTENTION` | attention | అవధాన | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | దిగుమతి | `digumati` | namespace |
| `KW_EXPORT` | export | ఎగుమతి | `egumati` | namespace |
| `KW_PACKAGE` | package | సంచి | `sa_nci` | namespace |
| `KW_NAMESPACE` | namespace | నామాకాశ | `naamaakaasha` | namespace |
| `KW_USE` | use | ఉపయోగ | `upayauga` | namespace |
| `KW_INCLUDE` | include | అన్తర్భావ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | తః | `ta_h` | namespace |
| `KW_AS` | as | ఇవ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | తంతువు | `ta_ntuvu` | concurrency |
| `KW_SPAWN` | spawn | సృష్టించు | `sr_sti_ncu` | concurrency |
| `KW_LOCK` | lock | తాళం | `taala_m` | concurrency |
| `KW_SYNC` | synchronized | సమకాలీకరణ | `samakaaliikara_na` | concurrency |
| `KW_CHANNEL` | channel | మార్గం | `maarga_m` | concurrency |
| `KW_SELECT` | select | ఎంచుకో | `e_ncukoo` | concurrency |

### Paradigm: dataflow

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | ధారా | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | ప్రణాల | `pra_naala` | reactive |
| `KW_MAP` | map | ప్రతిచిత్ర | `praticitra` | reactive |
| `KW_FILTER` | filter | ఛాల | `chaala` | reactive |
| `KW_REDUCE` | reduce | న్యూనీకృ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | సంవేష్ట | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | నిరీక్ష | `niriik_sa` | reactive |
| `KW_EMIT` | emit | ఉత్సృజ | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | అభినివేశ | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | స్పన్దశోధన | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | గ్రన్థి | `granthi` | cluster |
| `KW_REPLICA` | replica | ప్రతికృతి | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | సర్వసమ్మతి | `sarvasammati` | cluster |
| `KW_SHARD` | shard | ఖణ్డ | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | జనవాద | `janavaada` | cluster |
| `KW_LEADER` | leader | నాయక | `naayaka` | cluster |
| `KW_RPC` | rpc | దూరప్రక్రియా | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | కర్తృ | `kartr_` | cluster |
| `KW_MESSAGE` | message | సన్దేశ | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | అజ్ఞాత | `ajnyaata` | function |
| `KW_MATCH` | match | సరిపోల్చు | `saripoolcu` | pattern |
| `KW_WHEN` | when | ఎప్పుడు | `eppudu` | pattern |
| `KW_FUN` | fun | ప్రమేయ | `prameeya` | function |
| `KW_REC` | rec | పునరావృత | `punaraavr_ta` | recursion |
| `KW_IN` | in | లో | `loo` | binding |
| `KW_WHERE` | where | ఎక్కడ | `ekkada` | binding |
| `KW_DATA` | data | దత్తాంశం | `dattaa_msha_m` | type_def |
| `KW_TYPE` | type | రకం | `raka_m` | type_def |
| `KW_MODULE` | module | మాడ్యూల్ | `maadyuula` | namespace |

### Paradigm: gpu

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | బీజ | `biija` | compute |
| `KW_DEVICE` | device | యన్త్ర | `yantra` | compute |
| `KW_HOST` | host | ఆతిథేయ | `aatitheeya` | compute |
| `KW_GLOBAL` | global | వైశ్విక | `vaishvika` | compute |
| `KW_SHARED` | shared | సహభాజిత | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | తన్త్వఙ్క | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | ఖణ్డాఙ్క | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | జాల | `jaala` | compute |
| `KW_BARRIER` | barrier | అవరోధ | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | ఆణవిక | `aa_navika` | compute |
| `KW_WARP` | warp | తన్తుసమూహ | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | అస్తిత్వం | `astitva_m` | hardware |
| `KW_ARCH` | architecture | నిర్మాణకళ | `nirmaa_nakala` | hardware |
| `KW_SIGNAL` | signal | సంకేతం | `sa_nkeeta_m` | hardware |
| `KW_PORT` | port | రేవు | `reevu` | hardware |
| `KW_WIRE` | wire | తీగ | `tiiga` | hardware |
| `KW_REG` | reg | నమోదిక | `namoodika` | hardware |
| `KW_MODULE_HW` | module | భాగం | `bhaaga_m` | hardware |
| `KW_ALWAYS` | always | ఎల్లప్పుడూ | `ellappuduu` | hardware |
| `KW_ASSIGN` | assign | కేటాయింపు | `keetaayi_mpu` | hardware |
| `KW_BEGIN` | begin | ప్రారంభం | `praara_mbha_m` | block |
| `KW_END` | end | ముగింపు | `mugi_mpu` | block |

### Paradigm: imperative

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | ఒకవేళ | `okaveela` | control_flow |
| `KW_ELSE` | else | లేకపోతే | `leekapootee` | control_flow |
| `KW_ELIF` | elif | లేదావేళ | `leedaaveela` | control_flow |
| `KW_WHILE` | while | వరకు | `varaku` | control_flow |
| `KW_DO` | do | చేయి | `ceeyi` | control_flow |
| `KW_FOR` | for | కొరకు | `koraku` | control_flow |
| `KW_BREAK` | break | ఆపు | `aapu` | control_flow |
| `KW_CONTINUE` | continue | కొనసాగు | `konasaagu` | control_flow |
| `KW_SWITCH` | switch | ఎంపిక | `empika` | control_flow |
| `KW_CASE` | case | స్థితి | `sthiti` | control_flow |
| `KW_DEFAULT` | default | అప్రమేయ | `aprameeya` | control_flow |
| `KW_RETURN` | return | తిరిగి | `tirigi` | control_flow |
| `KW_GOTO` | goto | వెళ్ళు | `vellu` | control_flow |
| `KW_VAR` | var | చరరాశి | `cararaashi` | declaration |
| `KW_CONST` | const | స్థిరరాశి | `sthiraraashi` | declaration |
| `KW_LET` | let | అనుకో | `anukoo` | declaration |
| `KW_INT` | int | పూర్ణాంకం | `puur_naa_nka_m` | type |
| `KW_FLOAT` | float | దశాంశం | `dashaa_msha_m` | type |
| `KW_DOUBLE` | double | ద్విగుణ | `dvigu_na` | type |
| `KW_CHAR` | char | అక్షరం | `ak_sara_m` | type |
| `KW_BOOL` | bool | తార్కిక | `taarkika` | type |
| `KW_STRING` | string | పదబంధం | `padaba_ndha_m` | type |
| `KW_VOID` | void | శూన్య | `shuunya` | type |
| `KW_TRUE` | true | నిజం | `nija_m` | literal |
| `KW_FALSE` | false | అబద్ధం | `abaddha_m` | literal |
| `KW_NULL` | null | ఖాళీ | `khaalii` | literal |
| `KW_TRY` | try | ప్రయత్నించు | `prayatni_ncu` | exception |
| `KW_CATCH` | catch | పట్టుకో | `pattukoo` | exception |
| `KW_FINALLY` | finally | చివరగా | `civaragaa` | exception |
| `KW_THROW` | throw | విసురు | `visuru` | exception |
| `KW_RAISE` | raise | లేపు | `leepu` | exception |
| `KW_EXCEPT` | except | మినహాయింపు | `minahaayi_mpu` | exception |

### Paradigm: iot

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | కీలక | `kiilaka` | io |
| `KW_READ` | read | పఠ | `patha` | io |
| `KW_WRITE` | write | లిఖ | `likha` | io |
| `KW_ANALOG` | analog | సదృశ | `sadr_sha` | io |
| `KW_DIGITAL` | digital | అఙ్కీయ | `a_nkiiya` | io |
| `KW_PWM` | pwm | స్పన్దవిస్తార | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | విఘ్న | `vighna` | io |
| `KW_TIMER` | timer | కాలయన్త్ర | `kaalayantra` | io |
| `KW_SENSOR` | sensor | సంవేదక | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | ప్రవర్తక | `pravartaka` | io |
| `KW_BUS` | bus | మార్గ | `maarga` | io |
| `KW_PROTOCOL` | protocol | నియమావలీ | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | సుషుప్తి | `su_supti` | power |
| `KW_WAKE` | wake | జాగృ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | నియమం | `niyama_m` | clause |
| `KW_FACT` | fact | వాస్తవం | `vaastava_m` | clause |
| `KW_QUERY` | query | ప్రశ్న | `prashna` | clause |
| `KW_NOT` | not | కాదు | `kaadu` | operator |
| `KW_AND` | and | మరియు | `mariyu` | operator |
| `KW_OR` | or | లేదా | `leedaa` | operator |

### Paradigm: memory

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | స్వామిత్వ | `svaamitva` | ownership |
| `KW_BORROW` | borrow | ఋణ | `r_na` | ownership |
| `KW_MOVE` | move | స్థానాన్తర | `sthaanaantara` | ownership |
| `KW_MUT` | mut | పరివర్త్య | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | ఆయుష్కాల | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | క్షేత్ర | `k_seetra` | allocation |
| `KW_GC` | gc | మలసంగ్రహ | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | స్మృతికీలక | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | తరగతి | `taragati` | type_def |
| `KW_OBJECT` | object | వస్తువు | `vastuvu` | type_def |
| `KW_INTERFACE` | interface | అంతరముఖం | `a_ntaramukha_m` | type_def |
| `KW_EXTENDS` | extends | విస్తరించు | `vistari_ncu` | inheritance |
| `KW_IMPLEMENTS` | implements | అమలుచేయు | `amaluceeyu` | inheritance |
| `KW_NEW` | new | కొత్త | `kotta` | instantiation |
| `KW_THIS` | this | ఇది | `idi` | reference |
| `KW_SUPER` | super | పర | `para` | reference |
| `KW_PUBLIC` | public | బహిరంగ | `bahira_nga` | access |
| `KW_PRIVATE` | private | అంతరంగ | `a_ntara_nga` | access |
| `KW_PROTECTED` | protected | రక్షిత | `rak_sita` | access |
| `KW_STATIC` | static | స్థిర | `sthira` | storage |
| `KW_ABSTRACT` | abstract | నైరూప్య | `nairuupya` | modifier |
| `KW_VIRTUAL` | virtual | మాయా | `maayaa` | modifier |
| `KW_OVERRIDE` | override | అధిరోహణ | `adhirauha_na` | modifier |

### Paradigm: procedural

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | ప్రమేయం | `prameeya_m` | subroutine |
| `KW_PROC` | procedure | విధానం | `vidhaana_m` | subroutine |
| `KW_CALL` | call | పిలువు | `piluvu` | subroutine |
| `KW_PARAM` | param | ప్రాచలం | `praacala_m` | subroutine |
| `KW_YIELD` | yield | ఇవ్వు | `ivvu` | coroutine |
| `KW_AWAIT` | await | వేచిఉండు | `veeciu_ndu` | async |
| `KW_ASYNC` | async | అసమకాలిక | `asamakaalika` | async |

### Paradigm: robotics

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | చాలక | `caalaka` | control |
| `KW_SERVO` | servo | అనుచాలక | `anucaalaka` | control |
| `KW_JOINT` | joint | సన్ధి | `sandhi` | control |
| `KW_POSE` | pose | ముద్రా | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | ప్రక్షేపపథ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | ప్రతిపుష్టి | `pratipu_sti` | control |
| `KW_PID` | pid | నియన్త్రక | `niyantraka` | control |
| `KW_DEADLINE` | deadline | కాలసీమా | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | ఆవర్తిక | `aavartika` | realtime |
| `KW_PRIORITY` | priority | ప్రాథమ్య | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | ప్రవర్తయ | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | ప్రత్యక్ష | `pratyak_sa` | control |
| `KW_PLAN` | plan | యోజనా | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | సూచిక | `suucika` | memory |
| `KW_REF` | ref | సూచన | `suucana` | memory |
| `KW_ALLOC` | alloc | కేటాయించు | `keetaayi_ncu` | memory |
| `KW_FREE` | free | విడుదల | `vidudala` | memory |
| `KW_SIZEOF` | sizeof | పరిమాణం | `parimaa_na_m` | memory |
| `KW_STRUCT` | struct | నిర్మాణం | `nirmaa_na_m` | type_def |
| `KW_UNION` | union | సంఘం | `sa_ngha_m` | type_def |
| `KW_ENUM` | enum | గణన | `ga_nana` | type_def |
| `KW_TYPEDEF` | typedef | రకనిర్వచనం | `rakanirvacana_m` | type_def |
| `KW_VOLATILE` | volatile | అస్థిర | `asthira` | modifier |
| `KW_REGISTER` | register | నమోదు | `namoodu` | storage |
| `KW_EXTERN` | extern | బాహ్య | `baahya` | linkage |
| `KW_INLINE` | inline | అంతఃవరుస | `a_nta_hvarusa` | modifier |

### Paradigm: verification

| Construct | English | Telugu | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | అపేక్షతే | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | సునిశ్చయతి | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | అపరివర్త్య | `aparivartya` | contract |
| `KW_ASSERT` | assert | ప్రతిజ్ఞా | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | అధ్యవస్యతి | `adhyavasyati` | contract |
| `KW_PROVE` | prove | సాధయతి | `saadhayati` | contract |
| `KW_REFINES` | refines | పరిష్కరోతి | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | ప్రతిమానపరీక్షా | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Telugu native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Telugu a first-class systems-programming language, not a localized skin.

## Example

```
ఒకవేళ (x > 0)        // romenagri: okaveela
    ...
లేకపోతే              // romenagri: leekapootee
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Telugu keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*