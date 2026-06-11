# Punjabi Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Punjabi
- **ISO 639 code**: pan
- **Script**: Gurmukhi
- **Native speakers**: 125 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Punjabi-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Punjabi keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | ਪ੍ਰਦਿਸ਼ | `pradisha` | ml |
| `KW_MATRIX` | matrix | ਆਵ੍ਯੂਹ | `aavyuuha` | ml |
| `KW_VECTOR` | vector | ਸਦਿਸ਼ | `sadisha` | ml |
| `KW_GRAD` | gradient | ਪ੍ਰਵਣਤਾ | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | ਪ੍ਰਤਿਪ੍ਰਸਾਰ | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | ਅਗ੍ਰਪ੍ਰਸਾਰ | `agraprasaara` | ml |
| `KW_LAYER` | layer | ਸ੍ਤਰ | `stara` | ml |
| `KW_MODEL` | model | ਪ੍ਰਤਿਮਾਨ | `pratimaana` | ml |
| `KW_TRAIN` | train | ਪ੍ਰਸ਼ਿਕ੍਷ਣ | `prashik_sa_na` | ml |
| `KW_INFER` | infer | ਅਨੁਮਾਨ | `anumaana` | ml |
| `KW_LOSS` | loss | ਹਾਨਿ | `haani` | ml |
| `KW_OPTIMIZE` | optimize | ਅਨੁਕੂਲਨ | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | ਸਕ੍ਰਿਯਣ | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | ਭਾਰ | `bhaara` | ml |
| `KW_BIAS` | bias | ਪਕ੍਷ਪਾਤ | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | ਕਲ੍ਪ | `kalpa` | ml |
| `KW_BATCH` | batch | ਪੁਞ੍ਜ | `pu_nja` | ml |
| `KW_DATASET` | dataset | ਦਤ੍ਤਸਮੂਹ | `dattasamuuha` | ml |
| `KW_EMBED` | embed | ਨਿਵੇਸ਼ਨ | `niveeshana` | ml |
| `KW_ATTENTION` | attention | ਅਵਧਾਨ | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | ਆਯਾਤ | `aayaata` | namespace |
| `KW_EXPORT` | export | ਨਿਰਯਾਤ | `niryaata` | namespace |
| `KW_PACKAGE` | package | ਪੈਕੇਜ | `paikeeja` | namespace |
| `KW_NAMESPACE` | namespace | ਨਾਮਾਕਾਸ਼ | `naamaakaasha` | namespace |
| `KW_USE` | use | ਉਪਯੋਗ | `upayauga` | namespace |
| `KW_INCLUDE` | include | ਅਨ੍ਤਰ੍ਭਾਵ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | ਤਃ | `ta_h` | namespace |
| `KW_AS` | as | ਇਵ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | ਧਾਗਾ | `dhaagaa` | concurrency |
| `KW_SPAWN` | spawn | ਪੈਦਾ | `paidaa` | concurrency |
| `KW_LOCK` | lock | ਜਿੰਦਰਾ | `ji_ndaraa` | concurrency |
| `KW_SYNC` | synchronized | ਸਮਕਾਲੀ | `samakaalii` | concurrency |
| `KW_CHANNEL` | channel | ਮਾਧਿਅਮ | `maadhiama` | concurrency |
| `KW_SELECT` | select | ਚੁਣੋ | `cu_nau` | concurrency |

### Paradigm: dataflow

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | ਧਾਰਾ | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | ਪ੍ਰਣਾਲ | `pra_naala` | reactive |
| `KW_MAP` | map | ਪ੍ਰਤਿਚਿਤ੍ਰ | `praticitra` | reactive |
| `KW_FILTER` | filter | ਛਾਲ | `chaala` | reactive |
| `KW_REDUCE` | reduce | ਨ੍ਯੂਨੀਕ੃ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | ਸਂਵੇ਷੍ਟ | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | ਨਿਰੀਕ੍਷ | `niriik_sa` | reactive |
| `KW_EMIT` | emit | ਉਤ੍ਸ੃ਜ | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | ਅਭਿਨਿਵੇਸ਼ | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | ਸ੍ਪਨ੍ਦਸ਼ੋਧਨ | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | ਗ੍ਰਨ੍ਥਿ | `granthi` | cluster |
| `KW_REPLICA` | replica | ਪ੍ਰਤਿਕ੃ਤਿ | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | ਸਰ੍ਵਸਮ੍ਮਤਿ | `sarvasammati` | cluster |
| `KW_SHARD` | shard | ਖਣ੍ਡ | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | ਜਨਵਾਦ | `janavaada` | cluster |
| `KW_LEADER` | leader | ਨਾਯਕ | `naayaka` | cluster |
| `KW_RPC` | rpc | ਦੂਰਪ੍ਰਕ੍ਰਿਯਾ | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | ਕਰ੍ਤ੃ | `kartr_` | cluster |
| `KW_MESSAGE` | message | ਸਨ੍ਦੇਸ਼ | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | ਅਨਾਮ | `anaama` | function |
| `KW_MATCH` | match | ਮੇਲ | `meela` | pattern |
| `KW_WHEN` | when | ਜਦੋਂ | `jadau_n` | pattern |
| `KW_FUN` | fun | ਫਲਨ | `phalana` | function |
| `KW_REC` | rec | ਆਵਰਤੀ | `aavartii` | recursion |
| `KW_IN` | in | ਵਿੱਚ | `vicca` | binding |
| `KW_WHERE` | where | ਕਿੱਥੇ | `kitthee` | binding |
| `KW_DATA` | data | ਡਾਟਾ | `daataa` | type_def |
| `KW_TYPE` | type | ਕਿਸਮ | `kisama` | type_def |
| `KW_MODULE` | module | ਮਾਡਿਊਲ | `maadiuula` | namespace |

### Paradigm: gpu

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | ਬੀਜ | `biija` | compute |
| `KW_DEVICE` | device | ਯਨ੍ਤ੍ਰ | `yantra` | compute |
| `KW_HOST` | host | ਆਤਿਥੇਯ | `aatitheeya` | compute |
| `KW_GLOBAL` | global | ਵੈਸ਼੍ਵਿਕ | `vaishvika` | compute |
| `KW_SHARED` | shared | ਸਹਭਾਜਿਤ | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | ਤਨ੍ਤ੍ਵਙ੍ਕ | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | ਖਣ੍ਡਾਙ੍ਕ | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | ਜਾਲ | `jaala` | compute |
| `KW_BARRIER` | barrier | ਅਵਰੋਧ | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | ਆਣਵਿਕ | `aa_navika` | compute |
| `KW_WARP` | warp | ਤਨ੍ਤੁਸਮੂਹ | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | ਇਕਾਈ | `ikaaii` | hardware |
| `KW_ARCH` | architecture | ਬਣਤਰਕਲਾ | `ba_natarakalaa` | hardware |
| `KW_SIGNAL` | signal | ਸੰਕੇਤ | `sa_nkeeta` | hardware |
| `KW_PORT` | port | ਬੰਦਰਗਾਹ | `ba_ndaragaaha` | hardware |
| `KW_WIRE` | wire | ਤਾਰ | `taara` | hardware |
| `KW_REG` | reg | ਰਜਿਸਟਰ | `rajisatara` | hardware |
| `KW_MODULE_HW` | module | ਪੁਰਜ਼ਾ | `puraza` | hardware |
| `KW_ALWAYS` | always | ਹਮੇਸ਼ਾ | `hameeshaa` | hardware |
| `KW_ASSIGN` | assign | ਨਿਯੁਕਤ | `niyukata` | hardware |
| `KW_BEGIN` | begin | ਆਰੰਭ | `aara_nbha` | block |
| `KW_END` | end | ਅੰਤ | `a_nta` | block |

### Paradigm: imperative

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | ਜੇ | `jee` | control_flow |
| `KW_ELSE` | else | ਨਹੀਂਤਾਂ | `nahii_ntaa_n` | control_flow |
| `KW_ELIF` | elif | ਜਾਂਜੇ | `jaa_njee` | control_flow |
| `KW_WHILE` | while | ਜਦਤੱਕ | `jadatakka` | control_flow |
| `KW_DO` | do | ਕਰੋ | `karau` | control_flow |
| `KW_FOR` | for | ਲਈ | `laii` | control_flow |
| `KW_BREAK` | break | ਰੋਕੋ | `raukau` | control_flow |
| `KW_CONTINUE` | continue | ਜਾਰੀ | `jaarii` | control_flow |
| `KW_SWITCH` | switch | ਚੋਣ | `cau_na` | control_flow |
| `KW_CASE` | case | ਹਾਲਤ | `haalata` | control_flow |
| `KW_DEFAULT` | default | ਮੂਲ | `muula` | control_flow |
| `KW_RETURN` | return | ਵਾਪਸ | `vaapasa` | control_flow |
| `KW_GOTO` | goto | ਜਾਓ | `jaaau` | control_flow |
| `KW_VAR` | var | ਚਲ | `cala` | declaration |
| `KW_CONST` | const | ਅਚਲ | `acala` | declaration |
| `KW_LET` | let | ਮੰਨੋ | `ma_nnau` | declaration |
| `KW_INT` | int | ਪੂਰਨਅੰਕ | `puurana_nka` | type |
| `KW_FLOAT` | float | ਦਸ਼ਮਲਵ | `dashamalava` | type |
| `KW_DOUBLE` | double | ਦੁੱਗਣਾ | `duggsa_naa` | type |
| `KW_CHAR` | char | ਅੱਖਰ | `akkhara` | type |
| `KW_BOOL` | bool | ਤਾਰਕਿਕ | `taarkika` | type |
| `KW_STRING` | string | ਸ਼ਬਦਮਾਲਾ | `shabadamaalaa` | type |
| `KW_VOID` | void | ਖਾਲੀ | `khaalii` | type |
| `KW_TRUE` | true | ਸੱਚ | `sacca` | literal |
| `KW_FALSE` | false | ਝੂਠ | `jhuutha` | literal |
| `KW_NULL` | null | ਨਿਰਾ | `niraa` | literal |
| `KW_TRY` | try | ਕੋਸ਼ਿਸ਼ | `kaushisha` | exception |
| `KW_CATCH` | catch | ਫੜੋ | `pha_dau` | exception |
| `KW_FINALLY` | finally | ਅਖੀਰ | `akhiira` | exception |
| `KW_THROW` | throw | ਸੁੱਟੋ | `suttau` | exception |
| `KW_RAISE` | raise | ਉਠਾਓ | `uthaaau` | exception |
| `KW_EXCEPT` | except | ਅਪਵਾਦ | `apavaada` | exception |

### Paradigm: iot

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | ਕੀਲਕ | `kiilaka` | io |
| `KW_READ` | read | ਪਠ | `patha` | io |
| `KW_WRITE` | write | ਲਿਖ | `likha` | io |
| `KW_ANALOG` | analog | ਸਦ੃ਸ਼ | `sadr_sha` | io |
| `KW_DIGITAL` | digital | ਅਙ੍ਕੀਯ | `a_nkiiya` | io |
| `KW_PWM` | pwm | ਸ੍ਪਨ੍ਦਵਿਸ੍ਤਾਰ | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | ਵਿਘ੍ਨ | `vighna` | io |
| `KW_TIMER` | timer | ਕਾਲਯਨ੍ਤ੍ਰ | `kaalayantra` | io |
| `KW_SENSOR` | sensor | ਸਂਵੇਦਕ | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | ਪ੍ਰਵਰ੍ਤਕ | `pravartaka` | io |
| `KW_BUS` | bus | ਮਾਰ੍ਗ | `maarga` | io |
| `KW_PROTOCOL` | protocol | ਨਿਯਮਾਵਲੀ | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | ਸੁ਷ੁਪ੍ਤਿ | `su_supti` | power |
| `KW_WAKE` | wake | ਜਾਗ੃ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | ਨਿਯਮ | `niyama` | clause |
| `KW_FACT` | fact | ਤੱਥ | `tattha` | clause |
| `KW_QUERY` | query | ਸਵਾਲ | `savaala` | clause |
| `KW_NOT` | not | ਨਹੀਂ | `nahii_n` | operator |
| `KW_AND` | and | ਅਤੇ | `atee` | operator |
| `KW_OR` | or | ਜਾਂ | `jaa_n` | operator |

### Paradigm: memory

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | ਸ੍ਵਾਮਿਤ੍ਵ | `svaamitva` | ownership |
| `KW_BORROW` | borrow | ਋ਣ | `r_na` | ownership |
| `KW_MOVE` | move | ਸ੍ਥਾਨਾਨ੍ਤਰ | `sthaanaantara` | ownership |
| `KW_MUT` | mut | ਪਰਿਵਰ੍ਤ੍ਯ | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | ਆਯੁ਷੍ਕਾਲ | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | ਕ੍਷ੇਤ੍ਰ | `k_seetra` | allocation |
| `KW_GC` | gc | ਮਲਸਂਗ੍ਰਹ | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | ਸ੍ਮ੃ਤਿਕੀਲਕ | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | ਵਰਗ | `varga` | type_def |
| `KW_OBJECT` | object | ਵਸਤੂ | `vastuu` | type_def |
| `KW_INTERFACE` | interface | ਅੰਤਰਮੁਖ | `a_ntaramukha` | type_def |
| `KW_EXTENDS` | extends | ਵਧਾਓ | `vadhaaau` | inheritance |
| `KW_IMPLEMENTS` | implements | ਲਾਗੂ | `laaguu` | inheritance |
| `KW_NEW` | new | ਨਵਾਂ | `navaa_n` | instantiation |
| `KW_THIS` | this | ਇਹ | `iha` | reference |
| `KW_SUPER` | super | ਪਰਮ | `parama` | reference |
| `KW_PUBLIC` | public | ਜਨਤਕ | `janataka` | access |
| `KW_PRIVATE` | private | ਨਿਜੀ | `nijii` | access |
| `KW_PROTECTED` | protected | ਸੁਰੱਖਿਅਤ | `surakkhiata` | access |
| `KW_STATIC` | static | ਸਥਿਰ | `sathira` | storage |
| `KW_ABSTRACT` | abstract | ਅਮੂਰਤ | `amuurata` | modifier |
| `KW_VIRTUAL` | virtual | ਆਭਾਸੀ | `aabhaasii` | modifier |
| `KW_OVERRIDE` | override | ਉਪਰਲਿਖ | `uparalikha` | modifier |

### Paradigm: procedural

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | ਕਾਰਜ | `kaaraja` | subroutine |
| `KW_PROC` | procedure | ਵਿਧੀ | `vidhii` | subroutine |
| `KW_CALL` | call | ਬੁਲਾਓ | `bulaaau` | subroutine |
| `KW_PARAM` | param | ਪ੍ਰਾਚਲ | `praacala` | subroutine |
| `KW_YIELD` | yield | ਦਿਓ | `diau` | coroutine |
| `KW_AWAIT` | await | ਉਡੀਕ | `udiika` | async |
| `KW_ASYNC` | async | ਅਸਮਕਾਲੀ | `asamakaalii` | async |

### Paradigm: robotics

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | ਚਾਲਕ | `caalaka` | control |
| `KW_SERVO` | servo | ਅਨੁਚਾਲਕ | `anucaalaka` | control |
| `KW_JOINT` | joint | ਸਨ੍ਧਿ | `sandhi` | control |
| `KW_POSE` | pose | ਮੁਦ੍ਰਾ | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | ਪ੍ਰਕ੍਷ੇਪਪਥ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | ਪ੍ਰਤਿਪੁ਷੍ਟਿ | `pratipu_sti` | control |
| `KW_PID` | pid | ਨਿਯਨ੍ਤ੍ਰਕ | `niyantraka` | control |
| `KW_DEADLINE` | deadline | ਕਾਲਸੀਮਾ | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | ਆਵਰ੍ਤਿਕ | `aavartika` | realtime |
| `KW_PRIORITY` | priority | ਪ੍ਰਾਥਮ੍ਯ | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | ਪ੍ਰਵਰ੍ਤਯ | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | ਪ੍ਰਤ੍ਯਕ੍਷ | `pratyak_sa` | control |
| `KW_PLAN` | plan | ਯੋਜਨਾ | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | ਸੰਕੇਤਕ | `sa_nkeetaka` | memory |
| `KW_REF` | ref | ਹਵਾਲਾ | `havaalaa` | memory |
| `KW_ALLOC` | alloc | ਵੰਡ | `va_nda` | memory |
| `KW_FREE` | free | ਮੁਕਤ | `mukata` | memory |
| `KW_SIZEOF` | sizeof | ਆਕਾਰ | `aakaara` | memory |
| `KW_STRUCT` | struct | ਬਣਤਰ | `ba_natara` | type_def |
| `KW_UNION` | union | ਸੰਘ | `sa_ngha` | type_def |
| `KW_ENUM` | enum | ਗਿਣਤੀ | `gi_natii` | type_def |
| `KW_TYPEDEF` | typedef | ਕਿਸਮਪਰਿਭਾਸ਼ਾ | `kisamaparibhaashaa` | type_def |
| `KW_VOLATILE` | volatile | ਅਸਥਿਰ | `asathira` | modifier |
| `KW_REGISTER` | register | ਰਜਿਸਟਰ | `rajisatara` | storage |
| `KW_EXTERN` | extern | ਬਾਹਰੀ | `baaharii` | linkage |
| `KW_INLINE` | inline | ਸਤਰਅੰਦਰ | `sataranda_n` | modifier |

### Paradigm: verification

| Construct | English | Punjabi | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | ਅਪੇਕ੍਷ਤੇ | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | ਸੁਨਿਸ਼੍ਚਯਤਿ | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | ਅਪਰਿਵਰ੍ਤ੍ਯ | `aparivartya` | contract |
| `KW_ASSERT` | assert | ਪ੍ਰਤਿਜ੍ਞਾ | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | ਅਧ੍ਯਵਸ੍ਯਤਿ | `adhyavasyati` | contract |
| `KW_PROVE` | prove | ਸਾਧਯਤਿ | `saadhayati` | contract |
| `KW_REFINES` | refines | ਪਰਿ਷੍ਕਰੋਤਿ | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | ਪ੍ਰਤਿਮਾਨਪਰੀਕ੍਷ਾ | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Punjabi native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Punjabi a first-class systems-programming language, not a localized skin.

## Example

```
ਜੇ (x > 0)        // romenagri: jee
    ...
ਨਹੀਂਤਾਂ              // romenagri: nahii_ntaa_n
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Punjabi keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*