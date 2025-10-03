# BidNLP Development Roadmap & Onboarding

**Persian (Farsi) Natural Language Processing Library**

Last Updated: 2025-10-02

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Current Status](#current-status)
3. [Completed Modules](#completed-modules)
4. [Module Details](#module-details)
5. [Known Issues & Fixes](#known-issues--fixes)
6. [Next Steps](#next-steps)
7. [Development Notes](#development-notes)
8. [Testing](#testing)

---

## 🎯 Project Overview

BidNLP is a comprehensive Persian (Farsi) NLP library designed to handle the unique challenges of Persian language processing, including:
- ZWNJ (zero-width non-joiner) handling
- Arabic to Persian normalization
- Compound words
- Mixed script text
- Complex morphology

### Project Structure

```
bidnlp/
├── bidnlp/
│   ├── __init__.py
│   ├── preprocessing/       ✅ COMPLETE
│   ├── tokenization/        ✅ COMPLETE
│   ├── stemming/           ⚠️ PARTIAL (needs refinement)
│   ├── lemmatization/      ⚠️ PARTIAL (needs refinement)
│   ├── classification/     ❌ TODO
│   └── utils/              ❌ TODO
├── tests/
│   ├── preprocessing/      ✅ 58 tests passing
│   ├── tokenization/       ✅ 64 tests passing
│   ├── stemming/          ⚠️ 7/14 tests passing
│   └── lemmatization/     ⚠️ 9/20 tests passing
├── examples/
│   ├── preprocessing_example.py  ✅
│   └── tokenization_example.py   ✅
├── docs/                   ❌ TODO
├── setup.py               ✅
└── README.md              ✅
```

---

## ✅ Current Status

### Fully Completed & Production-Ready Modules

#### 1. **Preprocessing Module** 🟢
- **Status**: 100% Complete
- **Tests**: 58/58 passing
- **Files**:
  - `bidnlp/preprocessing/normalizer.py`
  - `bidnlp/preprocessing/cleaner.py`
  - `bidnlp/preprocessing/number_normalizer.py`
  - `bidnlp/preprocessing/punctuation.py`

#### 2. **Tokenization Module** 🟢
- **Status**: 100% Complete
- **Tests**: 64/64 passing
- **Files**:
  - `bidnlp/tokenization/word_tokenizer.py`
  - `bidnlp/tokenization/sentence_tokenizer.py`
  - `bidnlp/tokenization/subword_tokenizer.py`

### Partially Complete Modules

#### 3. **Stemming Module** 🟡
- **Status**: ~50% Complete
- **Tests**: 7/14 passing
- **Issues**:
  - Over-aggressive single-character suffix removal (ی, د, م)
  - Some test expectations need updating
  - Works correctly for Arabic broken plurals (e.g., سبزیجات → سبزی)

#### 4. **Lemmatization Module** 🟡
- **Status**: ~45% Complete
- **Tests**: 9/20 passing
- **Issues**:
  - Verb lemmatization needs refinement
  - False positives in verb prefix detection
  - Some irregular forms need better handling

### Fully Complete Modules

#### 5. **Classification Module** 🟢
- **Status**: 100% Complete
- **Tests**: 46/46 passing
- **Files**:
  - `bidnlp/classification/base_classifier.py`
  - `bidnlp/classification/sentiment_analyzer.py`
  - `bidnlp/classification/keyword_classifier.py`
  - `bidnlp/classification/feature_extraction.py`

#### 6. **Utils Module** 🟢
- **Status**: 100% Complete
- **Tests**: 117/117 passing
- **Files**:
  - `bidnlp/utils/characters.py`
  - `bidnlp/utils/statistics.py`
  - `bidnlp/utils/stopwords.py`
  - `bidnlp/utils/validators.py`
  - `bidnlp/utils/metrics.py`

---

## 📦 Completed Modules

### 1. Preprocessing Module

#### Components:

**PersianNormalizer**
- ✅ Arabic to Persian character conversion (ك→ک, ي→ی)
- ✅ Arabic-Indic to Persian digits (٠→۰)
- ✅ Diacritic removal (تشکیل)
- ✅ Kashida removal (ـ)
- ✅ ZWNJ normalization
- ✅ Whitespace normalization
- ✅ Unicode normalization (NFKC)
- ✅ Invisible character removal
- ✅ Spacing around punctuation

**PersianTextCleaner**
- ✅ URL removal/replacement
- ✅ Email removal/replacement
- ✅ Mention (@) handling
- ✅ Hashtag (#) handling
- ✅ HTML tag removal
- ✅ Emoji removal/replacement
- ✅ Special character removal
- ✅ Punctuation removal
- ✅ Number removal
- ✅ Non-Persian text removal
- ✅ Repeated character normalization

**PersianNumberNormalizer**
- ✅ Persian ↔ English digit conversion
- ✅ Arabic-Indic ↔ Persian conversion
- ✅ Number word to digit (یک → 1)
- ✅ Digit to word (25 → بیست و پنج)
- ✅ Phone number formatting
- ✅ Currency normalization
- ✅ Number extraction

**PersianDateNormalizer**
- ✅ Jalali date normalization
- ✅ Date format standardization
- ✅ Month name mapping
- ✅ Date extraction

**PersianPunctuationNormalizer**
- ✅ Persian ↔ Latin punctuation
- ✅ Quotation mark normalization
- ✅ Spacing fixes
- ✅ Ellipsis normalization
- ✅ Duplicate removal

### 2. Tokenization Module

#### Components:

**PersianWordTokenizer**
- ✅ ZWNJ-aware word tokenization
- ✅ Compound word handling
- ✅ Mixed script support (Persian/English/Numbers)
- ✅ Punctuation separation
- ✅ Position tracking
- ✅ Token type detection
- ✅ Decimal number preservation
- ✅ Detokenization support

**PersianSentenceTokenizer**
- ✅ Persian & Latin punctuation handling
- ✅ Abbreviation detection
- ✅ Decimal number awareness
- ✅ Quotation support
- ✅ Position tracking
- ✅ Sentence counting

**PersianCharacterTokenizer**
- ✅ Character-level tokenization
- ✅ Diacritic handling

**PersianMorphemeTokenizer**
- ✅ Prefix detection (می، نمی، بی، etc.)
- ✅ Suffix detection (ها، تر، ترین، etc.)
- ✅ Morphological tagging
- ✅ Stem extraction

**PersianSyllableTokenizer**
- ✅ Syllable segmentation
- ✅ Syllable counting

---

## 🔍 Module Details

### Preprocessing Usage

```python
from bidnlp.preprocessing import (
    PersianNormalizer,
    PersianTextCleaner,
    PersianNumberNormalizer
)

# Normalize text
normalizer = PersianNormalizer()
text = normalizer.normalize("كتاب يک مدرسة")
# Output: "کتاب یک مدرسه"

# Clean text
cleaner = PersianTextCleaner(
    remove_urls=True,
    remove_emojis=True
)
clean_text = cleaner.clean("سلام 😊 https://test.com")
# Output: "سلام"

# Normalize numbers
num_normalizer = PersianNumberNormalizer()
result = num_normalizer.normalize_digits("۱۲۳", 'english')
# Output: "123"
```

### Tokenization Usage

```python
from bidnlp.tokenization import (
    PersianWordTokenizer,
    PersianSentenceTokenizer,
    PersianMorphemeTokenizer
)

# Word tokenization
word_tokenizer = PersianWordTokenizer()
tokens = word_tokenizer.tokenize("من کتاب می‌خوانم")
# Output: ['من', 'کتاب', 'می', 'خوانم']

# Sentence tokenization
sent_tokenizer = PersianSentenceTokenizer()
sentences = sent_tokenizer.tokenize("جمله اول. جمله دوم؟")
# Output: ['جمله اول.', 'جمله دوم؟']

# Morpheme analysis
morph_tokenizer = PersianMorphemeTokenizer()
morphemes = morph_tokenizer.tokenize_with_tags("میروم")
# Output: [('می', 'PRES'), ('رو', 'STEM'), ('م', 'POSS_1S')]
```

### Classification Usage

```python
from bidnlp.classification import (
    PersianSentimentAnalyzer,
    KeywordClassifier,
    TfidfVectorizer
)

# Sentiment analysis
analyzer = PersianSentimentAnalyzer()
sentiment = analyzer.predict("این کتاب خیلی خوب است")
# Output: 'positive'

# Text classification
classifier = KeywordClassifier()
classifier.add_category('ورزش', {'فوتبال', 'بازیکن', 'تیم'})
category = classifier.predict("تیم فوتبال برد")
# Output: 'ورزش'

# Feature extraction
tfidf = TfidfVectorizer(max_features=100)
vectors = tfidf.fit_transform(documents)
```

### Utils Usage

```python
from bidnlp.utils import (
    PersianCharacters,
    PersianTextStatistics,
    PersianStopWords,
    PersianTextValidator,
    PersianTextMetrics
)

# Character utilities
chars = PersianCharacters()
is_persian = chars.is_persian_text("سلام دنیا")

# Statistics
stats = PersianTextStatistics()
statistics = stats.get_statistics("من به دانشگاه می‌روم")

# Stop words
stopwords = PersianStopWords()
filtered = stopwords.remove_stopwords("من از دانشگاه می روم")

# Validation
validator = PersianTextValidator()
quality = validator.get_quality_score("سلام دنیا")

# Metrics
metrics = PersianTextMetrics()
f1 = metrics.f1_score({'a', 'b'}, {'a', 'c'})
```

---

## ⚠️ Known Issues & Fixes

### Stemming/Lemmatization Issues

**Issue #1: Arabic Broken Plurals**
- **Problem**: سبزیجات was stemming to سبزیج instead of سبزی
- **Solution**: ✅ FIXED
  - Added `arabic_broken_plurals` patterns
  - Moved broken plural handling before regular plural removal
  - Pattern: یجات → ی, جات → ''

**Issue #2: Over-aggressive Single Character Removal**
- **Problem**: Single letters like ی, د, م were being removed too aggressively
- **Solution**: ✅ PARTIALLY FIXED
  - Removed ی from verb_suffixes and adjectival_suffixes
  - Made 'ه' removal more conservative (only for words > 4 chars)
  - **Still needs**: Context-aware suffix removal

**Issue #3: Verb Prefix False Positives**
- **Problem**: Words like میوه being treated as verbs (می + وه)
- **Solution**: ✅ FIXED
  - Added minimum stem length check (> 2 chars) after prefix removal
  - Prevents short words from being misidentified as verbs

**Issue #4: Test Failures**
- **Stemming**: 7 tests failing (mostly due to conservative suffix removal changes)
- **Lemmatization**: 11 tests failing (verb lemmatization needs work)
- **Action Needed**: Review test expectations vs actual behavior
  - Some may need test updates
  - Some need algorithm refinement

---

## 🚀 Next Steps

### Immediate Priorities

1. **Fix Stemming/Lemmatization Tests** (High Priority)
   - Review failing tests
   - Decide: update tests or fix algorithms
   - Document expected behavior
   - Consider adding confidence scores

2. **Improve Verb Handling** (High Priority)
   - Better irregular verb dictionary
   - More sophisticated verb stem recognition
   - Handle compound verbs (e.g., غذا خوردن)

3. **Add More Test Cases** (Medium Priority)
   - Real-world text examples
   - Edge cases
   - Performance benchmarks

### Future Development

4. **Classification Module** (Not Started)
   - Text classification framework
   - Sentiment analysis
   - Named Entity Recognition
   - Part-of-speech tagging

5. **Utils Module** (Not Started)
   - Common text utilities
   - Evaluation metrics
   - Data loaders
   - Visualization tools

6. **Documentation** (Low Priority)
   - API documentation
   - User guide
   - Examples and tutorials
   - Contributing guide

7. **Performance Optimization**
   - Caching for repeated operations
   - Parallel processing for batch operations
   - Memory optimization

8. **Additional Features**
   - Stop word removal
   - N-gram generation
   - Collocation detection
   - Text similarity

---

## 💡 Development Notes

### Important Decisions Made

1. **ZWNJ Handling**:
   - Decided to normalize ZWNJ usage by default
   - Insert ZWNJ after prefixes (می، نمی، بی)
   - Critical for Persian compound words

2. **Number Format**:
   - Support both Persian (۰-۹) and English (0-9) digits
   - Default to English for internal processing
   - Allow user to specify output format

3. **Suffix Removal Strategy**:
   - Moved from aggressive to conservative
   - Prefer precision over recall
   - Added minimum stem length constraints

4. **Test Philosophy**:
   - Comprehensive test coverage
   - Real-world examples
   - Both positive and negative cases

### Code Style

- **Imports**: Use explicit imports
- **Docstrings**: Google style
- **Type Hints**: Used where beneficial
- **Error Handling**: Fail gracefully
- **Configuration**: Boolean flags for flexibility

### Persian-Specific Considerations

1. **Character Normalization**:
   - Always normalize Arabic ك→ک, ي→ی
   - Handle both Arabic-Indic and Persian digits
   - Remove diacritics by default

2. **Word Boundaries**:
   - ZWNJ (‌) creates visual word boundaries but semantic unity
   - Handle compound words carefully
   - Consider both forms with/without ZWNJ

3. **Morphology**:
   - Rich prefix/suffix system
   - Verb conjugation is complex
   - Irregular forms need dictionary lookup

---

## 🧪 Testing

### Running Tests

```bash
# All tests
pytest tests/

# Specific module
pytest tests/preprocessing/ -v
pytest tests/tokenization/ -v
pytest tests/stemming/ -v
pytest tests/lemmatization/ -v

# Quiet mode
pytest tests/preprocessing/ -q

# With coverage
pytest tests/ --cov=bidnlp
```

### Current Test Status

| Module | Tests | Passing | Status |
|--------|-------|---------|--------|
| Preprocessing | 58 | 58 | ✅ 100% |
| Tokenization | 64 | 64 | ✅ 100% |
| Utils | 117 | 117 | ✅ 100% |
| Classification | 46 | 46 | ✅ 100% |
| Stemming | 14 | 7 | ⚠️ 50% |
| Lemmatization | 20 | 9 | ⚠️ 45% |
| **TOTAL** | **321** | **302** | **94.1%** |

### Running Examples

```bash
# Set PYTHONPATH
export PYTHONPATH=.

# Run examples
python3 examples/preprocessing_example.py
python3 examples/tokenization_example.py
python3 examples/utils_example.py
python3 examples/classification_example.py
```

---

## 📝 Quick Reference

### Key Files to Know

**Configuration & Setup**:
- `setup.py` - Package configuration
- `README.md` - User-facing documentation
- `.gitignore` - Git ignore patterns

**Core Modules**:
- `bidnlp/preprocessing/normalizer.py` - Main text normalizer
- `bidnlp/tokenization/word_tokenizer.py` - Word tokenization
- `bidnlp/stemming/persian_stemmer.py` - Stemming logic
- `bidnlp/lemmatization/persian_lemmatizer.py` - Lemmatization logic

**Tests**:
- `tests/preprocessing/` - All preprocessing tests
- `tests/tokenization/` - All tokenization tests

**Examples**:
- `examples/preprocessing_example.py` - Comprehensive preprocessing demo
- `examples/tokenization_example.py` - Comprehensive tokenization demo

### Common Commands

```bash
# Run specific test
python -m pytest tests/stemming/test_persian_stemmer.py::TestPersianStemmer::test_arabic_broken_plurals -v

# Run with specific Python path
PYTHONPATH=. python3 script.py

# Check module import
python3 -c "from bidnlp.preprocessing import PersianNormalizer; print('OK')"
```

---

## 🎓 Key Learnings

### Persian NLP Challenges

1. **Arabic vs Persian Characters**: Many texts mix Arabic and Persian characters (ك vs ک)
2. **ZWNJ Usage**: Critical for compound words, inconsistently used in text
3. **Number Systems**: Three systems in use (Persian, Arabic-Indic, English)
4. **Morphological Complexity**: Rich prefix/suffix system requires careful handling
5. **Irregular Forms**: Many common words have irregular plurals and conjugations

### Technical Decisions

1. **Regex Unicode Escapes**: Use variables for Unicode characters in regex replacements
   ```python
   zwnj = '\u200c'
   text = re.sub(pattern, r'\1' + zwnj + r'\2', text)
   ```

2. **Punctuation in Quotes**: Use Unicode escapes for fancy quotes
   ```python
   '\u201c': '\u201d'  # Instead of: '"': '"'
   ```

3. **Conservative Stemming**: Better to understem than overstem
   - Minimum stem length: 2
   - Remove 'ه' only for words > 4 characters
   - Avoid single-letter suffix removal

---

## 📧 Contact & Notes

**Project**: BidNLP - Persian NLP Library
**Language**: Python 3.7+
**License**: MIT
**Last Session**: 2025-10-02

### Session Summary

**Completed**:
1. ✅ Full preprocessing module with 58 passing tests
2. ✅ Full tokenization module with 64 passing tests
3. ✅ Fixed Arabic broken plural handling in stemming/lemmatization
4. ✅ Created comprehensive examples
5. ✅ Documented all modules

**Partially Complete**:
1. ⚠️ Stemming module (needs test review)
2. ⚠️ Lemmatization module (needs verb handling improvement)

**Next Session Should Focus On**:
1. Review and fix failing stemming/lemmatization tests
2. Improve verb lemmatization logic
3. Add more real-world test cases
4. Consider starting classification module

---

*This roadmap is a living document. Update it as the project evolves.*
