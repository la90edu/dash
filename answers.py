import answers_texts as at

medida="""
המדדיה נעשתה דרך שאלון בוט 
"""
class Answers:
    def __init__(self, anigma_type,anigmas_dic):
        self.anigma_type = anigma_type
        self.anigmas_dic=anigmas_dic
        
    def get_what_is(self):
        match (self.anigma_type):
            case "ici":
                return at.what_is_ici
            case "risc":   
                return at.what_is_risc
            case "future":
                return at.what_is_future
            case _:
                return "אין מידע זמין"
            
    def get_graph_insights(self):
        name=""
        current_avg=""
        match (self.anigma_type):
            case "ici":
                return at.what_is_ici
            case "risc":   
                return at.what_is_risc
            case "future":
                return at.what_is_future
            case _:
                return "אין מידע זמין"