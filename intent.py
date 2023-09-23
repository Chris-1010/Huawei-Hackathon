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

    #Dummy Text
    text = """
        Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
        Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
        Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.
        Python consistently ranks as one of the most popular programming languages.
        Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL, capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life", a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a five-member "Steering Council" to lead the project.
        Python 2.0 was released on 16 October 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode.
        Python 3.0 was released on 3 December 2008. It was a major revision of the language that is not completely backward-compatible. Many of its major features were backported to Python 2.6.x and 2.7.x version series. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.
        Python 2.7's end-of-life date was initially set at 2015 then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3. No more security patches or other improvements will be released for it. With Python 2's end-of-life, only Python 3.6.x and later are supported.
        Python 3.9.2 and 3.8.8 were expedited as all versions of Python (including 2.7) had security issues, leading to possible remote code execution and web cache poisoning.
        """

    i = IntentRecognition(text)
    i.intent()
