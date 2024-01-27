class BasicTokenizer:
    def __init__(self, text, lower, mode):
        self.text = text
        self.lower = lower
        self.mode = mode

        if self.lower == True:
            self.lowerTxt()
        
        if mode == 'pher':
            self.tokenizePher()
        
        self.tokenizePunct()

    def lowerTxt(self):
        return self.text.lower()

    def tokenizePher(self):
        ignwords = ['is', 'was', 'has', 'had', 'have', 'will', 'would', 'could', 'should', "couldn't", "shouldn't", "wouldn't", 
                    'must','can', 'i', 'he', 'she', 'mine', 'my', 'be', 'or', 'ours', 'our', 'a', 'an', 'for', 'off', 'under', 'on', 'before',
                    'after', 'the', 'that', 'this', 'thus', 'do', 'does', 'done', "don't", '']

        text = self.text.split()

        pheripherals = []

        for i in ignwords:
            for text in text:
                if i in text:
                    words = text.remove(i)
                    pheripherals.append(words)
                    return text
        print(text)


    def tokenizePunct(self):
        punctuations = [',', '.', '!', '-', '_', '...', ';', ':']

        for punct in punctuations:
            if punct in self.text:
                self.text.replace(punct, '')
        print(self.text)


BasicTokenizer(text='All things bright and beutifull, he made them all',
               lower=True,
               mode='punct')