"""
SanTOK Core Module - Essential tokenization functions
"""

def all_tokenizations(text):
    """Perform all tokenization methods on input text"""
    results = {}
    
    # Space tokenization
    results['space'] = [{'text': token, 'frontend': 1} for token in text.split()]
    
    # Word tokenization (simple)
    import re
    words = re.findall(r'\b\w+\b', text)
    results['word'] = [{'text': word, 'frontend': 2} for word in words]
    
    # Character tokenization
    results['char'] = [{'text': char, 'frontend': 3} for char in text]
    
    # Grammar tokenization (simplified)
    grammar_tokens = re.findall(r'[A-Za-z]+|[0-9]+|[^\w\s]', text)
    results['grammar'] = [{'text': token, 'frontend': 4} for token in grammar_tokens]
    
    # Subword tokenization (simple chunking)
    chunk_size = 3
    subwords = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    results['subword'] = [{'text': chunk, 'frontend': 5} for chunk in subwords]
    
    # Byte tokenization
    byte_tokens = [str(ord(char)) for char in text]
    results['byte'] = [{'text': byte_token, 'frontend': 6} for byte_token in byte_tokens]
    
    # BPE tokenization (simplified)
    bpe_tokens = text.split()
    results['bpe'] = [{'text': token, 'frontend': 7} for token in bpe_tokens]
    
    # Syllable tokenization (simplified)
    syllables = re.findall(r'[aeiouAEIOU]*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]*', text)
    results['syllable'] = [{'text': syl, 'frontend': 8} for syl in syllables if syl]
    
    # Frequency tokenization (simplified)
    from collections import Counter
    word_counts = Counter(words)
    freq_tokens = [f"{word}({count})" for word, count in word_counts.items()]
    results['frequency'] = [{'text': token, 'frontend': 9} for token in freq_tokens]
    
    return results

def numerology_sum(text):
    """Calculate numerology sum for text"""
    total = sum(ord(char) for char in text)
    return total % 9 + 1

def main():
    """Main function for CLI usage"""
    print("SanTOK Tokenizer - Core Module")
    print("Use: import santok; result = santok.all_tokenizations('your text')")
