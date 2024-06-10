import re


def extract_ans(response_str, language):
    if language == 'ch':
        pattern = [
            r'答案：([A-D, ]+)',
            r'正确选项：([A-D])',
            r'正确选项：([A-D, ]+)',
            r'正确选项：([A-D]).',
            r'[A-D](?=[、。])',
            r'([A-D])、?',
            r'[A-D]',
            r'^([A-D])\.',
            r'[A-D](?=\.)',
        ]
    elif language == 'en':
        pattern = [
            r"Answer: ([A-Za-z]+)",
            r"Answer: (.*)",
            r"Right Answer: (.*)",
            r"Option (.*)",
            r'[A-E](?=\.)',
            r'([A-E])、?',
            r'[A-E]',
            r'^([A-E])\.',
            r'[A-E](?=\.)',
        ]

    ans_list = []

    for p in pattern:
        if len(ans_list) == 0:
            ans_list = re.findall(p, response_str, flags=re.MULTILINE)
            temp = []
            for i in ans_list:
                temp += i.split(',')
            ans_list = temp
        else:
            break
    return ans_list
