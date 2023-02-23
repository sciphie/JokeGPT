# after https://github.com/terry3041/pyChatGPT 

from pyChatGPT import ChatGPT
import pandas as pd 
import time, random
from numpy import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


#session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..bTBe1GBvpwfrZGdj.1cWMi-xhZ6VXC7fPQZPYPcg2sWZ8JryVWiV6oTM-8P486twhoHwYX61uX-dCLCH1jsgbyRD-kivnh4yRRjxQOBwwodfO37TDo7oHOPaVFetM-9nrofLjqI_lz5eTQfG3u8V229O_CK25gpMpmKjsUFUAU1dSdT-AGfG6FN6l5EYm3tU0dNwgZSnwHkoz7lChs3EPTppDPLoMKLFUrWKXHR1eWHaD1CxXHvhboUjA4EUpvB6t6eEf-_sK0if_dbCKiVRL4G1YJbzsxWiu6uOfPI7XGF3V6kDPpM3KwHh7ZGZuQM-rIJIdq0frirR9iCEyIzUpzQ1feeCXeZTrmuKtsjhDNdgMD2JSGSOpNAGI8mw2vpAXSWSMqi0DNPjhQmt3MLazVkaz8VJwacAAefEtQN0zq_jP-goS1MId2lIIFeZRfH1shcNB-3sx25S9AIOfyk8-t-hDyis9cxLHTscd6mm1DX1PcN8MMEb9AcIWyC0ZiMtefQVac6UtxdPQWl3HAUe7mjSpwBsiPc1TgKz6wbZl4weYmGBj8ABGOQmrW634WT6Jp4m10KjcLP1mK9xpab-KCRpq1Ns0nyjc2WLLYz4jInPCY-uiFdvhuP_aIdIqhKMvUgjKZPRPJW0rPcLqDx59qCnziFODg215qIX4Wki3m_WHjogJXpvUBNt0bknnWB4xD8WwRlq0i1qBY9QQdx4U47u7A8Jtdu8jmQceWaBQmVi-9PS-eSYRqu4eDeUucIl9J89NTYS-QRVfYAgSnJP-2zGaIQOuj8pv6L0PeviGInmtovTN38JX1T_wdTb8hQMQGqDn1vCB1drEh9ArqSdXYerpa6z7GY0EVqnwQympBqKlfWoLaA8h-CT8iwk466j89UK-9_IJmX575tGs37b118C31PRrrTCca4_d0AerREzDEGOMpzUlV0kFsLiCP2kzEJ-bOOOd8JDrHsa2E9uTj6BZzzCSXf0p0sx8CWP4_ljsMA3OrtcYo3ZvNRzIH4f3QhYSbbVlRmumcTQg4F4bKRvf8yq5EOE4edMdHEoqAUCkZbe4nlHRS4_vzLVR-5mrYAw3tEGo5g7fDCL7kwWo5gmlhdsEsAurkahMqL4jzVt_kt5fSHdc13cowrOw6pG0XRuezuOt8CJ6mE0vtkIQy12BmaIY1kPInwUyyg2p4oywyQgaqb--ydx_Ep6MZ-u7T6IFC79sH1MGtXLld0GzjW5H4VnEqPrmba8LfH55uD0q_kCEH8PoOnwI6yxCfPqbwAwIjwRsOUdQjCOhIdIMVFSMKZgKvEe-507xCRu3R586sGpj3qAol1lzXf-YezOkukwb6uFuXG76tnkwtjGwtpQC1zOXhCrsdv50GLdyw4MaD-b7znDPWvw_vY-0n3EHHS3NmQYfOII6GoiIRqidCvC1mePJs2r2E6vKr22UZkHR8Gv1LVZugkGg-mlOKN4gD1lDADCnx1IMYiiZG2iUfHnRH9e9bnNEuL8NZKeVemIjaWrJuMe1cSmT9B0hR2hDhssVIXqy0lC9Emvk8nnT8s6Mz9KPQc4VcM-nYYEDfxqXXWR9Nllmz29pkXtEbt3_SRq1RbfiYXd-lSIlcklqeQJlGT6aESHsmQDh7zsxIt4703yheiAFzq7fiU6h2qyp_SiWYC5g7EI1w8znOdMbAb5zO8jUlF-MdzGKexZu_ovcNCkUWdjwSY76Up5v7Gaerl_mkgdx-TNFAJ8x1jwhN9p-jkYOhLLOEyGaYBnq53KvcW3dlUy2cbBzOACQWqHdCxVKs2XyXwKvUqiawstTMUaelUIUzU4WDqvPGGKiKeMhMGmk7X_cQKF5r0D3ANsgm9xX_A5Yo-R4HK8jtrmtFu-Kyvf3BmJbnihOn2je50vePUoX4eao2AIh82YPYVUZ9PaCU5bVkPiHFBRhLF3feup-xPZ3FwlOqQN5xdDkN-GMyS5wX_M79BtPBENlHMHxEiGQFUNX895VhCDiye3P8qd53sUu6rg0WO-WpDNMKhSVVkmvncRPXgra-OwRX1fDbVrMWVwLGsOZgZ90V7ocCvf-Se81E2Z2AkOMj3bG5S0aEKjTakoHFytmQEYTxlPnAzYB8b89MblM99OGTCAzYq8KLHdN04umBbTt6vgFePI2nftHveGIcqN4BBWHL07mtrgcD4Atr1bfoDkgqAU4DKIuoRrweH54ByQkKkErl0HJjGvu3YCJzg1k6iBG8d0wodi2mmYWnsekNcFr-yGzeX1-6U16n8dV70bbQ57bZqIXfQozwpUBNIHi6A7G-EHkU7wmWLTkKTWalV2uWAaQHv5fJb7jlYMokEcER7leUzka_nkIshdFv6mDj-glh0socgia65p6LzdmWYgkrgVZ28EHqiEwrZ19XC9k4vck6IA6XLg93I2ctMavPxUb1zcweTMgqBXF5Hc4aP4pmTf5Bj3_j9AYomANG3loAbmjOHvzTLPJxMQQwShlC9MJ6Uddk8lIn6L8UgzIbEk-h-5bRLRIHk3IeBYCDC6zJZAzo4Hr8EtxAI6u-AoBd-M7CI12gBXCei0p7S58xqTYoabxUKegidgEn3bbjPI0zrv_PrhrWtUEvKt8UimVe6jPv1bS26I0K754PaDTykpwRzQJyI6dUf8k4YafTPIRhqH5cTcLLFlrlw4D1r6SmzxRWq7vgzlZRpPfK7vaC2rvYKA_1RlND4fV9w.-02cBocRommHqhgNLBXw3Q"
#session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..6JqTJTIGpm3mUXNG.InLG2wGCED-m78MYHJgSIPOIGGQ0GSezGeghmTzeHXTqTH1FZS099r8uNr7UZXFP2384JnKr5kcuLnlYzO06ixPxeLIL_-p3VKTb8SkplL6vEIoorrcFwx-W4s6bbGPaTsb0quJCalG-Ax_8DSQv5_iCHMpyDtXXDYei9Vui75kb9Y1Rf_Aw89HvBeorQHi7ikiI1YMIgZdV79eeZh97rbjeINuak0ua-MQcReXYnkZsU3lKPJ2LmngpX3v0iaq2-5tUJ3kU9-t9yOCkM-1wVzkcOw1OKcRJ0_8ozkUUp4MfImFbSxZMwBvYMivSQYFxX2vgn1BA5p3xmemAWjbQyOdigmpcARFgqfyRXy0Ts6gCnXTJH9WaejBs7n_kUjesDUZgJmT1AbnjkIWT3HaDiIp0-UT3uM27EBVZUWRRuS6ASmjs1DcMqHvCGAPdNijOM0-JBIYU3MkYBZ6LmSSFpbLXh074ACOh6RVLnMwlpHezGgqIC1VNJuEgwTaXYIoiqx98IVc-62D1lE9ELFZJ8f2VaF-R41yASEbJ2Jd9SZUeexW4dSkPCGEEWok49na-jOG-WELCKAuWcvnOdenNKi745jl2agNNeGw9t1H9h0k82qZ_1QzAi5ZqO1AmIi1CqZ3g4n-yL6oDU3Tg56gFpdsxaYex9X1MQK5p3Wmxb8wojdMsRSWEEQ4bJjfiS5YcIlzA7BT2NbdL0bjrZOa8lHsrGty9vPDvDfnniywfEBwO3H-MawhJ7vL19EnHZs8LLSWkrsf9m7NtJ9Q3b9RyiCtDHGuJRndUx7upT3hlufPLAc0qIfyXHGxcJTMsnaexKcTOYHJTcNi-4fRb2hqdefxk1aiQmgS1qpvh_rwepgiAA11O7qqMqqbaguJlESMW6PUflNW9zMbZrOfs4AHfz6T_s8IbI3c-xTl4n0bYAo140yUEOege17YgB41LImqunGJuDT1rfxDaN8c-q7y7eThRKAWkLZoQwks7zkYM4NBnRgCg_YTkW1DIiDl3NKcKz8SyUJCVkbJkAKI6sF6Q9a_1LJGAr4ybA9Dopjq_d95_foAWvDYSKcitKVjI3TQuSrNsxvtGV6WAcjoRt8qOamAtghMF1Aj-64Yxh82DZMRz4VFoSCJ8LiolJc1g1JGM1-JVzQtKDuFMZy3rWl3A8CxCR-PCTEuvyu08qJJtS0JNk9vgXNk2xn0YJVCRNNYgD-S8Dnx-Fzvt9HVV3_dhaJ9eS41X08_IQbqb7_FbO5cHkrRPjUn051Z7sV4yb25j6N5AMfz1UgA02xLX4QX1S4t2dRqYkx3pcmd5-tXH7lZ5q4OGFTWrhtovu40Hcqw039Uyt4ggyqDsDNvfZZeZLxUqJuGtrCvs9wMkbafJk5Ph0rzqAeTIO5y1XPlQMmvHjL_4Sk5eYwzNtc4E9RzpVrY2QPbRpYjCiljC-pMvlfq2CiVt4UebKo1CR8XHoU8n9AIboywaqQTGUwz-fraY_cQ3nq1lXnkZ2yc2vU2n5snLS15K5YlJvBJieZvY5BxDNAFHwKeUgZnGW34Nyy48SYkQK09kGINN_qjmY9o0PL7N36vj-OCUmawYRyPZqeGTE1i6DsSFEPxJ3j0qvZDe4-hvKB7LlbQDGdbW3k6myE-3C2LEY4tb_qj9xAir_iZPLbw0y7L4M7f12EzPDyfoQbzniClz9lVw6ETUwEGX-nJX9J_J2_8UEvmtGNrT2jF514Hhx5_KgQtJYQvvccbJext8KtuVTJ_fk4TJ7GnwZcr5uMgjwd-e8ZK0YxTfpvc_zHzP7egiA_lCM0_cbMbZwejMYiyM-lxpbMApYAhNT6F8VTNJOQhxcGgTrwG94243mh0EMWUYghxKt49mxE2ZgSsLy5ZeksrfacQSfniI2eq-AZ6XG0EnFtMjzQYcRfqgWygbbSIFM5F0OqycCZTizUS-tzZzCCJdT5xXSrT7vHT5CUo4f4E_WdCLPeQyneowA_6MxiyNXGd_yWpohDkvjlKDQCSpOhACNVDXnO1hzKxSY7kF7kC3G4TOOJCbQiOavCNoJtD2xcTAkwaPtrNZOjm73SqjBG001rwQpNGT1P5MLuryOn6UlQfBKnkgqwuDaLkm1HUS6H-cw5mM-boskpH9ezMV_dOv_1IHka5B-u0I8C7AyNxAk-PCR-aPfXD-lKxWQvJxrrmNqGEQ9Z7zB2kZqQZCW2KSYbrNWsk-aYf6UNbNlY0d-OFWefQZmAqR5222rOSR-rGa7WMVtwb6yJG8FYG7qdrurIqsXVcJ8vWuYKmEZsK5SZ6tbqjrv4TDVaOEQtih5-0v1fn2j9EXb0Nx0A-kDqKai9Rug0iEzA98OU6JVH9jnhWqt1ar5k8B2YrqvpIbmQr1eo4Xpy5oH0i0vbbfcLcn9xgL7Vrf8LBdNjStDC8TyGPg_i-XL7ShFC3vQj6kOHS_TImeYo7aka4JQXogF3I1chxeh36QiorULzFNdzVEb-PsA5fgeFfndf3NSuT0hG0Q9fgmR5eX-iY7X-zD1jt6M59q9LRhfo7cMO3_DwTP2DhFfeS8zRdkNS1xcEwsXVhZm7hOCdzz42AJxtbYQ2nWh_FennMXEiSucHnMWyL4ngWlRuSRSoNyMyOFmxOvHjJEP4MBec63k_Ti5eDF8JU2FBkdF2eY2cdlhfCShz6zvILv9Pwtaly0xqn8UxkDDJeWGcqqoRAI9wxORkjbYhMX._nYJzk19w7JO_BAUTCN0lA"
session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..1TXVaoJMznQjYgyw.nRJJ3YJEro-M0PDUE67JISyPqMFzeie6yLL_GH85ahGpUF71tdXamnHS1rdfLJUD129NKbw47ZS9ZMhK-sFtTjMLiQGnTy7an6sEpbVB0UQRC2HNUfGtWdLunsa4rkOZLKBK8CAcOW3n67YW8vntiRBpk2reZTfP0kH3ZrBa1LpJuDOP2vE5SELaAoxzBG-v3Luf3QjrYw0YiJh141hxCOxOroYAIM8l86xAPg4c_lcEJCkmqRPDSncAfDAXjAF6p5Ohzrue-d1eVJZpapxf1O7EmIJamBLbHX55l7XKJMtl0FVLnfJGoHoE-L9cwElvTKQt2wDSULA_jjiZGCwqnOsJ9xm3aXdsHEKrXS6hC4wMfzIj-ImSmPYQB_2-YfCLwP-SjAYWH5qcKwDhViLmx8cwfKHL22trLoUaOHdIaQEBAN_Lbvce12GOTsvDzgwss5mOHjhcssHtQvCifRHr0c02UuhURvbbegdlkrSsD7C0PQPIEGiCyBOhvmM_7wSdg4gKdjTtC5prn_sKHOL40n7sGnDMVuucxtppiS72W-pDN2FVAkKHAwUW1CDO8BCnmT6jJK1jlPFQHC4VcukGdJq8zQExahAzklw1Bp651_nRRmpy2pfeyOT90qGtVaeFWT7uXzjdXTzJsSiXlOoe17xbN-TZOtUAAo9pNj8gjpAtYnyYJTrqC8Sdcw7bEUARllJLHUhGSJyksYOnLElw2QGPYMPiZQ-kEkwlfTt7SYV_Bz4UGRCyV1lNkmUc8ZL2s46tX0bcRhcO3J0kbzDtpWn5JYG3hBijknfBtTpg9Bul09nOtdLLOvaqEkzyBdoMYEoEiMLh19J2zhYcNO6az6FzyvfFfeAEH7LJDS4ruy-Q0WX8-swQ2eVkQ0JZSJRvtfkpvYCoUmRHIoUUrG_pVxilcmom4rRji6LZVTasCA5ke9-bXluxUppFVaGFJrDDeVBXaRsT_ur5J1SmiI7x07fst25nTl4an8v33YjXiJ_7D96lRaHeyCgXTTJTMzm-3wADAopYQqXaMkFAHVwpa60M_4cQuxNvmgU1Kgwy95KCwgv93pmLXqjf8dt0nePOBST92po6Czb8F84gmH3ujyWzKvSOoqVKr68htZ-mBqGcirErdIOsGRfZCjGvzCQCaRq7Q9Ohr_N98Ve1OMQ4jGuetM56YLGXOoKwTT5l8AvV-HItNib56N0JFNGL9zt3ni_UXcOKTNjUQ5C7QFBkPvGBek9EBMDxFU0Po6_6sATiXe-LFvoT01lpHHfV8lG7iOl_qfdJphlFrarV6BV29weS91IvfxisLGOZKTpyBT7beHO1tzfpiOKTNPZALJsYGzn-RUlU8SB40CN-kBtnrQamvubgzkCiuwcN-QRV_3AllGFRg7Cf3q7s7HIBTj9akZoKxrsS9ZjOVuzHZhuUKOkvK5tkzpANViBJPu3hBflDuTbc7GYsxOUUmuJYmFQbg1piiExDtcXXgmVYhywTArLbBnlltaZEfIk1P-C1X7eo2yFMf9GIh2frjMdqg7zf5xezo7A4wWHWH7cNk3IdDFoiPEAfioVjCJ45aiMqiCTUnkz5ABdV8LV25Z1dJl0w2IUpsMrx6L2RzZTDR7SEGbFWf-rWWi2zv-pDx0rlzAH74BBd9yE6dYpnvft3ueb8g1EqKWZmI-_WCOU_dJJa04YRvED-a4IdQj3Yw-XPIOXwexTRLGFzbFrr7HScIAAank0TvJlKTbXOMfwlJjGs8O6NslGiEvBqwTLES_Vn3HFrdxlTbXN1CpIVVT7ra7lPY_Jow9xksxYPgTyWyMFeAeuwhgwlpnBtPNJ5wXav4TuipL-w8OQghcMMcO7Y7qB472_786RnAKyoibcZdkVBNjJal6Q2IpcFlRhOOK95G7QTXtbNls7vrrdPZ6mUIubey26WoaeCuuIOF8vyYnrYRshqVKMTUiHwJKjx6iLl53qQm8q_3LMQdv_IMfu5iyO-9zaD_y9pWQkDXhz5E55SEwbACdmC4Bz1TagpX_rDXhamOJojMuYfGt90C3gHA1-vtjaFMj64bsiJ1aOSSvG-4QhVrMqD0yea5zYG75burNvdz_NIRCz5wf58NTdvoIdhxDUbpN7JpT3TG8DwaNQtisbIkQ6ykwQDnlepx-nGmfnwm6F6D1SlcBQZY3A2rASIyDKWL8rvqX_A1g4HkGRtmgioDeYX8QufuUXc2pjdjRMnVJDQz14WMB05zK-FO6QGr9naSmgQUaP5ZZXalTRba9aOoVq5HxT-jifokOs13ztMGb2YI0A21Wy_TKFBb_yIZ4I0qojDk2Gjks65_2tC63aU3WeBc_ykWl7vvLB8QJrn5pdFjg_tkxl0CVq5r-myBmu0tY2XB6oMkEtuQlPEbzwbI7utpItaJz4ofKol-cJWcvr3EBqPSBL3rBOrdyX4WSG-n8zUCMfI45kEP-TzdGEd3QWUwi2_TEnmSYFmsKJb_gt6CAxXfWByvRfPGSHx4rpj2Ni14ZC_ohMoRZAJcO6lEIvVsXyNX30dzu6wqs3gX6mwus1teXZC7SWcr3TmajSfk2t-SwdJ-WqK9gx7rWuErBFk2NAEDJCaoh9OrTyRj2xnu5pNQrFizSLhR7UipWSKTeOkoTBAqIlgHhIfmSaW-IIzaubLg2TNts7ckDQRPO9BMW0MnO3qKuyK.4pkkPVJh9wDqvNmAMW63Ug"

#"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0" # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)# conversation_id="d9debae4-854a-43e4-8b92-4e593795c820")  # auth with session token

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why was the math book sad? Because it had too many problems.",
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why did the cookie go to the doctor? Because it was feeling crumbly.",
    "Why couldn't the bicycle stand up by itself? Because it was two-tired.",
    "Why did the frog call his insurance company? He had a jump in his car.",
    "Why did the chicken cross the playground? To get to the other slide.",
    "Why was the computer cold? Because it left its Windows open.",
    "Why did the hipster burn his tongue? He drank his coffee before it was cool.",
    "Why don't oysters give to charity? Because they're shellfish.",
    "Why did the computer go to the doctor? Because it had a virus.",
    "Why did the banana go to the doctor? Because it wasn't peeling well.",
    "Why did the coffee file a police report? Because it got mugged.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why did the man put his money in the freezer? He wanted cold hard cash.",
    "Why don't seagulls fly over the bay? Because then they'd be bagels.",
    "Why did the chicken go to the seance? To talk to the other side.",
    "Why was the belt sent to jail? Because it held up a pair of pants.",
    "Why did the chicken cross the road? To get to the other side.",
    "Why did the computer go to the doctor? Because it had a byte.",
    "Why did the cow go to outer space? To see the moooon.",
    "Why did the man put his money in the blender? He wanted to make liquid assets.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call an alligator in a vest? An investigator.",
]

jokes_onesen = [
    "The scarecrow won an award because he was outstanding in his field.",
    "The tomato turned red because it saw the salad dressing.",
    "The math book was sad because it had too many problems.",
    "Scientists don't trust atoms because they make up everything.",
    "The cookie went to the doctor because it was feeling crumbly.",
    "The bicycle couldn't stand up by itself because it was two-tired.",
    "The frog called his insurance company because he had a jump in his car.",
    "The chicken crossed the playground to get to the other slide.",
    "The computer was cold because it left its Windows open.",
    "The hipster burned his tongue because he drank his coffee before it was cool.",
    "Oysters don't give to charity because they're shellfish.",
    "The computer went to the doctor because it had a virus.",
    "The banana went to the doctor because it wasn't peeling well.",
    "The coffee filed a police report because it got mugged.",
    "The golfer brings two pairs of pants in case he got a hole in one.",
    "The man put his money in the freezer because he wanted cold hard cash.",
    "Seagulls don't fly over the bay because then they'd be bagels.",
    "The chicken went to the seance to talk to the other side.",
    "The belt was sent to jail because it held up a pair of pants.",
    "The chicken crossed the road to get to the other side.",
    "The computer went to the doctor because it had a byte.",
    "The cow went to outer space to see the moooon.",
    "The man put his money in the blender because he wanted to make liquid assets.",
    "Skeletons don't fight each other because they don't have the guts.",
    "An alligator in a vest is called an investigator.",
]

no_jokes = [
    "Why did the scarecrow win an award? Because he did very good work.",
    "Why did the tomato turn red? Because it had a lot sun recently.",
    "Why was the novel sad? Because it had too many problems.",
    "Why don't scientists trust atoms? Because they lied before.",
    "Why did the cookie go to the doctor? Because it was feeling unwell.",
    "Why couldn't the bicycle stand up by itself? Because it didn't have racks",
    "Why did the frog call his insurance company? He had a scratch in his car.",
    "Why did the kid cross the playground? To get to the slide.", 
    "Why was the computer cold? Because the was broken.",
    "Why did the hipster burn his tongue? He drank too hot coffee.",
    "Why don't oysters give to charity? Because they cannot walk.",
    "Why did the computer go to the doctor? Because it was sick.",
    "Why did the banana go to the doctor? Because it was sick.",
    "Why did the coffee file a police report? Because it got robbed.",
    "Why did the swimmer bring two pairs of pants? In case he got a hole in one.", ##########
    "Why did the man put his money in the piggy bank? To save some cash.", ##########
    "Why don't seagulls fly over the bay? Because then are mostly living in ports.", #############
    #"Why did the chicken go to the seance? To talk to the other side.", ########
    "Why was the belt sent to jail? Because it stole a pair of pants.",
    #"Why did the chicken cross the road? To get to the other side.", ######
    "Why did the computer go to the doctor? Because it wasn't feeling well.",
    "Why did the chicken go to outer space? To see the moon.",
    "Why did the man put bananas in the blender? He wanted to make a smoothie.", #####
    "Why don't skeletons fight each other? They are quite peaceful.",
    "Why don't skeletons fight each other? They are dead already.",
    "Why did the boy win an award? Because he did very good work.",
    "Why did the man turn red? Because he saw the neighbour dressing.",
    "Why was the child sad? Because it had too many problems.",
    "Why don't scientists trust journalists? Because they make up everything.",
    "Why did the woman go to the doctor? Because it was feeling crumbly.",
    "Why couldn't the kid stand up by itself? Because it was too tired.",
    "Why did the driver call his insurance company? He had a jump in his car.",
    "Why did the cild cross the playground? To get to the slide.", 
    "Why was the woman cold? Because she left its Windows open.",
    "Why did the coworker burn his tongue? He drank his coffee before it was cool.",
    "Why don't millionaire give to charity? Because he is selfish.",
    "Why did the man go to the doctor? Because he had a virus.",
    "Why did the teacher go to the doctor? Because he wasn't peeling well.",
    "Why did the driver file a police report? Because she got mugged.",
    "Why did the athlete bring two pairs of pants? In case one gets dirty.", ###
    "Why did the man put his money in the freezer? To hide it from intruders.", ##########
    "Why don't seagulls fly over the bay? Because then are mostly living in ports.", #############
    "Why did the daughter go to the seance? To talk to the other side.", ########
    "Why was the cashier sent to jail? Because she held up a pair of pants.",
    "Why did the man cross the road? To get to the other side.", ######
    "Why did the man go to the doctor? Because he had a bite.",
    "Why did the astronaut go to outer space? To see the moon.",
    "Why did the man put bananas in the blender? He wanted to make a smoothie.", #####
    "Why don't schoolboys fight each other? They don't have the guts.",
    "What do you call an man in a vest? A vest wearer.", 
    "Why was the computer cold? Because the heater was broken.",
    "Why was the computer cold? Because it was winter.",
    "Why was the student cold? Because the heater was broken.",
    "Why was the student cold? Because it was winter.",
    "Why did the teacher go to the doctor? Because he wasn't peeling well.",
    "Why don't oysters give to charity? Because they have no money.",
]


all = jokes + jokes_onesen + no_jokes
random.shuffle(all)
#print(all)
#    "Why did the man put his money in the freezer? He wanted cold hard cash.",
 #   "Why don't seagulls fly over the bay? Because then they'd be bagels.",
    
  #  "Why did the man put his money in the blender? He wanted to make liquid assets.",


#prompts = [F"Can you explain why this joke is funny: \n\n {j}" for j in jokes]

#bot = ChatGPT()
#n = 1100 # number of generated jokes 
path = 'joke_detection_allshuffle'############################################################################
try:
    df = pd.read_pickle(path)
except:
    # create dataframe and 
    df = pd.DataFrame({"prompt": [], "response": []})
    df.to_pickle(path)
print(df.shape)
#print(prompts)
#print('####', df.shape[1])

# i = df.shape%len(prompts)
j = 0 # max prompt per hour 
n = 100
i = 0
for elem in all: ############################################################################
    print(i, n-df.shape[0])
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
    df = pd.read_pickle(path)
    #prompt_number = df.shape[0]%len(prompts)
    #print(prompt_number)
    prompt = F'What kind of sentence is that: {elem}'
    
    try:
        resp = api.send_message(prompt) 
        # print(i ==df.shape[1]+1) # this does not work whith multiple iterations
        print(F"{i}: {prompt} - {resp}")
        
        data = {"prompt": [prompt], "response": [resp]}
        df2 = pd.DataFrame(data)
        df = pd.concat([df,df2])
        df.to_pickle(path) 
        time.sleep(3)
        i+=1
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

print("### reached the end ###")

    