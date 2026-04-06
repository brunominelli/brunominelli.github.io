from dataclasses import dataclass

@dataclass
class Proposal:
    lead_id:str
    problem:str
    context:str
    solution:str
    complexity:str
    price:str
    deadline:str


    def _to_dict(self) -> dict:
        return {
            'lead_id':self.lead_id,
            'problem':self.problem,
            'context':self.context,
            'solution':self.solution,
            'complexity':self.complexity,
            'price':self.price,
            'deadline':self.deadline
        }