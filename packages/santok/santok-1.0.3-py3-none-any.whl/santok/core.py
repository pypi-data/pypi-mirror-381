#!/usr/bin/env python3
"""
SanTOK Core Functionality - Essential tokenization and numerology functions
"""

import re
from collections import Counter

def tokenize_space(text):
    """Split text by whitespace characters"""
    if not text:
        return []
    
    tokens = []
    current_token = ""
    
    for i, char in enumerate(text):
        if char.isspace():
            if current_token:
                tokens.append({
                    "text": current_token,
                    "index": i - len(current_token)
                })
                current_token = ""
        else:
            current_token += char
    
    if current_token:
        tokens.append({
            "text": current_token,
            "index": len(text) - len(current_token)
        })
    
    return tokens

def tokenize_word(text):
    """Extract words using regex pattern"""
    if not text:
        return []
    
    word_pattern = r'\b\w+\b'
    matches = re.finditer(word_pattern, text)
    
    tokens = []
    for match in matches:
        tokens.append({
            "text": match.group(),
            "index": match.start()
        })
    
    return tokens

def tokenize_char(text):
    """Split text into individual characters"""
    if not text:
        return []
    
    tokens = []
    for i, char in enumerate(text):
        tokens.append({
            "text": char,
            "index": i
        })
    
    return tokens

def tokenize_grammar(text):
    """Grammar-aware tokenization"""
    if not text:
        return []
    
    patterns = [
        r'\b\w+\b',  # Words
        r'[.!?]+',   # Sentence endings
        r'[,;:]+',   # Punctuation
        r'[()[\]{}]+',  # Brackets
        r'["\']',    # Quotes
        r'\s+',      # Whitespace
        r'[^\w\s.!?,:;()[\]{}"\']+',  # Other characters
    ]
    
    tokens = []
    processed_chars = set()
    
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            start, end = match.span()
            if not any(i in processed_chars for i in range(start, end)):
                tokens.append({
                    "text": match.group(),
                    "index": start
                })
                processed_chars.update(range(start, end))
    
    tokens.sort(key=lambda x: x["index"])
    return tokens

def tokenize_subword(text, chunk_size=3):
    """Fixed-length subword tokenization"""
    if not text:
        return []
    
    tokens = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        tokens.append({
            "text": chunk,
            "index": i
        })
    
    return tokens

def tokenize_byte(text):
    """Convert text to ASCII byte representation"""
    if not text:
        return []
    
    tokens = []
    for i, char in enumerate(text):
        ascii_val = str(ord(char))
        tokens.append({
            "text": ascii_val,
            "index": i
        })
    
    return tokens

def split_word_syllables(word):
    """Simple syllable splitting based on vowel patterns"""
    if not word:
        return []
    
    word = word.lower()
    vowels = "aeiouy"
    syllables = []
    current_syllable = ""
    
    for i, char in enumerate(word):
        current_syllable += char
        
        if char in vowels and i < len(word) - 1:
            next_char = word[i + 1]
            if next_char not in vowels:
                if i < len(word) - 2:
                    syllables.append(current_syllable)
                    current_syllable = ""
    
    if current_syllable:
        syllables.append(current_syllable)
    
    return syllables if syllables else [word]

def tokenize_syllable(text):
    """Syllable-based tokenization"""
    if not text:
        return []
    
    tokens = []
    words = re.findall(r'\b\w+\b', text)
    current_index = 0
    
    for word in words:
        word_start = text.find(word, current_index)
        syllables = split_word_syllables(word)
        
        syllable_start = word_start
        for syllable in syllables:
            tokens.append({
                "text": syllable,
                "index": syllable_start
            })
            syllable_start += len(syllable)
        
        current_index = word_start + len(word)
    
    return tokens

def tokenize_frequency(text, frequency_threshold=2):
    """Frequency-based tokenization with grouping"""
    if not text:
        return []
    
    word_tokens = tokenize_word(text)
    word_counts = Counter(token["text"] for token in word_tokens)
    
    tokens = []
    for token in word_tokens:
        word = token["text"]
        count = word_counts[word]
        
        if count >= frequency_threshold:
            token_text = f"{word}({count})"
        else:
            token_text = word
        
        tokens.append({
            "text": token_text,
            "index": token["index"]
        })
    
    return tokens

def tokenize_bpe_santok(text, iterations=5):
    """Custom Byte Pair Encoding implementation"""
    if not text:
        return []
    
    tokens = list(text)
    
    for _ in range(iterations):
        pairs = Counter()
        for i in range(len(tokens) - 1):
            pair = (tokens[i], tokens[i + 1])
            pairs[pair] += 1
        
        if not pairs:
            break
        
        most_frequent = pairs.most_common(1)[0][0]
        
        new_tokens = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1 and tokens[i] == most_frequent[0] and tokens[i + 1] == most_frequent[1]:
                new_tokens.append(most_frequent[0] + most_frequent[1])
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        
        tokens = new_tokens
    
    result_tokens = []
    current_index = 0
    for token in tokens:
        result_tokens.append({
            "text": token,
            "index": current_index
        })
        current_index += len(token)
    
    return result_tokens

def all_tokenizations(text):
    """Apply all tokenization methods to the input text"""
    if not text:
        return {method: [] for method in ["space", "word", "char", "grammar", "subword", "byte", "bpe", "syllable", "frequency"]}
    
    return {
        "space": tokenize_space(text),
        "word": tokenize_word(text),
        "char": tokenize_char(text),
        "grammar": tokenize_grammar(text),
        "subword": tokenize_subword(text),
        "byte": tokenize_byte(text),
        "bpe": tokenize_bpe_santok(text),
        "syllable": tokenize_syllable(text),
        "frequency": tokenize_frequency(text)
    }

def numerology_sum(token_text):
    """COMBINED METHOD: Weighted Sum + Hash for frontend digit calculation"""
    if not token_text:
        return 0
    
    # METHOD 1: Weighted Sum Calculation
    weighted_sum = 0
    for i, char in enumerate(token_text):
        weighted_sum += ord(char) * (i + 1)
    
    # Convert to 9-centric digital root (1-9)
    weighted_digit = ((weighted_sum - 1) % 9) + 1 if weighted_sum > 0 else 0
    
    # METHOD 2: Hash Calculation (31-based rolling hash)
    hash_value = 0
    for char in token_text:
        hash_value = hash_value * 31 + ord(char)
    
    # Convert hash to single digit (1-9)
    hash_digit = ((hash_value - 1) % 9) + 1 if hash_value > 0 else 0
    
    # COMBINATION FORMULA: Final Digit = (Weighted_Digit * 9 + Hash_Digit) % 9 + 1
    final_digit = ((weighted_digit * 9 + hash_digit) % 9) + 1
    
    return final_digit

def numerology_sum_fast(token_text):
    """Fast numerology calculation (same algorithm as numerology_sum)"""
    return numerology_sum(token_text)

def test_reconstruction_simple(text):
    """Simple reconstruction test for core module"""
    print(f"\n[TEST] TESTING RECONSTRUCTION FOR: '{text}'")
    print("="*60)
    
    tokens_result = all_tokenizations(text)
    
    # Define lossless vs analytical methods
    lossless_methods = {"space", "char", "bpe"}
    
    print("LOSSLESS RECONSTRUCTION METHODS:")
    print("-" * 40)
    
    perfect_count = 0
    for method in lossless_methods:
        tokens = tokens_result[method]
        # Simple reconstruction for space and char
        if method == "space":
            reconstructed = " ".join([t['text'] for t in tokens])
        elif method == "char":
            reconstructed = "".join([t['text'] for t in tokens])
        elif method == "bpe":
            reconstructed = "".join([t['text'] for t in tokens])
        else:
            reconstructed = "".join([t['text'] for t in tokens])
        
        is_perfect = reconstructed == text
        if is_perfect:
            perfect_count += 1
            status = "✅ PERFECT"
        else:
            status = "⚠️  NEEDS FIX"
        
        print(f"{method.upper():12} | {status:12} | Tokens: {len(tokens):3} | '{reconstructed}'")
    
    print("\nANALYTICAL METHODS (Transform text for analysis):")
    print("-" * 50)
    
    analytical_methods = {"word", "grammar", "subword", "byte", "syllable", "frequency"}
    for method in analytical_methods:
        tokens = tokens_result[method]
        reconstructed = "".join([t['text'] for t in tokens])
        status = "🔄 ANALYTICAL"
        print(f"{method.upper():12} | {status:12} | Tokens: {len(tokens):3} | '{reconstructed}'")
    
    print(f"\n[SUMMARY] RECONSTRUCTION TEST COMPLETE")
    print(f"Lossless methods: {perfect_count}/{len(lossless_methods)} working perfectly")
    print(f"Analytical methods: {len(analytical_methods)} working as designed")


def main():
    """Main function for command-line interface"""
    print("SanTOK Multi-Format Tokenizer")
    print("=" * 50)
    
    while True:
        print("\nINPUT OPTIONS:")
        print("1. Text input")
        print("2. File input")
        print("3. Reconstruction test")
        print("9. Exit")
        print("Choose option (1-3, 9):")
        
        mode = input()
        
        if mode == '9' or mode.lower() == 'exit':
            print("Goodbye!")
            break
            
        if mode == '1':
            print("Enter text:")
            text = input()
            
            if not text.strip():
                print("ERROR: Please enter some text!")
                continue
            
            tokens = all_tokenizations(text)
            
            print(f"\nTokenization Results:")
            for method, token_list in tokens.items():
                print(f"{method.upper()}: {len(token_list)} tokens")
                if token_list:
                    sample = [t['text'] for t in token_list[:5]]
                    print(f"  Sample: {sample}")
            
        elif mode == '2':
            print("File input functionality available in full version")
            continue
            
        elif mode == '3':
            print("Enter text to test reconstruction:")
            text = input()
            
            if not text.strip():
                print("ERROR: Please enter some text!")
                continue
            
            test_reconstruction_simple(text)
            
        else:
            print("ERROR: Invalid option!")
            continue

if __name__ == "__main__":
    main()
