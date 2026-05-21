class MockAIService:

    @staticmethod
    def analyze_notes(notes):

        notes_lower = notes.lower()

        if "delay" in notes_lower:
            return {
                "summary": "Customer reported delay issue.",
                "risk": "HIGH"
            }

        elif "angry" in notes_lower:
            return {
                "summary": "Customer appeared unhappy.",
                "risk": "HIGH"
            }

        return {
            "summary": "Visit completed successfully.",
            "risk": "LOW"
        }