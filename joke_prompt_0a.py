# after https://github.com/terry3041/pyChatGPT 

from pyChatGPT import ChatGPT
import pandas as pd 

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..bTBe1GBvpwfrZGdj.1cWMi-xhZ6VXC7fPQZPYPcg2sWZ8JryVWiV6oTM-8P486twhoHwYX61uX-dCLCH1jsgbyRD-kivnh4yRRjxQOBwwodfO37TDo7oHOPaVFetM-9nrofLjqI_lz5eTQfG3u8V229O_CK25gpMpmKjsUFUAU1dSdT-AGfG6FN6l5EYm3tU0dNwgZSnwHkoz7lChs3EPTppDPLoMKLFUrWKXHR1eWHaD1CxXHvhboUjA4EUpvB6t6eEf-_sK0if_dbCKiVRL4G1YJbzsxWiu6uOfPI7XGF3V6kDPpM3KwHh7ZGZuQM-rIJIdq0frirR9iCEyIzUpzQ1feeCXeZTrmuKtsjhDNdgMD2JSGSOpNAGI8mw2vpAXSWSMqi0DNPjhQmt3MLazVkaz8VJwacAAefEtQN0zq_jP-goS1MId2lIIFeZRfH1shcNB-3sx25S9AIOfyk8-t-hDyis9cxLHTscd6mm1DX1PcN8MMEb9AcIWyC0ZiMtefQVac6UtxdPQWl3HAUe7mjSpwBsiPc1TgKz6wbZl4weYmGBj8ABGOQmrW634WT6Jp4m10KjcLP1mK9xpab-KCRpq1Ns0nyjc2WLLYz4jInPCY-uiFdvhuP_aIdIqhKMvUgjKZPRPJW0rPcLqDx59qCnziFODg215qIX4Wki3m_WHjogJXpvUBNt0bknnWB4xD8WwRlq0i1qBY9QQdx4U47u7A8Jtdu8jmQceWaBQmVi-9PS-eSYRqu4eDeUucIl9J89NTYS-QRVfYAgSnJP-2zGaIQOuj8pv6L0PeviGInmtovTN38JX1T_wdTb8hQMQGqDn1vCB1drEh9ArqSdXYerpa6z7GY0EVqnwQympBqKlfWoLaA8h-CT8iwk466j89UK-9_IJmX575tGs37b118C31PRrrTCca4_d0AerREzDEGOMpzUlV0kFsLiCP2kzEJ-bOOOd8JDrHsa2E9uTj6BZzzCSXf0p0sx8CWP4_ljsMA3OrtcYo3ZvNRzIH4f3QhYSbbVlRmumcTQg4F4bKRvf8yq5EOE4edMdHEoqAUCkZbe4nlHRS4_vzLVR-5mrYAw3tEGo5g7fDCL7kwWo5gmlhdsEsAurkahMqL4jzVt_kt5fSHdc13cowrOw6pG0XRuezuOt8CJ6mE0vtkIQy12BmaIY1kPInwUyyg2p4oywyQgaqb--ydx_Ep6MZ-u7T6IFC79sH1MGtXLld0GzjW5H4VnEqPrmba8LfH55uD0q_kCEH8PoOnwI6yxCfPqbwAwIjwRsOUdQjCOhIdIMVFSMKZgKvEe-507xCRu3R586sGpj3qAol1lzXf-YezOkukwb6uFuXG76tnkwtjGwtpQC1zOXhCrsdv50GLdyw4MaD-b7znDPWvw_vY-0n3EHHS3NmQYfOII6GoiIRqidCvC1mePJs2r2E6vKr22UZkHR8Gv1LVZugkGg-mlOKN4gD1lDADCnx1IMYiiZG2iUfHnRH9e9bnNEuL8NZKeVemIjaWrJuMe1cSmT9B0hR2hDhssVIXqy0lC9Emvk8nnT8s6Mz9KPQc4VcM-nYYEDfxqXXWR9Nllmz29pkXtEbt3_SRq1RbfiYXd-lSIlcklqeQJlGT6aESHsmQDh7zsxIt4703yheiAFzq7fiU6h2qyp_SiWYC5g7EI1w8znOdMbAb5zO8jUlF-MdzGKexZu_ovcNCkUWdjwSY76Up5v7Gaerl_mkgdx-TNFAJ8x1jwhN9p-jkYOhLLOEyGaYBnq53KvcW3dlUy2cbBzOACQWqHdCxVKs2XyXwKvUqiawstTMUaelUIUzU4WDqvPGGKiKeMhMGmk7X_cQKF5r0D3ANsgm9xX_A5Yo-R4HK8jtrmtFu-Kyvf3BmJbnihOn2je50vePUoX4eao2AIh82YPYVUZ9PaCU5bVkPiHFBRhLF3feup-xPZ3FwlOqQN5xdDkN-GMyS5wX_M79BtPBENlHMHxEiGQFUNX895VhCDiye3P8qd53sUu6rg0WO-WpDNMKhSVVkmvncRPXgra-OwRX1fDbVrMWVwLGsOZgZ90V7ocCvf-Se81E2Z2AkOMj3bG5S0aEKjTakoHFytmQEYTxlPnAzYB8b89MblM99OGTCAzYq8KLHdN04umBbTt6vgFePI2nftHveGIcqN4BBWHL07mtrgcD4Atr1bfoDkgqAU4DKIuoRrweH54ByQkKkErl0HJjGvu3YCJzg1k6iBG8d0wodi2mmYWnsekNcFr-yGzeX1-6U16n8dV70bbQ57bZqIXfQozwpUBNIHi6A7G-EHkU7wmWLTkKTWalV2uWAaQHv5fJb7jlYMokEcER7leUzka_nkIshdFv6mDj-glh0socgia65p6LzdmWYgkrgVZ28EHqiEwrZ19XC9k4vck6IA6XLg93I2ctMavPxUb1zcweTMgqBXF5Hc4aP4pmTf5Bj3_j9AYomANG3loAbmjOHvzTLPJxMQQwShlC9MJ6Uddk8lIn6L8UgzIbEk-h-5bRLRIHk3IeBYCDC6zJZAzo4Hr8EtxAI6u-AoBd-M7CI12gBXCei0p7S58xqTYoabxUKegidgEn3bbjPI0zrv_PrhrWtUEvKt8UimVe6jPv1bS26I0K754PaDTykpwRzQJyI6dUf8k4YafTPIRhqH5cTcLLFlrlw4D1r6SmzxRWq7vgzlZRpPfK7vaC2rvYKA_1RlND4fV9w.-02cBocRommHqhgNLBXw3Q"
#"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0" # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)  # auth with session token

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
    # bot = ChatGPT()
    prompt_number = i%len(prompts)
    prompt = prompts[prompt_number]
    
    resp = api.send_message(prompt) 
    print(F"{i}: {prompt} - {resp}")
    
    data['prompt'].append(prompt_number)
    data['response'].append(resp)
    
    #if resp = %%error%% :
    #    do something... safe Error 
    
    # api.reset_conversation()  # reset the conversation or not after each prompt? 
    if i%10==9:
        assert(len(data['prompt']) == len(data['response']))
        
        df = pd.DataFrame(data) 
        df.to_pickle('joke_prompt_generation_2') 
    
    
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