from openai import OpenAI
from colorama import init, Fore, Style

init()  # Initialize colorama

class CavalierChatbot:
    def __init__(self):
        self.system_message = {
            "role": "system",
            "content": """You are a chatbot that ONLY uses the following information about Cavalier King Charles Spaniels. 
            Do not provide any information beyond what is explicitly listed here:
            
            Core Facts About Cavaliers:
            1. History:
               - Descended from toy spaniels seen in 16th-18th century paintings
               - Named after King Charles II of England
               - Recognized by AKC in 1995
            
            2. Physical Characteristics:
               - Four recognized colors: Blenheim, Ruby, Black and Tan, Tricolor
               - Weight range: 13-18 pounds
               - Distinctive dome-shaped skull
            
            3. Health Considerations:
               - Mitral Valve Disease (MVD)
               - Syringomyelia (SM)
               - Regular heart checkups recommended
            
            4. Temperament:
               - Gentle and affectionate
               - Good with children and other pets
               - Known as 'comforter spaniels'
            
            STRICT RULES:
            1. Only use the facts listed above. Do not draw from any other knowledge.
            2. If asked about anything not in this list, respond: "I can only provide specific information about Cavalier history, physical characteristics, temperament, or health considerations. Would you like to know about that?"
            3. Never make assumptions or provide information beyond these exact facts.
            4. If unsure, default to: "That specific detail isn't in my approved fact list. I can tell you about Cavalier history, physical characteristics, temperament, or health considerations."
            """
        }
        self.conversation_history = [self.system_message]
        self.client = OpenAI()
        self.print_welcome()  # Add this line to print welcome message when bot is created
    
    def print_welcome(self):
        print(f"""
{Fore.CYAN}╔══════════════════════════════════════════╗
║ Welcome to the Cavalier Spaniel Chatbot! ║
╚══════════════════════════════════════════╝{Style.RESET_ALL}
        
Type your questions about Cavalier King Charles Spaniels
{Fore.YELLOW}Commands:{Style.RESET_ALL}
• {Fore.GREEN}clear{Style.RESET_ALL} - Reset conversation
• {Fore.RED}exit{Style.RESET_ALL}  - End chat
""")
    
    def get_response(self, user_prompt):
        # Add the new user message
        self.conversation_history.append({"role": "user", "content": user_prompt})
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=self.conversation_history,
            temperature=0.2,
            presence_penalty=2.0,
            frequency_penalty=2.0
        )
        
        # Add the assistant's response
        assistant_response = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": assistant_response})
        
        return assistant_response
    
    def clear_history(self):
        # Reset the conversation while keeping the system message
        self.conversation_history = [self.system_message]

# Usage example:
chatbot = CavalierChatbot()

while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'bye']:
        break
    elif user_input.lower() == 'clear':
        chatbot.clear_history()
        print("Conversation history cleared!")
        continue
    
    response = chatbot.get_response(user_input)
    print("CavBot:", response)