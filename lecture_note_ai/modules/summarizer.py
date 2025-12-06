def summarize_text(text):
    if len(text) <= 100:
        summary = text
    else:
        summary = text[:100] + "... (자동생성 요약/예시)"
    # 아주 단순하게 빈도수 높은 단어 추출(한글/영어 둘다)
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    keywords = sorted(freq, key=freq.get, reverse=True)[:3]
    topics = keywords
    return summary, keywords, topics
