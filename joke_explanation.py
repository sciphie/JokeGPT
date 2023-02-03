# after https://github.com/terry3041/pyChatGPT 

from pyChatGPT import ChatGPT
import pandas as pd 
import time

from numpy import random

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..bTBe1GBvpwfrZGdj.1cWMi-xhZ6VXC7fPQZPYPcg2sWZ8JryVWiV6oTM-8P486twhoHwYX61uX-dCLCH1jsgbyRD-kivnh4yRRjxQOBwwodfO37TDo7oHOPaVFetM-9nrofLjqI_lz5eTQfG3u8V229O_CK25gpMpmKjsUFUAU1dSdT-AGfG6FN6l5EYm3tU0dNwgZSnwHkoz7lChs3EPTppDPLoMKLFUrWKXHR1eWHaD1CxXHvhboUjA4EUpvB6t6eEf-_sK0if_dbCKiVRL4G1YJbzsxWiu6uOfPI7XGF3V6kDPpM3KwHh7ZGZuQM-rIJIdq0frirR9iCEyIzUpzQ1feeCXeZTrmuKtsjhDNdgMD2JSGSOpNAGI8mw2vpAXSWSMqi0DNPjhQmt3MLazVkaz8VJwacAAefEtQN0zq_jP-goS1MId2lIIFeZRfH1shcNB-3sx25S9AIOfyk8-t-hDyis9cxLHTscd6mm1DX1PcN8MMEb9AcIWyC0ZiMtefQVac6UtxdPQWl3HAUe7mjSpwBsiPc1TgKz6wbZl4weYmGBj8ABGOQmrW634WT6Jp4m10KjcLP1mK9xpab-KCRpq1Ns0nyjc2WLLYz4jInPCY-uiFdvhuP_aIdIqhKMvUgjKZPRPJW0rPcLqDx59qCnziFODg215qIX4Wki3m_WHjogJXpvUBNt0bknnWB4xD8WwRlq0i1qBY9QQdx4U47u7A8Jtdu8jmQceWaBQmVi-9PS-eSYRqu4eDeUucIl9J89NTYS-QRVfYAgSnJP-2zGaIQOuj8pv6L0PeviGInmtovTN38JX1T_wdTb8hQMQGqDn1vCB1drEh9ArqSdXYerpa6z7GY0EVqnwQympBqKlfWoLaA8h-CT8iwk466j89UK-9_IJmX575tGs37b118C31PRrrTCca4_d0AerREzDEGOMpzUlV0kFsLiCP2kzEJ-bOOOd8JDrHsa2E9uTj6BZzzCSXf0p0sx8CWP4_ljsMA3OrtcYo3ZvNRzIH4f3QhYSbbVlRmumcTQg4F4bKRvf8yq5EOE4edMdHEoqAUCkZbe4nlHRS4_vzLVR-5mrYAw3tEGo5g7fDCL7kwWo5gmlhdsEsAurkahMqL4jzVt_kt5fSHdc13cowrOw6pG0XRuezuOt8CJ6mE0vtkIQy12BmaIY1kPInwUyyg2p4oywyQgaqb--ydx_Ep6MZ-u7T6IFC79sH1MGtXLld0GzjW5H4VnEqPrmba8LfH55uD0q_kCEH8PoOnwI6yxCfPqbwAwIjwRsOUdQjCOhIdIMVFSMKZgKvEe-507xCRu3R586sGpj3qAol1lzXf-YezOkukwb6uFuXG76tnkwtjGwtpQC1zOXhCrsdv50GLdyw4MaD-b7znDPWvw_vY-0n3EHHS3NmQYfOII6GoiIRqidCvC1mePJs2r2E6vKr22UZkHR8Gv1LVZugkGg-mlOKN4gD1lDADCnx1IMYiiZG2iUfHnRH9e9bnNEuL8NZKeVemIjaWrJuMe1cSmT9B0hR2hDhssVIXqy0lC9Emvk8nnT8s6Mz9KPQc4VcM-nYYEDfxqXXWR9Nllmz29pkXtEbt3_SRq1RbfiYXd-lSIlcklqeQJlGT6aESHsmQDh7zsxIt4703yheiAFzq7fiU6h2qyp_SiWYC5g7EI1w8znOdMbAb5zO8jUlF-MdzGKexZu_ovcNCkUWdjwSY76Up5v7Gaerl_mkgdx-TNFAJ8x1jwhN9p-jkYOhLLOEyGaYBnq53KvcW3dlUy2cbBzOACQWqHdCxVKs2XyXwKvUqiawstTMUaelUIUzU4WDqvPGGKiKeMhMGmk7X_cQKF5r0D3ANsgm9xX_A5Yo-R4HK8jtrmtFu-Kyvf3BmJbnihOn2je50vePUoX4eao2AIh82YPYVUZ9PaCU5bVkPiHFBRhLF3feup-xPZ3FwlOqQN5xdDkN-GMyS5wX_M79BtPBENlHMHxEiGQFUNX895VhCDiye3P8qd53sUu6rg0WO-WpDNMKhSVVkmvncRPXgra-OwRX1fDbVrMWVwLGsOZgZ90V7ocCvf-Se81E2Z2AkOMj3bG5S0aEKjTakoHFytmQEYTxlPnAzYB8b89MblM99OGTCAzYq8KLHdN04umBbTt6vgFePI2nftHveGIcqN4BBWHL07mtrgcD4Atr1bfoDkgqAU4DKIuoRrweH54ByQkKkErl0HJjGvu3YCJzg1k6iBG8d0wodi2mmYWnsekNcFr-yGzeX1-6U16n8dV70bbQ57bZqIXfQozwpUBNIHi6A7G-EHkU7wmWLTkKTWalV2uWAaQHv5fJb7jlYMokEcER7leUzka_nkIshdFv6mDj-glh0socgia65p6LzdmWYgkrgVZ28EHqiEwrZ19XC9k4vck6IA6XLg93I2ctMavPxUb1zcweTMgqBXF5Hc4aP4pmTf5Bj3_j9AYomANG3loAbmjOHvzTLPJxMQQwShlC9MJ6Uddk8lIn6L8UgzIbEk-h-5bRLRIHk3IeBYCDC6zJZAzo4Hr8EtxAI6u-AoBd-M7CI12gBXCei0p7S58xqTYoabxUKegidgEn3bbjPI0zrv_PrhrWtUEvKt8UimVe6jPv1bS26I0K754PaDTykpwRzQJyI6dUf8k4YafTPIRhqH5cTcLLFlrlw4D1r6SmzxRWq7vgzlZRpPfK7vaC2rvYKA_1RlND4fV9w.-02cBocRommHqhgNLBXw3Q"
#session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..bTBe1GBvpwfrZGdj.1cWMi-xhZ6VXC7fPQZPYPcg2sWZ8JryVWiV6oTM-8P486twhoHwYX61uX-dCLCH1jsgbyRD-kivnh4yRRjxQOBwwodfO37TDo7oHOPaVFetM-9nrofLjqI_lz5eTQfG3u8V229O_CK25gpMpmKjsUFUAU1dSdT-AGfG6FN6l5EYm3tU0dNwgZSnwHkoz7lChs3EPTppDPLoMKLFUrWKXHR1eWHaD1CxXHvhboUjA4EUpvB6t6eEf-_sK0if_dbCKiVRL4G1YJbzsxWiu6uOfPI7XGF3V6kDPpM3KwHh7ZGZuQM-rIJIdq0frirR9iCEyIzUpzQ1feeCXeZTrmuKtsjhDNdgMD2JSGSOpNAGI8mw2vpAXSWSMqi0DNPjhQmt3MLazVkaz8VJwacAAefEtQN0zq_jP-goS1MId2lIIFeZRfH1shcNB-3sx25S9AIOfyk8-t-hDyis9cxLHTscd6mm1DX1PcN8MMEb9AcIWyC0ZiMtefQVac6UtxdPQWl3HAUe7mjSpwBsiPc1TgKz6wbZl4weYmGBj8ABGOQmrW634WT6Jp4m10KjcLP1mK9xpab-KCRpq1Ns0nyjc2WLLYz4jInPCY-uiFdvhuP_aIdIqhKMvUgjKZPRPJW0rPcLqDx59qCnziFODg215qIX4Wki3m_WHjogJXpvUBNt0bknnWB4xD8WwRlq0i1qBY9QQdx4U47u7A8Jtdu8jmQceWaBQmVi-9PS-eSYRqu4eDeUucIl9J89NTYS-QRVfYAgSnJP-2zGaIQOuj8pv6L0PeviGInmtovTN38JX1T_wdTb8hQMQGqDn1vCB1drEh9ArqSdXYerpa6z7GY0EVqnwQympBqKlfWoLaA8h-CT8iwk466j89UK-9_IJmX575tGs37b118C31PRrrTCca4_d0AerREzDEGOMpzUlV0kFsLiCP2kzEJ-bOOOd8JDrHsa2E9uTj6BZzzCSXf0p0sx8CWP4_ljsMA3OrtcYo3ZvNRzIH4f3QhYSbbVlRmumcTQg4F4bKRvf8yq5EOE4edMdHEoqAUCkZbe4nlHRS4_vzLVR-5mrYAw3tEGo5g7fDCL7kwWo5gmlhdsEsAurkahMqL4jzVt_kt5fSHdc13cowrOw6pG0XRuezuOt8CJ6mE0vtkIQy12BmaIY1kPInwUyyg2p4oywyQgaqb--ydx_Ep6MZ-u7T6IFC79sH1MGtXLld0GzjW5H4VnEqPrmba8LfH55uD0q_kCEH8PoOnwI6yxCfPqbwAwIjwRsOUdQjCOhIdIMVFSMKZgKvEe-507xCRu3R586sGpj3qAol1lzXf-YezOkukwb6uFuXG76tnkwtjGwtpQC1zOXhCrsdv50GLdyw4MaD-b7znDPWvw_vY-0n3EHHS3NmQYfOII6GoiIRqidCvC1mePJs2r2E6vKr22UZkHR8Gv1LVZugkGg-mlOKN4gD1lDADCnx1IMYiiZG2iUfHnRH9e9bnNEuL8NZKeVemIjaWrJuMe1cSmT9B0hR2hDhssVIXqy0lC9Emvk8nnT8s6Mz9KPQc4VcM-nYYEDfxqXXWR9Nllmz29pkXtEbt3_SRq1RbfiYXd-lSIlcklqeQJlGT6aESHsmQDh7zsxIt4703yheiAFzq7fiU6h2qyp_SiWYC5g7EI1w8znOdMbAb5zO8jUlF-MdzGKexZu_ovcNCkUWdjwSY76Up5v7Gaerl_mkgdx-TNFAJ8x1jwhN9p-jkYOhLLOEyGaYBnq53KvcW3dlUy2cbBzOACQWqHdCxVKs2XyXwKvUqiawstTMUaelUIUzU4WDqvPGGKiKeMhMGmk7X_cQKF5r0D3ANsgm9xX_A5Yo-R4HK8jtrmtFu-Kyvf3BmJbnihOn2je50vePUoX4eao2AIh82YPYVUZ9PaCU5bVkPiHFBRhLF3feup-xPZ3FwlOqQN5xdDkN-GMyS5wX_M79BtPBENlHMHxEiGQFUNX895VhCDiye3P8qd53sUu6rg0WO-WpDNMKhSVVkmvncRPXgra-OwRX1fDbVrMWVwLGsOZgZ90V7ocCvf-Se81E2Z2AkOMj3bG5S0aEKjTakoHFytmQEYTxlPnAzYB8b89MblM99OGTCAzYq8KLHdN04umBbTt6vgFePI2nftHveGIcqN4BBWHL07mtrgcD4Atr1bfoDkgqAU4DKIuoRrweH54ByQkKkErl0HJjGvu3YCJzg1k6iBG8d0wodi2mmYWnsekNcFr-yGzeX1-6U16n8dV70bbQ57bZqIXfQozwpUBNIHi6A7G-EHkU7wmWLTkKTWalV2uWAaQHv5fJb7jlYMokEcER7leUzka_nkIshdFv6mDj-glh0socgia65p6LzdmWYgkrgVZ28EHqiEwrZ19XC9k4vck6IA6XLg93I2ctMavPxUb1zcweTMgqBXF5Hc4aP4pmTf5Bj3_j9AYomANG3loAbmjOHvzTLPJxMQQwShlC9MJ6Uddk8lIn6L8UgzIbEk-h-5bRLRIHk3IeBYCDC6zJZAzo4Hr8EtxAI6u-AoBd-M7CI12gBXCei0p7S58xqTYoabxUKegidgEn3bbjPI0zrv_PrhrWtUEvKt8UimVe6jPv1bS26I0K754PaDTykpwRzQJyI6dUf8k4YafTPIRhqH5cTcLLFlrlw4D1r6SmzxRWq7vgzlZRpPfK7vaC2rvYKA_1RlND4fV9w.-02cBocRommHqhgNLBXw3Q"
#"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0" # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)# conversation_id="d9debae4-854a-43e4-8b92-4e593795c820")  # auth with session token

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the tomato turn red? Because it saw the salad dressing.", 
    "Why was the math book sad? Because it had too many problems.",
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "Why did the frog call his insurance company? He had a jump in his car.",
    "Why did the chicken cross the playground? To get to the other slide.",
    "Why did the cookie go to the doctor? Because it was feeling crumbly",
    "Why was the computer cold? Because it left its Windows open.",
    "Why did the hipster burn his tongue? He drank his coffee before it was cool."
    "Why did the computer go to the doctor? Because it had a virus.",
    "Why did the banana go to the doctor? Because it wasn't peeling well.",
    "Why did the coffee file a police report? Because it got mugged.",
    "Why don't oysters give to charity? Because they're shellfish.",
    "Why couldn't the bicycle stand up by itself? Because it was two-tired.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why did the man put his money in the freezer? He wanted cold hard cash.",
    "Why don't seagulls fly over the bay? Because then they'd be bagels.",
    "Why was the belt sent to jail? Because it held up a pair of pants.",
    "Why did the cow go to outer space? To see the moooon.",
    "Why did the man put his money in the blender? He wanted to make liquid assets.",
]

prompts = [F"Can you explain why this joke is funny: \n\n {j}" for j in jokes]

#bot = ChatGPT()
#n = 1100 # number of generated jokes 
path = 'joke_explanation'
try:
    df = pd.read_pickle(path)
except:
    # create dataframe and 
    df = pd.DataFrame({"prompt": [], "response": []})
    df.to_pickle(path)
print(df.shape)

#print('####', df.shape[1])

# i = df.shape%len(prompts)
j = 0 # max prompt per hour 
n = 100
for i in range(n-df.shape[1]): 
    j += 1
    if j > 74:
        print("Reached max. Sleep for one hour.")
        time.sleep(900)
        print("15 minutes passed.")
        time.sleep(900)
        print("Half an hour left")
        time.sleep(900)
        print("15 more minutes.")
        time.sleep(900)
        j = 1
    print('new loop')

#while(df.shape[1]<=1000):
    df = pd.read_pickle(path)
    # bot = ChatGPT()
    prompt_number = df.shape[1]%len(prompts)
    #prompt_numbers_left = [,7,,7,7,7,2,2,2,3,3,4,4]
    #prompt_number = random.choice(prompt_numbers_left)
    print(prompt_number)
    prompt = prompts[prompt_number]
    
    try:
        resp = api.send_message(prompt) 
        # print(i ==df.shape[1]+1) # this does not work whith multiple iterations
        print(F"{i}: {prompt} - {resp}")
        
        data = {"prompt": [prompt], "response": [resp]}
        df2 = pd.DataFrame(data)
        df = pd.concat([df,df2])
        df.to_pickle(path) 
        time.sleep(3)
    except TimeoutException as ex:
        print(F"Oops! {ex}")
        api.refresh_chat_page()
        time.sleep(3)
    except ValueError as err:
        print(F"Oops! {err}")
        print(type(err))
        if "Too many requests" in str(err): 
            print(err)#)"I'll try again in 15 Minutes")
            #time.sleep(900)
            #api.refresh_chat_page()
            #raise
        if "Only one message at a time":
            i=i-1
            #raise
        else: 
            print(F'something else: {err}')

print("### reached 1000 examples ###")

    

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