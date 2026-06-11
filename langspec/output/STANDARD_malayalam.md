# Malayalam Programming Language Standard

**ILM / Hindawi Programming System — Per-Language Programming Standard**

**Copyright © 1993-2026 Abhishek Choudhary**

- **Human language**: Malayalam
- **ISO 639 code**: mal
- **Script**: Malayalam
- **Native speakers**: 38 million
- **Constructs covered**: 201 of 201
- **Generated**: 2026-05-31

## What this standard defines

This document defines the Malayalam-language keyword set for programming across all major paradigms, together with the **Romenagri** ASCII-7 identifier form for each keyword. The Romenagri form is reversible, case-independent, diacritic-free, and legal as a C identifier — which means a compiler or lexer can accept the Malayalam keyword directly, in native script, and map it deterministically to the ASCII-7 form for the toolchain.

This is the per-language realisation of the Hindawi Programming System principle: complete systems-programming capability in any human language, with the compiler back-end unchanged.

## Keyword tables by paradigm

### Paradigm: ai

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_TENSOR` | tensor | പ്രദിശ | `pradisha` | ml |
| `KW_MATRIX` | matrix | ആവ്യൂഹ | `aavyuuha` | ml |
| `KW_VECTOR` | vector | സദിശ | `sadisha` | ml |
| `KW_GRAD` | gradient | പ്രവണതാ | `prava_nataa` | ml |
| `KW_BACKPROP` | backprop | പ്രതിപ്രസാര | `pratiprasaara` | ml |
| `KW_FORWARD` | forward | അഗ്രപ്രസാര | `agraprasaara` | ml |
| `KW_LAYER` | layer | സ്തര | `stara` | ml |
| `KW_MODEL` | model | പ്രതിമാന | `pratimaana` | ml |
| `KW_TRAIN` | train | പ്രശിക്ഷണ | `prashik_sa_na` | ml |
| `KW_INFER` | infer | അനുമാന | `anumaana` | ml |
| `KW_LOSS` | loss | ഹാനി | `haani` | ml |
| `KW_OPTIMIZE` | optimize | അനുകൂലന | `anukuulana` | ml |
| `KW_ACTIVATION` | activation | സക്രിയണ | `sakriya_na` | ml |
| `KW_WEIGHT` | weight | ഭാര | `bhaara` | ml |
| `KW_BIAS` | bias | പക്ഷപാത | `pak_sapaata` | ml |
| `KW_EPOCH` | epoch | കല്പ | `kalpa` | ml |
| `KW_BATCH` | batch | പുഞ്ജ | `pu_nja` | ml |
| `KW_DATASET` | dataset | ദത്തസമൂഹ | `dattasamuuha` | ml |
| `KW_EMBED` | embed | നിവേശന | `niveeshana` | ml |
| `KW_ATTENTION` | attention | അവധാന | `avadhaana` | ml |

### Paradigm: common

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IMPORT` | import | ഇറക്കുമതി | `irakkumati` | namespace |
| `KW_EXPORT` | export | കയറ്റുമതി | `kayatttumati` | namespace |
| `KW_PACKAGE` | package | പൊതി | `poti` | namespace |
| `KW_NAMESPACE` | namespace | നാമാകാശ | `naamaakaasha` | namespace |
| `KW_USE` | use | ഉപയോഗ | `upayauga` | namespace |
| `KW_INCLUDE` | include | അന്തര്ഭാവ | `antarbhaava` | preprocessor |
| `KW_FROM` | from | തഃ | `ta_h` | namespace |
| `KW_AS` | as | ഇവ | `iva` | namespace |

### Paradigm: concurrent

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_THREAD` | thread | നൂൽ | `nuula` | concurrency |
| `KW_SPAWN` | spawn | സൃഷ്ടിക്കുക | `sr_stikkuka` | concurrency |
| `KW_LOCK` | lock | പൂട്ട് | `puutt` | concurrency |
| `KW_SYNC` | synchronized | സമന്വയം | `samanvaya_m` | concurrency |
| `KW_CHANNEL` | channel | മാർഗ്ഗം | `maarggsa_m` | concurrency |
| `KW_SELECT` | select | തിരഞ്ഞെടുക്കുക | `tira_nyedukkuka` | concurrency |

### Paradigm: dataflow

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_STREAM` | stream | ധാരാ | `dhaaraa` | reactive |
| `KW_PIPE` | pipe | പ്രണാല | `pra_naala` | reactive |
| `KW_MAP` | map | പ്രതിചിത്ര | `praticitra` | reactive |
| `KW_FILTER` | filter | ഛാല | `chaala` | reactive |
| `KW_REDUCE` | reduce | ന്യൂനീകൃ | `nyuuniikr_` | reactive |
| `KW_FOLD` | fold | സംവേഷ്ട | `sa_nvee_sta` | reactive |
| `KW_OBSERVE` | observe | നിരീക്ഷ | `niriik_sa` | reactive |
| `KW_EMIT` | emit | ഉത്സൃജ | `utsr_ja` | reactive |
| `KW_SUBSCRIBE` | subscribe | അഭിനിവേശ | `abhiniveesha` | reactive |
| `KW_DEBOUNCE` | debounce | സ്പന്ദശോധന | `spandashaudhana` | reactive |

### Paradigm: distributed

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_NODE` | node | ഗ്രന്ഥി | `granthi` | cluster |
| `KW_REPLICA` | replica | പ്രതികൃതി | `pratikr_ti` | cluster |
| `KW_CONSENSUS` | consensus | സര്വസമ്മതി | `sarvasammati` | cluster |
| `KW_SHARD` | shard | ഖണ്ഡ | `kha_nda` | cluster |
| `KW_GOSSIP` | gossip | ജനവാദ | `janavaada` | cluster |
| `KW_LEADER` | leader | നായക | `naayaka` | cluster |
| `KW_RPC` | rpc | ദൂരപ്രക്രിയാ | `duuraprakriyaa` | cluster |
| `KW_ACTOR` | actor | കര്തൃ | `kartr_` | cluster |
| `KW_MESSAGE` | message | സന്ദേശ | `sandeesha` | cluster |

### Paradigm: functional

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_LAMBDA` | lambda | അജ്ഞാത | `ajnyaata` | function |
| `KW_MATCH` | match | പൊരുത്തം | `poruttha_m` | pattern |
| `KW_WHEN` | when | എപ്പോൾ | `eppaula` | pattern |
| `KW_FUN` | fun | ഫലനം | `phalana_m` | function |
| `KW_REC` | rec | ആവർത്തന | `aavarttana` | recursion |
| `KW_IN` | in | ഇൽ | `ila` | binding |
| `KW_WHERE` | where | എവിടെ | `evide` | binding |
| `KW_DATA` | data | വിവരം | `vivara_m` | type_def |
| `KW_TYPE` | type | തരം | `tara_m` | type_def |
| `KW_MODULE` | module | ഘടകം | `ghataka_m` | namespace |

### Paradigm: gpu

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_KERNEL` | kernel | ബീജ | `biija` | compute |
| `KW_DEVICE` | device | യന്ത്ര | `yantra` | compute |
| `KW_HOST` | host | ആതിഥേയ | `aatitheeya` | compute |
| `KW_GLOBAL` | global | വൈശ്വിക | `vaishvika` | compute |
| `KW_SHARED` | shared | സഹഭാജിത | `sahabhaajita` | compute |
| `KW_THREADIDX` | threadidx | തന്ത്വങ്ക | `tantva_nka` | compute |
| `KW_BLOCKIDX` | blockidx | ഖണ്ഡാങ്ക | `kha_ndaa_nka` | compute |
| `KW_GRID` | grid | ജാല | `jaala` | compute |
| `KW_BARRIER` | barrier | അവരോധ | `avaurudha` | compute |
| `KW_ATOMIC` | atomic | ആണവിക | `aa_navika` | compute |
| `KW_WARP` | warp | തന്തുസമൂഹ | `tantusamuuha` | compute |

### Paradigm: hdl

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_ENTITY` | entity | അസ്തിത്വം | `astitva_m` | hardware |
| `KW_ARCH` | architecture | വാസ്തുവിദ്യ | `vaastuvidya` | hardware |
| `KW_SIGNAL` | signal | സൂചന | `suucana` | hardware |
| `KW_PORT` | port | തുറമുഖം | `turamukha_m` | hardware |
| `KW_WIRE` | wire | കമ്പി | `kampi` | hardware |
| `KW_REG` | reg | രജിസ്റ്റർ | `rajisttara` | hardware |
| `KW_MODULE_HW` | module | ഭാഗം | `bhaaga_m` | hardware |
| `KW_ALWAYS` | always | എപ്പോഴും | `eppaazhu_m` | hardware |
| `KW_ASSIGN` | assign | നൽകുക | `nalkuka` | hardware |
| `KW_BEGIN` | begin | ആരംഭം | `aara_mbha_m` | block |
| `KW_END` | end | അവസാനം | `avasaana_m` | block |

### Paradigm: imperative

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_IF` | if | എങ്കിൽ | `e_nkila` | control_flow |
| `KW_ELSE` | else | അല്ലെങ്കിൽ | `alle_nkila` | control_flow |
| `KW_ELIF` | elif | അല്ലെങ്കിലെങ്കിൽ | `alle_nkile_nkila` | control_flow |
| `KW_WHILE` | while | വരെ | `vare` | control_flow |
| `KW_DO` | do | ചെയ്യുക | `ceyyuka` | control_flow |
| `KW_FOR` | for | വേണ്ടി | `ve_ndi` | control_flow |
| `KW_BREAK` | break | നിർത്തുക | `nirttuka` | control_flow |
| `KW_CONTINUE` | continue | തുടരുക | `tudaruka` | control_flow |
| `KW_SWITCH` | switch | തിരഞ്ഞെടുപ്പ് | `tira_nyedupp` | control_flow |
| `KW_CASE` | case | അവസ്ഥ | `avastha` | control_flow |
| `KW_DEFAULT` | default | സ്ഥിരസ്ഥിതി | `sthirasthiti` | control_flow |
| `KW_RETURN` | return | മടക്കുക | `madakkuka` | control_flow |
| `KW_GOTO` | goto | പോകുക | `paukuka` | control_flow |
| `KW_VAR` | var | ചരം | `cara_m` | declaration |
| `KW_CONST` | const | സ്ഥിരം | `sthira_m` | declaration |
| `KW_LET` | let | ആകട്ടെ | `aakatte` | declaration |
| `KW_INT` | int | പൂർണ്ണസംഖ്യ | `puur_n_nasa_mkhya` | type |
| `KW_FLOAT` | float | ദശാംശം | `dashaa_msha_m` | type |
| `KW_DOUBLE` | double | ഇരട്ട | `iratta` | type |
| `KW_CHAR` | char | അക്ഷരം | `ak_sara_m` | type |
| `KW_BOOL` | bool | തർക്കം | `tarkka_m` | type |
| `KW_STRING` | string | വാക്യം | `vaakya_m` | type |
| `KW_VOID` | void | ശൂന്യം | `shuunya_m` | type |
| `KW_TRUE` | true | സത്യം | `satya_m` | literal |
| `KW_FALSE` | false | അസത്യം | `asatya_m` | literal |
| `KW_NULL` | null | ശൂന്യ | `shuunya` | literal |
| `KW_TRY` | try | ശ്രമിക്കുക | `shramikkuka` | exception |
| `KW_CATCH` | catch | പിടിക്കുക | `pidikkuka` | exception |
| `KW_FINALLY` | finally | അവസാനമായി | `avasaanamaayi` | exception |
| `KW_THROW` | throw | എറിയുക | `eriyuka` | exception |
| `KW_RAISE` | raise | ഉയർത്തുക | `uyarttuka` | exception |
| `KW_EXCEPT` | except | അപവാദം | `apavaada_m` | exception |

### Paradigm: iot

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PIN` | pin | കീലക | `kiilaka` | io |
| `KW_READ` | read | പഠ | `patha` | io |
| `KW_WRITE` | write | ലിഖ | `likha` | io |
| `KW_ANALOG` | analog | സദൃശ | `sadr_sha` | io |
| `KW_DIGITAL` | digital | അങ്കീയ | `a_nkiiya` | io |
| `KW_PWM` | pwm | സ്പന്ദവിസ്താര | `spandavistaara` | io |
| `KW_INTERRUPT` | interrupt | വിഘ്ന | `vighna` | io |
| `KW_TIMER` | timer | കാലയന്ത്ര | `kaalayantra` | io |
| `KW_SENSOR` | sensor | സംവേദക | `sa_nveedaka` | io |
| `KW_ACTUATOR` | actuator | പ്രവര്തക | `pravartaka` | io |
| `KW_BUS` | bus | മാര്ഗ | `maarga` | io |
| `KW_PROTOCOL` | protocol | നിയമാവലീ | `niyamaavalii` | io |
| `KW_SLEEP` | sleep | സുഷുപ്തി | `su_supti` | power |
| `KW_WAKE` | wake | ജാഗൃ | `jaagr_` | power |

### Paradigm: logic

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_RULE` | rule | നിയമം | `niyama_m` | clause |
| `KW_FACT` | fact | വസ്തുത | `vastuta` | clause |
| `KW_QUERY` | query | ചോദ്യം | `caudya_m` | clause |
| `KW_NOT` | not | അല്ല | `alla` | operator |
| `KW_AND` | and | ഒപ്പം | `oppa_m` | operator |
| `KW_OR` | or | അഥവാ | `athavaa` | operator |

### Paradigm: memory

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_OWN` | own | സ്വാമിത്വ | `svaamitva` | ownership |
| `KW_BORROW` | borrow | ഋണ | `r_na` | ownership |
| `KW_MOVE` | move | സ്ഥാനാന്തര | `sthaanaantara` | ownership |
| `KW_MUT` | mut | പരിവര്ത്യ | `parivartya` | ownership |
| `KW_LIFETIME` | lifetime | ആയുഷ്കാല | `aayu_skaala` | ownership |
| `KW_ARENA` | arena | ക്ഷേത്ര | `k_seetra` | allocation |
| `KW_GC` | gc | മലസംഗ്രഹ | `malasa_ngraha` | allocation |
| `KW_PIN_MEM` | pin | സ്മൃതികീലക | `smr_tikiilaka` | allocation |

### Paradigm: oop

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_CLASS` | class | വർഗ്ഗം | `varggsa_m` | type_def |
| `KW_OBJECT` | object | വസ്തു | `vastu` | type_def |
| `KW_INTERFACE` | interface | സമ്പർക്കമുഖം | `sa_mparkkamukha_m` | type_def |
| `KW_EXTENDS` | extends | വിപുലീകരിക്കുക | `vipuliikarikkuka` | inheritance |
| `KW_IMPLEMENTS` | implements | നടപ്പാക്കുക | `nadappaakkuka` | inheritance |
| `KW_NEW` | new | പുതിയ | `putiya` | instantiation |
| `KW_THIS` | this | ഇത് | `it` | reference |
| `KW_SUPER` | super | പരം | `para_m` | reference |
| `KW_PUBLIC` | public | പൊതു | `potu` | access |
| `KW_PRIVATE` | private | സ്വകാര്യ | `svakaarya` | access |
| `KW_PROTECTED` | protected | സംരക്ഷിത | `sa_mrak_sita` | access |
| `KW_STATIC` | static | സ്ഥിതം | `sthita_m` | storage |
| `KW_ABSTRACT` | abstract | അമൂർത്ത | `amuurtta` | modifier |
| `KW_VIRTUAL` | virtual | മായാ | `maayaa` | modifier |
| `KW_OVERRIDE` | override | അതിലംഘിക്കുക | `atila_mghikkuka` | modifier |

### Paradigm: procedural

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_FUNC` | function | ധർമ്മം | `dharmma_m` | subroutine |
| `KW_PROC` | procedure | നടപടി | `nadapadi` | subroutine |
| `KW_CALL` | call | വിളിക്കുക | `vilikkuka` | subroutine |
| `KW_PARAM` | param | പ്രാചലം | `praacala_m` | subroutine |
| `KW_YIELD` | yield | നൽകുക | `nalkuka` | coroutine |
| `KW_AWAIT` | await | കാത്തിരിക്കുക | `kaattirikkuka` | async |
| `KW_ASYNC` | async | അസമകാലിക | `asamakaalika` | async |

### Paradigm: robotics

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_MOTOR` | motor | ചാലക | `caalaka` | control |
| `KW_SERVO` | servo | അനുചാലക | `anucaalaka` | control |
| `KW_JOINT` | joint | സന്ധി | `sandhi` | control |
| `KW_POSE` | pose | മുദ്രാ | `mudraa` | control |
| `KW_TRAJECTORY` | trajectory | പ്രക്ഷേപപഥ | `prak_seepapatha` | control |
| `KW_FEEDBACK` | feedback | പ്രതിപുഷ്ടി | `pratipu_sti` | control |
| `KW_PID` | pid | നിയന്ത്രക | `niyantraka` | control |
| `KW_DEADLINE` | deadline | കാലസീമാ | `kaalasiimaa` | realtime |
| `KW_PERIODIC` | periodic | ആവര്തിക | `aavartika` | realtime |
| `KW_PRIORITY` | priority | പ്രാഥമ്യ | `praathamya` | realtime |
| `KW_ACTUATE` | actuate | പ്രവര്തയ | `pravartaya` | control |
| `KW_PERCEIVE` | perceive | പ്രത്യക്ഷ | `pratyak_sa` | control |
| `KW_PLAN` | plan | യോജനാ | `yaujanaa` | control |

### Paradigm: systems

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_PTR` | pointer | സൂചകം | `suucaka_m` | memory |
| `KW_REF` | ref | പരാമർശം | `paraamarsha_m` | memory |
| `KW_ALLOC` | alloc | അനുവദിക്കുക | `anuvadikkuka` | memory |
| `KW_FREE` | free | സ്വതന്ത്രം | `svatantra_m` | memory |
| `KW_SIZEOF` | sizeof | വലുപ്പം | `valuppa_m` | memory |
| `KW_STRUCT` | struct | ഘടന | `ghatana` | type_def |
| `KW_UNION` | union | സംഘം | `sa_mgha_m` | type_def |
| `KW_ENUM` | enum | എണ്ണൽ | `e_n_nala` | type_def |
| `KW_TYPEDEF` | typedef | തരനിർവചനം | `taranirvacana_m` | type_def |
| `KW_VOLATILE` | volatile | അസ്ഥിര | `asthira` | modifier |
| `KW_REGISTER` | register | രജിസ്റ്റർ | `rajisttara` | storage |
| `KW_EXTERN` | extern | ബാഹ്യ | `baahya` | linkage |
| `KW_INLINE` | inline | വരിയിൽ | `variyila` | modifier |

### Paradigm: verification

| Construct | English | Malayalam | Romenagri (ASCII-7) | Category |
|---|---|---|---|---|
| `KW_REQUIRES` | requires | അപേക്ഷതേ | `apeek_satee` | contract |
| `KW_ENSURES` | ensures | സുനിശ്ചയതി | `sunishcayati` | contract |
| `KW_INVARIANT` | invariant | അപരിവര്ത്യ | `aparivartya` | contract |
| `KW_ASSERT` | assert | പ്രതിജ്ഞാ | `pratijnyaa` | contract |
| `KW_ASSUME` | assume | അധ്യവസ്യതി | `adhyavasyati` | contract |
| `KW_PROVE` | prove | സാധയതി | `saadhayati` | contract |
| `KW_REFINES` | refines | പരിഷ്കരോതി | `pari_skarauti` | contract |
| `KW_MODEL_CHECK` | modelcheck | പ്രതിമാനപരീക്ഷാ | `pratimaanapariik_saa` | contract |

## Reversibility guarantee

Every Romenagri form in this standard is ASCII-7, contains no uppercase, no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. Each maps back deterministically to its Malayalam native-script keyword via the ILM reverse projection (rmn2acii). This is what makes Malayalam a first-class systems-programming language, not a localized skin.

## Example

```
എങ്കിൽ (x > 0)        // romenagri: e_nkila
    ...
അല്ലെങ്കിൽ              // romenagri: alle_nkila
    ...
```

---

*Copyright © 1993-2026 Abhishek Choudhary. This standard document is licensed CC BY-SA 4.0. The Malayalam keyword assignments and their Romenagri forms are an original contribution of the ILM / Hindawi Programming System project, with priority dating to the Hindawi Programming System public release of 15 August 2004.*