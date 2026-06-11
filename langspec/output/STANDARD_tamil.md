# Tamil Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Tamil
- **ISO 639 code**: tam
- **Script**: Tamil
- **Native speakers**: 80 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Tamil-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Tamil keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | ப்ர஦ிஶ | `pradisha` | ml |
| `KW_MATRIX` | matrix | ஆவ்யூஹ | `aavyuuha` | ml |
| `KW_VECTOR` | vector | ஸ஦ிஶ | `sadisha` | ml |
| `KW_GRAD` | gradient | ப்ரவணதா | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | ப்ரதிப்ரஸார | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | அ஗்ரப்ரஸார | `agraprasaara` | ml |
| `KW_LAYER` | layer | ஸ்தர | `stara` | ml |
| `KW_MODEL` | model | ப்ரதிமாந | `pratimaana` | ml |
| `KW_TRAIN` | train | ப்ரஶிக்ஷண | `prashik_sa_na` | ml |
| `KW_INFER` | infer | அநுமாந | `anumaana` | ml |
| `KW_LOSS` | loss | ஹாநி | `haani` | ml |
| `KW_OPTIMIZE` | optimize | அநுகூலந | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | ஸக்ரியண | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | ஭ார | `bhaara` | ml |
| `KW_BIAS` | bias | பக்ஷபாத | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | கல்ப | `kalpa` | ml |
| `KW_BATCH` | batch | புஞ்ஜ | `pu_nja` | ml |
| `KW_DATASET` | dataset | ஦த்தஸமூஹ | `dattasamuuha` | ml |
| `KW_EMBED` | embed | நிவேஶந | `niveeshana` | ml |
| `KW_ATTENTION` | attention | அவ஧ாந | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | இறக்குமதி | `irakkumati` | namespace |
| `KW_EXPORT` | export | ஏற்றுமதி | `eerrumati` | namespace |
| `KW_PACKAGE` | package | தொகுப்பு | `tokuppu` | namespace |
| `KW_NAMESPACE` | namespace | நாமாகாஶ | `naamaakaasha` | namespace |
| `KW_USE` | use | உபயோ஗ | `upayauga` | namespace |
| `KW_INCLUDE` | include | அந்தர்஭ாவ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | தஃ | `ta_h` | namespace |
| `KW_AS` | as | இவ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | இழை | `izai` | concurrency |
| `KW_SPAWN` | spawn | உருவாக்கு | `uruvaakku` | concurrency |
| `KW_LOCK` | lock | பூட்டு | `puuttu` | concurrency |
| `KW_SYNC` | synchronized | ஒத்திசை | `ottisai` | concurrency |
| `KW_CHANNEL` | channel | வழி | `vazi` | concurrency |
| `KW_SELECT` | select | தேர்ந்தெடு | `teerntedu` | concurrency |

### Paradigm: dataflow

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | ஧ாரா | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | ப்ரணால | `pra_naala` | reactive |
| `KW_MAP` | map | ப்ரதிசித்ர | `praticitra` | reactive |
| `KW_FILTER` | filter | ஛ால | `chaala` | reactive |
| `KW_REDUCE` | reduce | ந்யூநீக௃ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | ஸஂவேஷ்ட | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | நிரீக்ஷ | `niriik_sa` | reactive |
| `KW_EMIT` | emit | உத்ஸ௃ஜ | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | அ஭ிநிவேஶ | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | ஸ்பந்஦ஶோ஧ந | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | ஗்ரந்஥ி | `granthi` | cluster |
| `KW_REPLICA` | replica | ப்ரதிக௃தி | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | ஸர்வஸம்மதி | `sarvasammati` | cluster |
| `KW_SHARD` | shard | ஖ண்஡ | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | ஜநவா஦ | `janavaada` | cluster |
| `KW_LEADER` | leader | நாயக | `naayaka` | cluster |
| `KW_RPC` | rpc | ஦ூரப்ரக்ரியா | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | கர்த௃ | `kartr_` | cluster |
| `KW_MESSAGE` | message | ஸந்஦ேஶ | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | பெயரிலி | `peyarili` | function |
| `KW_MATCH` | match | பொருத்து | `poruttu` | pattern |
| `KW_WHEN` | when | போது | `pootu` | pattern |
| `KW_FUN` | fun | சார்பு | `saarpu` | function |
| `KW_REC` | rec | சுழல் | `suzala` | recursion |
| `KW_IN` | in | உள் | `ula` | binding |
| `KW_WHERE` | where | எங்கு | `e_nku` | binding |
| `KW_DATA` | data | தரவு | `taravu` | type_def |
| `KW_TYPE` | type | வகை | `vakai` | type_def |
| `KW_MODULE` | module | கூறு | `kuuru` | namespace |

### Paradigm: gpu

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | ஬ீஜ | `biija` | compute |
| `KW_DEVICE` | device | யந்த்ர | `yantra` | compute |
| `KW_HOST` | host | ஆதி஥ேய | `aatitheeya` | compute |
| `KW_GLOBAL` | global | வைஶ்விக | `vaishvika` | compute |
| `KW_SHARED` | shared | ஸஹ஭ாஜித | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | தந்த்வங்க | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | ஖ண்஡ாங்க | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | ஜால | `jaala` | compute |
| `KW_BARRIER` | barrier | அவரோ஧ | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | ஆணவிக | `aa_navika` | compute |
| `KW_WARP` | warp | தந்துஸமூஹ | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | பொருண்மை | `porunmai` | hardware |
| `KW_ARCH` | architecture | கட்டடக்கலை | `kattadakkalai` | hardware |
| `KW_SIGNAL` | signal | சமிக்ஞை | `samiknyai` | hardware |
| `KW_PORT` | port | துறை | `turai` | hardware |
| `KW_WIRE` | wire | கம்பி | `kampi` | hardware |
| `KW_REG` | reg | பதிவகம் | `pativakama` | hardware |
| `KW_MODULE_HW` | module | உறுப்பு | `uruppu` | hardware |
| `KW_ALWAYS` | always | எப்போதும் | `eppootuma` | hardware |
| `KW_ASSIGN` | assign | ஒதுக்கீடு | `otukkiidu` | hardware |
| `KW_BEGIN` | begin | தொடங்கு | `todanku` | block |
| `KW_END` | end | முடி | `mudi` | block |

### Paradigm: imperative

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | எனில் | `enila` | control_flow |
| `KW_ELSE` | else | இல்லையெனில் | `illaiyenila` | control_flow |
| `KW_ELIF` | elif | அல்லதெனில் | `allatenila` | control_flow |
| `KW_WHILE` | while | வரை | `varai` | control_flow |
| `KW_DO` | do | செய் | `sey` | control_flow |
| `KW_FOR` | for | க்கு | `kku` | control_flow |
| `KW_BREAK` | break | நிறுத்து | `niruttu` | control_flow |
| `KW_CONTINUE` | continue | தொடர் | `todara` | control_flow |
| `KW_SWITCH` | switch | தேர்வு | `teervu` | control_flow |
| `KW_CASE` | case | நிலை | `nilai` | control_flow |
| `KW_DEFAULT` | default | இயல்பு | `iyalpu` | control_flow |
| `KW_RETURN` | return | திரும்பு | `tirumpu` | control_flow |
| `KW_GOTO` | goto | செல் | `sela` | control_flow |
| `KW_VAR` | var | மாறி | `maari` | declaration |
| `KW_CONST` | const | மாறிலி | `maarili` | declaration |
| `KW_LET` | let | கொள் | `kola` | declaration |
| `KW_INT` | int | முழு | `muzu` | type |
| `KW_FLOAT` | float | தசம | `tasama` | type |
| `KW_DOUBLE` | double | இரட்டை | `irattai` | type |
| `KW_CHAR` | char | எழுத்து | `ezuttu` | type |
| `KW_BOOL` | bool | தருக்க | `tarukka` | type |
| `KW_STRING` | string | சரம் | `sarama` | type |
| `KW_VOID` | void | வெறுமை | `verumai` | type |
| `KW_TRUE` | true | உண்மை | `unmai` | literal |
| `KW_FALSE` | false | பொய் | `poy` | literal |
| `KW_NULL` | null | வெற்று | `verru` | literal |
| `KW_TRY` | try | முயல் | `muyala` | exception |
| `KW_CATCH` | catch | பிடி | `pidi` | exception |
| `KW_FINALLY` | finally | இறுதியாக | `irutiyaaka` | exception |
| `KW_THROW` | throw | எறி | `eri` | exception |
| `KW_RAISE` | raise | எழுப்பு | `ezuppu` | exception |
| `KW_EXCEPT` | except | விதிவிலக்கு | `vitivilakku` | exception |

### Paradigm: iot

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | கீலக | `kiilaka` | io |
| `KW_READ` | read | ப஠ | `patha` | io |
| `KW_WRITE` | write | லி஖ | `likha` | io |
| `KW_ANALOG` | analog | ஸ஦௃ஶ | `sadr_sha` | io |
| `KW_DIGITAL` | digital | அங்கீய | `a_nkiiya` | io |
| `KW_PWM` | pwm | ஸ்பந்஦விஸ்தார | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | வி஘்ந | `vighna` | io |
| `KW_TIMER` | timer | காலயந்த்ர | `kaalayantra` | io |
| `KW_SENSOR` | sensor | ஸஂவே஦க | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | ப்ரவர்தக | `pravartaka` | io |
| `KW_BUS` | bus | மார்஗ | `maarga` | io |
| `KW_PROTOCOL` | protocol | நியமாவலீ | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | ஸுஷுப்தி | `su_supti` | power |
| `KW_WAKE` | wake | ஜா஗௃ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | விதி | `viti` | clause |
| `KW_FACT` | fact | உண்மை | `unmai` | clause |
| `KW_QUERY` | query | வினா | `vinaa` | clause |
| `KW_NOT` | not | இல்லை | `illai` | operator |
| `KW_AND` | and | மற்றும் | `marruma` | operator |
| `KW_OR` | or | அல்லது | `allatu` | operator |

### Paradigm: memory

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | ஸ்வாமித்வ | `svaamitva` | ownership |
| `KW_BORROW` | borrow | ஋ண | `r_na` | ownership |
| `KW_MOVE` | move | ஸ்஥ாநாந்தர | `sthaanaantara` | ownership |
| `KW_MUT` | mut | பரிவர்த்ய | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | ஆயுஷ்கால | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | க்ஷேத்ர | `k_seetra` | allocation |
| `KW_GC` | gc | மலஸஂ஗்ரஹ | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | ஸ்ம௃திகீலக | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | வகுப்பு | `vakuppu` | type_def |
| `KW_OBJECT` | object | பொருள் | `porula` | type_def |
| `KW_INTERFACE` | interface | இடைமுகம் | `idaimukama` | type_def |
| `KW_EXTENDS` | extends | நீட்டிக்கும் | `niittikkuma` | inheritance |
| `KW_IMPLEMENTS` | implements | செயல்படுத்து | `seyalpaduttu` | inheritance |
| `KW_NEW` | new | புதிய | `putiya` | instantiation |
| `KW_THIS` | this | இது | `itu` | reference |
| `KW_SUPER` | super | மேல் | `meela` | reference |
| `KW_PUBLIC` | public | பொது | `potu` | access |
| `KW_PRIVATE` | private | தனிப்பட்ட | `tanippatta` | access |
| `KW_PROTECTED` | protected | பாதுகாக்கப்பட்ட | `paatukaakkappatta` | access |
| `KW_STATIC` | static | நிலையான | `nilaiyaana` | storage |
| `KW_ABSTRACT` | abstract | சுருக்க | `surukka` | modifier |
| `KW_VIRTUAL` | virtual | மெய்நிகர் | `meynikara` | modifier |
| `KW_OVERRIDE` | override | மேலெழுது | `meelezutu` | modifier |

### Paradigm: procedural

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | செயல் | `seyala` | subroutine |
| `KW_PROC` | procedure | நடைமுறை | `nadaimurai` | subroutine |
| `KW_CALL` | call | அழை | `azai` | subroutine |
| `KW_PARAM` | param | அளபுரு | `alapuru` | subroutine |
| `KW_YIELD` | yield | தா | `taa` | coroutine |
| `KW_AWAIT` | await | காத்திரு | `kaattiru` | async |
| `KW_ASYNC` | async | ஒத்திசையா | `ottisaiyaa` | async |

### Paradigm: robotics

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | சாலக | `caalaka` | control |
| `KW_SERVO` | servo | அநுசாலக | `anucaalaka` | control |
| `KW_JOINT` | joint | ஸந்஧ி | `sandhi` | control |
| `KW_POSE` | pose | மு஦்ரா | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | ப்ரக்ஷேபப஥ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | ப்ரதிபுஷ்டி | `pratipu_sti` | control |
| `KW_PID` | pid | நியந்த்ரக | `niyantraka` | control |
| `KW_DEADLINE` | deadline | காலஸீமா | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | ஆவர்திக | `aavartika` | realtime |
| `KW_PRIORITY` | priority | ப்ரா஥ம்ய | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | ப்ரவர்தய | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | ப்ரத்யக்ஷ | `pratyak_sa` | control |
| `KW_PLAN` | plan | யோஜநா | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | சுட்டி | `sutti` | memory |
| `KW_REF` | ref | குறிப்பு | `kurippu` | memory |
| `KW_ALLOC` | alloc | ஒதுக்கு | `otukku` | memory |
| `KW_FREE` | free | விடுவி | `viduvi` | memory |
| `KW_SIZEOF` | sizeof | அளவு | `alavu` | memory |
| `KW_STRUCT` | struct | கட்டமைப்பு | `kattamaippu` | type_def |
| `KW_UNION` | union | ஒன்றிப்பு | `onrippu` | type_def |
| `KW_ENUM` | enum | எண்ணிக்கை | `ennikkai` | type_def |
| `KW_TYPEDEF` | typedef | வகைவரை | `vakaivarai` | type_def |
| `KW_VOLATILE` | volatile | நிலையற்ற | `nilaiyarra` | modifier |
| `KW_REGISTER` | register | பதிவு | `pativu` | storage |
| `KW_EXTERN` | extern | வெளி | `veli` | linkage |
| `KW_INLINE` | inline | உள்வரி | `ulvari` | modifier |

### Paradigm: verification

| Construct | English | Tamil | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | அபேக்ஷதே | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | ஸுநிஶ்சயதி | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | அபரிவர்த்ய | `aparivartya` | contract |
| `KW_ASSERT` | assert | ப்ரதிஜ்ஞா | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | அ஧்யவஸ்யதி | `adhyavasyati` | contract |
| `KW_PROVE` | prove | ஸா஧யதி | `saadhayati` | contract |
| `KW_REFINES` | refines | பரிஷ்கரோதி | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | ப்ரதிமாநபரீக்ஷா | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Tamil native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Tamil a first-class systems-programming language, not a localized skin.

## Example

```
எனில் (x > 0)        // romenagri: enila
    ...
இல்லையெனில்              // romenagri: illaiyenila
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Tamil keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*