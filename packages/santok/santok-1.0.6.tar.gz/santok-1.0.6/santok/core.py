"""
SanTOK Core Module - Essential tokenization functions
"""

import re
from collections import Counter

def all_tokenizations(text):
    """
    Perform all tokenization methods on input text
    
    Args:
        text (str): Input text to tokenize
        
    Returns:
        dict: Dictionary with tokenization results for each method
    """
    results = {}
    
    # Space tokenization - splits on whitespace
    space_tokens = text.split()
    results['space'] = [{'text': token, 'frontend': 1} for token in space_tokens]
    
    # Word tokenization - extracts words only
    words = re.findall(r'\b\w+\b', text)
    results['word'] = [{'text': word, 'frontend': 2} for word in words]
    
    # Character tokenization - each character
    results['char'] = [{'text': char, 'frontend': 3} for char in text]
    
    # Grammar tokenization - separates words, numbers, punctuation
    grammar_tokens = re.findall(r'[A-Za-z]+|[0-9]+|[^\w\s]', text)
    results['grammar'] = [{'text': token, 'frontend': 4} for token in grammar_tokens]
    
    # Subword tokenization - fixed length chunks
    chunk_size = 3
    subwords = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    results['subword'] = [{'text': chunk, 'frontend': 5} for chunk in subwords]
    
    # Byte tokenization - ASCII values
    byte_tokens = [str(ord(char)) for char in text]
    results['byte'] = [{'text': byte_token, 'frontend': 6} for byte_token in byte_tokens]
    
    # BPE tokenization - simple word splitting
    bpe_tokens = text.split()
    results['bpe'] = [{'text': token, 'frontend': 7} for token in bpe_tokens]
    
    # Syllable tokenization - vowel-based splitting
    syllables = re.findall(r'[aeiouAEIOU]*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]*', text)
    results['syllable'] = [{'text': syl, 'frontend': 8} for syl in syllables if syl]
    
    # Frequency tokenization - word frequency analysis
    word_counts = Counter(words)
    freq_tokens = [f"{word}({count})" for word, count in word_counts.items()]
    results['frequency'] = [{'text': token, 'frontend': 9} for token in freq_tokens]
    
    return results

def numerology_sum(text):
    """
    Calculate numerology sum for text
    
    Args:
        text (str): Input text
        
    Returns:
        int: Numerology sum (1-9)
    """
    total = sum(ord(char) for char in text)
    return total % 9 + 1

def main():
    """Main function for CLI usage"""
    print("SanTOK Tokenizer - Core Module")
    print("=" * 40)
    print("Usage: import santok")
    print("       result = santok.all_tokenizations('your text')")
    print("=" * 40)
    
    # Demo
    demo_text = "Hello world!"
    print(f"Demo with: '{demo_text}'")
    result = all_tokenizations(demo_text)
    print(f"Methods available: {list(result.keys())}")
    print(f"Space tokens: {len(result['space'])}")
    print(f"Character tokens: {len(result['char'])}")

if __name__ == "__main__":
    main()
