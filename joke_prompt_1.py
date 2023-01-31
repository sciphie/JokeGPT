from chatgpt_wrapper import ChatGPT
import pandas as pd 

prompts = [
    "Can you tell me a joke?", 
    "Please, tell me a joke.",
    
    "Let me hear a joke, please.",

    "Do you know any good jokes?",
    "Tell me a joke, please!",
    "Tell me another joke.",
    #"I would like to hear a joke, please.",
    "I would love to hear a joke.",
    "I would like to hear a joke.",
    "I'd love to hear a joke.",
    "I'd like to hear a joke."
]

#bot = ChatGPT()
n = 1000 # number of generated jokes 


data = {"prompt": [], "response": []}

for i in range(n): 
    bot = ChatGPT()
    prompt_number = i%len(prompts)
    prompt = prompts[prompt_number]
    
    try: 
        resp = bot.ask(prompt)
        print(F"{i}: {prompt} - {resp}")
    except playwright._impl._api_types.Error as e:
        print("playwright Error has occurred")
        print(f"{e},{e.__class_}")
        resp = "Error: " + e 
    
    data['prompt'].append(prompt_number)
    data['response'].append(resp)
    
    #if resp = %%error%% :
    #    do something... safe Error 
    
    # api.reset_conversation()  # reset the conversation or not after each prompt? 
    if i%10==9:
        assert(len(data['prompt']) == len(data['response']))
        
        df = pd.DataFrame(data) 
        df.to_pickle('joke_prompt_generation') 
    

    
df = pd.DataFrame(data) 
df.to_picke('joke_prompt_generation') 


joke_outputs = [
    "Why was the math book sad? Because it had too many problems.",
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why was the computer cold? Because it left its Windows open.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why don't oysters give to charity? Because they're shellfish.",
    "Why don't eggs tell jokes? Because they'd crack each other up.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the cookie go to the doctor? Because it was feeling crumbly.",
]