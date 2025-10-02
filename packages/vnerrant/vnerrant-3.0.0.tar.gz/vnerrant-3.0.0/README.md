# VNERRANT v3.0.0

## Overview

The main aim of VNERRANT is to automatically annotate parallel English sentences with error type information.
Specifically, given an original and corrected sentence pair, VNERRANT will extract the edits that transform the
former to the latter and classify them according to a rule-based error type framework. This can be used to
standardise parallel datasets or facilitate detailed error type evaluation. Annotated output files are in
M2 format and an evaluation script is provided.

### Example

**Original**: This are gramamtical sentence .
**Corrected**: This is a grammatical sentence .
**Output M2**:

```text
S This are gramamtical sentence .
A 1 2|||R:VERB:SVA|||is|||REQUIRED|||-NONE-|||0
A 2 2|||M:DET|||a|||REQUIRED|||-NONE-|||0
A 2 3|||R:SPELL|||grammatical|||REQUIRED|||-NONE-|||0
A -1 -1|||noop|||-NONE-|||REQUIRED|||-NONE-|||1
```

## Installation

### Pip Install

```bash
conda create -n vnerrant python=3.9
conda activate vnerrant
```

You have two options for installing VNERRANT:

- Option 1: Install VNERRANT using pip with the following commands:

```bash
pip install -U pip setuptools wheel
pip install vnerrant
```

- Option 2: Alternatively, if you want to install VNERRANT from the source, you can follow these steps:

```bash
git clone https://gitlab.testsprep.online/nlp/research/vnerrant
cd vnerrant
pip install -U pip setuptools wheel
pip install -e .
```

Please obtain a Spacy model by using the following command:

```bash
python -m spacy download en_core_web_sm
```

You can verify the available models at [this](https://spacy.io/models/en) location.

## Usage

### CLI

Two main commands are provided with VNERRANT: `convert` and `evaluate`. You can run them from anywhere on the command line without having to invoke a specific python script.

1.`vnerrant convert parallel-to-m2`

This is the main annotation command that takes an original text file and at least one parallel corrected text file as input, and outputs an annotated M2 file. By default, it is assumed that the original and corrected text files are word tokenised with one sentence per line.
Example:

```cli
vnerrant convert parallel-to-m2 -o <orig_file> -c <cor_file1> [<cor_file2> ...] -out <out_m2>
```

2.`vnerrant convert m2-to-m2`

This is a variant of `parallel-to-m2` that operates on an M2 file instead of parallel text files. This makes it easier to reprocess existing M2 files. You must also specify whether you want to use gold or auto edits; i.e. `-gold` will only classify the existing edits, while `-auto` will extract and classify automatic edits. In both settings, uncorrected edits and noops are preserved.
Example:

```cli
vnerrant convert m2-to-m2  -i <in_m2> -o <out_m2> {-auto|-gold}
```

3.`vnerrant evaluate m2`

This is the evaluation command that compares a hypothesis M2 file against a reference M2 file. The default behaviour evaluates the hypothesis overall in terms of span-based correction. The `-cat {1,2,3}` flag can be used to evaluate error types at increasing levels of granularity, while the `-ds` or `-dt` flag can be used to evaluate in terms of span-based or token-based detection (i.e. ignoring the correction). All scores are presented in terms of Precision, Recall and F-score (default: F0.5), and counts for True Positives (TP), False Positives (FP) and False Negatives (FN) are also shown.
Examples:

```cli
vnerrant evaluate m2 -hyp <hyp_m2> -ref <ref_m2>
vnerrant evaluate m2 -hyp <hyp_m2> -ref <ref_m2> -cat {1,2,3}
vnerrant evaluate m2 -hyp <hyp_m2> -ref <ref_m2> -ds
vnerrant evaluate m2 -hyp <hyp_m2> -ref <ref_m2> -ds -cat {1,2,3}
```

All these scripts also have additional advanced command line options which can be displayed using the `-h` flag.

### API

As of v3.0.0, VNERRANT now also comes with an API.

### Quick Start

```python
import vnerrant

annotator = vnerrant.load('en')

orig = 'My    name    is   the     John'
cor = 'My name is John'
edits = annotator.annotate_raw(orig, cor)

for e in edits:
    print(e.original.start_token, e.original.end_token, e.original.text)
    print(e.corrected.start_token, e.corrected.end_token, e.corrected.text)
    print(e.original.start_char, e.original.end_char, e.edit_type)
```

### Loading

`vnerrant.load(lang, model_name)`

Instantiate an VNERRANT Annotator object. Presently, the lang parameter exclusively accepts 'en' for English, though we aspire to broaden its language support in future iterations. The model_name corresponds to the name of the SpaCy model being utilized. Optionally, you can provide the nlp parameter if you've previously loaded SpaCy and wish to prevent VNERRANT from loading it redundantly.

### Annotator Objects

An Annotator object is the main interface for VNERRANT.

#### Methods

<details>
<summary>annotator.parse</summary>

`annotator.parse(string, tokenize_type='string')`

Lemmatise, POS tag, and parse a text string with spacy. Returns a spacy Doc object.

`tokenize_type` must be in `["spacy", "split", "string"]`

- `spacy`: tokenizing by default spacy tokenizer.
- `split`: tokenizing by split function.
- `string`: tokenizing by spacy and string tokenizer.

</details>

<details>
<summary>annotator.align</summary>

`annotator.align(orig, cor, lev=False)`

Align spacy-parsed original and corrected text. The default uses a linguistically-enhanced Damerau-Levenshtein alignment, but the `lev` flag can be used for a standard Levenshtein alignment. Returns an Alignment object.

</details>

<details>
<summary>annotator.merge</summary>

`annotator.merge(alignment, merging='rules')`

Extract edits from the optimum alignment in an Alignment object. Four different merging strategies are available:

1. rules: Use a rule-based merging strategy (default)
2. all-split: Merge nothing: MSSDI -> M, S, S, D, I
3. all-merge: Merge adjacent non-matches: MSSDI -> M, SSDI
4. all-equal: Merge adjacent same-type non-matches: MSSDI -> M, SS, D, I

Returns a list of Edit objects.
</details>

<details>
<summary>annotator.classify</summary>

`annotator.classify(edit)`

Classify an edit. Sets the `edit.type` attribute in an Edit object and returns the same Edit object.

</details>

<details>
<summary>annotator.annotate</summary>

`annotator.annotate(orig, cor, lev=False, merging='rules')`

Run the full annotation pipeline to align two sequences and extract and classify the edits.
Equivalent to running `annotator.align`, `annotator.merge` and `annotator.classify` in sequence.
Returns a list of Edit objects.

```python
import vnerrant

annotator = vnerrant.load(lang="en", model_name="en_core_web_sm")
orig = annotator.parse("My   name   is    the    John")
cor = annotator.parse("My name is John")
edits = annotator.annotate(orig, cor)
for e in edits:
    print(e)
```

</details>

<details>
<summary>annotator.annotate_raw</summary>

`annotator.annotate_raw(orig: str, cor: str, lev=False, merging='rules', tokenize_type='string')`

Run the full annotation pipeline to align two strings, extract and classify the edits.
Equivalent to running `annotator.parse`, `annotator.align`, `annotator.merge` and `annotator.classify` in sequence.
Returns a list of Edit objects.

```python
import vnerrant

annotator = vnerrant.load(lang="en", model_name="en_core_web_sm")
orig = "My   name   is    the    John"
cor = "My name is John"
edits = annotator.annotate_raw(orig, cor)
for e in edits:
    print(e)
```

</details>

<details>
<summary>annotator.import_edit</summary>

`annotator.import_edit(orig, cor, edit, min=True, old_cat=False)`

Load an Edit object from a list. `orig` and `cor` must be spacy-parsed Doc objects and the edit must be of the form:
`[o_start, o_end, c_start, c_end(, type)]`. The values must be integers that correspond to the token start and end
offsets in the original and corrected Doc objects. The `type` value is an optional string that denotes the error type
of the edit (if known). Set `min` to True to minimise the edit (e.g. [a b -> a c] = [b -> c]) and `old_cat` to True
to preserve the old error type category (i.e. turn off the classifier).

```python
import vnerrant

annotator = vnerrant.load('en')
orig = annotator.parse('This are gramamtical sentence .')
cor = annotator.parse('This is a grammatical sentence .')
edit = [1, 2, 1, 2, 'SVA'] # are -> is
edit = annotator.import_edit(orig, cor, edit)
print(edit.to_m2())
```

</details>

### Alignment Objects

An Alignment object is created from two spacy-parsed text sequences.

#### Attributes

`alignment`.**orig**
`alignment`.**cor**
The spacy-parsed original and corrected text sequences.

`alignment`.**cost_matrix**
`alignment`.**op_matrix**
The cost matrix and operation matrix produced by the alignment.

`alignment`.**align_seq**
The first cheapest alignment between the two sequences.

### Edit Objects

An Edit object represents a transformation between two text sequences.

**Attributes**

`edit`.**o_start**
`edit`.**o_end**
`edit`.**o_toks**
`edit`.**o_str**
The start and end offsets, the spacy tokens, and the string for the edit in the *original* text.

`edit`.**c_start**
`edit`.**c_end**
`edit`.**c_toks**
`edit`.**c_str**
The start and end offsets, the spacy tokens, and the string for the edit in the *corrected* text.

`edit`.**type**
The error type string.

**Method**

`edit`.**to_m2**(id=0)
Format the edit for an output M2 file. `id` is the annotator id.
