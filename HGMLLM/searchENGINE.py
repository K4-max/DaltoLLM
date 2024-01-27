import wikipedia

class ReceiveDoc:
    def __init__(self, Document: str):
        self.Document = Document
        self.Doc = self.readDoc()

    def readDoc(self):
        Doc = open(self.Document)
        Doc = Doc.read()
        return Doc

    def predictWord(self, word):
        Doc = self.Doc.split()

        if word in Doc:
            index = Doc.index(word)
            next_index = index + 1
            next_word = Doc[next_index]
            
            print(next_word)


class GetDomain:
    def __init__(self):
        pass

li = ['i', 'am', 'is', 'guy']

ignw = ['is']

li.remove(ignw[0])
print(li)

ignwords = ['is', 'was', 'has', 'had', 'have', 'will', 'would', 'could', 'should', "couldn't", "shouldn't", "wouldn't", 
'must','can', 'i', 'he', 'she', 'mine', 'my', 'be', 'or', 'ours', 'our', 'a', 'an', 'for', 'off', 'under', 'on', 'before',
'after', 'the', 'that', 'this', 'thus', 'do', 'does', 'done', "don't"]

class Domain_Extraction:
    def __init__(self, prompt, ignwords):
        self.prompt = prompt
        self.ignwords = ignwords

        self.Extract_Domain()
        self.Search_Domain()

    def Extract_Domain(self):
        global domains

        domains = self.prompt.split()
        
        for i in self.ignwords:
            if i in domains:
                domains.remove(i)

        print(domains)


    def Search_Domain(self):
        for domain in domains:
            domain_search = (wikipedia.page(domain + 'language').content)
            print(domain_search)

pr = Domain_Extraction(prompt='the english teacher is nice', 
                       ignwords=ignwords)