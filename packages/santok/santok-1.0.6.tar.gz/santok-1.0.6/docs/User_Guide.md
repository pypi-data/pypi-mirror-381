# SanTOK User Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Interactive Mode](#interactive-mode)
3. [Advanced Processing Features](#advanced-processing-features)
4. [Command Line Usage](#command-line-usage)
5. [Output Formats](#output-formats)
6. [Advanced Features](#advanced-features)
7. [Examples and Tutorials](#examples-and-tutorials)
8. [Troubleshooting](#troubleshooting)
9. [Best Practices](#best-practices)

---

## Getting Started

### Installation
SanTOK is a Python-based tokenization system. No additional dependencies are required beyond Python 3.7+.

### Quick Start
1. **Download**: Get the SanTOK.py file
2. **Run**: Execute `python SanTOK.py`
3. **Choose**: Select input option (Text, File, or Reconstruction test)
4. **Enter**: Provide your text or file
5. **Select**: Choose output format and options
6. **Export**: Save results in your preferred format

### First Example
```bash
python SanTOK.py
# Choose option 1: Text input
# Enter: "Hello world!"
# Choose output mode: 2 (USER summary)
# Select output format: JSON
# Enter filename: my_first_tokenization
# View results in outputs/json/ directory
```

### Advanced Processing Example
```bash
python SanTOK.py
# Choose option 1: Text input
# Enter: "Large text with multiple sentences for advanced processing analysis."
# Choose output mode: 4 (DEBUG - show everything)
# See all advanced features in action:
# - Concurrent processing statistics
# - Hash operations and quality analysis
# - Compression statistics and ratios
# - Embedding generation and similarity analysis
# - Pattern recognition and anomaly detection
```

---

## Advanced Processing Features

### Automatic Background Processing

**All advanced features operate automatically during every tokenization**:

- **Multithreading**: Automatic concurrent processing using multiple CPU cores
- **Hash-Driven Embeddings**: Every token gets 128-dimensional embeddings
- **Text Analysis**: Automatic similarity analysis, pattern recognition, anomaly detection
- **Advanced Hashing**: 4 hash algorithms (FNV-1a, MurmurHash3, CityHash64, XXHash64)
- **Compression Analysis**: Automatic compression testing with 5 algorithms
- **Performance Monitoring**: Real-time performance metrics and optimization

### Viewing Advanced Features

**Debug Mode (Option 4)** shows all advanced processing:

```bash
python SanTOK.py
# Choose option 1: Text input
# Enter your text
# Choose output mode: 4 (DEBUG - show everything)
```

**Debug Mode Output Includes**:
- **Input Processing**: Text sanitization and normalization
- **Numerology Calculations**: Combined weighted sum + hash methodology
- **Tokenization Details**: All 9 methods with token counts
- **OOP Stream Details**: Token objects with embeddings and UIDs
- **Hash Operations**: Quality analysis of all 4 hash algorithms
- **Compression Statistics**: Compression ratios for all algorithms
- **Text Analysis**: Similarity groups, patterns, anomalies
- **Performance Metrics**: Processing time, memory usage, throughput

### Concurrent Processing Performance

**Automatic Multi-Core Utilization**:
- **Single-threaded**: ~10,000 tokens/second
- **4-core system**: ~40,000 tokens/second (4x speedup)
- **8-core system**: ~70,000 tokens/second (7x speedup)
- **Memory efficient**: Constant memory usage with streaming

### Hash-Driven Embeddings

**Every token automatically receives**:
- **Hash Embedding**: 128-dimensional stable embedding from 4 hash algorithms
- **Positional Embedding**: Position-aware representation using sinusoidal functions
- **Contextual Embedding**: Neighbor-aware embedding considering surrounding tokens
- **Numerology Embedding**: Embedding incorporating numerological properties
- **Combined Embedding**: Weighted fusion of all embedding types
- **Multi-Scale Embeddings**: Additional embeddings at 64, 128, and 256 dimensions

### Text Analysis Capabilities

**Automatic Analysis for Every Text**:

1. **Token Similarity Analysis**:
   - Finds groups of similar tokens using embedding similarity
   - Uses cosine similarity and Euclidean distance metrics
   - Configurable similarity threshold (default: 0.7)

2. **Pattern Recognition**:
   - Detects recurring token sequences (length 2-5)
   - Finds patterns with minimum frequency (default: 2)
   - Provides pattern positions and significance analysis

3. **Anomaly Detection**:
   - Statistical anomaly detection using z-score analysis
   - Configurable window size (default: 10 tokens)
   - Identifies tokens that don't fit local context patterns

### Advanced Hash Algorithms

**All 4 algorithms run for every token**:

| Algorithm | Speed | Quality | Use Case |
|-----------|-------|---------|----------|
| **FNV-1a** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | High-throughput applications |
| **MurmurHash3** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | High-quality hashing |
| **CityHash64** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 64-bit optimized systems |
| **XXHash64** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Speed-critical applications |

### Compression Analysis

**Automatic compression testing with 5 algorithms**:

1. **LZ77**: Sliding window compression (60-80% ratio)
2. **Run-Length Encoding**: Efficient for repetitive data (20-90% ratio)
3. **Huffman Coding**: Optimal for skewed frequencies (40-70% ratio)
4. **Dictionary-based**: Substring replacement (50-85% ratio)
5. **Adaptive**: Automatically chooses best algorithm (45-80% ratio)

---

## Interactive Mode

### Main Menu Options

#### 1. Text Input
**Purpose**: Process text directly entered by user
**Usage**:
- Choose option 1
- Enter your text when prompted
- Continue with output options

**Example**:
```
INPUT OPTIONS:
1. Text input
2. File input
3. Reconstruction test
9. Exit
Choose option (1-3, 9): 1
Enter text: Hello world! This is SanTOK.
```

#### 2. File Input
**Purpose**: Process text from various file formats
**Supported Formats**:
- **TXT**: Plain text files
- **CSV**: Comma-separated values
- **JSON**: JavaScript Object Notation
- **XML**: Extensible Markup Language
- **PDF**: Portable Document Format (basic text extraction)
- **DOCX**: Microsoft Word documents (basic text extraction)
- **XLSX**: Microsoft Excel files (basic text extraction)

**Usage**:
```
Choose option (1-3, 9): 2
Enter file path: /path/to/your/file.txt
Enter file type: txt
```

#### 3. Reconstruction Test
**Purpose**: Test lossless reconstruction capabilities
**Usage**:
```
Choose option (1-3, 9): 3
Enter text to test reconstruction: Hello world!
# View reconstruction results for all tokenization methods
```

#### 9. Exit
**Purpose**: Exit the program
**Usage**: Choose option 9 or type 'exit'

### Output Mode Selection

#### 1. DEV (Full Development Output)
**Purpose**: Detailed development information
**Shows**:
- Character counts
- Token previews for all methods
- Detailed tokenization results
- Backend calculations

#### 2. USER (Summary Output)
**Purpose**: Clean, user-friendly summary
**Shows**:
- Summary words (first 10)
- Character count
- Token counts per method
- Frontend digits
- Feature vector

#### 3. JSON (Structured Output)
**Purpose**: Machine-readable JSON format
**Shows**:
- Structured JSON with all data
- Word tokens and digits
- Feature vector
- Metadata

#### 4. DEBUG (Complete Internal Processing)
**Purpose**: Show everything happening inside the code
**Shows**:
- Input processing details
- Numerology calculations
- Tokenization method details
- Hash operations
- Compression statistics
- Embedding information
- Reconstruction validation
- Complete manifest

---

## Command Line Usage

### Basic Command
```bash
python SanTOK.py
```

### Interactive Flow
1. **Input Selection**: Choose text, file, or reconstruction test
2. **Text Entry**: Enter text or file path
3. **Configuration**: Set seed, embedding bit, output mode
4. **Output Selection**: Choose format and filename
5. **Export**: Save results to files

### Configuration Options

#### Seed Configuration
```
Enter integer seed (e.g., 12345): 12345
```
- **Purpose**: Controls UID generation for reproducibility
- **Range**: Any integer
- **Default**: 1

#### Embedding Bit
```
Use embedding bit? (0/1): 1
```
- **Purpose**: Controls embedding generation
- **0**: No embeddings
- **1**: Generate embeddings

#### Output Mode
```
Output mode? 1=DEV (full), 2=USER (summary), 3=JSON, 4=DEBUG (show everything):
```
- **1**: Development mode with full details
- **2**: User-friendly summary
- **3**: JSON format
- **4**: Debug mode with complete internal processing

---

## Output Formats

### JSON Format
**Structure**:
```json
{
  "file_info": {
    "input_text": "Hello world!",
    "tokenization_type": "word",
    "file_format": "json",
    "generated_by": "SanTOK Tokenizer"
  },
  "tokenization_results": {
    "tokens": [
      {
        "text": "Hello",
        "frontend": 6,
        "backend_scaled": 0.123456,
        "uid": 12345
      }
    ],
    "statistics": {
      "total_tokens": 2,
      "checksum": 8,
      "unique_tokens": 2
    }
  },
  "metadata": {
    "timestamp": "generated_by_santok",
    "version": "1.0",
    "structure": "organized_by_tokenization_type"
  }
}
```

### CSV Format
**Structure**:
```csv
text,tokenized_text,token,frontend
"Hello world!","Hello world!","Hello",6
"Hello world!","Hello world!","world",5
```

### TXT Format
**Structure**:
```
ESSENTIAL STRUCTURE:
1. TEXT: Hello world!

2. TOKENIZED TEXT: Hello world!

3. TOKENS (FRONTEND):
'Hello' -> 6
'world' -> 5

Tokenization Type: word
Tokens: ['Hello', 'world']
```

### XML Format
**Structure**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<tokenization>
  <file_info>
    <input_text>Hello world!</input_text>
    <tokenization_type>word</tokenization_type>
  </file_info>
  <tokens>
    <token text="Hello" frontend="6"/>
    <token text="world" frontend="5"/>
  </tokens>
</tokenization>
```

### Excel Format
**Structure**: CSV format saved as .csv files in excel directory
**Location**: `outputs/excel/[tokenization_type]/filename.csv`

### Parquet Format
**Structure**: JSON format saved as .json files in parquet directory
**Location**: `outputs/parquet/[tokenization_type]/filename.json`

### Avro Format
**Structure**: JSON format saved as .json files in avro directory
**Location**: `outputs/avro/[tokenization_type]/filename.json`

### Vector Format
**Structure**: Embedding vectors for machine learning
**Location**: `outputs/vectors/[tokenization_type]/filename_vectors.json`

---

## Advanced Features

### Reconstruction Testing

#### Purpose
Test the lossless reconstruction capabilities of different tokenization methods.

#### Usage
```
Choose option (1-3, 9): 3
Enter text to test reconstruction: Hello world!
```

#### Results Interpretation
- **[PERFECT]**: Perfect reconstruction (SPACE, CHAR, BPE)
- **[EXPECTED]**: Expected behavior for element extraction methods
- **Success Rate**: Percentage of perfect reconstructions

#### Example Output
```
[TEST] TESTING RECONSTRUCTION FOR: 'Hello world!'
============================================================
SPACE        | [PERFECT]    | Tokens:   2 | 'Hello world!'
WORD         | [EXPECTED]   | Tokens:   2 | 'Hello world'
CHAR         | [PERFECT]    | Tokens:  12 | 'Hello world!'
GRAMMAR      | [EXPECTED]   | Tokens:   3 | 'Helloworld!'
SUBWORD      | [EXPECTED]   | Tokens:   5 | 'Helloworld!'
BYTE         | [EXPECTED]   | Tokens:  33 | '721011081081113211911111410810033'
BPE          | [PERFECT]    | Tokens:   7 | 'Hello world!'
SYLLABLE     | [EXPECTED]   | Tokens:   5 | 'Helloworld!'
FREQUENCY    | [EXPECTED]   | Tokens:   2 | 'Helloworld'
```

### Debug Mode

#### Purpose
View complete internal processing of the SanTOK system.

#### Usage
```
Output mode? 1=DEV (full), 2=USER (summary), 3=JSON, 4=DEBUG (show everything): 4
```

#### Information Displayed
1. **Input Processing**: Original, sanitized, display text
2. **Numerology Calculations**: Weighted sum, hash, final digit
3. **Tokenization Methods**: Detailed breakdown for all 9 methods
4. **OOP Stream Details**: Length, checksum, frontend/backend digits
5. **Hash Operations**: FNV-1a, MurmurHash3, CityHash64, XXHash64
6. **Compression Statistics**: LZ77, RLE, Huffman compression
7. **Feature Vector**: Length factor, entropy index, balance index
8. **Manifest**: Complete validation manifest
9. **Reconstruction Validation**: Reconstruction test results

### Multi-Format Export

#### Purpose
Export results in multiple formats simultaneously.

#### Usage
```
OUTPUT FORMAT OPTIONS:
1. JSON
2. CSV
3. TXT
4. XML
5. Excel (XLSX)
6. Parquet
7. Avro
8. Vectorization (embeddings)
9. Multiple formats
10. Skip output
11. Exit
Choose output format (1-11): 9
```

#### Multiple Formats Selection
```
Choose formats (comma-separated, e.g., 1,2,3): 1,2,3
Enter output file name (without extension): my_analysis
```

---

## Examples and Tutorials

### Example 1: Basic Text Analysis

#### Scenario
Analyze the text "The quick brown fox jumps over the lazy dog."

#### Steps
1. **Run SanTOK**: `python SanTOK.py`
2. **Choose Text Input**: Option 1
3. **Enter Text**: "The quick brown fox jumps over the lazy dog."
4. **Set Seed**: 12345
5. **Enable Embeddings**: 1
6. **Choose Output Mode**: 2 (USER summary)
7. **Select Format**: JSON
8. **Enter Filename**: fox_analysis

#### Expected Results
- **Word Tokens**: 9 tokens
- **Character Tokens**: 44 tokens
- **Numerology Digits**: 1-9 range
- **Feature Vector**: Length factor, entropy index, balance index

### Example 2: File Processing

#### Scenario
Process a CSV file containing text data.

#### Steps
1. **Run SanTOK**: `python SanTOK.py`
2. **Choose File Input**: Option 2
3. **Enter File Path**: `/path/to/data.csv`
4. **Enter File Type**: csv
5. **Continue with normal processing**

#### File Structure
```csv
id,text
1,"Hello world!"
2,"This is a test"
3,"SanTOK tokenization"
```

### Example 3: Reconstruction Testing

#### Scenario
Test reconstruction capabilities with various text types.

#### Steps
1. **Run SanTOK**: `python SanTOK.py`
2. **Choose Reconstruction Test**: Option 3
3. **Enter Test Text**: "Hello world! 123 @#$"
4. **View Results**: Analyze reconstruction success rates

#### Expected Results
- **Perfect Reconstruction**: SPACE, CHAR, BPE methods
- **Element Extraction**: WORD, GRAMMAR, SUBWORD, SYLLABLE, FREQUENCY methods
- **Format Conversion**: BYTE method

### Example 4: Debug Analysis

#### Scenario
Understand internal processing for educational purposes.

#### Steps
1. **Run SanTOK**: `python SanTOK.py`
2. **Choose Text Input**: Option 1
3. **Enter Text**: "Hello world!"
4. **Choose Debug Mode**: Option 4
5. **View Complete Processing**: Analyze all internal steps

#### Information Gained
- **Numerology Calculations**: Step-by-step calculation process
- **Hash Operations**: Multiple hash algorithm results
- **Compression Statistics**: Compression ratios for different algorithms
- **Embedding Generation**: Hash-driven embedding creation
- **Reconstruction Validation**: Reconstruction test results

### Example 5: Multi-Format Export

#### Scenario
Export results in multiple formats for different use cases.

#### Steps
1. **Run SanTOK**: `python SanTOK.py`
2. **Process Text**: Follow normal processing steps
3. **Choose Multiple Formats**: Option 9
4. **Select Formats**: 1,2,3 (JSON, CSV, TXT)
5. **Enter Filename**: comprehensive_analysis
6. **View Results**: Check outputs directory

#### Output Structure
```
outputs/
├── json/
│   ├── space/comprehensive_analysis.json
│   ├── word/comprehensive_analysis.json
│   └── ...
├── csv/
│   ├── space/comprehensive_analysis.csv
│   ├── word/comprehensive_analysis.csv
│   └── ...
└── txt/
    ├── space/comprehensive_analysis.txt
    ├── word/comprehensive_analysis.txt
    └── ...
```

---

## Troubleshooting

### Common Issues

#### 1. Unicode Encoding Errors
**Problem**: `UnicodeEncodeError: 'charmap' codec can't encode character`
**Solution**: 
- Use ASCII-compatible characters
- Set environment variable: `PYTHONIOENCODING=utf-8`
- Use debug mode to identify problematic characters

#### 2. File Not Found Errors
**Problem**: `FileNotFoundError: [Errno 2] No such file or directory`
**Solution**:
- Ensure output directories exist
- Check file permissions
- Verify file path is correct

#### 3. Memory Issues
**Problem**: Out of memory errors with large texts
**Solution**:
- Process text in smaller chunks
- Increase system memory
- Use character tokenization for large texts
- Disable embeddings for memory-intensive operations

#### 4. Reconstruction Failures
**Problem**: Some tokenization methods don't reconstruct perfectly
**Solution**:
- This is expected behavior for element extraction methods
- Use SPACE, CHAR, or BPE for perfect reconstruction
- Check reconstruction test results for expected behavior

### Debug Mode Usage

#### Enable Debug Mode
```
Output mode? 1=DEV (full), 2=USER (summary), 3=JSON, 4=DEBUG (show everything): 4
```

#### Information Available
- **Complete Internal Processing**: See every step of the algorithm
- **Error Details**: Detailed error information
- **Performance Metrics**: Processing times and memory usage
- **Validation Results**: Checksum validation and reconstruction tests

### Performance Optimization

#### For Large Texts
- **Use Character Tokenization**: Fastest method for large texts
- **Disable Embeddings**: Reduces memory usage
- **Process in Chunks**: Break large texts into smaller pieces
- **Use Simple Output Formats**: TXT or CSV instead of JSON

#### For Memory Constraints
- **Reduce Embedding Dimensions**: Use smaller embedding dimensions
- **Disable Multi-Scale Embeddings**: Reduces memory usage
- **Use Streaming Processing**: Process text incrementally
- **Clear Intermediate Results**: Free memory between operations

---

## Best Practices

### Text Processing

#### Input Preparation
- **Clean Text**: Remove unnecessary characters before processing
- **Normalize Encoding**: Use UTF-8 encoding for best compatibility
- **Handle Special Characters**: Be aware of Unicode characters
- **Validate Input**: Check text length and content

#### Output Management
- **Organize Files**: Use descriptive filenames
- **Choose Appropriate Formats**: Select formats based on use case
- **Backup Results**: Keep copies of important analyses
- **Document Processing**: Record parameters and settings used

### Performance Optimization

#### Algorithm Selection
- **Character Tokenization**: Use for perfect reconstruction
- **Word Tokenization**: Use for word-level analysis
- **BPE Tokenization**: Use for advanced subword analysis
- **Syllable Tokenization**: Use for phonetic analysis

#### Configuration Optimization
- **Seed Selection**: Use consistent seeds for reproducible results
- **Embedding Usage**: Enable only when needed
- **Output Mode**: Use USER mode for clean results, DEBUG for analysis
- **Format Selection**: Choose formats based on downstream processing

### Quality Assurance

#### Validation
- **Reconstruction Testing**: Test reconstruction capabilities
- **Checksum Validation**: Verify data integrity
- **Cross-Validation**: Compare results across different methods
- **Error Checking**: Monitor for processing errors

#### Documentation
- **Record Parameters**: Document all settings used
- **Save Results**: Keep copies of all analyses
- **Version Control**: Track changes to input data
- **Quality Metrics**: Monitor success rates and accuracy

### Integration Guidelines

#### API Usage
- **Consistent Interfaces**: Use standard function signatures
- **Error Handling**: Implement proper error handling
- **Documentation**: Document all functions and parameters
- **Testing**: Test all functions thoroughly

#### Data Pipeline
- **Input Validation**: Validate all inputs
- **Processing Steps**: Document all processing steps
- **Output Validation**: Verify output quality
- **Error Recovery**: Implement error recovery mechanisms

---

*This user guide is maintained by the SanTOK development team. For questions or contributions, please refer to the project repository.*
