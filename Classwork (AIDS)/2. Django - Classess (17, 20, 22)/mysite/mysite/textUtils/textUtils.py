def text_utils(text, remove_punc,  upper_case, lower_case):
    # print(text)

    text = text.strip()
    punc = '''!()[]{}-,.'";:?/\<>!@#$%^&*`~_'''
    analyze_text = ''
    apbet_count, digit_count, punc_count = 0, 0, 0

    if text.strip() != '':

        if remove_punc == 'on':
            for char in text:
                if char not in punc:
                    analyze_text += char
        else:
            analyze_text = text

        if upper_case == 'on':
            analyze_text = analyze_text.upper()
        elif lower_case == 'on':
            analyze_text = analyze_text.lower()

        for char in analyze_text:
            if char.isalpha():
                apbet_count += 1
            if char.isdigit():
                digit_count += 1
            if char in punc:
                punc_count += 1

    return {
        'analyzed_text': analyze_text, 
        'char_count':  len(analyze_text),
        'apbet_count': apbet_count,
        'digit_count': digit_count,
        'punc_count': punc_count,
    }
