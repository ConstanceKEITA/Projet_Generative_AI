import re
from agent.agent import Agent
from rag.rag_chain import ask_rag
from memory import MemoryManager


class Router:
    """
    Router intelligent :
    - Météo/Calcul/Web explicite → Agent
    - Par défaut → RAG
    - Mémoire pour conserver le contexte
    """

    def __init__(self):
        self.memory = MemoryManager()
        self.agent = Agent(rag_callable=ask_rag)

    def route(self, query: str) -> str:
        q = query.lower()

        # 1. Météo
        if "météo" in q or "meteo" in q:
            answer = self.agent.decide_and_answer(query)

        # 2. Calcul
        elif re.search(r'\d+\s*[\+\-\*\/]\s*\d+', q):
            answer = self.agent.decide_and_answer(query)

        # 3. Web explicite
        elif "recherche" in q or "google" in q or "web" in q:
            answer = self.agent.decide_and_answer(query)

        # 4. Résumé ou citation → Agent
        elif "résume" in q or "formate" in q or "citation" in q:
            answer = self.agent.decide_and_answer(query)

        # 5. Par défaut → RAG
        else:
            answer = ask_rag(query)

        self.memory.add_user_message(query)
        self.memory.add_ai_message(answer)
        return answer

    def get_history(self):
        return self.memory.get_history()