from agent.agent import Agent
from rag.rag_chain import ask_rag
from memory import MemoryManager

class Router:
    """
    Router intelligent :
    - RAG si question documentaire
    - Agent si un tool est nécessaire
    - Chat simple sinon
    - Mémoire pour conserver le contexte
    """

    def __init__(self):
        self.memory = MemoryManager()
        self.agent = Agent(rag_callable=ask_rag)

    def route(self, query: str) -> str:
        q = query.lower()

        # 1. Mots-clés documentaires → RAG
        if any(k in q for k in ["document", "politique", "procédure", "manuel", "article"]):
            answer = ask_rag(query)
            self.memory.add_user_message(query)
            self.memory.add_ai_message(answer)
            return answer

        # 2. Tools → Agent
        if any(k in q for k in ["météo", "meteo", "+", "-", "*", "/", "recherche", "google", "web"]):
            answer = self.agent.decide_and_answer(query)
            self.memory.add_user_message(query)
            self.memory.add_ai_message(answer)
            return answer

        # 3. Small talk → Chat simple (mock)
        answer = f"Réponse conversationnelle simple (mock) à : {query}"
        self.memory.add_user_message(query)
        self.memory.add_ai_message(answer)
        return answer

    def get_history(self):
        return self.memory.get_history()
