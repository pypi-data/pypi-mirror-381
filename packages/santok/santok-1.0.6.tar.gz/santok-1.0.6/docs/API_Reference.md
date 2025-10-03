# SanTOK API Reference

## Table of Contents
1. [Core Functions](#core-functions)
2. [Tokenization Functions](#tokenization-functions)
3. [Numerology Functions](#numerology-functions)
4. [Hash Functions](#hash-functions)
5. [Compression Functions](#compression-functions)
6. [Embedding Functions](#embedding-functions)
7. [Reconstruction Functions](#reconstruction-functions)
8. [OOP Classes](#oop-classes)
9. [Utility Functions](#utility-functions)
10. [Error Handling](#error-handling)

---

## Core Functions

### `all_tokenizations(text)`
**Purpose**: Generate all tokenization methods for input text
**Parameters**:
- `text` (str): Input text to tokenize
**Returns**: Dictionary with tokenization results for all methods
**Example**:
```python
result = all_tokenizations("Hello world!")
print(result["word"])  # [{"text": "Hello", "index": 0}, {"text": "world", "index": 6}]
print(result["char"])  # [{"text": "H", "index": 0}, {"text": "e", "index": 1}, ...]
```

### `main()`
**Purpose**: Main entry point for interactive CLI
**Parameters**: None
**Returns**: None
**Description**: Provides interactive menu system for text processing

---

## Tokenization Functions

### `tokenize_space(text)`
**Purpose**: Split text by whitespace characters
**Parameters**:
- `text` (str): Input text
**Returns**: List of token dictionaries with text and index
**Algorithm**: Identifies space boundaries and preserves tokens

### `tokenize_word(text)`
**Purpose**: Extract words, ignoring punctuation
**Parameters**:
- `text` (str): Input text
**Returns**: List of word token dictionaries
**Algorithm**: Identifies word boundaries using character classification

### `tokenize_char(text)`
**Purpose**: Split text into individual characters
**Parameters**:
- `text` (str): Input text
**Returns**: List of character token dictionaries
**Algorithm**: Iterates through each character

### `tokenize_grammar(text)`
**Purpose**: Extract grammar elements
**Parameters**:
- `text` (str): Input text
**Returns**: List of grammar token dictionaries
**Algorithm**: Identifies word characters vs. non-word characters

### `tokenize_subword(text, chunk_len=3)`
**Purpose**: Split words into subword units
**Parameters**:
- `text` (str): Input text
- `chunk_len` (int): Length of subword chunks (default: 3)
**Returns**: List of subword token dictionaries
**Algorithm**: Fixed-length chunking

### `tokenize_codepoint_digits(text)`
**Purpose**: Convert to ASCII byte representation
**Parameters**:
- `text` (str): Input text
**Returns**: List of byte token dictionaries
**Algorithm**: Converts each character to ASCII code

### `tokenize_bpe_santok(text, iterations=5)`
**Purpose**: Byte Pair Encoding for subword tokenization
**Parameters**:
- `text` (str): Input text
- `iterations` (int): Number of BPE iterations (default: 5)
**Returns**: List of BPE token dictionaries
**Algorithm**: Iteratively merges most frequent character pairs

### `tokenize_syllable(text)`
**Purpose**: Split words into syllables
**Parameters**:
- `text` (str): Input text
**Returns**: List of syllable token dictionaries
**Algorithm**: Vowel-consonant pattern recognition

### `tokenize_frequency(text, frequency_threshold=2)`
**Purpose**: Group tokens by frequency
**Parameters**:
- `text` (str): Input text
- `frequency_threshold` (int): Minimum frequency for marking (default: 2)
**Returns**: List of frequency token dictionaries
**Algorithm**: Counts token occurrences and marks high-frequency tokens

---

## Numerology Functions

### `numerology_sum(token_text)`
**Purpose**: Calculate numerology digit using combined method
**Parameters**:
- `token_text` (str): Text to analyze
**Returns**: Integer (1-9) representing numerology digit
**Algorithm**: Combined Weighted Sum + Advanced Hash method
**Formula**: `Final Digit = (Weighted_Digit × 9 + Hash_Digit) % 9 + 1`

### `numerology_sum_fast(token_text)`
**Purpose**: Fast version of numerology calculation
**Parameters**:
- `token_text` (str): Text to analyze
**Returns**: Integer (1-9) representing numerology digit
**Algorithm**: Optimized version of combined method

---

## Hash Functions

### `fnv1a_hash(data)`
**Purpose**: FNV-1a hash algorithm
**Parameters**:
- `data` (str): Data to hash
**Returns**: 64-bit hash value
**Algorithm**: FNV offset basis with prime multiplication

### `murmur_hash3_32(data, seed=0)`
**Purpose**: MurmurHash3 32-bit hash
**Parameters**:
- `data` (str): Data to hash
- `seed` (int): Hash seed (default: 0)
**Returns**: 32-bit hash value
**Algorithm**: High-quality hash with good avalanche effect

### `city_hash_64(data)`
**Purpose**: CityHash64 algorithm
**Parameters**:
- `data` (str): Data to hash
**Returns**: 64-bit hash value
**Algorithm**: Google's high-performance hash

### `xxhash_64(data, seed=0)`
**Purpose**: XXHash64 algorithm
**Parameters**:
- `data` (str): Data to hash
- `seed` (int): Hash seed (default: 0)
**Returns**: 64-bit hash value
**Algorithm**: Extremely fast hash algorithm

### `advanced_hash_combination(token_text)`
**Purpose**: Generate advanced hash using multiple algorithms
**Parameters**:
- `token_text` (str): Text to hash
**Returns**: 64-bit hash value
**Algorithm**: Combines FNV-1a, MurmurHash3, CityHash64, XXHash64

### `analyze_hash_quality(test_tokens)`
**Purpose**: Analyze hash algorithm quality
**Parameters**:
- `test_tokens` (list): List of test tokens
**Returns**: Dictionary with quality metrics
**Metrics**: Collision rate, distribution uniformity, avalanche effect

### `get_hash_statistics(token_text)`
**Purpose**: Get detailed hash statistics for a token
**Parameters**:
- `token_text` (str): Text to analyze
**Returns**: Dictionary with hash statistics
**Statistics**: Individual hash values, combined hash, quality metrics

---

## Compression Functions

### `lz77_compress(data, window_size=4096, lookahead_buffer=18)`
**Purpose**: LZ77 compression algorithm
**Parameters**:
- `data` (str): Data to compress
- `window_size` (int): Sliding window size (default: 4096)
- `lookahead_buffer` (int): Lookahead buffer size (default: 18)
**Returns**: Compressed data string
**Algorithm**: Sliding window compression with references

### `lz77_decompress(compressed_data)`
**Purpose**: LZ77 decompression
**Parameters**:
- `compressed_data` (str): Compressed data
**Returns**: Decompressed data string
**Algorithm**: Reconstructs original data from references

### `run_length_encode(data)`
**Purpose**: Run-length encoding compression
**Parameters**:
- `data` (str): Data to compress
**Returns**: Compressed data string
**Algorithm**: Counts consecutive identical characters

### `run_length_decode(compressed_data)`
**Purpose**: Run-length decoding
**Parameters**:
- `compressed_data` (str): Compressed data
**Returns**: Decompressed data string
**Algorithm**: Reconstructs original data from counts

### `huffman_compress(data)`
**Purpose**: Huffman coding compression
**Parameters**:
- `data` (str): Data to compress
**Returns**: Compressed data string
**Algorithm**: Optimal prefix coding based on frequency

### `huffman_decompress(compressed_data)`
**Purpose**: Huffman decoding
**Parameters**:
- `compressed_data` (str): Compressed data
**Returns**: Decompressed data string
**Algorithm**: Reconstructs original data using Huffman tree

### `dictionary_compress(data)`
**Purpose**: Dictionary compression
**Parameters**:
- `data` (str): Data to compress
**Returns**: Tuple of (compressed_data, dictionary)
**Algorithm**: Replaces repeated patterns with references

### `dictionary_decompress(compressed_data, dictionary)`
**Purpose**: Dictionary decompression
**Parameters**:
- `compressed_data` (str): Compressed data
- `dictionary` (dict): Compression dictionary
**Returns**: Decompressed data string
**Algorithm**: Reconstructs original data using dictionary

### `adaptive_compress(data)`
**Purpose**: Adaptive compression algorithm selection
**Parameters**:
- `data` (str): Data to compress
**Returns**: Tuple of (compressed_data, algorithm_name)
**Algorithm**: Analyzes data and selects optimal compression method

### `adaptive_decompress(compressed_data, algorithm)`
**Purpose**: Adaptive decompression
**Parameters**:
- `compressed_data` (str): Compressed data
- `algorithm` (str): Compression algorithm used
**Returns**: Decompressed data string
**Algorithm**: Uses appropriate decompression method

### `calculate_compression_ratio(original_data, compressed_data)`
**Purpose**: Calculate compression ratio
**Parameters**:
- `original_data` (str): Original data
- `compressed_data` (str): Compressed data
**Returns**: Compression ratio percentage
**Formula**: `(original_size - compressed_size) / original_size * 100`

---

## Embedding Functions

### `generate_hash_embedding(token_text, embedding_dim=128, hash_seed=0)`
**Purpose**: Generate hash-driven embedding
**Parameters**:
- `token_text` (str): Text to embed
- `embedding_dim` (int): Embedding dimension (default: 128)
- `hash_seed` (int): Hash seed for reproducibility (default: 0)
**Returns**: List of float values representing embedding
**Algorithm**: Uses multiple hash algorithms to generate stable embeddings

### `generate_positional_embedding(position, embedding_dim=128)`
**Purpose**: Generate positional embedding
**Parameters**:
- `position` (int): Token position
- `embedding_dim` (int): Embedding dimension (default: 128)
**Returns**: List of float values representing positional embedding
**Algorithm**: Sinusoidal positional encoding

### `generate_numerology_embedding(token_text, frontend_digit, backend_scaled, embedding_dim=128)`
**Purpose**: Generate numerology-influenced embedding
**Parameters**:
- `token_text` (str): Text to embed
- `frontend_digit` (int): Numerology frontend digit
- `backend_scaled` (float): Scaled backend number
- `embedding_dim` (int): Embedding dimension (default: 128)
**Returns**: List of float values representing numerology embedding
**Algorithm**: Incorporates numerology calculations into embedding

### `generate_contextual_embedding(token_text, prev_text, next_text, embedding_dim=128)`
**Purpose**: Generate contextual embedding
**Parameters**:
- `token_text` (str): Current token text
- `prev_text` (str): Previous token text
- `next_text` (str): Next token text
- `embedding_dim` (int): Embedding dimension (default: 128)
**Returns**: List of float values representing contextual embedding
**Algorithm**: Considers surrounding context for embedding generation

### `combine_embeddings(embeddings, weights)`
**Purpose**: Combine multiple embeddings with weights
**Parameters**:
- `embeddings` (list): List of embedding vectors
- `weights` (list): List of weights for each embedding
**Returns**: Combined embedding vector
**Algorithm**: Weighted combination of embeddings

### `generate_multi_scale_embedding(token_text, scales)`
**Purpose**: Generate embeddings at multiple scales
**Parameters**:
- `token_text` (str): Text to embed
- `scales` (list): List of embedding dimensions
**Returns**: Dictionary with embeddings at each scale
**Algorithm**: Generates embeddings at different resolutions

### `calculate_embedding_similarity(embedding1, embedding2)`
**Purpose**: Calculate cosine similarity between embeddings
**Parameters**:
- `embedding1` (list): First embedding vector
- `embedding2` (list): Second embedding vector
**Returns**: Cosine similarity score (-1 to 1)
**Algorithm**: Cosine similarity calculation

### `calculate_embedding_distance(embedding1, embedding2)`
**Purpose**: Calculate Euclidean distance between embeddings
**Parameters**:
- `embedding1` (list): First embedding vector
- `embedding2` (list): Second embedding vector
**Returns**: Euclidean distance
**Algorithm**: Euclidean distance calculation

### `normalize_embedding(embedding)`
**Purpose**: Normalize embedding vector
**Parameters**:
- `embedding` (list): Embedding vector to normalize
**Returns**: Normalized embedding vector
**Algorithm**: L2 normalization

### `embedding_to_hash_signature(embedding)`
**Purpose**: Convert embedding to hash signature
**Parameters**:
- `embedding` (list): Embedding vector
**Returns**: Hash signature string
**Algorithm**: Converts embedding to compact hash representation

---

## Reconstruction Functions

### `reconstruct_space(tokens)`
**Purpose**: Reconstruct text from space tokenization
**Parameters**:
- `tokens` (list): List of token dictionaries
**Returns**: Reconstructed text string
**Algorithm**: Joins tokens with spaces

### `reconstruct_word(tokens)`
**Purpose**: Reconstruct text from word tokenization
**Parameters**:
- `tokens` (list): List of token dictionaries
**Returns**: Reconstructed text string
**Algorithm**: Joins words with spaces (loses punctuation)

### `reconstruct_char(tokens)`
**Purpose**: Reconstruct text from character tokenization
**Parameters**:
- `tokens` (list): List of token dictionaries
**Returns**: Reconstructed text string
**Algorithm**: Joins characters directly

### `reconstruct_grammar(tokens)`
**Purpose**: Reconstruct text from grammar tokenization
**Parameters**:
- `tokens` (list): List of token dictionaries
**Returns**: Reconstructed text string
**Algorithm**: Joins grammar tokens directly

### `reconstruct_subword(tokens)`
**Purpose**: Reconstruct text from subword tokenization
**Parameters**:
- `tokens` (list): List of token dictionaries
**Returns**: Reconstructed text string
**Algorithm**: Joins subwords directly

### `reconstruct_codepoint_digits(tokens)`
**Purpose**: Reconstruct text from byte tokenization
**Parameters**:
- `tokens` (list): List of token dictionaries
**Returns**: Reconstructed text string
**Algorithm**: Converts ASCII codes back to characters

### `reconstruct_bpe(tokens)`
**Purpose**: Reconstruct text from BPE tokenization
**Parameters**:
- `tokens` (list): List of token dictionaries
**Returns**: Reconstructed text string
**Algorithm**: Joins BPE tokens directly

### `reconstruct_syllable(tokens)`
**Purpose**: Reconstruct text from syllable tokenization
**Parameters**:
- `tokens` (list): List of token dictionaries
**Returns**: Reconstructed text string
**Algorithm**: Joins syllables directly

### `reconstruct_frequency(tokens)`
**Purpose**: Reconstruct text from frequency tokenization
**Parameters**:
- `tokens` (list): List of token dictionaries
**Returns**: Reconstructed text string
**Algorithm**: Joins tokens directly (frequency info as metadata)

### `reconstruct_from_tokens(tokens, tokenization_type)`
**Purpose**: Universal reconstruction function
**Parameters**:
- `tokens` (list): List of token dictionaries
- `tokenization_type` (str): Type of tokenization used
**Returns**: Reconstructed text string
**Algorithm**: Calls appropriate reconstruction method based on type

### `validate_reconstruction(original_text, reconstructed_text, tokenization_type)`
**Purpose**: Validate reconstruction accuracy
**Parameters**:
- `original_text` (str): Original text
- `reconstructed_text` (str): Reconstructed text
- `tokenization_type` (str): Type of tokenization used
**Returns**: Tuple of (is_perfect, message)
**Algorithm**: Compares original and reconstructed text

### `test_all_reconstructions(text)`
**Purpose**: Test reconstruction for all tokenization methods
**Parameters**:
- `text` (str): Text to test
**Returns**: Dictionary with reconstruction results
**Algorithm**: Tests all tokenization methods and validates reconstruction

---

## OOP Classes

### `SanTOKToken`
**Purpose**: Individual token representation with full metadata
**Attributes**:
- `text` (str): Token text content
- `stream` (str): Stream identifier
- `index` (int): Position in original text
- `uid` (int): Unique identifier
- `prev_uid` (int): Previous token UID
- `next_uid` (int): Next token UID
- `content_id` (int): Content identifier
- `global_id` (int): Global identifier
- `frontend` (int): Numerology digit (1-9)
- `backend_huge` (int): Large backend number
- `backend_scaled` (float): Scaled backend number
- `embedding_dim` (int): Embedding dimension
- `hash_embedding` (list): Hash-driven embedding vector
- `positional_embedding` (list): Positional embedding vector
- `numerology_embedding` (list): Numerology embedding vector
- `contextual_embedding` (list): Contextual embedding vector
- `combined_embedding` (list): Combined embedding vector
- `multi_scale_embeddings` (dict): Multi-scale embeddings

**Methods**:
- `to_row()`: Convert token to dictionary representation
- `get_embedding_summary()`: Get embedding summary
- `get_numerology_info()`: Get numerology information

### `SanTOKTokenizer`
**Purpose**: Main tokenization engine
**Parameters**:
- `seed` (int): Random seed for UID generation
- `embedding_bit` (bool): Whether to use embedding bit

**Methods**:
- `build(text)`: Generate token streams for all methods
- `validate(streams)`: Validate token streams
- `checksum_digits()`: Calculate checksum for validation
- `generate_uid()`: Generate unique identifier
- `process_text(text)`: Process text through all tokenization methods

### `TokenStream`
**Purpose**: Collection of tokens with metadata
**Attributes**:
- `tokens` (list): List of SanTOKToken objects
- `stream_name` (str): Name of the stream
- `checksum` (int): Stream checksum

**Methods**:
- `length()`: Get number of tokens
- `checksum_digits()`: Calculate stream checksum
- `add_token(token)`: Add token to stream
- `get_tokens_by_type(type)`: Get tokens by type
- `validate()`: Validate stream integrity

---

## Utility Functions

### `_is_space(char)`
**Purpose**: Check if character is whitespace
**Parameters**:
- `char` (str): Character to check
**Returns**: Boolean indicating if character is whitespace

### `_is_word_char(char)`
**Purpose**: Check if character is word character
**Parameters**:
- `char` (str): Character to check
**Returns**: Boolean indicating if character is word character

### `_len(text)`
**Purpose**: Get length of text
**Parameters**:
- `text` (str): Text to measure
**Returns**: Integer length

### `_truncate_list(lst, max_len)`
**Purpose**: Truncate list to maximum length
**Parameters**:
- `lst` (list): List to truncate
- `max_len` (int): Maximum length
**Returns**: Truncated list

### `_count_chars(text)`
**Purpose**: Count characters in text
**Parameters**:
- `text` (str): Text to count
**Returns**: Integer character count

### `digits_only(numbers, max_digits)`
**Purpose**: Extract digits from numbers
**Parameters**:
- `numbers` (list): List of numbers
- `max_digits` (int): Maximum number of digits to extract
**Returns**: List of digits

### `_content_id(text)`
**Purpose**: Generate content ID for text
**Parameters**:
- `text` (str): Text to process
**Returns**: Integer content ID

### `_ensure_dir(dir_path)`
**Purpose**: Create directory structure
**Parameters**:
- `dir_path` (str): Directory path to create
**Returns**: Boolean indicating success

### `_parse_input_file(file_path, file_type)`
**Purpose**: Parse input file based on type
**Parameters**:
- `file_path` (str): Path to input file
- `file_type` (str): Type of file (txt, csv, json, xml, pdf, docx, xlsx)
**Returns**: Parsed text content

### `_export_output(data, output_path, output_format)`
**Purpose**: Export data in specified format
**Parameters**:
- `data`: Data to export
- `output_path` (str): Path for output file
- `output_format` (str): Format for export (json, csv, txt, xml)
**Returns**: Boolean indicating success

---

## Error Handling

### Common Exceptions
- `ValueError`: Invalid input parameters
- `FileNotFoundError`: File not found
- `UnicodeEncodeError`: Unicode encoding issues
- `MemoryError`: Insufficient memory
- `IndexError`: Index out of range

### Error Recovery
- Automatic fallback to alternative methods
- Graceful degradation of features
- Comprehensive error logging
- User-friendly error messages

### Debugging Support
- Debug mode for complete internal visibility
- Detailed error reporting
- Performance monitoring
- Memory usage tracking

---

*This API reference is maintained by the SanTOK development team. For questions or contributions, please refer to the project repository.*
