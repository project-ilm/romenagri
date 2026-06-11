# Gujarati Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Gujarati
- **ISO 639 code**: guj
- **Script**: Gujarati
- **Native speakers**: 55 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Gujarati-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Gujarati keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | પ્રદિશ | `pradisha` | ml |
| `KW_MATRIX` | matrix | આવ્યૂહ | `aavyuuha` | ml |
| `KW_VECTOR` | vector | સદિશ | `sadisha` | ml |
| `KW_GRAD` | gradient | પ્રવણતા | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | પ્રતિપ્રસાર | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | અગ્રપ્રસાર | `agraprasaara` | ml |
| `KW_LAYER` | layer | સ્તર | `stara` | ml |
| `KW_MODEL` | model | પ્રતિમાન | `pratimaana` | ml |
| `KW_TRAIN` | train | પ્રશિક્ષણ | `prashik_sa_na` | ml |
| `KW_INFER` | infer | અનુમાન | `anumaana` | ml |
| `KW_LOSS` | loss | હાનિ | `haani` | ml |
| `KW_OPTIMIZE` | optimize | અનુકૂલન | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | સક્રિયણ | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | ભાર | `bhaara` | ml |
| `KW_BIAS` | bias | પક્ષપાત | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | કલ્પ | `kalpa` | ml |
| `KW_BATCH` | batch | પુઞ્જ | `pu_nja` | ml |
| `KW_DATASET` | dataset | દત્તસમૂહ | `dattasamuuha` | ml |
| `KW_EMBED` | embed | નિવેશન | `niveeshana` | ml |
| `KW_ATTENTION` | attention | અવધાન | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | આયાત | `aayaata` | namespace |
| `KW_EXPORT` | export | નિકાસ | `nikaasa` | namespace |
| `KW_PACKAGE` | package | પૅકેજ | `paikeeja` | namespace |
| `KW_NAMESPACE` | namespace | નામાકાશ | `naamaakaasha` | namespace |
| `KW_USE` | use | ઉપયોગ | `upayauga` | namespace |
| `KW_INCLUDE` | include | અન્તર્ભાવ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | તઃ | `ta_h` | namespace |
| `KW_AS` | as | ઇવ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | તંતુ | `ta_ntu` | concurrency |
| `KW_SPAWN` | spawn | ઉત્પન્ન | `utpanna` | concurrency |
| `KW_LOCK` | lock | તાળું | `taalu_n` | concurrency |
| `KW_SYNC` | synchronized | સમકાલિક | `samakaalika` | concurrency |
| `KW_CHANNEL` | channel | માધ્યમ | `maadhyama` | concurrency |
| `KW_SELECT` | select | પસંદ | `pasa_nda` | concurrency |

### Paradigm: dataflow

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | ધારા | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | પ્રણાલ | `pra_naala` | reactive |
| `KW_MAP` | map | પ્રતિચિત્ર | `praticitra` | reactive |
| `KW_FILTER` | filter | છાલ | `chaala` | reactive |
| `KW_REDUCE` | reduce | ન્યૂનીકૃ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | સંવેષ્ટ | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | નિરીક્ષ | `niriik_sa` | reactive |
| `KW_EMIT` | emit | ઉત્સૃજ | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | અભિનિવેશ | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | સ્પન્દશોધન | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | ગ્રન્થિ | `granthi` | cluster |
| `KW_REPLICA` | replica | પ્રતિકૃતિ | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | સર્વસમ્મતિ | `sarvasammati` | cluster |
| `KW_SHARD` | shard | ખણ્ડ | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | જનવાદ | `janavaada` | cluster |
| `KW_LEADER` | leader | નાયક | `naayaka` | cluster |
| `KW_RPC` | rpc | દૂરપ્રક્રિયા | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | કર્તૃ | `kartr_` | cluster |
| `KW_MESSAGE` | message | સન્દેશ | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | અનામી | `anaamii` | function |
| `KW_MATCH` | match | મેળ | `meela` | pattern |
| `KW_WHEN` | when | જ્યારે | `jyaaree` | pattern |
| `KW_FUN` | fun | ફલન | `phalana` | function |
| `KW_REC` | rec | પુનરાવર્તી | `punaraavartii` | recursion |
| `KW_IN` | in | માં | `maa_n` | binding |
| `KW_WHERE` | where | જ્યાં | `jyaa_n` | binding |
| `KW_DATA` | data | માહિતી | `maahitii` | type_def |
| `KW_TYPE` | type | પ્રકાર | `prakaara` | type_def |
| `KW_MODULE` | module | વિભાગ | `vibhaaga` | namespace |

### Paradigm: gpu

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | બીજ | `biija` | compute |
| `KW_DEVICE` | device | યન્ત્ર | `yantra` | compute |
| `KW_HOST` | host | આતિથેય | `aatitheeya` | compute |
| `KW_GLOBAL` | global | વૈશ્વિક | `vaishvika` | compute |
| `KW_SHARED` | shared | સહભાજિત | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | તન્ત્વઙ્ક | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | ખણ્ડાઙ્ક | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | જાલ | `jaala` | compute |
| `KW_BARRIER` | barrier | અવરોધ | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | આણવિક | `aa_navika` | compute |
| `KW_WARP` | warp | તન્તુસમૂહ | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | એકમ | `eekama` | hardware |
| `KW_ARCH` | architecture | સ્થાપત્ય | `sthaapatya` | hardware |
| `KW_SIGNAL` | signal | સંકેત | `sa_nkeeta` | hardware |
| `KW_PORT` | port | દ્વાર | `dvaara` | hardware |
| `KW_WIRE` | wire | તાર | `taara` | hardware |
| `KW_REG` | reg | નોંધ | `nau_ndha` | hardware |
| `KW_MODULE_HW` | module | ભાગ | `bhaaga` | hardware |
| `KW_ALWAYS` | always | હંમેશા | `ha_nmeeshaa` | hardware |
| `KW_ASSIGN` | assign | સોંપો | `sau_npau` | hardware |
| `KW_BEGIN` | begin | શરૂ | `sharuu` | block |
| `KW_END` | end | અંત | `a_nta` | block |

### Paradigm: imperative

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | જો | `jau` | control_flow |
| `KW_ELSE` | else | નહીંતર | `nahii_ntara` | control_flow |
| `KW_ELIF` | elif | અથવાજો | `athavaajau` | control_flow |
| `KW_WHILE` | while | જ્યાંસુધી | `jyaa_nsudhii` | control_flow |
| `KW_DO` | do | કરો | `karau` | control_flow |
| `KW_FOR` | for | માટે | `maatee` | control_flow |
| `KW_BREAK` | break | તોડો | `taudau` | control_flow |
| `KW_CONTINUE` | continue | ચાલુ | `caalu` | control_flow |
| `KW_SWITCH` | switch | પસંદગી | `pasa_ndagii` | control_flow |
| `KW_CASE` | case | સ્થિતિ | `sthiti` | control_flow |
| `KW_DEFAULT` | default | મૂળભૂત | `muulabhuuta` | control_flow |
| `KW_RETURN` | return | પાછા | `paachaa` | control_flow |
| `KW_GOTO` | goto | જાઓ | `jaaau` | control_flow |
| `KW_VAR` | var | ચલ | `cala` | declaration |
| `KW_CONST` | const | અચલ | `acala` | declaration |
| `KW_LET` | let | ધારો | `dhaarau` | declaration |
| `KW_INT` | int | પૂર્ણાંક | `puur_naa_nka` | type |
| `KW_FLOAT` | float | દશાંશ | `dashaa_nsha` | type |
| `KW_DOUBLE` | double | દ્વિગુણ | `dvigu_na` | type |
| `KW_CHAR` | char | અક્ષર | `ak_sara` | type |
| `KW_BOOL` | bool | તાર્કિક | `taarkika` | type |
| `KW_STRING` | string | શબ્દમાળા | `shabdamaalaa` | type |
| `KW_VOID` | void | શૂન્ય | `shuunya` | type |
| `KW_TRUE` | true | સાચું | `saacu_n` | literal |
| `KW_FALSE` | false | ખોટું | `khautu_n` | literal |
| `KW_NULL` | null | ખાલી | `khaalii` | literal |
| `KW_TRY` | try | પ્રયાસ | `prayaasa` | exception |
| `KW_CATCH` | catch | પકડો | `pakadau` | exception |
| `KW_FINALLY` | finally | છેવટે | `cheevatee` | exception |
| `KW_THROW` | throw | ફેંકો | `phee_nkau` | exception |
| `KW_RAISE` | raise | ઉઠાવો | `uthaavau` | exception |
| `KW_EXCEPT` | except | અપવાદ | `apavaada` | exception |

### Paradigm: iot

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | કીલક | `kiilaka` | io |
| `KW_READ` | read | પઠ | `patha` | io |
| `KW_WRITE` | write | લિખ | `likha` | io |
| `KW_ANALOG` | analog | સદૃશ | `sadr_sha` | io |
| `KW_DIGITAL` | digital | અઙ્કીય | `a_nkiiya` | io |
| `KW_PWM` | pwm | સ્પન્દવિસ્તાર | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | વિઘ્ન | `vighna` | io |
| `KW_TIMER` | timer | કાલયન્ત્ર | `kaalayantra` | io |
| `KW_SENSOR` | sensor | સંવેદક | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | પ્રવર્તક | `pravartaka` | io |
| `KW_BUS` | bus | માર્ગ | `maarga` | io |
| `KW_PROTOCOL` | protocol | નિયમાવલી | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | સુષુપ્તિ | `su_supti` | power |
| `KW_WAKE` | wake | જાગૃ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | નિયમ | `niyama` | clause |
| `KW_FACT` | fact | હકીકત | `hakiikata` | clause |
| `KW_QUERY` | query | પ્રશ્ન | `prashna` | clause |
| `KW_NOT` | not | નહીં | `nahii_n` | operator |
| `KW_AND` | and | અને | `anee` | operator |
| `KW_OR` | or | અથવા | `athavaa` | operator |

### Paradigm: memory

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | સ્વામિત્વ | `svaamitva` | ownership |
| `KW_BORROW` | borrow | ઋણ | `r_na` | ownership |
| `KW_MOVE` | move | સ્થાનાન્તર | `sthaanaantara` | ownership |
| `KW_MUT` | mut | પરિવર્ત્ય | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | આયુષ્કાલ | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | ક્ષેત્ર | `k_seetra` | allocation |
| `KW_GC` | gc | મલસંગ્રહ | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | સ્મૃતિકીલક | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | વર્ગ | `varga` | type_def |
| `KW_OBJECT` | object | વસ્તુ | `vastu` | type_def |
| `KW_INTERFACE` | interface | આંતરફલક | `aa_ntaraphalaka` | type_def |
| `KW_EXTENDS` | extends | વિસ્તરે | `vistaree` | inheritance |
| `KW_IMPLEMENTS` | implements | અમલ | `amala` | inheritance |
| `KW_NEW` | new | નવું | `navu_n` | instantiation |
| `KW_THIS` | this | આ | `aa` | reference |
| `KW_SUPER` | super | પરમ | `parama` | reference |
| `KW_PUBLIC` | public | જાહેર | `jaaheera` | access |
| `KW_PRIVATE` | private | ખાનગી | `khaanagii` | access |
| `KW_PROTECTED` | protected | સુરક્ષિત | `surak_sita` | access |
| `KW_STATIC` | static | સ્થિર | `sthira` | storage |
| `KW_ABSTRACT` | abstract | અમૂર્ત | `amuurta` | modifier |
| `KW_VIRTUAL` | virtual | આભાસી | `aabhaasii` | modifier |
| `KW_OVERRIDE` | override | ઉપરવટ | `uparavata` | modifier |

### Paradigm: procedural

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | વિધેય | `vidheeya` | subroutine |
| `KW_PROC` | procedure | પ્રક્રિયા | `prakriyaa` | subroutine |
| `KW_CALL` | call | બોલાવો | `baulaavau` | subroutine |
| `KW_PARAM` | param | પ્રાચલ | `praacala` | subroutine |
| `KW_YIELD` | yield | આપો | `aapau` | coroutine |
| `KW_AWAIT` | await | રાહજુઓ | `raahajuau` | async |
| `KW_ASYNC` | async | અસમકાલીન | `asamakaaliina` | async |

### Paradigm: robotics

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | ચાલક | `caalaka` | control |
| `KW_SERVO` | servo | અનુચાલક | `anucaalaka` | control |
| `KW_JOINT` | joint | સન્ધિ | `sandhi` | control |
| `KW_POSE` | pose | મુદ્રા | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | પ્રક્ષેપપથ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | પ્રતિપુષ્ટિ | `pratipu_sti` | control |
| `KW_PID` | pid | નિયન્ત્રક | `niyantraka` | control |
| `KW_DEADLINE` | deadline | કાલસીમા | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | આવર્તિક | `aavartika` | realtime |
| `KW_PRIORITY` | priority | પ્રાથમ્ય | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | પ્રવર્તય | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | પ્રત્યક્ષ | `pratyak_sa` | control |
| `KW_PLAN` | plan | યોજના | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | નિર્દેશક | `nirdeeshaka` | memory |
| `KW_REF` | ref | સંદર્ભ | `sa_ndarbha` | memory |
| `KW_ALLOC` | alloc | ફાળવો | `phaalavau` | memory |
| `KW_FREE` | free | મુક્ત | `mukta` | memory |
| `KW_SIZEOF` | sizeof | કદ | `kada` | memory |
| `KW_STRUCT` | struct | સંરચના | `sa_nracanaa` | type_def |
| `KW_UNION` | union | સંઘ | `sa_ngha` | type_def |
| `KW_ENUM` | enum | ગણના | `ga_nanaa` | type_def |
| `KW_TYPEDEF` | typedef | પ્રકારવ્યાખ્યા | `prakaaravyaakhyaa` | type_def |
| `KW_VOLATILE` | volatile | અસ્થિર | `asthira` | modifier |
| `KW_REGISTER` | register | નોંધણી | `nau_ndha_nii` | storage |
| `KW_EXTERN` | extern | બાહ્ય | `baahya` | linkage |
| `KW_INLINE` | inline | અંતઃરેખ | `a_nta_hreekha` | modifier |

### Paradigm: verification

| Construct | English | Gujarati | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | અપેક્ષતે | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | સુનિશ્ચયતિ | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | અપરિવર્ત્ય | `aparivartya` | contract |
| `KW_ASSERT` | assert | પ્રતિજ્ઞા | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | અધ્યવસ્યતિ | `adhyavasyati` | contract |
| `KW_PROVE` | prove | સાધયતિ | `saadhayati` | contract |
| `KW_REFINES` | refines | પરિષ્કરોતિ | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | પ્રતિમાનપરીક્ષા | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Gujarati native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Gujarati a first-class systems-programming language, not a localized skin.

## Example

```
જો (x > 0)        // romenagri: jau
    ...
નહીંતર              // romenagri: nahii_ntara
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Gujarati keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*