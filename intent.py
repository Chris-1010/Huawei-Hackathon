import pke.unsupervised
import spacy

class IntentRecognition():
    def __init__(self, text):
        self._text = text

    def intent(self):

        print("ENTERED FUNCTION")
        #define the valid Parts-of-Speech
        pos = {"NOUN", "PROPN", "ADJ"}

        #Create a TextRank Extractor - extracts keywords using a part-of-speech tag-based approach to identify candidate keywords
        extractor = pke.unsupervised.TextRank()

        #Load content of the document
        extractor.load_document(input=self._text, language="en", normalization=None)

        # 3. build the graph representation of the document and rank the words.
        #    Key phrase candidates are composed from the 33-percent highest-ranked words.
        extractor.candidate_weighting(window=2, pos=pos, top_percent=0.33)

        # 4. get the 10-highest scored candidates as keyphrases
        keyphrases = extractor.get_n_best(n=10)

        print(keyphrases)


if __name__ == "__main__":
    
    nlp = spacy.load("en_core_web_sm")

    #Input Text - Question
    text = ""

    i = IntentRecognition(text)
    i.intent()
