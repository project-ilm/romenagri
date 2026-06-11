# Odia Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Odia
- **ISO 639 code**: ori
- **Script**: Odia
- **Native speakers**: 38 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Odia-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Odia keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | ପ୍ରଦିଶ | `pradisha` | ml |
| `KW_MATRIX` | matrix | ଆଵ୍ଯୂହ | `aavyuuha` | ml |
| `KW_VECTOR` | vector | ସଦିଶ | `sadisha` | ml |
| `KW_GRAD` | gradient | ପ୍ରଵଣତା | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | ପ୍ରତିପ୍ରସାର | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | ଅଗ୍ରପ୍ରସାର | `agraprasaara` | ml |
| `KW_LAYER` | layer | ସ୍ତର | `stara` | ml |
| `KW_MODEL` | model | ପ୍ରତିମାନ | `pratimaana` | ml |
| `KW_TRAIN` | train | ପ୍ରଶିକ୍ଷଣ | `prashik_sa_na` | ml |
| `KW_INFER` | infer | ଅନୁମାନ | `anumaana` | ml |
| `KW_LOSS` | loss | ହାନି | `haani` | ml |
| `KW_OPTIMIZE` | optimize | ଅନୁକୂଲନ | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | ସକ୍ରିଯଣ | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | ଭାର | `bhaara` | ml |
| `KW_BIAS` | bias | ପକ୍ଷପାତ | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | କଲ୍ପ | `kalpa` | ml |
| `KW_BATCH` | batch | ପୁଞ୍ଜ | `pu_nja` | ml |
| `KW_DATASET` | dataset | ଦତ୍ତସମୂହ | `dattasamuuha` | ml |
| `KW_EMBED` | embed | ନିଵେଶନ | `niveeshana` | ml |
| `KW_ATTENTION` | attention | ଅଵଧାନ | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | ଆମଦାନୀ | `aamadaanii` | namespace |
| `KW_EXPORT` | export | ରପ୍ତାନୀ | `raptaanii` | namespace |
| `KW_PACKAGE` | package | ପ୍ୟାକେଜ | `pyaakeeja` | namespace |
| `KW_NAMESPACE` | namespace | ନାମାକାଶ | `naamaakaasha` | namespace |
| `KW_USE` | use | ଉପଯୋଗ | `upayauga` | namespace |
| `KW_INCLUDE` | include | ଅନ୍ତର୍ଭାଵ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | ତଃ | `ta_h` | namespace |
| `KW_AS` | as | ଇଵ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | ସୂତା | `suutaa` | concurrency |
| `KW_SPAWN` | spawn | ସୃଷ୍ଟି | `sr_sti` | concurrency |
| `KW_LOCK` | lock | ତାଲା | `taalaa` | concurrency |
| `KW_SYNC` | synchronized | ସମକାଳ | `samakaala` | concurrency |
| `KW_CHANNEL` | channel | ମାଧ୍ୟମ | `maadhyama` | concurrency |
| `KW_SELECT` | select | ବାଛ | `baacha` | concurrency |

### Paradigm: dataflow

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | ଧାରା | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | ପ୍ରଣାଲ | `pra_naala` | reactive |
| `KW_MAP` | map | ପ୍ରତିଚିତ୍ର | `praticitra` | reactive |
| `KW_FILTER` | filter | ଛାଲ | `chaala` | reactive |
| `KW_REDUCE` | reduce | ନ୍ଯୂନୀକୃ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | ସଂଵେଷ୍ଟ | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | ନିରୀକ୍ଷ | `niriik_sa` | reactive |
| `KW_EMIT` | emit | ଉତ୍ସୃଜ | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | ଅଭିନିଵେଶ | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | ସ୍ପନ୍ଦଶୋଧନ | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | ଗ୍ରନ୍ଥି | `granthi` | cluster |
| `KW_REPLICA` | replica | ପ୍ରତିକୃତି | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | ସର୍ଵସମ୍ମତି | `sarvasammati` | cluster |
| `KW_SHARD` | shard | ଖଣ୍ଡ | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | ଜନଵାଦ | `janavaada` | cluster |
| `KW_LEADER` | leader | ନାଯକ | `naayaka` | cluster |
| `KW_RPC` | rpc | ଦୂରପ୍ରକ୍ରିଯା | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | କର୍ତୃ | `kartr_` | cluster |
| `KW_MESSAGE` | message | ସନ୍ଦେଶ | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | ଅନାମ | `anaama` | function |
| `KW_MATCH` | match | ମିଳାଅ | `milaaa` | pattern |
| `KW_WHEN` | when | ଯେତେବେଳେ | `yeeteebeelee` | pattern |
| `KW_FUN` | fun | ଫଳନ | `phala_na` | function |
| `KW_REC` | rec | ପୁନରାବର୍ତୀ | `punaraabartii` | recursion |
| `KW_IN` | in | ଭିତରେ | `bhitaree` | binding |
| `KW_WHERE` | where | କେଉଁଠି | `keeu_nthi` | binding |
| `KW_DATA` | data | ତଥ୍ୟ | `tathya` | type_def |
| `KW_TYPE` | type | ପ୍ରକାର | `prakaara` | type_def |
| `KW_MODULE` | module | ଅଂଶ | `a_nsha` | namespace |

### Paradigm: gpu

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | ବୀଜ | `biija` | compute |
| `KW_DEVICE` | device | ଯନ୍ତ୍ର | `yantra` | compute |
| `KW_HOST` | host | ଆତିଥେଯ | `aatitheeya` | compute |
| `KW_GLOBAL` | global | ଵୈଶ୍ଵିକ | `vaishvika` | compute |
| `KW_SHARED` | shared | ସହଭାଜିତ | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | ତନ୍ତ୍ଵଙ୍କ | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | ଖଣ୍ଡାଙ୍କ | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | ଜାଲ | `jaala` | compute |
| `KW_BARRIER` | barrier | ଅଵରୋଧ | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | ଆଣଵିକ | `aa_navika` | compute |
| `KW_WARP` | warp | ତନ୍ତୁସମୂହ | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | ସତ୍ତା | `sattaa` | hardware |
| `KW_ARCH` | architecture | ସ୍ଥାପତ୍ୟ | `sthaapatya` | hardware |
| `KW_SIGNAL` | signal | ସଙ୍କେତ | `sa_nkeeta` | hardware |
| `KW_PORT` | port | ବନ୍ଦର | `bandara` | hardware |
| `KW_WIRE` | wire | ତାର | `taara` | hardware |
| `KW_REG` | reg | ପଞ୍ଜିକା | `pa_njikaa` | hardware |
| `KW_MODULE_HW` | module | ଭାଗ | `bhaaga` | hardware |
| `KW_ALWAYS` | always | ସର୍ବଦା | `sarbadaa` | hardware |
| `KW_ASSIGN` | assign | ନିଯୁକ୍ତ | `niyukta` | hardware |
| `KW_BEGIN` | begin | ଆରମ୍ଭ | `aarambha` | block |
| `KW_END` | end | ଶେଷ | `sheesa` | block |

### Paradigm: imperative

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | ଯଦି | `yadi` | control_flow |
| `KW_ELSE` | else | ଅନ୍ୟଥା | `anyathaa` | control_flow |
| `KW_ELIF` | elif | ନଚେତଯଦି | `naceetayadi` | control_flow |
| `KW_WHILE` | while | ଯେପର୍ଯ୍ୟନ୍ତ | `yeeparyyanta` | control_flow |
| `KW_DO` | do | କର | `kara` | control_flow |
| `KW_FOR` | for | ପାଇଁ | `paaii_n` | control_flow |
| `KW_BREAK` | break | ଭାଙ୍ଗ | `bhaa_nga` | control_flow |
| `KW_CONTINUE` | continue | ଜାରି | `jaari` | control_flow |
| `KW_SWITCH` | switch | ବାଛ | `baacha` | control_flow |
| `KW_CASE` | case | ସ୍ଥିତି | `sthiti` | control_flow |
| `KW_DEFAULT` | default | ପୂର୍ବନିର୍ଦ୍ଧାରିତ | `puurbanirddhaarita` | control_flow |
| `KW_RETURN` | return | ଫେରାଅ | `pheeraaa` | control_flow |
| `KW_GOTO` | goto | ଯାଅ | `yaaa` | control_flow |
| `KW_VAR` | var | ଚଳ | `cala` | declaration |
| `KW_CONST` | const | ଅଚଳ | `acala` | declaration |
| `KW_LET` | let | ଧର | `dhara` | declaration |
| `KW_INT` | int | ପୂର୍ଣ୍ଣସଂଖ୍ୟା | `puur_n_nasa_mkhyaa` | type |
| `KW_FLOAT` | float | ଦଶମିକ | `dashamika` | type |
| `KW_DOUBLE` | double | ଦ୍ୱିଗୁଣ | `dvigu_na` | type |
| `KW_CHAR` | char | ଅକ୍ଷର | `ak_sara` | type |
| `KW_BOOL` | bool | ତାର୍କିକ | `taarkika` | type |
| `KW_STRING` | string | ବାକ୍ୟ | `baakya` | type |
| `KW_VOID` | void | ଶୂନ୍ୟ | `shuunya` | type |
| `KW_TRUE` | true | ସତ୍ୟ | `satya` | literal |
| `KW_FALSE` | false | ମିଥ୍ୟା | `mithyaa` | literal |
| `KW_NULL` | null | ଖାଲି | `khaali` | literal |
| `KW_TRY` | try | ଚେଷ୍ଟା | `cee_staa` | exception |
| `KW_CATCH` | catch | ଧର | `dhara` | exception |
| `KW_FINALLY` | finally | ଶେଷରେ | `sheesaree` | exception |
| `KW_THROW` | throw | ଫିଙ୍ଗ | `phi_nga` | exception |
| `KW_RAISE` | raise | ଉଠାଅ | `uthaaa` | exception |
| `KW_EXCEPT` | except | ବ୍ୟତିକ୍ରମ | `byatikrama` | exception |

### Paradigm: iot

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | କୀଲକ | `kiilaka` | io |
| `KW_READ` | read | ପଠ | `patha` | io |
| `KW_WRITE` | write | ଲିଖ | `likha` | io |
| `KW_ANALOG` | analog | ସଦୃଶ | `sadr_sha` | io |
| `KW_DIGITAL` | digital | ଅଙ୍କୀଯ | `a_nkiiya` | io |
| `KW_PWM` | pwm | ସ୍ପନ୍ଦଵିସ୍ତାର | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | ଵିଘ୍ନ | `vighna` | io |
| `KW_TIMER` | timer | କାଲଯନ୍ତ୍ର | `kaalayantra` | io |
| `KW_SENSOR` | sensor | ସଂଵେଦକ | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | ପ୍ରଵର୍ତକ | `pravartaka` | io |
| `KW_BUS` | bus | ମାର୍ଗ | `maarga` | io |
| `KW_PROTOCOL` | protocol | ନିଯମାଵଲୀ | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | ସୁଷୁପ୍ତି | `su_supti` | power |
| `KW_WAKE` | wake | ଜାଗୃ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | ନିୟମ | `niyama` | clause |
| `KW_FACT` | fact | ବାସ୍ତବ | `baastaba` | clause |
| `KW_QUERY` | query | ପ୍ରଶ୍ନ | `prashna` | clause |
| `KW_NOT` | not | ନୁହେଁ | `nuhee_n` | operator |
| `KW_AND` | and | ଏବଂ | `eeba_n` | operator |
| `KW_OR` | or | କିମ୍ବା | `kimbaa` | operator |

### Paradigm: memory

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | ସ୍ଵାମିତ୍ଵ | `svaamitva` | ownership |
| `KW_BORROW` | borrow | ଋଣ | `r_na` | ownership |
| `KW_MOVE` | move | ସ୍ଥାନାନ୍ତର | `sthaanaantara` | ownership |
| `KW_MUT` | mut | ପରିଵର୍ତ୍ଯ | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | ଆଯୁଷ୍କାଲ | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | କ୍ଷେତ୍ର | `k_seetra` | allocation |
| `KW_GC` | gc | ମଲସଂଗ୍ରହ | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | ସ୍ମୃତିକୀଲକ | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | ଶ୍ରେଣୀ | `shree_nii` | type_def |
| `KW_OBJECT` | object | ବସ୍ତୁ | `bastu` | type_def |
| `KW_INTERFACE` | interface | ଅନ୍ତରମୁଖ | `antaramukha` | type_def |
| `KW_EXTENDS` | extends | ବିସ୍ତାର | `bistaara` | inheritance |
| `KW_IMPLEMENTS` | implements | କାର୍ଯ୍ୟକାରୀ | `kaaryyakaarii` | inheritance |
| `KW_NEW` | new | ନୂତନ | `nuutana` | instantiation |
| `KW_THIS` | this | ଏହି | `eehi` | reference |
| `KW_SUPER` | super | ପରମ | `parama` | reference |
| `KW_PUBLIC` | public | ସର୍ବସାଧାରଣ | `sarbasaadhaara_na` | access |
| `KW_PRIVATE` | private | ବ୍ୟକ୍ତିଗତ | `byaktigata` | access |
| `KW_PROTECTED` | protected | ସୁରକ୍ଷିତ | `surak_sita` | access |
| `KW_STATIC` | static | ସ୍ଥିର | `sthira` | storage |
| `KW_ABSTRACT` | abstract | ଅମୂର୍ତ | `amuurta` | modifier |
| `KW_VIRTUAL` | virtual | ଆଭାସୀ | `aabhaasii` | modifier |
| `KW_OVERRIDE` | override | ଅଧିରୋହଣ | `adhirauha_na` | modifier |

### Paradigm: procedural

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | କାର୍ଯ୍ୟ | `kaaryya` | subroutine |
| `KW_PROC` | procedure | ପ୍ରକ୍ରିୟା | `prakriyaa` | subroutine |
| `KW_CALL` | call | ଡାକ | `daaka` | subroutine |
| `KW_PARAM` | param | ପ୍ରାଚଳ | `praacala` | subroutine |
| `KW_YIELD` | yield | ଦିଅ | `dia` | coroutine |
| `KW_AWAIT` | await | ଅପେକ୍ଷା | `apeek_saa` | async |
| `KW_ASYNC` | async | ଅସମକାଳିକ | `asamakaalika` | async |

### Paradigm: robotics

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | ଚାଲକ | `caalaka` | control |
| `KW_SERVO` | servo | ଅନୁଚାଲକ | `anucaalaka` | control |
| `KW_JOINT` | joint | ସନ୍ଧି | `sandhi` | control |
| `KW_POSE` | pose | ମୁଦ୍ରା | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | ପ୍ରକ୍ଷେପପଥ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | ପ୍ରତିପୁଷ୍ଟି | `pratipu_sti` | control |
| `KW_PID` | pid | ନିଯନ୍ତ୍ରକ | `niyantraka` | control |
| `KW_DEADLINE` | deadline | କାଲସୀମା | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | ଆଵର୍ତିକ | `aavartika` | realtime |
| `KW_PRIORITY` | priority | ପ୍ରାଥମ୍ଯ | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | ପ୍ରଵର୍ତଯ | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | ପ୍ରତ୍ଯକ୍ଷ | `pratyak_sa` | control |
| `KW_PLAN` | plan | ଯୋଜନା | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | ସୂଚକ | `suucaka` | memory |
| `KW_REF` | ref | ସନ୍ଦର୍ଭ | `sandarbha` | memory |
| `KW_ALLOC` | alloc | ଆବଣ୍ଟନ | `aaba_ntana` | memory |
| `KW_FREE` | free | ମୁକ୍ତ | `mukta` | memory |
| `KW_SIZEOF` | sizeof | ଆକାର | `aakaara` | memory |
| `KW_STRUCT` | struct | ସଂରଚନା | `sa_nracanaa` | type_def |
| `KW_UNION` | union | ସଂଘ | `sa_ngha` | type_def |
| `KW_ENUM` | enum | ଗଣନା | `ga_nanaa` | type_def |
| `KW_TYPEDEF` | typedef | ପ୍ରକାରବ୍ୟାଖ୍ୟା | `prakaarabyaakhyaa` | type_def |
| `KW_VOLATILE` | volatile | ଅସ୍ଥିର | `asthira` | modifier |
| `KW_REGISTER` | register | ପଞ୍ଜିକରଣ | `pa_njikara_na` | storage |
| `KW_EXTERN` | extern | ବାହ୍ୟ | `baahya` | linkage |
| `KW_INLINE` | inline | ଧାଡ଼ିଭିତରେ | `dhaadibhitaree` | modifier |

### Paradigm: verification

| Construct | English | Odia | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | ଅପେକ୍ଷତେ | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | ସୁନିଶ୍ଚଯତି | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | ଅପରିଵର୍ତ୍ଯ | `aparivartya` | contract |
| `KW_ASSERT` | assert | ପ୍ରତିଜ୍ଞା | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | ଅଧ୍ଯଵସ୍ଯତି | `adhyavasyati` | contract |
| `KW_PROVE` | prove | ସାଧଯତି | `saadhayati` | contract |
| `KW_REFINES` | refines | ପରିଷ୍କରୋତି | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | ପ୍ରତିମାନପରୀକ୍ଷା | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Odia native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Odia a first-class systems-programming language, not a localized skin.

## Example

```
ଯଦି (x > 0)        // romenagri: yadi
    ...
ଅନ୍ୟଥା              // romenagri: anyathaa
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Odia keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*