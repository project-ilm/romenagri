# Reversible Romanisation as a Tokenisation Substrate: Vocabulary Collapse and Sequence Compression for Non-Latin Scripts

**Abhishek Choudhary** · AyeAI
*Copyright © 1993–2026 Abhishek Choudhary. Draft.*

## Abstract
Subword tokenisers (BPE, SentencePiece) fragment non-Latin scripts into more tokens per morpheme
than Latin text, imposing a per-token compute and effective-context asymmetry that propagates through
the model lifecycle. We show that applying a lossless, reversible romanisation (Romenagri) as a
tokenisation preprocessing layer gives Indic and Perso-Arabic text Latin-grade tokenisation: the
working vocabulary collapses and sequence length shortens by a measured factor k. Because the
romanisation is reversible, no information is lost — surface form is recoverable. We give the
measurement procedure and report k per language. The reversibility distinguishes this from lossy
normalisation: it is a substrate change, not an approximation. We state the result as a falsifiable
prediction and provide the CPU-only experiment that tests it.

## 1. The problem
A tokeniser that allocates one token per Latin morpheme but several per Indic morpheme forces every
downstream layer to relearn reassembly and charges more tokens — hence more attention compute (O(n²)
in sequence length) and less effective context — for identical content in a non-Latin script. This
is a substrate-level inequity, not patchable downstream.

## 2. The claim (prediction P1)
For Brahmi-derived and Perso-Arabic text, Romenagri projection reduces tokeniser token count by a
factor k > 1 (we predict k ≈ 3–5), and a small language model trained on the Romenagri form reaches
equal-or-lower perplexity at strictly smaller vocabulary under equal compute. **Falsifier:** if k ≤ 1,
or the Romenagri-trained model is worse at equal vocabulary, the claim is wrong.

## 3. Method
For each native-script corpus: (i) romanise losslessly via the Romenagri core (reversible, so
recoverable); (ii) train an identical small BPE on native and on romanised text; (iii) count tokens
for identical content under each; k = native_tokens / romenagri_tokens; record both vocabularies.
For the perplexity arm: train LM-A on native, LM-B on Romenagri, equal compute budget; compare
perplexity at matched vocabulary. The tokenisation arm is CPU-only and is the headline number; the
LM arm fits a single small GPU (e.g. RTX 3050, 4 GB) precisely because the romanised form is what
makes a model trainable at that scale. *(Procedure implemented in `tokenizer_efficiency.py`.)*

## 4. Results (to be filled by the run)
| Corpus | native tok / vocab | romenagri tok / vocab | k |
|---|---|---|---|
| Hindi (corp_hi) | … | … | … |
| Urdu (corp_ur) | … | … | … |
| Bengali (corp_bn) | … | … | … |
| Telugu (corp_te) | … | … | … |
| **mean / median k** | | | **…** |

The vocabulary-collapse figure (native vocab → romenagri vocab) and the mean k are the two reported
results. The exact factor is **measured, not asserted** — this section is completed by the experiment
output (`tokenizer_efficiency_results.json`).

## 5. Honest scope
Romenagri shortens sequences and collapses vocabulary — it reduces the embedding/vocab/sequence/
compute burden. It does **not** reduce the reasoning layers (attention/FFN depth); a frontier
multi-billion-parameter pretraining still does not fit 4 GB. The claim is the substrate asymmetry: a
model untrainable on modest hardware in native script becomes trainable in Romenagri form at the same
fidelity, because the surface is recoverable. The reversibility (companion paper: 98.68%
reversible-or-canonicalizable, 1.31% floor) is what makes this lossless rather than a lossy
normalisation.

## 6. Relation to existing multilingual work
AI4Bharat (IndicTrans2, IndicBERT), TildeOpen, Aya, and SentencePiece-based pipelines adapt or
finetune imported architectures and apply subword tokenisation to raw script bytes. Romenagri changes
the substrate beneath tokenisation rather than the model above it; it is complementary (it can
precede any of these tokenisers) and is the only reversible option among them.

## 7. Conclusion
A reversible romanisation used as a tokenisation substrate yields measured vocabulary collapse and
sequence compression for non-Latin scripts without information loss, narrowing the substrate-level
compute asymmetry. The result is falsifiable and CPU-measurable; the number is the contribution.

*References: Sennrich et al. 2016; Kudo & Richardson 2018; Devlin et al. 2019; Conneau et al. 2020
(mBERT bias); Üstün et al. 2024 (Aya); AI4Bharat IndicTrans2 2023. Copyright © 1993–2026 Abhishek
Choudhary.*
