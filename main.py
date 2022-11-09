import config 
from telegram.ext import *
import responses as R 
import requests
#import json

print("bot started...")


name = 'PapaToken'
symbol = 'Papa'
address2 = '0x18f1f69fe1d80c8ff9472bc5387ff7b40e34c860' #papa contract address
chartA = "https://poocoin.app/tokens/" + address2
buyPancake = "https://exchange.pancakeswap.finance/#/swap?outputCurrency=" + address2

twitter = "https://twitter.com/papaexchange"
contract = "https://bscscan.com/address/" + address2

helpcommands = " Type : /papa, /shill, /chart , /buy, /contract or /helpPapa to see this message again"


def start_command(update, context):
    update.message.reply_text('start shilling on /biz')


def help_command(update, context):
    update.message.reply_text(helpcommands)


def get_tokenInfo(update, context):
   
    def run_query(query):  # A simple function to use requests.post to make the API call.
        headers = {'X-API-KEY': config.api}
        request = requests.post('https://graphql.bitquery.io/',
                                json={'query': query}, headers=headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                            query))


    # The GraphQL query to get the latest token price

    query = """
            {
            ethereum(network: bsc) {
                dexTrades(
                options: {desc: ["block.height","tradeIndex"], limit: 1}
                exchangeName: {in: ["Pancake", "Pancake v2"]}
                baseCurrency: {is: "0x18f1f69fe1d80c8ff9472bc5387ff7b40e34c860"}
                ) {
                transaction {
                    hash
                }
                tradeIndex
                smartContract {
                    address {
                    address
                    }
                    contractType
                    currency {
                    name
                    }
                }
                tradeIndex
                block {
                    height
                }
                baseCurrency {
                    symbol
                    address
                }
                quoteCurrency {
                    symbol
                    address
                }
                quotePrice
            
                }
            }
            }
        """
    result = run_query(query)  # Execute the query

    url = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd').json()

    binance = url['binancecoin']['usd']

    priceBnb = format(result['data']['ethereum']['dexTrades'][0]['quotePrice'], ".5f")
    yorkieusd = format(float(priceBnb) * float(binance), ".4f")
        
    websitedomain = "papaexchange.online"
    website = "https://" + websitedomain
    buyNow = "https://exchange.pancakeswap.finance/#/swap?outputCurrency=" + address2
    charts = "https://poocoin.app/tokens/" + address2

    message = f"TokenName: {name}\nTokenSymbol: {symbol}\nTokenAddress: {address2}\n🚀🚀 PriceUSD: {Papausd} USD\n🚀🚀 PriceBNB: {priceBnb} BNB\n\nWebsite: {website}\n\n💰 Buy here: {buyNow}\n📈 Charts: {charts}"

    update.message.reply_text(message)



def hello(update,context):
    update.message.reply_text("If you hold we will get to the SecondUniverse")

def chart(update, context):
    update.message.reply_text("Papa Token Charts on Poocoin\n " + chartA)

def buy(update,context):
    update.message.reply_text("Buy Papa Token on \n" + buyPancake)

def contract2(update,context):
    update.message.reply_text("Papa Token Contract \n " + contract)

def twitter2(update,context):
    update.message.reply_text("The official Twitter \n " + twitter)


def telegramShillGroup(update,context):
    message2 = """ 
    
Spread the word about our 1 in a million token with our🔥HARD SHILL GROUP LIST!
 
@Safugun

@Cryptofanscommunity1

@freecryptoshilling

@NordicApes

@steezyturtlegang

@rugfreetalks

@medusasgroup

@newtokenmarketglobal

@wenlambochat

@VirusLounge

@earlyapes

@goobygamblers

@bruisersbackyard

@shrimpysafehaven

@neverscamagain

@degenapeschat

@erlypotential

@zerotwopay

@Richmuskcallslounge

@Cryptofrogslounge

@SatoshiGem

@tsamoon

@GubbinLounge

@gogetacryptolounge

@CryptoTalkandshill

@PhillipsDiscussion

@hitmancalls_chat

@mooncalls20041223

@CryptoMoonshots_Chat

@MrCroCrosLounge

@shitcoinhouse

@astershitcalls
    
     """
    update.message.reply_text(message2)


def handle_message(update, context):
    text = str(update.message.text).lower()

    response = R.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(config.API_KEY, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler("hello", hello))
    #dp.add_handler(CommandHandler("startPapa", start_command))
    #dp.add_handler(CommandHandler("helpPapa", help_command))
    #dp.add_handler(CommandHandler("price", get_price))
    dp.add_handler(CommandHandler("Papa", get_tokenInfo))
    dp.add_handler(CommandHandler("shill", telegramShillGroup))
    dp.add_handler(CommandHandler("chart", chart))
    dp.add_handler(CommandHandler("buy", buy))
    dp.add_handler(CommandHandler("twitter", twitter2))
    dp.add_handler(CommandHandler("contract", contract2))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling()   
    updater.idle()

main() 



