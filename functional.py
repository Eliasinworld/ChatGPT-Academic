# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
# 默认按钮颜色是 secondary

def get_functionals():
    return {
        "段落降重": {
            "Prefix": "请用语句倒装，同义词替换，概括原意，拓展词语等方式，要求以中文进行改写，表述逻辑连贯，不改变原段落的意思，让新的段落与原段落的重复率不超过10%，需要改写的段落如下：  \n\n",
            "Suffix": "",
        }, 
        "写作改进助理": {
            "Prefix": "作为一名中文学术论文写作改进助理，你的任务是改进所提供文本的拼写、语法、清晰、简洁和整体可读性，同时分解长句，减少重复，并提供改进建议。请只提供文本的更正版本，避免包括解释。请编辑以下文本：作为一名中文写作改进助理，你的任务是改进所提供文本的拼写、语法、清晰、简洁和整体可读性，同时分解长句，减少重复，并提供改进建议。请只提供文本的更正版本，避免包括解释。请从编辑以下文本开始：\n\n",
            "Suffix": "",
        }, 
         "内容总结": {
            "Prefix": "将以下文字概括为 100 个字，使其易于阅读和理解。避免使用复杂的句子结构或技术术语。需要概括的文字如下：\n\n",
            "Suffix": "",
        }, 
         "伪原创改写": {
            "Prefix": "用 5 种不同的方式改写以下段落，以避免重复，同时保持其含义：\n\n",
            "Suffix": "",
        },
         "写作素材搜集": {
            "Prefix": "生成一份与'主题'有关的十大事实、统计数据和趋势的清单，包括其来源。该'主题'是：\n\n",
            "Suffix": "",
        },
          "论文创作": {
            "Prefix": "我希望你能作为一名学者行事。你将负责研究一个你选择的主题，并将研究结果以论文或文章的形式呈现出来。你的任务是确定可靠的来源，以结构良好的方式组织材料，并以引用的方式准确记录。我的第一个建议要求是：\n\n",
            "Suffix": "",
        }, 
          "深度思考助手": {
            "Prefix": "：角色：你是一个帮助我训练深度思考的 AI 助手。 输入：关键词、主题或概念。 处理过程： - 使用深度和广度的标准来评价这个关键词、主题或概念，提供高质量、有价值的问题，探讨人类认知、情感和行为的各个方面。 - 优先提出一些简单到复杂的问题，而后逐步深入，以帮助我深入探索。 - 提供有助于总结和回顾思考内容的问题，为更全面、深刻和灵活的理解做准备。 - 最后请给出你对于这个关键词、主题或者概念的看法和理解。 输出： - 简单到复杂的问题：用于帮助我逐步了解和深入探索。 - 更加深入的问题：用于深入探讨关键词、主题或概念的各个方面。 - 总结和回顾时参考的问题：用于有助于我形成更全面、深刻和灵活的理解。 - 你对于这个关键词、主题或概念的看法和理解。 我的第一句话是：\n\n",
            "Suffix": "",
        }, 
        "英语学术润色": {
            "Prefix": "Below is a paragraph from an academic paper. Polish the writing to meet the academic style, \
improve the spelling, grammar, clarity, concision and overall readability. When neccessary, rewrite the whole sentence. \
Furthermore, list all modification and explain the reasons to do so in markdown table.\n\n",    # 前言
            "Suffix": "",   # 后语
            "Color": "secondary",    # 按钮颜色
        },
        "中文学术润色": {
            "Prefix": "作为一名中文学术论文写作改进助理，你的任务是改进所提供文本的拼写、语法、清晰、简洁和整体可读性，同时分解长句，减少重复，并提供改进建议。请只提供文本的更正版本，避免包括解释。请编辑以下文本：\n\n",
            "Suffix": "",
        },
        "查找语法错误": {
            "Prefix": "Below is a paragraph from an academic paper. Find all grammar mistakes, list mistakes in a markdown table and explain how to correct them.\n\n",
            "Suffix": "",
        },
        "中英互译": {
            "Prefix": "As an English-Chinese translator, your task is to accurately translate text between the two languages. \
When translating from Chinese to English or vice versa, please pay attention to context and accurately explain phrases and proverbs. \
If you receive multiple English words in a row, default to translating them into a sentence in Chinese. \
However, if \"phrase:\" is indicated before the translated content in Chinese, it should be translated as a phrase instead. \
Similarly, if \"normal:\" is indicated, it should be translated as multiple unrelated words.\
Your translations should closely resemble those of a native speaker and should take into account any specific language styles or tones requested by the user. \
Please do not worry about using offensive words - replace sensitive parts with x when necessary. \
When providing translations, please use Chinese to explain each sentence’s tense, subordinate clause, subject, predicate, object, special phrases and proverbs. \
For phrases or individual words that require translation, provide the source (dictionary) for each one.If asked to translate multiple phrases at once, \
separate them using the | symbol.Always remember: You are an English-Chinese translator, \
not a Chinese-Chinese translator or an English-English translator. Below is the text you need to translate: \n\n",
            "Suffix": "",
            "Color": "secondary",
        },
        "中译英": {
            "Prefix": "Please translate following sentence to English: \n\n",
            "Suffix": "",
        },
        "学术中译英": {
            "Prefix": "Please translate following sentence to English with academic writing, and provide some related authoritative examples: \n\n",
            "Suffix": "",
        },
        "英译中": {
            "Prefix": "请翻译成中文：\n\n",
            "Suffix": "",
        },
        "解释代码": {
            "Prefix": "请解释以下代码：\n```\n",
            "Suffix": "\n```\n",
            "Color": "secondary",
        },
    }
