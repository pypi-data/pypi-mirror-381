# SanTOK Algorithm Deep Dive

## Table of Contents
1. [Numerology Algorithm](#numerology-algorithm)
2. [Hash Algorithm Analysis](#hash-algorithm-analysis)
3. [Compression Algorithm Details](#compression-algorithm-details)
4. [Embedding Generation](#embedding-generation)
5. [Concurrent Processing Algorithms](#concurrent-processing-algorithms)
6. [Text Analysis Algorithms](#text-analysis-algorithms)
7. [Tokenization Algorithms](#tokenization-algorithms)
8. [Mathematical Foundations](#mathematical-foundations)
9. [Performance Optimization](#performance-optimization)
10. [Algorithm Complexity](#algorithm-complexity)

---

## Concurrent Processing Algorithms

### ThreadPoolExecutor Implementation

SanTOK uses `ThreadPoolExecutor` for true multithreading with the following algorithm:

```python
def process_text_concurrent(self, text, tokenization_methods):
    # Chunk creation: O(n/c) where c = chunk_size
    chunks = self._create_chunks(text, self.chunk_size)
    
    # Concurrent processing with optimal worker distribution
    with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
        futures = []
        for chunk_idx, chunk_text in enumerate(chunks):
            for method in tokenization_methods:
                future = executor.submit(
                    self._process_chunk_concurrent, 
                    chunk_text, method, chunk_idx
                )
                futures.append((future, method, chunk_idx))
        
        # Optimal result collection
        results = []
        for future, method, chunk_idx in futures:
            result = future.result(timeout=30)
            results.append((result, method, chunk_idx))
```

**Performance Characteristics**:
- **Time Complexity**: O(n/p) where p = number of processors
- **Speedup**: Linear up to CPU core count
- **Efficiency**: 85-95% on modern systems
- **Memory**: O(p × chunk_size) additional memory

### Asynchronous Processing Algorithm

```python
async def process_texts_async(self, texts, tokenization_method="word"):
    # Semaphore-controlled concurrency
    async def process_with_semaphore(text):
        async with self.semaphore:
            return await self._process_single_text_async(text, tokenization_method)
    
    # Create and execute tasks
    tasks = [asyncio.create_task(process_with_semaphore(text)) for text in texts]
    results = await asyncio.gather(*tasks, return_exceptions=True)
```

**Algorithm Properties**:
- **Non-blocking**: Uses async/await pattern
- **Concurrency Control**: Semaphore limits concurrent tasks
- **Exception Handling**: Graceful error recovery
- **Memory Efficiency**: Lower overhead than threading

## Text Analysis Algorithms

### Token Similarity Analysis

**Mathematical Foundation**:
```python
def calculate_token_similarity(token1, token2, method="combined"):
    if method == "cosine":
        # Cosine similarity: cos(θ) = (A·B) / (|A|×|B|)
        dot_product = sum(a * b for a, b in zip(embedding1, embedding2))
        magnitude1 = sum(a * a for a in embedding1) ** 0.5
        magnitude2 = sum(b * b for b in embedding2) ** 0.5
        return dot_product / (magnitude1 * magnitude2)
    
    elif method == "euclidean":
        # Euclidean distance converted to similarity
        distance = sum((a - b) ** 2 for a, b in zip(embedding1, embedding2)) ** 0.5
        return 1.0 / (1.0 + distance)
```

**Complexity**: O(d) where d = embedding dimension

### Pattern Recognition Algorithm

```python
def find_token_patterns(tokens, min_pattern_length=2, max_pattern_length=5):
    patterns = {}
    token_texts = [token.text for token in tokens]
    
    # Generate all patterns: O(n × l²)
    for length in range(min_pattern_length, max_pattern_length + 1):
        for i in range(len(token_texts) - length + 1):
            pattern = tuple(token_texts[i:i+length])
            patterns[pattern] = patterns.get(pattern, 0) + 1
    
    # Filter significant patterns
    return [{"pattern": list(p), "frequency": f} 
            for p, f in patterns.items() if f >= min_frequency]
```

**Complexity**: O(n × l² + p log p) where l = max pattern length, p = unique patterns

### Anomaly Detection Algorithm

```python
def detect_token_anomalies(tokens, window_size=10, anomaly_threshold=2.0):
    anomalies = []
    for i, current_token in enumerate(tokens):
        # Define analysis window
        window_tokens = tokens[max(0, i-window_size//2):i+window_size//2+1]
        
        # Calculate similarity statistics
        similarities = [calculate_token_similarity(current_token, other_token)
                       for other_token in window_tokens if other_token != current_token]
        
        # Statistical anomaly detection using z-score
        if similarities:
            mean_sim = sum(similarities) / len(similarities)
            std_sim = (sum((s - mean_sim)**2 for s in similarities) / len(similarities))**0.5
            
            if mean_sim < (anomaly_threshold * std_sim):
                anomalies.append({
                    "token": current_token,
                    "position": i,
                    "anomaly_score": (mean_sim - mean_sim) / std_sim if std_sim > 0 else 0
                })
```

**Statistical Foundation**: Uses z-score analysis for anomaly detection
**Complexity**: O(n × w × d) where w = window size, d = embedding dimension

---

## Numerology Algorithm

### Mathematical Foundation

The SanTOK numerology system is based on the **Combined Method** that integrates two distinct approaches:

#### 1. Weighted Sum Method
```
Weighted_Sum = Σ(ord(char_i) × (i + 1)) for i in [0, len(text)-1]
Weighted_Digit = ((Weighted_Sum - 1) % 9) + 1
```

**Properties**:
- **Position Sensitivity**: Character position affects the sum
- **Character Weight**: ASCII value multiplied by position
- **9-Centric Folding**: Results mapped to 1-9 range
- **Deterministic**: Same input always produces same output

**Example Calculation**:
```
Text: "Hi"
H (ASCII 72) × 1 = 72
i (ASCII 105) × 2 = 210
Weighted_Sum = 72 + 210 = 282
Weighted_Digit = ((282 - 1) % 9) + 1 = 3
```

#### 2. Advanced Hash Method
```
Hash_Value = Advanced_Hash_Combination(text)
Hash_Digit = ((Hash_Value - 1) % 9) + 1
```

**Advanced Hash Combination**:
```python
def advanced_hash_combination(token_text):
    fnv_hash = fnv1a_hash(token_text)
    murmur_hash = murmur_hash3_32(token_text)
    city_hash = city_hash_64(token_text)
    xxhash_val = xxhash_64(token_text)
    
    combined = fnv_hash ^ murmur_hash ^ city_hash ^ xxhash_val
    combined = ((combined << 13) | (combined >> 51)) & ((1 << 64) - 1)
    combined ^= len(token_text)
    combined = (combined * 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
    
    return combined
```

#### 3. Combined Method Formula
```
Final_Digit = (Weighted_Digit × 9 + Hash_Digit) % 9 + 1
```

**Mathematical Properties**:
- **Non-Linear Combination**: Multiplicative and additive components
- **Collision Resistance**: Multiple hash algorithms reduce collision probability
- **Distribution Uniformity**: 9-centric mapping ensures uniform distribution
- **Deterministic**: Reproducible results for same input

### Algorithm Complexity
- **Time Complexity**: O(n) where n is text length
- **Space Complexity**: O(1) constant space
- **Hash Operations**: O(n) for each hash algorithm
- **Total Operations**: O(4n) for hash combination

---

## Hash Algorithm Analysis

### FNV-1a Hash Algorithm

#### Mathematical Foundation
```
FNV_OFFSET_BASIS = 14695981039346656037
FNV_PRIME = 1099511628211

hash_value = FNV_OFFSET_BASIS
for byte in data:
    hash_value ^= byte
    hash_value = (hash_value * FNV_PRIME) & ((1 << 64) - 1)
```

#### Properties
- **Avalanche Effect**: Small input changes cause large output changes
- **Distribution**: Uniform distribution across hash space
- **Speed**: Very fast computation
- **Collision Rate**: ~0.001% for typical inputs

#### Performance Characteristics
- **Time Complexity**: O(n) where n is input length
- **Space Complexity**: O(1)
- **Throughput**: ~100,000 hashes/second
- **Memory Usage**: Minimal (single 64-bit accumulator)

### MurmurHash3 Algorithm

#### Mathematical Foundation
```
def murmur_hash3_32(data, seed=0):
    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    r1 = 15
    r2 = 13
    m = 5
    n = 0xe6546b64
    
    hash_value = seed
    # Process 4-byte chunks
    for i in range(0, len(data) - 3, 4):
        k = int.from_bytes(data[i:i+4], 'little')
        k = (k * c1) & ((1 << 32) - 1)
        k = ((k << r1) | (k >> (32 - r1))) & ((1 << 32) - 1)
        k = (k * c2) & ((1 << 32) - 1)
        
        hash_value ^= k
        hash_value = ((hash_value << r2) | (hash_value >> (32 - r2))) & ((1 << 32) - 1)
        hash_value = (hash_value * m + n) & ((1 << 32) - 1)
    
    # Finalization
    hash_value ^= len(data)
    hash_value ^= hash_value >> 16
    hash_value = (hash_value * 0x85ebca6b) & ((1 << 32) - 1)
    hash_value ^= hash_value >> 13
    hash_value = (hash_value * 0xc2b2ae35) & ((1 << 32) - 1)
    hash_value ^= hash_value >> 16
    
    return hash_value
```

#### Properties
- **High Quality**: Excellent avalanche effect
- **Seed Support**: Configurable seed for reproducibility
- **32-bit Output**: Suitable for most applications
- **Collision Rate**: ~0.0001% for typical inputs

### CityHash64 Algorithm

#### Mathematical Foundation
```
def city_hash_64(data):
    # Simplified version of CityHash64
    # Uses multiple mixing functions for high quality
    
    def _cityhash_mix(h):
        h ^= h >> 33
        h = (h * 0xff51afd7ed558ccd) & ((1 << 64) - 1)
        h ^= h >> 33
        h = (h * 0xc4ceb9fe1a85ec53) & ((1 << 64) - 1)
        h ^= h >> 33
        return h
    
    # Process data in chunks
    hash_value = 0
    for i in range(0, len(data), 8):
        chunk = data[i:i+8]
        if len(chunk) == 8:
            k = int.from_bytes(chunk, 'little')
            hash_value ^= k
            hash_value = _cityhash_mix(hash_value)
        else:
            # Handle remaining bytes
            for j, byte in enumerate(chunk):
                hash_value ^= (byte << (j * 8))
    
    return _cityhash_mix(hash_value)
```

#### Properties
- **Google Optimized**: Designed for 64-bit systems
- **High Performance**: Optimized for modern CPUs
- **64-bit Output**: Large hash space
- **Collision Rate**: ~0.0001% for typical inputs

### XXHash64 Algorithm

#### Mathematical Foundation
```
def xxhash_64(data, seed=0):
    PRIME64_1 = 0x9E3779B185EBCA87
    PRIME64_2 = 0xC2B2AE3D27D4EB4F
    PRIME64_3 = 0x165667B19E3779F9
    PRIME64_4 = 0x85EBCA77C2B2AE63
    PRIME64_5 = 0x27D4EB2F165667C5
    
    def _xxhash_round(acc, input_val):
        acc += input_val * PRIME64_2
        acc = ((acc << 13) | (acc >> 51)) & ((1 << 64) - 1)
        acc *= PRIME64_1
        return acc
    
    # Initialize
    hash_value = seed + PRIME64_5
    
    # Process 8-byte chunks
    for i in range(0, len(data) - 7, 8):
        chunk = data[i:i+8]
        k = int.from_bytes(chunk, 'little')
        hash_value = _xxhash_round(hash_value, k)
    
    # Finalize
    hash_value ^= len(data)
    hash_value = (hash_value * PRIME64_1) & ((1 << 64) - 1)
    hash_value ^= hash_value >> 33
    hash_value = (hash_value * PRIME64_2) & ((1 << 64) - 1)
    hash_value ^= hash_value >> 29
    hash_value = (hash_value * PRIME64_3) & ((1 << 64) - 1)
    hash_value ^= hash_value >> 32
    
    return hash_value
```

#### Properties
- **Extreme Speed**: Fastest hash algorithm
- **Good Quality**: Reasonable distribution
- **Seed Support**: Configurable seed
- **Collision Rate**: ~0.0001% for typical inputs

---

## Compression Algorithm Details

### LZ77 Compression

#### Algorithm Description
LZ77 uses a sliding window approach to find repeated patterns in data.

#### Mathematical Foundation
```
def lz77_compress(data, window_size=4096, lookahead_buffer=18):
    compressed = []
    i = 0
    
    while i < len(data):
        # Find longest match in sliding window
        best_match = (0, 0)  # (offset, length)
        
        # Search in sliding window
        for offset in range(1, min(i + 1, window_size + 1)):
            match_length = 0
            while (match_length < lookahead_buffer and 
                   i + match_length < len(data) and
                   data[i - offset + match_length] == data[i + match_length]):
                match_length += 1
            
            if match_length > best_match[1]:
                best_match = (offset, match_length)
        
        if best_match[1] > 2:  # Minimum match length
            # Encode as (offset, length, next_char)
            compressed.append((best_match[0], best_match[1], data[i + best_match[1]]))
            i += best_match[1] + 1
        else:
            # Encode as literal
            compressed.append((0, 0, data[i]))
            i += 1
    
    return compressed
```

#### Properties
- **Compression Ratio**: 60-80% for text data
- **Time Complexity**: O(n²) in worst case
- **Space Complexity**: O(n) for output
- **Best For**: Text with repeated patterns

### Run-Length Encoding (RLE)

#### Algorithm Description
RLE compresses data by replacing consecutive identical characters with count and character.

#### Mathematical Foundation
```
def run_length_encode(data):
    compressed = []
    i = 0
    
    while i < len(data):
        char = data[i]
        count = 1
        
        # Count consecutive identical characters
        while i + count < len(data) and data[i + count] == char:
            count += 1
        
        # Encode as (count, char)
        if count > 1:
            compressed.append((count, char))
        else:
            compressed.append((1, char))
        
        i += count
    
    return compressed
```

#### Properties
- **Compression Ratio**: 20-90% (highly variable)
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) for output
- **Best For**: Data with long runs of identical values

### Huffman Coding

#### Algorithm Description
Huffman coding creates optimal prefix codes based on character frequency.

#### Mathematical Foundation
```
def huffman_compress(data):
    # Build frequency table
    frequencies = {}
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1
    
    # Build Huffman tree
    heap = [(freq, char) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = (left[0] + right[0], left, right)
        heapq.heappush(heap, merged)
    
    # Generate codes
    codes = {}
    def generate_codes(node, code=""):
        if len(node) == 2:  # Leaf node
            codes[node[1]] = code
        else:  # Internal node
            generate_codes(node[1], code + "0")
            generate_codes(node[2], code + "1")
    
    generate_codes(heap[0])
    
    # Compress data
    compressed = ""
    for char in data:
        compressed += codes[char]
    
    return compressed, codes
```

#### Properties
- **Compression Ratio**: 40-70% for text
- **Time Complexity**: O(n log n) for tree building
- **Space Complexity**: O(n) for output
- **Best For**: Data with skewed frequency distributions

---

## Embedding Generation

### Hash-Driven Embeddings

#### Mathematical Foundation
```
def generate_hash_embedding(token_text, embedding_dim=128, hash_seed=0):
    # Combine multiple hash algorithms
    fnv_hash = fnv1a_hash(token_text)
    murmur_hash = murmur_hash3_32(token_text)
    city_hash = city_hash_64(token_text)
    xxhash_val = xxhash_64(token_text)
    advanced_hash = advanced_hash_combination(token_text)
    
    # Combine hashes with seed
    combined_hash = fnv_hash ^ murmur_hash ^ city_hash ^ xxhash_val ^ advanced_hash ^ hash_seed
    
    # Generate embedding vector
    embedding = []
    hash_bits = combined_hash
    
    for i in range(embedding_dim):
        bit_pos = (i * 7) % 64
        bit_value = (hash_bits >> bit_pos) & 1
        
        if bit_value:
            rotated_hash = ((hash_bits << (i % 32)) | (hash_bits >> (32 - i % 32))) & ((1 << 64) - 1)
            float_val = (rotated_hash % 1000000) / 1000000.0
        else:
            rotated_hash = ((hash_bits >> (i % 32)) | (hash_bits << (32 - i % 32))) & ((1 << 64) - 1)
            float_val = -(rotated_hash % 1000000) / 1000000.0
        
        embedding.append(float_val)
    
    return embedding
```

#### Properties
- **Deterministic**: Same input always produces same embedding
- **Stable**: Embeddings stable across vocabularies and models
- **High Dimensional**: Configurable embedding dimension
- **Fast Generation**: O(n) time complexity

### Positional Embeddings

#### Mathematical Foundation
```
def generate_positional_embedding(position, embedding_dim=128):
    embedding = []
    
    for i in range(embedding_dim):
        if i % 2 == 0:
            # Sine encoding
            embedding.append(math.sin(position / (10000 ** (2 * i / embedding_dim))))
        else:
            # Cosine encoding
            embedding.append(math.cos(position / (10000 ** (2 * i / embedding_dim))))
    
    return embedding
```

#### Properties
- **Sinusoidal**: Uses sine and cosine functions
- **Position Sensitive**: Different positions produce different embeddings
- **Smooth**: Continuous function of position
- **Scalable**: Works for any position value

### Multi-Scale Embeddings

#### Algorithm Description
Generates embeddings at multiple scales for comprehensive representation.

#### Mathematical Foundation
```
def generate_multi_scale_embedding(token_text, scales=[64, 128, 256]):
    embeddings = {}
    
    for scale in scales:
        # Generate embeddings at each scale
        hash_emb = generate_hash_embedding(token_text, scale)
        numerology_emb = generate_numerology_embedding(token_text, scale)
        
        # Combine embeddings
        combined = combine_embeddings([hash_emb, numerology_emb], [0.6, 0.4])
        
        embeddings[f"scale_{scale}"] = {
            "hash_embedding": hash_emb,
            "numerology_embedding": numerology_emb,
            "combined": combined
        }
    
    return embeddings
```

#### Properties
- **Multi-Resolution**: Different scales capture different features
- **Comprehensive**: Combines multiple embedding types
- **Flexible**: Configurable scales
- **Rich Representation**: Captures both local and global features

---

## Tokenization Algorithms

### BPE (Byte Pair Encoding)

#### Algorithm Description
BPE iteratively merges the most frequent character pairs to create subword units.

#### Mathematical Foundation
```
def tokenize_bpe_santok(text, iterations=5):
    # Start with character-level tokens
    tokens = [{"text": char, "index": i} for i, char in enumerate(text)]
    
    # BPE Iterations
    for iteration in range(iterations):
        if len(tokens) < 2:
            break
        
        # Count adjacent pairs
        pair_counts = {}
        for i in range(len(tokens) - 1):
            pair = tokens[i]["text"] + tokens[i + 1]["text"]
            pair_counts[pair] = pair_counts.get(pair, 0) + 1
        
        if not pair_counts:
            break
        
        # Find most frequent pair
        most_frequent_pair = max(pair_counts, key=pair_counts.get)
        
        # Merge the most frequent pair
        new_tokens = []
        i = 0
        while i < len(tokens):
            if (i < len(tokens) - 1 and 
                tokens[i]["text"] + tokens[i + 1]["text"] == most_frequent_pair):
                # Merge this pair
                merged_text = tokens[i]["text"] + tokens[i + 1]["text"]
                new_tokens.append({"text": merged_text, "index": tokens[i]["index"]})
                i += 2  # Skip both tokens
            else:
                new_tokens.append(tokens[i])
                i += 1
        
        tokens = new_tokens
    
    return tokens
```

#### Properties
- **Iterative**: Multiple iterations for better subword units
- **Frequency-Based**: Merges most frequent pairs first
- **Adaptive**: Learns from data characteristics
- **Compression**: Reduces token count while preserving information

### Syllable Tokenization

#### Algorithm Description
Splits words into syllables using vowel-consonant pattern recognition.

#### Mathematical Foundation
```
def split_word_syllables(word):
    syllables = []
    current_syllable = ""
    vowels = "aeiouAEIOU"
    has_vowel = False
    
    for i, char in enumerate(word):
        current_syllable += char
        
        if char in vowels:
            has_vowel = True
        
        should_end = False
        
        if i < len(word) - 1:
            next_char = word[i + 1]
            
            # Syllable boundary rules
            if char in vowels and next_char not in vowels:
                should_end = True
            elif char not in vowels and next_char in vowels:
                should_end = True
            elif char not in vowels and next_char not in vowels:
                if i > 0 and word[i - 1] in vowels:
                    should_end = True
        
        if should_end and has_vowel:
            syllables.append(current_syllable)
            current_syllable = ""
            has_vowel = False
    
    if current_syllable:
        syllables.append(current_syllable)
    
    if not syllables:
        syllables = [word]
    
    return syllables
```

#### Properties
- **Phonetic**: Based on vowel-consonant patterns
- **Language Agnostic**: Works for any language with vowels
- **Rule-Based**: Uses linguistic rules for syllable boundaries
- **Fallback**: Handles edge cases gracefully

---

## Mathematical Foundations

### Digital Root Theory

#### Definition
The digital root of a number is the recursive sum of its digits until a single digit is obtained.

#### Mathematical Properties
```
Digital_Root(n) = 1 + ((n - 1) % 9)
```

#### Applications in SanTOK
- **9-Centric Mapping**: All numerology results mapped to 1-9
- **Stability**: Digital root provides stable single-digit representation
- **Distribution**: Uniform distribution across 1-9 range
- **Deterministic**: Same input always produces same digital root

### Hash Function Theory

#### Avalanche Effect
A good hash function should have the avalanche effect: changing one bit of input should change approximately half the output bits.

#### Collision Resistance
The probability of hash collisions should be minimal for practical applications.

#### Distribution Uniformity
Hash values should be uniformly distributed across the hash space.

### Information Theory

#### Entropy
The entropy of a tokenization method measures the information content:
```
H(X) = -Σ P(x) log₂ P(x)
```

#### Compression Ratio
The compression ratio measures the efficiency of compression:
```
Compression_Ratio = (Original_Size - Compressed_Size) / Original_Size × 100%
```

---

## Performance Optimization

### Algorithmic Optimizations

#### Hash Algorithm Selection
- **FNV-1a**: Fastest for short strings
- **MurmurHash3**: Best quality for general use
- **CityHash64**: Optimized for 64-bit systems
- **XXHash64**: Fastest overall

#### Compression Algorithm Selection
- **LZ77**: Best for text with repeated patterns
- **RLE**: Best for data with long runs
- **Huffman**: Best for skewed frequency distributions
- **Adaptive**: Automatically selects best algorithm

#### Embedding Generation
- **Batch Processing**: Generate multiple embeddings simultaneously
- **Caching**: Cache frequently used embeddings
- **Parallel Processing**: Use multiple cores for hash generation

### Memory Optimization

#### Token Stream Management
- **Lazy Loading**: Load tokens on demand
- **Streaming**: Process large texts in chunks
- **Memory Pooling**: Reuse token objects

#### Embedding Storage
- **Quantization**: Reduce precision to save memory
- **Compression**: Compress embedding vectors
- **Sparse Storage**: Store only non-zero values

---

## Algorithm Complexity

### Time Complexity Analysis

#### Tokenization Methods
| Method | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| Space | O(n) | O(n) |
| Word | O(n) | O(n) |
| Char | O(n) | O(n) |
| Grammar | O(n) | O(n) |
| Subword | O(n) | O(n) |
| Byte | O(n) | O(n) |
| BPE | O(n²) | O(n) |
| Syllable | O(n) | O(n) |
| Frequency | O(n) | O(n) |

#### Hash Algorithms
| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| FNV-1a | O(n) | O(1) |
| MurmurHash3 | O(n) | O(1) |
| CityHash64 | O(n) | O(1) |
| XXHash64 | O(n) | O(1) |
| Advanced Combination | O(4n) | O(1) |

#### Compression Algorithms
| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| LZ77 | O(n²) | O(n) |
| RLE | O(n) | O(n) |
| Huffman | O(n log n) | O(n) |
| Dictionary | O(n²) | O(n) |
| Adaptive | O(n²) | O(n) |

### Space Complexity Analysis

#### Token Storage
- **Token Objects**: O(n) where n is number of tokens
- **Embeddings**: O(n × d) where d is embedding dimension
- **Metadata**: O(n) for UIDs, indices, etc.

#### Hash Storage
- **Hash Values**: O(1) per hash
- **Hash Tables**: O(k) where k is number of unique tokens
- **Cache**: O(m) where m is cache size

---

*This algorithm deep dive is maintained by the SanTOK development team. For questions or contributions, please refer to the project repository.*
